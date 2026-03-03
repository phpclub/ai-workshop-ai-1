# Финальная верстка лендинга для TVM

# Импортируем необходимые модули
from typing import List, Dict, Any
import json

# Определяем структуру блоков
BLOCKS = [
    "hero",
    "problem",
    "solution",
    "services",
    "proof-social",
    "process",
    "guarantees",
    "final-cta",
    "faq",
    "contact-footer"
]

# Основной класс для генерации HTML
class LandingGenerator:
    def __init__(self):
        self.blocks = BLOCKS
        self.design_tokens = {
            "primary": "#7B3FA0",
            "secondary": "#2ECFC4",
            "accent": "#C4266A",
            "warning": "#FF5E1A",
            "success": "#FFD000",
            "neutral": "#FFFFFF",
            "text-primary": "#333333",
            "text-secondary": "#666666",
            "border": "#E0E0E0"
        }
        self.typography = {
            "h1": "font-size: 32px; font-weight: 700; line-height: 1.2;",
            "h2": "font-size: 24px; font-weight: 600; line-height: 1.3;",
            "h3": "font-size: 20px; font-weight: 600; line-height: 1.4;",
            "body": "font-size: 16px; font-weight: 400; line-height: 1.6;",
            "caption": "font-size: 14px; font-weight: 400; line-height: 1.4;",
            "button": "font-size: 16px; font-weight: 600; text-transform: uppercase;"
        }
        self.spacing = {
            "xs": "4px",
            "sm": "8px",
            "md": "12px",
            "base": "16px",
            "lg": "24px",
            "xl": "32px",
            "2xl": "48px",
            "3xl": "64px"
        }

    def generate_css(self) -> str:
        """Генерация CSS-стилей"""
        css = f"""
        :root {{
            /* Цветовые токены */
            --primary: {self.design_tokens['primary']};
            --secondary: {self.design_tokens['secondary']};
            --accent: {self.design_tokens['accent']};
            --warning: {self.design_tokens['warning']};
            --success: {self.design_tokens['success']};
            --neutral: {self.design_tokens['neutral']};
            --text-primary: {self.design_tokens['text-primary']};
            --text-secondary: {self.design_tokens['text-secondary']};
            --border: {self.design_tokens['border']};

            /* Типографика */
            --font-size-h1: 32px;
            --font-size-h2: 24px;
            --font-size-h3: 20px;
            --font-size-body: 16px;
            --font-size-caption: 14px;
            --font-size-button: 16px;
            --font-weight-button: 600;

            /* Отступы */
            --space-xs: {self.spacing['xs']};
            --space-sm: {self.spacing['sm']};
            --space-md: {self.spacing['md']};
            --space-base: {self.spacing['base']};
            --space-lg: {self.spacing['lg']};
            --space-xl: {self.spacing['xl']};
            --space-2xl: {self.spacing['2xl']};
            --space-3xl: {self.spacing['3xl']};

            /* Радиусы */
            --border-radius-sm: 4px;
            --border-radius-md: 8px;
            --border-radius-lg: 12px;
            --border-radius-xl: 16px;

            /* Тени */
            --box-shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.1);
            --box-shadow-md: 0 4px 12px rgba(0, 0, 0, 0.15);
            --box-shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.2);
        }}

        /* Общие стили */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            color: var(--text-primary);
            line-height: 1.6;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 var(--space-base);
        }}

        .section {{
            padding: var(--space-2xl) 0;
            background: var(--neutral);
        }}

        .section--alt {{
            background: #f8f9fa;
        }}

        .section__title {{
            text-align: center;
            margin-bottom: var(--space-xl);
            font-size: var(--font-size-h2);
            font-weight: 600;
        }}

        .section__content {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 var(--space-base);
        }}

        .button {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: var(--space-sm) var(--space-base);
            font-family: inherit;
            font-size: var(--font-size-button);
            font-weight: var(--font-weight-button);
            text-transform: uppercase;
            border: none;
            border-radius: var(--border-radius-md);
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .button--primary {{
            background: var(--primary);
            color: var(--neutral);
        }}

        .button--primary:hover:not(:disabled) {{
            background: #6a3a94;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(123, 63, 160, 0.3);
        }}

        .button--primary:disabled {{
            background: #ccc;
            cursor: not-allowed;
        }}

        .card {{
            background: var(--neutral);
            border-radius: var(--border-radius-lg);
            box-shadow: var(--box-shadow-md);
            overflow: hidden;
            transition: transform 0.3s ease;
            margin-bottom: var(--space-base);
        }}

        .card:hover {{
            transform: translateY(-4px);
        }}

        .card__image {{
            width: 100%;
            height: 200px;
            object-fit: cover;
        }}

        .card__content {{
            padding: var(--space-base);
        }}

        .card__title {{
            margin-bottom: var(--space-sm);
            font-size: var(--font-size-h3);
        }}

        .testimonial {{
            text-align: center;
            padding: var(--space-xl);
            background: var(--neutral);
            border-radius: var(--border-radius-lg);
        }}

        .testimonial__text {{
            font-size: 18px;
            line-height: 1.6;
            margin-bottom: var(--space-base);
        }}

        .testimonial__author {{
            font-weight: 600;
            color: var(--text-primary);
        }}

        .testimonial__rating {{
            color: var(--warning);
            margin-bottom: var(--space-sm);
        }}

        .fade-in {{
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.6s ease, transform 0.6s ease;
        }}

        .fade-in.is-visible {{
            opacity: 1;
            transform: translateY(0);
        }}

        /* Адаптивность */
        @media (max-width: 768px) {{
            .section {{
                padding: var(--space-xl) 0;
            }}

            .section__title {{
                font-size: 24px;
            }}

            .button {{
                width: 100%;
                margin-bottom: var(--space-sm);
            }}
        }}
        """
        return css

    def generate_hero_section(self) -> str:
        """Генерация секции hero"""
        return """
        <section class="section fade-in" id="hero">
            <div class="section__content">
                <div class="hero-content">
                    <div class="hero-image">
                        <img src="office.jpg" alt="Офис TVM" style="width: 100%; height: auto; border-radius: var(--border-radius-lg);">
                    </div>
                    <div class="hero-text">
                        <h1 class="section__title">TVM — всё в одном месте: телефоны, авиабилеты, печать рядом</h1>
                        <p class="hero-description">25+ лет опыта в Москве, рейтинг 4.7/40</p>
                        <div class="hero-buttons">
                            <button class="button button--primary">Оставить заявку</button>
                            <button class="button">Позвонить</button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """

    def generate_problem_section(self) -> str:
        """Генерация секции problem"""
        return """
        <section class="section section--alt fade-in" id="problem">
            <div class="section__content">
                <h2 class="section__title">Устали от б/у телефонов и отменённых заказов?</h2>
                <p class="section__subtitle">Не можете разобраться в авиабилетах?</p>
                <div class="problem-content">
                    <div class="problem-icons">
                        <div class="icon">📱</div>
                        <div class="icon">🎫</div>
                        <div class="icon">💸</div>
                    </div>
                    <div class="problem-reviews">
                        <div class="testimonial">
                            <p class="testimonial__text">Продают б/у товар под видом нового</p>
                        </div>
                        <div class="testimonial">
                            <p class="testimonial__text">Деньги списали, билеты не выписали 5 дней</p>
                        </div>
                        <div class="testimonial">
                            <p class="testimonial__text">Продавец грубый, нет внятных объяснений</p>
                        </div>
                    </div>
                </div>
                <div class="problem-cta">
                    <button class="button">Наши решения ниже</button>
                </div>
            </div>
        </section>
        """

    def generate_solution_section(self) -> str:
        """Генерация секции solution"""
        return """
        <section class="section fade-in" id="solution">
            <div class="section__content">
                <h2 class="section__title">TVM — честный магазин с живым сервисом</h2>
                <p class="section__subtitle">Только новый товар, реальный человек на связи</p>
                <div class="solution-content">
                    <div class="solution-image">
                        <img src="consultants.jpg" alt="Консультанты" style="width: 100%; height: auto; border-radius: var(--border-radius-lg);">
                    </div>
                    <div class="solution-process">
                        <p>Помогаем выбрать телефон и оформить билет без очередей, без автоответов и без сюрпризов</p>
                        <button class="button">Смотреть услуги</button>
                    </div>
                </div>
            </div>
        </section>
        """

    def generate_services_section(self) -> str:
        """Генерация секции services"""
        return """
        <section class="section section--alt fade-in" id="services">
            <div class="section__content">
                <h2 class="section__title">6 услуг в одном месте: от телефона до авиабилета</h2>
                <p class="section__subtitle">Единственная точка в Мытищах с полным комплексом</p>
                <div class="services-cards">
                    <div class="card">
                        <div class="card__image" style="background-color: #2ECFC4; display: flex; align-items: center; justify-content: center; color: white; font-size: 24px;">📱</div>
                        <div class="card__content">
                            <h3 class="card__title">Телефоны</h3>
                            <p>Широкий выбор смартфонов и аксессуаров</p>
                            <button class="button">Подробнее</button>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card__image" style="background-color: #C4266A; display: flex; align-items: center; justify-content: center; color: white; font-size: 24px;">🎫</div>
                        <div class="card__content">
                            <h3 class="card__title">Авиабилеты</h3>
                            <p>Быстрое оформление авиабилетов</p>
                            <button class="button">Подробнее</button>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card__image" style="background-color: #FF5E1A; display: flex; align-items: center; justify-content: center; color: white; font-size: 24px;">🖨️</div>
                        <div class="card__content">
                            <h3 class="card__title">Печать</h3>
                            <p>Распечатаем документы рядом с домом</p>
                            <button class="button">Подробнее</button>
                        </div>
                    </div>
                </div>
                <div class="services-cta">
                    <button class="button">Подробнее о каждом направлении</button>
                </div>
            </div>
        </section>
        """

    def generate_proof_social_section(self) -> str:
        """Генерация секции proof-social"""
        return """
        <section class="section fade-in" id="proof-social">
            <div class="section__content">
                <h2 class="section__title">Нам доверяют 40+ клиентов</h2>
                <div class="testimonials-container">
                    <div class="testimonial">
                        <p class="testimonial__text">Низкие цены. Вежливый продавец</p>
                        <p class="testimonial__author">Анна, Москва</p>
                        <div class="testimonial__rating">★★★★★</div>
                    </div>
                    <div class="testimonial">
                        <p class="testimonial__text">Грамотный консультант</p>
                        <p class="testimonial__author">Иван, Мытищи</p>
                        <div class="testimonial__rating">★★★★★</div>
                    </div>
                    <div class="testimonial">
                        <p class="testimonial__text">Можно распечатать документы</p>
                        <p class="testimonial__author">Мария, Москва</p>
                        <div class="testimonial__rating">★★★★★</div>
                    </div>
                    <div class="testimonial">
                        <p class="testimonial__text">Быстро и удобно</p>
                        <p class="testimonial__author">Дмитрий, Мытищи</p>
                        <div class="testimonial__rating">★★★★★</div>
                    </div>
                    <div class="testimonial">
                        <p class="testimonial__text">Рекомендую</p>
                        <p class="testimonial__author">Елена, Москва</p>
                        <div class="testimonial__rating">★★★★★</div>
                    </div>
                </div>
                <div class="proof-cta">
                    <button class="button">Все отзывы</button>
                </div>
            </div>
        </section>
        """

    def generate_process_section(self) -> str:
        """Генерация секции process"""
        return """
        <section class="section section--alt fade-in" id="process">
            <div class="section__content">
                <h2 class="section__title">Оформление за 3 шага: выбор → консультация → покупка</h2>
                <p class="section__subtitle">Помогаем с выбором, подбираем под задачи, делаем скидки</p>
                <div class="process-content">
                    <div class="process-step">
                        <div class="step-icon">1</div>
                        <p>Выбор товара или услуги</p>
                    </div>
                    <div class="process-step">
                        <div class="step-icon">2</div>
                        <p>Консультация с экспертом</p>
                    </div>
                    <div class="process-step">
                        <div class="step-icon">3</div>
                        <p>Оформление и покупка</p>
                    </div>
                </div>
                <div class="process-cta">
                    <button class="button">Начать оформление</button>
                </div>
            </div>
        </section>
        """

    def generate_guarantees_section(self) -> str:
        """Генерация секции guarantees"""
        return """
        <section class="section fade-in" id="guarantees">
            <div class="section__content">
                <h2 class="section__title">Гарантии честности и качества</h2>
                <p class="section__subtitle">Только новый товар, обмен по