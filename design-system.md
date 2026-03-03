# Дизайн-система для лендинга TVM

## 🎨 Цветовые токены

| Имя | HEX | Применение |
|-----|-----|------------|
| `--primary` | `#7B3FA0` | Основной цвет, кнопки, заголовки |
| `--secondary` | `#2ECFC4` | Телефоны/аксессуары, акценты |
| `--accent` | `#C4266A` | Авиабилеты, важные элементы |
| `--warning` | `#FF5E1A` | Сервис, печать, CTA-кнопки |
| `--success` | `#FFD000` | Финансы, акции, скидки |
| `--neutral` | `#FFFFFF` | Фон, разделители |
| `--text-primary` | `#333333` | Основной текст |
| `--text-secondary` | `#666666` | Вспомогательный текст |
| `--border` | `#E0E0E0` | Границы, разделители |

## 🖋️ Типографика

| Элемент | Стиль | Применение |
|---------|-------|------------|
| `h1` | `font-size: 32px; font-weight: 700; line-height: 1.2;` | Главные заголовки |
| `h2` | `font-size: 24px; font-weight: 600; line-height: 1.3;` | Подзаголовки |
| `h3` | `font-size: 20px; font-weight: 600; line-height: 1.4;` | Секции |
| `body` | `font-size: 16px; font-weight: 400; line-height: 1.6;` | Основной текст |
| `caption` | `font-size: 14px; font-weight: 400; line-height: 1.4;` | Мелкий текст |
| `button` | `font-size: 16px; font-weight: 600; text-transform: uppercase;` | Кнопки |

## 📐 Spacing Scale

| Имя | Значение | Применение |
|-----|----------|------------|
| `--space-xs` | `4px` | Микроотступы |
| `--space-sm` | `8px` | Маленькие отступы |
| `--space-md` | `12px` | Медиум отступы |
| `--space-base` | `16px` | Базовый отступ |
| `--space-lg` | `24px` | Большие отступы |
| `--space-xl` | `32px` | Очень большие отступы |
| `--space-2xl` | `48px` | Гигантские отступы |
| `--space-3xl` | `64px` | Максимальные отступы |

## 🧱 Компоненты

### Button
```css
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-sm) var(--space-base);
  font-family: inherit;
  font-size: var(--font-size-button);
  font-weight: var(--font-weight-button);
  text-transform: uppercase;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.button--primary {
  background: var(--primary);
  color: var(--neutral);
}

.button--primary:hover:not(:disabled) {
  background: #6a3a94;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(123, 63, 160, 0.3);
}

.button--primary:disabled {
  background: #ccc;
  cursor: not-allowed;
}
```

### Section
```css
.section {
  padding: var(--space-2xl) 0;
  background: var(--neutral);
}

.section--alt {
  background: #f8f9fa;
}

.section__title {
  text-align: center;
  margin-bottom: var(--space-xl);
}

.section__content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--space-base);
}
```

### Card
```css
.card {
  background: var(--neutral);
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
}

.card__image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card__content {
  padding: var(--space-base);
}

.card__title {
  margin-bottom: var(--space-sm);
}
```

### Badge
```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: 2px 8px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  border-radius: 4px;
}

.badge--success {
  background: var(--success);
  color: #333;
}

.badge--warning {
  background: var(--warning);
  color: var(--neutral);
}
```

### Input/Form
```css
.input {
  width: 100%;
  padding: var(--space-sm) var(--space-base);
  font-family: inherit;
  font-size: var(--font-size-body);
  border: 1px solid var(--border);
  border-radius: 8px;
  transition: border-color 0.2s ease;
}

.input:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(123, 63, 160, 0.1);
}

.form {
  display: flex;
  flex-direction: column;
}

.form__group {
  margin-bottom: var(--space-base);
}

.form__button {
  margin-top: var(--space-md);
}
```

