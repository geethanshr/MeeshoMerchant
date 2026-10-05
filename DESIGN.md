---
name: Meesho Merchant demo
description: Familiar berry commerce for a connected buyer and supplier concept demo.
colors:
  primary: "#9f2089"
  primary-hover: "#821b70"
  plum: "#321437"
  pink: "#f8e9f4"
  hero: "#f5e8ed"
  paper: "#faf9f7"
  surface: "#fff"
  text: "#302a32"
  muted: "#716975"
  border: "#e7dfe5"
  field-border: "#ddd2dd"
  focus: "#ac6cac"
  success: "#24694e"
  success-surface: "#eaf5ee"
  warning: "#82541a"
  warning-surface: "#fff2db"
typography:
  display:
    fontFamily: "Nunito, 'Segoe UI', sans-serif"
    fontSize: "54px"
    fontWeight: 800
    lineHeight: 1.18
    letterSpacing: "-.025em"
  headline:
    fontFamily: "Nunito, 'Segoe UI', sans-serif"
    fontSize: "38px"
    fontWeight: 800
    lineHeight: 1.18
    letterSpacing: "-.025em"
  title:
    fontFamily: "Nunito, 'Segoe UI', sans-serif"
    fontSize: "26px"
    fontWeight: 800
    lineHeight: 1.3
    letterSpacing: "-.025em"
  body:
    fontFamily: "Nunito, 'Segoe UI', sans-serif"
    fontSize: "15px"
    lineHeight: 1.5
  label:
    fontFamily: "Nunito, 'Segoe UI', sans-serif"
    fontSize: "13px"
    fontWeight: 800
rounded:
  field: "7px"
  control: "8px"
  panel: "12px"
  tour: "13px"
  modal: "14px"
  pill: "30px"
spacing:
  compact: "8px"
  small: "12px"
  medium: "16px"
  large: "24px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    rounded: "{rounded.control}"
    padding: "11px 18px"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.control}"
    padding: "11px 18px"
  button-quiet:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    rounded: "{rounded.control}"
    padding: "11px 18px"
  field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.field}"
    padding: "11px 12px"
  panel:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.panel}"
    padding: "24px"
  navigation-active:
    backgroundColor: "{colors.pink}"
    textColor: "{colors.primary}"
    rounded: "{rounded.control}"
    padding: "12px"
  filter-active:
    backgroundColor: "{colors.pink}"
    textColor: "{colors.primary}"
    rounded: "{rounded.pill}"
    padding: "7px 14px"
---

# Design System: Meesho Merchant demo

## Overview

**Creative North Star: "Familiar Meesho commerce"**

Preserve the user-pinned Meesho identity: berry-magenta actions, deep plum headlines, warm white canvas, subtle purple accents and useful home-textile photography. The interface feels approachable and practical, with simple English, clear quantities and complete buying terms. This is a code-first implementation; no approved interface image composition defines the layout.

**Key Characteristics:**
- Familiar commerce identity and product-led discovery.
- Compact, legible controls and calm bordered work surfaces.
- Connected buyer and supplier views with persistent prototype identification.

**The Honest Demo Rule.** Keep the concept label visible in both desktop and mobile headers. Stock, quotes, suppliers and order activity are illustrative; styling must not imply verified or live transactions.

## Colors

Primary berry identifies actions, links, selected navigation and selected filters. Plum anchors headings and totals; pale pink marks selected surfaces. The hero uses a softer rose field. Paper surrounds white panels, while muted text and fine borders establish hierarchy without heavy decoration. Success green appears on completed milestones and positive notices; amber marks review and issue states. Pair status colors with words and icons. The focus color supplies keyboard outlines.

## Typography

The locally hosted Nunito Sans asset (`assets/nunito-sans.woff2`) is registered under the CSS family name `Nunito`, with variable weights (200–900) and `font-display: swap`. Segoe UI and sans-serif are fallbacks. Headlines are bold with tight tracking; prices use tabular numerals and strong weight.

