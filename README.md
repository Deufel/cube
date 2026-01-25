# CUBE CSS Design System

A minimal CSS design system inspired by [CUBE CSS](https://cube.fyi), implemented with CSS Layers.

## Philosophy

- **Layered cascade** — Uses `@layer` for specificity control, eliminating the need for BEM naming or `!important`
- **Static props, semantic themes** — Raw tokens (`--size-1`, `--size-2`, `--blu-5`) live in props layer; themes map them to semantic names (`--space-sm`, `--color-pri`). Swap one theme file to restyle everything.
- **Exceptions use classes, not `data-*`** — Reserves `data-*` attributes for Datastar integration
- **Minimal media queries** — Layout uses intrinsic sizing (hero grid, auto-fit/fill) to adapt without breakpoints

## Layer Order

```css
@layer reset, props, theme, composition, utility, block, exception;
```

Each layer increases in specificity. Later layers override earlier ones without specificity wars.

## File Structure

| File | Layer | Purpose |
|------|-------|---------|
| `0_reset.css` | reset | Minimal normalize |
| `1_props.css` | props | Raw design tokens (colors, sizes, shadows, fonts) |
| `2_theme-*.css` | theme | Semantic mapping with t-shirt sizes, swappable |
| `3_composition.css` | composition | Layout primitives |
| `4_utility.css` | utility | Single-purpose modifiers |
| `5_block.css` | block | Components |
| `6_exception.css` | exception | Variants, sizes, states |

## Class APIs

### Layout API

Composition + utility classes for layout. Pattern: `composition:variant` + utilities.

```html
<div class="flex:stack gap:md align:center">...</div>
<div class="grid:hero gap:xs">...</div>
<div class="flex:cluster gap:sm wrap">...</div>
```

Composition sets the layout mode; utilities modify spacing, alignment, wrapping.

See [layout.html](layout.html) for full API documentation.

### Block API

Component classes. Pattern: `block:variant-exception`.

```html
<button class="btn:pri">Primary</button>
<button class="btn:dgr-sm">Small Danger</button>
<button class="btn:pri out">Primary Outline</button>
<span class="chip:inf-sm">Info</span>
```

- **Block** — Component name (`btn`, `chip`, `card`)
- **Variant** — Style variation (`pri`, `sec`, `dgr`, `inf`)
- **Exception** — Size or modifier suffix (`-sm`, `-lg`)
- **Modifiers** — Separate classes that combine with variants (`out`)

See individual component pages (button.html, chips.html, etc.) for API documentation.

## Page Layout

Default structure uses a fullscreen hero grid for app-like layouts:

```
┌─────────────────────────────────────┐
│             header                  │
├──────┬──────────────────────┬───────┤
│      │                      │       │
│ nav  │        main          │ aside │
│      │                      │       │
├──────┴──────────────────────┴───────┤
│             footer                  │
└─────────────────────────────────────┘
```

```html
<body class="fullscreen scroll-no">
  <div class="grid:hero gap:xs">
    <header>...</header>
    <nav class="desktop">...</nav>
    <main class="scroll-y">...</main>
    <aside>...</aside>
    <footer>...</footer>
  </div>
</body>
```

- **Nav/aside/footer** — Use `<dialog popover>` drawers on mobile, inline on desktop
- **No z-index tracking** — Drawers use top-layer via popover API
- **4-column forms** — Max columns that work on all screen sizes without media queries

## Theme Swapping

Themes are single CSS files. Switch by changing the `<link>`:

```html
<link rel="stylesheet" href="./css/2_theme-default.css">
```

With Datastar persistence:

```html
<link rel="stylesheet" data-attr:href="$prst_theme">
```

## Datastar Integration

This system is designed for use with [Datastar](https://data-star.dev). Key integrations:

- **Theme/mode switching** via signals and `data-attr`
- **Partial loading** with `data-init="@get('./partials/nav.html')"`
- **Signal persistence** with `data-persist`
- **`data-*` reserved** — Exceptions use class selectors, not data attributes

## Documentation

Component API documentation lives in individual HTML pages that serve as both docs and visual tests:

- [button.html](button.html) — Button component
- [icon_btn.html](icon_btn.html) — Icon button
- [chips.html](chips.html) — Chip/tag component
- [cards.html](cards.html) — Card component
- [forms.html](forms.html) — Form layout and inputs
- [layout.html](layout.html) — Composition and utility classes
- [colors.html](colors.html) — Color palette
