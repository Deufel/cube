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

### Class API

| Class | Purpose | Values |
|-------|---------|--------|
| variant | Variant | `pri`, `sec`, `out`, `gho` |
| size | Size | `xs`, `sm`, `md`, `lg`, `xl` |
| state | State | `err`, `suc`, `wrn`, `inf` |

**Note:** Use `disabled` attribute for disabled state, `aria-busy="true"` for loading state.

### Inline Controls (Shared Base)

`button`, `.btn`, `.tag`, `.badge`, `kbd` share: `text-box: trim-both cap alphabetic`, `line-height: 1`, `inline-flex` centering, `gap: var(--space-xs)`.

### Button

Interactive element for actions. Use `<button>` or `.btn` on anchors.

| Modifier | Values |
|----------|--------|
| variant | `pri`, `sec`, `gho`, `gra`, `gla`, `wrn`, `dgr`, `suc` |
| modifier | `out` (outline version of any variant) |
| size | `sm`, `lg` (default: md) |

```html
<button>Default</button>
<button class="pri">Primary</button>
<button class="gho">Ghost</button>
<button class="dgr out">Danger Outline</button>
<button class="sm">Small</button>
```

### Tag

Non-interactive label for status/categories. No pointer cursor.

| Modifier | Values |
|----------|--------|
| color | `inf`, `suc`, `wrn`, `dgr` |

```html
<span class="tag">Default</span>
<span class="tag inf">Info</span>
<span class="tag suc">Success</span>
<span class="tag wrn">Warning</span>
<span class="tag dgr">Danger</span>

<!-- Removable (button inside gets pointer) -->
<span class="tag suc">Done <button class="close">×</button></span>
```

### Badge

Notification count or status dot. Requires `position: relative` parent. Default: info blue.

| Modifier | Values |
|----------|--------|
| color | `suc`, `wrn`, `dgr` (default: inf) |

```html
<!-- Count badge -->
<span style="position: relative;">
  <svg>...</svg>
  <span class="badge">3</span>
</span>

<!-- Dot indicator (empty) -->
<span class="badge"></span>

<!-- Color variants -->
<span class="badge suc">✓</span>
<span class="badge wrn">!</span>
<span class="badge dgr">9</span>
```

### Kbd

Keyboard input indicator. Monospace font, subtle background.

```html
Press <kbd>Ctrl</kbd> + <kbd>S</kbd> to save.
```


### Card

Container with subtle primary-tinted background. Use for content grouping.

| Modifier | Values |
|----------|--------|
| variant | `pri`, `sec`, `gla` |

```html
<div class="card">Default (primary tint)</div>
<div class="card pri">Primary</div>
<div class="card sec">Secondary</div>
<div class="card gla">Glass (blur)</div>
```

### Alert Card

Status messages with colored border and glow. Use `card:alert` + color modifier.

| Modifier | Values |
|----------|--------|
| color | `inf`, `suc`, `wrn`, `dgr` |

```html
<div class="card:alert inf">Info message</div>
<div class="card:alert suc">Success message</div>
<div class="card:alert wrn">Warning message</div>
<div class="card:alert dgr">Danger message</div>
```

### Form

Forms use a 4-column grid layout. Use width classes on `.input-group` to set column span.

| Class | Span | Width |
|-------|------|-------|
| `w-1` | 1 column | 25% |
| `w-2` | 2 columns | 50% |
| `w-3` | 3 columns | 75% |
| `w-4` | 4 columns | 100% |

```html
<form class="form">
  <!-- Full width -->
  <label class="input-group w-4">
    Email <span class="feedback">Looks good!</span>
    <input type="email" placeholder="email@example.com" class="suc" />
  </label>
  
  <!-- Two equal columns -->
  <label class="input-group w-2">
    First Name
    <input type="text" placeholder="John" />
  </label>
  <label class="input-group w-2">
    Last Name
    <input type="text" placeholder="Doe" />
  </label>
  
  <!-- Asymmetric: 75% + 25% -->
  <label class="input-group w-3">
    Street Address
    <input type="text" placeholder="123 Main St" />
  </label>
  <label class="input-group w-1">
    Apt
    <input type="text" placeholder="#" />
  </label>
  
  <!-- Full width button -->
  <button class="w-4">Submit</button>
</form>
```

