# Дизайн-система для TVM.ru

**Цель:** Быстрая и надёжная верстка лендинга в CMS Мегагрупп  
**Стиль:** Современный, яркий, многоцветный, геометрический  
**Адаптивность:** Мобильная версия + планшеты (обязательно)  
**Время реализации:** 1–2 дня

---

## 1. Цветовые токены (6 цветов + нейтральные)

| Имя | HEX | Применение |
|-----|-----|------------|
| `--color-primary` | `#7B3FA0` | Основной (фиолетовый) — кнопки, заголовки, акценты |
| `--color-phones` | `#2ECFC4` | Телефоны и аксессуары (бирюзовый) |
| `--color-aviatickets` | `#C4266A` | Авиабилеты (малиновый) |
| `--color-service` | `#FF5E1A` | Сервис, печать, CTA-кнопки (оранжевый) |
| `--color-finance` | `#FFD000` | Финансы, акции, скидки (жёлтый) |
| `--color-bg` | `#FFFFFF` | Фон страницы |
| `--color-bg-alt` | `#F8F9FA` | Альтернативный фон (блоки) |
| `--color-text` | `#1A1A1A` | Основной текст |
| `--color-text-secondary` | `#666666` | Вторичный текст |
| `--color-border` | `#E0E0E0` | Границы карточек, форм |
| `--color-success` | `#27AE60` | Успех (галочки, гарантии) |
| `--color-error` | `#E74C3C` | Ошибки (валидация) |

**Примечание:**  
- Каждый блок использует свой цвет из палитры (например, блок «Телефоны» — `--color-phones`)  
- Акцентные CTA-кнопки: `--color-primary` + `--color-service`

---

## 2. Типографика

### Шрифты (CSS variables)
```css
:root {
  --font-heading: 'Inter', 'Roboto', sans-serif;
  --font-body: 'Inter', 'Roboto', sans-serif;
}
```

### Размеры и стили

| Элемент | CSS | Применение |
|---------|-----|------------|
| `H1` | `font-size: 32px; line-height: 1.2; font-weight: 700;` | Главный заголовок (блок `offer`) |
| `H2` | `font-size: 24px; line-height: 1.3; font-weight: 600;` | Подзаголовки (блоки `directions`, `guarantees`) |
| `H3` | `font-size: 20px; line-height: 1.4; font-weight: 600;` | Карточки направлений, FAQ |
| `Body` | `font-size: 16px; line-height: 1.6; font-weight: 400;` | Основной текст |
| `Caption` | `font-size: 14px; line-height: 1.5; font-weight: 400;` | Подписи, дата отзыва |
| `Button` | `font-size: 16px; line-height: 1.5; font-weight: 600;` | Кнопки |

**Адаптивность:**  
- `H1`: 28px (мобильный), 32px (десктоп)  
- `H2`: 20px (мобильный), 24px (десктоп)  
- `H3`: 18px (мобильный), 20px (десктоп)

---

## 3. Spacing scale

| Имя | Значение | Применение |
|-----|----------|------------|
| `--space-xs` | `4px` | Мелкие отступы (иконки, чекбоксы) |
| `--space-sm` | `8px` | Отступы внутри карточек |
| `--space-md` | `16px` | Отступы внутри блоков |
| `--space-lg` | `24px` | Отступы между элементами |
| `--space-xl` | `32px` | Отступы между блоками |
| `--space-2xl` | `48px` | Отступы между секциями |
| `--space-3xl` | `64px` | Отступы в хедере/футере |

**Примечание:**  
- Использовать `--space-lg` для вертикальных отступов между блоками  
- Использовать `--space-xl` для горизонтальных отступов контейнера

---

## 4. Компоненты

### Button

```css
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.button--primary {
  background-color: var(--color-primary);
  color: #FFFFFF;
}

.button--service {
  background-color: var(--color-service);
  color: #FFFFFF;
}

.button:hover {
  opacity: 0.9;
  transform: translateY(-1px);
}

.button:active {
  transform: translateY(0);
}

.button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

**Применение:**  
- `button--primary`: Основные действия («Позвонить», «Оформить заказ»)  
- `button--service`: Акцентные действия («Оставить заявку»)

---

### Section

```css
.section {
  padding: var(--space-2xl) 0;
  background-color: var(--color-bg);
}

.section--alt {
  background-color: var(--color-bg-alt);
}

.section__container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--space-xl);
}
```

**Применение:**  
- `section`: Базовый блок (все 10 блоков лендинга)  
- `section--alt`: Блоки с альтернативным фоном (например, `guarantees`)

---

### Card

```css
.card {
  background-color: #FFFFFF;
  border-radius: 12px;
  padding: var(--space-xl);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  border: 1px solid var(--color-border);
  transition: box-shadow 0.2s ease;
}