Desktop entry display uses the display role; workspace headings use headline. At the intermediate breakpoint, entry display becomes (44px). Mobile body becomes (14px), entry display (38px), page headline (27px), and compact catalogue hero headline (22px, line-height 1.25). Product titles are (15px) on desktop and (13px) on mobile. Small metadata remains subordinate to labelled controls.

## Layout

Desktop uses a sticky header (76px), left sidebar (224px), and flexible main column capped at (1560px), with main padding (30px 36px 70px). At widths up to (1150px), sidebar becomes (195px), main padding (25px), and catalogue drops from four to three columns. At widths from (1650px), it uses five columns.

At widths up to (760px), header becomes (66px), sidebar gives way to fixed bottom navigation, and main padding is (22px 18px 105px). Catalogue retains two equal columns with (12px) gaps and square photography. Filters scroll inside their own row. Feed, plans, split workspaces, quotes and product details collapse to one column. Forms retain two columns until the (370px) breakpoint, where fields and role-entry cards stack.

The final mobile catalogue hero is compact: copy padding (18px), a small photograph (78px square) at bottom right, reserved copy/action width beside it, and no floating image badge. This replaces the earlier stacked full-width image treatment. Below the brand, `Concept demo · sample data` stays visible on mobile. The walkthrough control displays `Guide`; its desktop label is `Walkthrough`.

**The Useful Space Rule.** Preserve room for products and decisions on a phone; keep the compact hero and two-column catalogue rather than expanding decorative photography above discovery.

## Elevation & Depth

Normal cards and panels are flat white surfaces separated by thin borders and tonal backgrounds. Depth belongs to floating layers: save controls use (`0 2px 10px #34212e14`), walkthrough uses (`0 12px 40px #32143722`), modal uses (`0 18px 65px #1b082c33`), and toast uses (`0 4px 20px #32143730`). Modal backdrop is translucent plum (`#25122780`).

**The Floating Layer Rule.** Reserve stronger shadows for walkthroughs, dialogs and feedback; do not apply modal depth to ordinary product or request cards.

## Shapes

Use gently rounded rectangular controls and panels according to the frontmatter roles. Photography clips to card corners. Filter pills are fully rounded; save and close controls are circles. Fine borders define editable fields and panels. Selected quotes use a stronger berry border (2px); selected service choices use a berry stroke and pale fill. Authored SVG icons use consistent strokes, normally (20px), with compact mobile header icons (17px).

## Components

### UI language

Lead with the final deck's plain-language promise, **Better buying for independent shops**. Define **one buying job** as confirming the buying list, comparing costs, agreeing terms, tracking delivery and checking receipt. Label the separate optional charge **buying help fee**; current proposed demo prices are ₹349 for one standard buying job and ₹1,199/month for up to four standard buying jobs.

Use the short glossary consistently: **minimum quantity** for the smallest supplier order; **prices for larger orders** for catalogue quantity prices; **supplier price offer** for exact-quantity quoted terms; **delivery charge** for freight; **cost of paying earlier (estimate)** for the cash-timing comparison; **possible losses (estimate)** for the planning loss allowance; **confirm stock** for the seller's stock confirmation; and **report a problem** for recording an order issue. Keep quantity-choice cautions, estimate labels and `Concept demo · sample data` visible. These copy choices preserve the existing proposal and simulated behavior.

### Buttons

Primary actions use berry fill, white text, bold weight and minimum height (44px). Secondary actions use white fill and a pale berry border; quiet actions are transparent with muted text. Small buttons use padding (7px 11px) and minimum height (36px); catalogue add buttons have a denser local variant. Primary hover darkens the fill; secondary/quiet hover add pale tones. Disabled buttons dim to opacity (.48). Interactive elements share keyboard outline (3px) with offset (3px).

### Fields and filters

Fields have white fill, a fine field border, field radius and explicit labels above. Helper text uses normal weight. Search reserves left padding (43px) for an icon. Selected filter pills use pale pink, berry text and a stronger pink border. Native selects, checkbox/radio accents and browser validation remain visible. Textareas resize vertically.

### Cards and photography