**Input states** — use `st` attribute on inputs to show feedback colors:

| State | Class |
|-------|-------|
| Success | `class="suc"` |
| Error | `class="err"` |
| Warning | `class="wrn"` |
| Info | `class="inf"` |

The `.feedback` span inside `.input-group` will automatically color based on the inputns state class.

### Icon Button

Icon buttons support size, variant, color, and shape classes.

| Class | Purpose | Values |
|-------|---------|--------|
| size | Size | `sm` (32px), default (40px), `lg` (48px) |
| variant | Variant | `pri`, `sec`, `out`, `gho`, `gra`, `gla` |
| color | Color | `suc`, `wrn`, `dgr` |
| shape | Shape | `round` (pill/circle) |

```html
<!-- Sizes -->
<button class="icon-btn" class="sm"><svg>...</svg></button>
<button class="icon-btn"><svg>...</svg></button>
<button class="icon-btn" class="lg"><svg>...</svg></button>

<!-- Variants -->
<button class="icon-btn" class="pri"><svg>...</svg></button>
<button class="icon-btn" class="sec"><svg>...</svg></button>
<button class="icon-btn" class="out"><svg>...</svg></button>
<button class="icon-btn" class="gho"><svg>...</svg></button>
<button class="icon-btn" class="gra"><svg>...</svg></button>
<button class="icon-btn" class="gla"><svg>...</svg></button>

<!-- Colors -->
<button class="icon-btn" class="out" class="suc"><svg>...</svg></button>
<button class="icon-btn" class="pri" class="dgr"><svg>...</svg></button>

<!-- Shape -->
<button class="icon-btn" class="pri" class="round"><svg>...</svg></button>

<!-- With label -->
<button class="icon-btn" class="lg">
  <svg>...</svg>
  <span>Label</span>
</button>
```

### Drawer

Viewport-anchored slide-out panels. Works with `<dialog>` (modal, backdrop) or `<div popover>` (lighter).

| Class | Direction | Size |
|-------|-----------|------|
| `drawer:left` | Left edge | `--drawer-width` |
| `drawer:right` | Right edge | `--drawer-width` |
| `drawer:top` | Top edge | `--drawer-height` |
| `drawer:bottom` | Bottom edge | `--drawer-height` |

**Props:**
| Token | Default |
|-------|---------|
| `--drawer-width` | `clamp(280px, 75vw, 360px)` |
| `--drawer-maxwidth` | `85vw` |
| `--drawer-height` | `clamp(200px, 40vh, 350px)` |
| `--drawer-maxheight` | `60vh` |
| `--drawer-backdrop` | `rgba(0, 0, 0, 0.5)` |

**Internal structure:**
- `.drawer-content` — scrollable content area with padding
- `.drawer-header` — flex split header with close button

```html
<!-- Dialog drawer (modal, has backdrop) -->
<dialog class="drawer:left" id="nav-drawer" popover="manual">
  <div class="drawer-content">
    <div class="drawer-header">
      <h3>Navigation</h3>
      <button class="close-btn" popovertarget="nav-drawer">Close</button>
    </div>
    <!-- content -->
  </div>
</dialog>

<!-- Popover drawer (no backdrop) -->
<div class="drawer:bottom" popover>
  <div class="drawer-content">...</div>
</div>
```

**Trigger:** Use `popovertarget` attribute on buttons.

```html
<button popovertarget="nav-drawer">Open Menu</button>
```

**Responsive pattern:** Pair with `.desktop` / `.mobile` utilities to show inline nav on desktop, drawer on mobile.

```html
<nav id="nav" class="desktop" style="grid-area: 2/1/4/2;">...</nav>
<dialog id="nav-drawer" class="drawer:left mobile" popover="manual">...</dialog>
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

- Avoid `!important` — unnecessary with proper CUBE usage; if needed, add an `important` layer
- Reserve `data-*` attributes for Datastar only