### Testimonial
```css
.testimonial {
  text-align: center;
  padding: var(--space-xl);
  background: var(--neutral);
  border-radius: 12px;
}

.testimonial__text {
  font-size: 18px;
  line-height: 1.6;
  margin-bottom: var(--space-base);
}

.testimonial__author {
  font-weight: 600;
  color: var(--text-primary);
}

.testimonial__rating {
  color: var(--warning);
  margin-bottom: var(--space-sm);
}
```

## 🎨 Состояния кнопок

```css
/* Default */
.button {
  background: var(--primary);
  color: var(--neutral);
}

/* Hover */
.button:hover:not(:disabled) {
  background: #6a3a94;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(123, 63, 160, 0.3);
}

/* Active */
.button:active:not(:disabled) {
  transform: translateY(0);
}

/* Disabled */
.button:disabled {
  background: #ccc;
  cursor: not-allowed;
  opacity: 0.6;
}
```

## 📏 Радиусы, бордеры, тени

```css
:root {
  --border-radius-sm: 4px;
  --border-radius-md: 8px;
  --border-radius-lg: 12px;
  --border-radius-xl: 16px;
  --border-width: 1px;
  --box-shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.1);
  --box-shadow-md: 0 4px 12px rgba(0, 0, 0, 0.15);
  --box-shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.2);
}
```

## 🎬 Простые анимации

### Fade in
```css
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.fade-in.is-visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Slide up
```css
.slide-up {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.5s ease, transform 0.5s ease;
}

.slide-up.is-visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Scale in
```css
.scale-in {
  opacity: 0;
  transform: scale(0.8);
  transition: opacity 0.4s ease, transform 0.4s ease;
}

.scale-in.is-visible {
  opacity: 1;
  transform: scale(1);
}
```

## 📋 Использование

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    :root {
      /* Цветовые токены */
      --primary: #7B3FA0;
      --secondary: #2ECFC4;
      --accent: #C4266A;
      --warning: #FF5E1A;
      --success: #FFD000;
      --neutral: #FFFFFF;
      --text-primary: #333333;
      --text-secondary: #666666;
      --border: #E0E0E0;
      
      /* Typography */
      --font-size-h1: 32px;
      --font-size-h2: 24px;
      --font-size-h3: 20px;
      --font-size-body: 16px;
      --font-size-caption: 14px;
      --font-size-button: 16px;
      --font-weight-button: 600;
      
      /* Spacing */
      --space-xs: 4px;
      --space-sm: 8px;
      --space-md: 12px;
      --space-base: 16px;
      --space-lg: 24px;
      --space-xl: 32px;
      --space-2xl: 48px;
      --space-3xl: 64px;
      
      /* Border radius */
      --border-radius-sm: 4px;
      --border-radius-md: 8px;
      --border-radius-lg: 12px;
      --border-radius-xl: 16px;
      
      /* Box shadows */
      --box-shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.1);
      --box-shadow-md: 0 4px 12px rgba(0, 0, 0, 0.15);
      --box-shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.2);
    }
    
    /* Включаем анимации */
    .fade-in.is-visible,
    .slide-up.is-visible,
    .scale-in.is-visible {
      opacity: 1;
      transform: none;
    }
  </style>
</head>
<body>
  <!-- Пример использования -->
  <section class="section fade-in">
    <div class="section__content">
      <h2 class="section__title">Наши услуги</h2>
      <div class="cards">
        <div class="card slide-up">
          <img src="phone.jpg" alt="Телефоны" class="card__image">
          <div class="card__content">
            <h3 class="card__title">Телефоны</h3>
            <p class="card__description">Широкий выбор смартфонов и аксессуаров</p>
            <button class="button button--primary">Подробнее</button>
          </div>
        </div>
        <!-- Ещё карточки -->
      </div>
    </div>
  </section>
</body>
</html>
```

## 🚀 Преимущества

- **Быстрая разработка** - все стили готовы к использованию
- **Согласованность** - единая цветовая палитра и типографика
- **Адаптивность** - все компоненты адаптированы
- **Анимации** - простые эффекты для лучшего UX
- **CSS переменные** - легко изменять стили
- **Масштабируемость** - можно добавлять новые компоненты