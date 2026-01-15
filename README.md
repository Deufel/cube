# CUBE CSS Design System (WIP)

A minimal CSS design system using CSS layers, custom attributes, and CUBE methodology.

## Layer Order

```html
<style>@layer reset, props, theme, composition, utility, block, exception;</style>
```

## File Structure

```
├── 0_reset.css         # Normalize/reset
├── 1_props.css         # Raw design tokens (Open Props style)
├── 2_theme-*.css       # Semantic tokens with t-shirt sizes
├── 3_composition.css   # Layout primitives
├── 4_utility.css       # Single-purpose classes
├── 5_block.css         # Components (btn, card, badge, etc.)
└── 6_exception.css     # Block modifications
```

---

## Composition Layer

Layout primitives use `type:variant` syntax.

### Flex Layouts

| Class | Behavior |
|-------|----------|
| `flex:cluster` | Horizontal flex, wraps |
| `flex:stack` | Vertical flex |
| `flex:split` / `flex:split-row` | Binary layout (2 children) — pushes items to opposite edges |
| `flex:split-col` | Binary layout, vertical — pushes items to top/bottom |
| `flex:spread-row` | Distribute *n* items horizontally with `space-between` |
| `flex:spread-column` | Distribute *n* items vertically with `space-between` |
| `flex:flank-start` | 2-child: first flanks at start, second fills (wraps at 50%) |
| `flex:flank-end` | 2-child: last flanks at end, first fills (wraps at 50%) |

**Flank custom properties:**
- `--flank-size`: Target size for the flanking element (default: `auto`)
- `--content-percentage`: Min width before wrapping (default: `50%`)

```html
<div class="flex:cluster gap:md">...</div>
<div class="flex:stack align:center gap:lg">...</div>
<div class="flex:split-row gap:sm">...</div>
<div class="flex:spread-row align:center">...</div>
```

### Grid Layouts

| Class | Behavior |
|-------|----------|
| `grid:lcr` | 3-column: left / center / right — true centering (`1fr auto 1fr`) |
| `grid:tmb` | 3-row: top / middle / bottom — true centering (`1fr auto 1fr` rows) |
| `grid:pancake` | Header / main / footer stack (`auto 1fr auto` rows) |
| `grid:hero` | 3×3 grid for full-page layouts (use with `body.fullscreen > div.grid:hero`) |
| `grid:auto-fit` | Responsive columns, uses `--grid-min` |
| `grid:auto-fill` | Like auto-fit but keeps empty tracks |

```html
<div class="grid:lcr gap:md">
  <div>Left</div>
  <div>Center</div>
  <div>Right</div>
</div>

<div class="grid:auto-fit gap:sm" style="--grid-min: 200px;">
  <div>Item</div>
  <div>Item</div>
</div>

<body class="grid:hero-full">
  <header>...</header>
  <nav>...</nav>
  <main>...</main>
  <aside>...</aside>
  <footer>...</footer>
</body>
```

### Frame (Aspect Ratio)

| Class | Aspect Ratio |
|-------|--------------|
| `frame` / `frame:square` | 1 / 1 |
| `frame:landscape` | 16 / 9 |
| `frame:portrait` | 9 / 16 |

```html
<div class="frame:landscape">
  <img src="..." alt="...">
</div>
```

---

## Utility Layer

Single-purpose modifiers that compose with layouts.

### Alignment

| Class | Property |
|-------|----------|
| `align:start` | `align-items: flex-start` |
| `align:end` | `align-items: flex-end` |
| `align:center` | `align-items: center` |
| `align:stretch` | `align-items: stretch` |
| `align:baseline` | `align-items: baseline` |

| Class | Property |
|-------|----------|
| `justify:start` | `justify-content: flex-start` |
| `justify:end` | `justify-content: flex-end` |
| `justify:center` | `justify-content: center` |
| `justify:between` | `justify-content: space-between` |
| `justify:around` | `justify-content: space-around` |
| `justify:evenly` | `justify-content: space-evenly` |

### Gap