.card:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}
```

**Применение:**  
- Карточки направлений (блок `directions`)  
- Карточки отзывов (блок `proof`)

---

### Badge

```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
}

.badge--success {
  background-color: rgba(39, 174, 96, 0.1);
  color: var(--color-success);
}

.badge--accent {
  background-color: rgba(255, 94, 26, 0.1);
  color: var(--color-service);
}
```

**Применение:**  
- `badge--success`: Гарантии («только новый товар», «возврат по чеку»)  
- `badge--accent`: Акции («скидка», «подарок»)

---

### Input/Form

```css
.form {
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
}

.input {
  padding: 12px 16px;
  border: 1px solid var(--color-border);
  border-radius: 8px;
  font-size: 16px;
  transition: border-color 0.2s ease;
}

.input:focus {
  outline: none;
  border-color: var(--color-primary);
}

.input--error {
  border-color: var(--color-error);
}

.input--success {
  border-color: var(--color-success);
}
```

**Применение:**  
- Форма заявки (блок `cta`)  
- Поля: Имя, Телефон, Выбор направления (select)

---

### Testimonial

```css
.testimonial {
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
}

.testimonial__quote {
  font-size: 18px;
  line-height: 1.6;
  color: var(--color-text);
}

.testimonial__author {
  display: flex;
  align-items: center;
  gap: var(--space-sm);
}

.testimonial__author-name {
  font-weight: 600;
  font-size: 16px;
}

.testimonial__author-date {
  font-size: 14px;
  color: var(--color-text-secondary);
}
```

**Применение:**  
- Отзывы (блок `proof`)  
- Структура: цитата → автор + дата

---

## 5. Состояния кнопок

| Состояние | CSS |
|-----------|-----|
| `default` | `background-color: var(--color-primary); color: #FFFFFF;` |
| `hover` | `opacity: 0.9; transform: translateY(-1px);` |
| `active` | `transform: translateY(0);` |
| `disabled` | `opacity: 0.5; cursor: not-allowed;` |

**Примечание:**  
- Анимация `transform` — плавная (0.2s)  
- Для `button--service` заменить `--color-primary` на `--color-service`

---

## 6. Радиусы, бордеры, тени

| Элемент | Значение |
|---------|----------|
| `--radius-sm` | `4px` | Мелкие элементы (чекбоксы) |
| `--radius-md` | `8px` | Кнопки, инпуты |
| `--radius-lg` | `12px` | Карточки, секции |
| `--radius-xl` | `24px` | Модальные окна |
| `--border-width` | `1px` | Границы |
| `--border-style` | `solid` | Сплошная линия |
| `--shadow-sm` | `0 2px 8px rgba(0, 0, 0, 0.04)` | Карточки |
| `--shadow-md` | `0 4px 16px rgba(0, 0, 0, 0.08)` | Акцентные карточки |

---

## 7. Анимации (2 простые)

### 1. Плавное появление (fade-in)

```css
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fadeIn 0.4s ease forwards;
}
```

**Применение:**  
- Блоки при скролле (опционально)  
- Отзывы (постепенное появление)

---

### 2. Нажатие кнопки (scale-down)

```css
@keyframes scaleDown {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(0.96);
  }
  100% {
    transform: scale(1);
  }
}

.button:active {
  animation: scaleDown 0.2s ease;
}
```

**Применение:**  
- Все кнопки (визуальный отклик при нажатии)

---

## 8. Адаптивность (мобильная версия)

### Медиа-запросы

```css
@media (max-width: 768px) {
  :root {
    --space-xl: 20px;
    --space-2xl: 32px;
  }

  .section__container {
    padding: 0 var(--space-md);
  }

  .card {
    padding: var(--space-lg);
  }

  .button {
    width: 100%;
  }
}
```

**Примечание:**  
- На мобильных кнопки — на всю ширину  
- Отступы уменьшены на 20%  
- Карточки — вертикальная верстка

---

## 9. Итоговая структура CSS variables

```css
:root {
  /* Цвета */
  --color-primary: #7B3FA0;
  --color-phones: #2ECFC4;
  --color-aviatickets: #C4266A;
  --color-service: #FF5E1A;
  --color-finance: #FFD000;
  --color-bg: #FFFFFF;
  --color-bg-alt: #F8F9FA;
  --color-text: #1A1A1A;
  --color-text-secondary: #666666;
  --color-border: #E0E0E0;
  --color-success: #27AE60;
  --color-error: #E74C3C;

  /* Типографика */
  --font-heading: 'Inter', 'Roboto', sans-serif;
  --font-body: 'Inter', 'Roboto', sans-serif;

  /* Spacing */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;
  --space-3xl: 64px;

  /* Радиусы и тени */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 24px;
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.04);
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.08);
}
```

---

*Дизайн-система готова к передаче в верстальщика. Время реализации: 1–2 дня.*