Product cards use panel radius, fine border, square photos, title/specification hierarchy and explicit add action. The catalogue uses 24 photographic cells from `assets/products.png`, a six-by-four sprite; retain correct cell position and square crop to avoid exposing adjoining products. Photos are illustrative demo assets. Panel padding becomes (19px) on mobile; product body padding becomes (11px). Demand cards place thumbnails beside details; seller inventory exposes compact stock/price metadata on mobile.

### Quantity pricing

Product details and basket lines use a labelled native range slider with berry accent, selected-quantity output and visible minimum/stock limits. The slider spans MOQ through available stock in single-unit increments. Four compact price-break cards show thresholds at MOQ, 2×MOQ, 4×MOQ and 8×MOQ, omitting thresholds above stock. Default discounts are (0%, 3%, 6%, 8%); seller listing fields allow non-decreasing discounts capped at (30%). These are illustrative all-unit tiers, applying the selected tier to every unit.

Price-break cards use field radius, white fill and a fine border; the selected card uses a stronger berry border (2px), pale pink fill and plum text. Selected unit price and goods total update live; basket goods, freight, optional service fee and payable update with quantity. Keep the next-break hint alongside the explicit caution that a lower unit price may require more cash. Quantity choice supports an existing required purchase and must not imply required sales growth. Request quotes retain exact requested quantity and independently quoted terms; catalogue tiers do not change them.

### Navigation and shared network

Desktop active navigation has pink fill and berry text; hover adds a lighter wash. Mobile navigation uses icons above short labels and berry active text. Role switching remains accessible even where a narrow header hides its visible role text. The seller workspace represents the shared demo supplier network, including mixed baskets. Switching roles preserves requests, quotes, stock and orders in browser-local state.

### Walkthrough and dialogs

The replayable walkthrough has seven buyer steps and six seller steps. It navigates to actual screens and uses a contextual spotlight: a berry border (2px), rounded corners (10px) and a translucent surrounding scrim (`rgba(34,18,32,.38)`). The spotlight allows pointer interaction through it. The guide shows labelled progress, Back/Next, exit and completion controls, and dynamically positions beside, above or below its target; scroll and resize update that placement. Desktop width is (385px); mobile uses side gutters (12px) and reserves room above bottom navigation. Guide content scrolls within a viewport-bound maximum height. Entrance lasts (.25s). The persistent labelled Guide reopens it.

Dialogs center in a plum backdrop, use modal radius, width capped at (880px), narrow variant (520px), and scroll within (92vh). Mobile padding reduces to (20px) and maximum height becomes (94vh). Close, backdrop click and Escape dismiss; keyboard focus is trapped while open and restored on close. Toast is a polite live status message above mobile navigation. Reduced-motion preference disables animations, transitions and smooth scrolling.

## Do's and Don'ts

### Do:
- **Do** preserve the berry identity, warm paper canvas and useful textile photography.
- **Do** keep Concept demo identification and the labelled mobile Guide visible.
- **Do** show full terms, clear quantities and separate optional service charges in legible work panels.
- **Do** retain keyboard focus, labelled fields, SVG icons and reduced-motion behavior.
- **Do** preserve shared buyer/supplier state when switching roles.

### Don't:
- **Don't** replace the pinned commerce aesthetic with a novel identity.
- **Don't** expand the mobile catalogue hero into a large photographic block above products.
- **Don't** use live-payment, verified-supplier or achieved-result styling for illustrative data.
- **Don't** substitute generic image placeholders for the implemented product-photo cells.

Source of truth: `index.html`, `styles.css`, `app.js`, and durable brand commitments in `../PRODUCT.md`. This document records implementation; it does not certify a whole-surface review pass.

Publishing preference: push verified demo changes directly to `https://github.com/geethanshr/MeeshoMerchant`, scoped to demo sources, assets and demo documentation. The user approved making the demo repository public on 5 October 2026. The live GitHub Pages demo is `https://geethanshr.github.io/MeeshoMerchant/`. Exclude private parent-project research; only the demo is published.
