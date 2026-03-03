from __future__ import annotations

import asyncio
import signal
from contextlib import suppress
from urllib.parse import urlsplit

from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from app.config import Settings


def resolve_webhook_path(webhook_url: str) -> str:
    path = urlsplit(webhook_url).path or "/"
    return path if path.startswith("/") else f"/{path}"


async def run_polling(bot: Bot, dispatcher: Dispatcher) -> None:
    await bot.delete_webhook(drop_pending_updates=False)
    await dispatcher.start_polling(bot)


async def run_webhook(bot: Bot, dispatcher: Dispatcher, settings: Settings) -> None:
    app = web.Application()
    webhook_path = resolve_webhook_path(settings.webhook_url or "/")

    SimpleRequestHandler(dispatcher=dispatcher, bot=bot).register(app, path=webhook_path)
    setup_application(app, dispatcher, bot=bot)

    async def register_webhook(_: web.Application) -> None:
        await bot.set_webhook(
            url=settings.webhook_url or "",
            allowed_updates=dispatcher.resolve_used_update_types(),
            drop_pending_updates=False,
        )

    app.on_startup.append(register_webhook)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, host="0.0.0.0", port=8080)
    stop_event = asyncio.Event()
    loop = asyncio.get_running_loop()

    for sig in (signal.SIGINT, signal.SIGTERM):
        with suppress(NotImplementedError):
            loop.add_signal_handler(sig, stop_event.set)

    try:
        await site.start()
        await stop_event.wait()
    finally:
        await runner.cleanup()