| Class | Value |
|-------|-------|
| `gap:xs` | `var(--space-xs)` |
| `gap:sm` | `var(--space-sm)` |
| `gap:md` | `var(--space-md)` |
| `gap:lg` | `var(--space-lg)` |
| `gap:xl` | `var(--space-xl)` |

### Wrap

| Class | Property |
|-------|----------|
| `wrap` | `flex-wrap: wrap` |
| `nowrap` | `flex-wrap: nowrap` |

### Spacing

| Class | Property |
|-------|----------|
| `p:xs` ... `p:xl` | `padding: var(--space-*)` |
| `m:xs` ... `m:xl` | `margin: var(--space-*)` |

### Text Size

| Class | Property |
|-------|----------|
| `text:xs` ... `text:xl` | `font-size: var(--text-*)` |

---

## Block Layer

Components use class + attribute API.

### Attribute API

| Attribute | Purpose | Values |
|-----------|---------|--------|
| `var` | Variant | `pri`, `sec`, `out`, `gho` |
| `sz` | Size | `xs`, `sm`, `md`, `lg`, `xl` |
| `st` | State | `def`, `lod`, `dis`, `err`, `suc`, `wrn`, `inf` |

### Button

```html
<button class="btn" var="pri" sz="md">Primary</button>
<button class="btn" var="sec" sz="lg">Secondary</button>
<button class="btn" var="out" sz="sm">Outline</button>
<button class="btn" var="gho" sz="md">Ghost</button>
<button class="btn" var="pri" st="lod">Loading...</button>
<button class="btn" var="pri" st="dis" disabled>Disabled</button>
```

### Badge

```html
<span class="badge" var="pri">Primary</span>
<span class="badge" var="suc">Success</span>
<span class="badge" var="err">Error</span>
<span class="badge" var="wrn">Warning</span>
```

### Card

```html
<div class="card" var="pri">
  <h3>Title</h3>
  <p>Content</p>
</div>
```

### Form

Forms use a 4-column grid layout. Use the `w` attribute on `.input-group` to set column span.

| Attribute | Span | Width |
|-----------|------|-------|
| `w="1"` | 1 column | 25% |
| `w="2"` | 2 columns | 50% |
| `w="3"` | 3 columns | 75% |
| `w="4"` | 4 columns | 100% |

```html
<form class="form">
  <!-- Full width -->
  <label class="input-group" w="4">
    Email <span class="feedback">Looks good!</span>
    <input type="email" placeholder="email@example.com" st="suc" />
  </label>
  
  <!-- Two equal columns -->
  <label class="input-group" w="2">
    First Name
    <input type="text" placeholder="John" />
  </label>
  <label class="input-group" w="2">
    Last Name
    <input type="text" placeholder="Doe" />
  </label>
  
  <!-- Asymmetric: 75% + 25% -->
  <label class="input-group" w="3">
    Street Address
    <input type="text" placeholder="123 Main St" />
  </label>
  <label class="input-group" w="1">
    Apt
    <input type="text" placeholder="#" />
  </label>
  
  <!-- Full width button -->
  <button w="4">Submit</button>
</form>
```

**Input states** — use `st` attribute on inputs to show feedback colors:

| State | Attribute |
|-------|-----------|
| Success | `st="suc"` |
| Error | `st="err"` |
| Warning | `st="wrn"` |
| Info | `st="inf"` |

The `.feedback` span inside `.input-group` will automatically color based on the input's `st` attribute.

### Icon Button

```html
<button class="icon-btn" sz="md" var="gho">
  <svg>...</svg>
</button>
```

---

## Exception Layer

Modifications to blocks for edge cases.

---

## Theme Switching

Themes are swappable CSS files. Only load one at a time.

```html
<link rel="stylesheet" href="../css/2_theme-default.css">
```

With Datastar persistence:

```html
<link rel="stylesheet" data-attr:href="$prst_theme">
```

---

## Rules

- Do **not** use `!important` — this breaks layer cascade
- Keep `data-*` attributes for Datastar only
- Keep `var`, `sz`, `st` attributes for styling

