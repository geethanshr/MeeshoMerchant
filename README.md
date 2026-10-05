# Meesho Merchant interactive demo

A responsive, credential-free concept prototype for the proposed Panipat–Karnal home-textile service. All products, suppliers, prices, quotes, messages and transactions are illustrative. No actual payment, purchase, shipment, verification or lending occurs.

## Plain-language UI

Use the final deck's promise, **Better buying for independent shops**, consistently. **One buying job** means confirming the buying list, comparing costs, agreeing terms, tracking delivery and checking receipt. The proposed **buying help fee** is ₹349 for one standard buying job, or ₹1,199/month for up to four standard buying jobs. These remain proposed prices in a labelled demo.

| UI wording | Meaning |
| --- | --- |
| Minimum quantity | The smallest order the supplier offers |
| Prices for larger orders | The listed quantity-based prices; buy only what the shop needs |
| Supplier price offer | The supplier's price and terms for the exact requested quantity |
| Delivery charge | The separate charge for delivering goods |
| Buying help fee | The separate optional fee for one buying job |
| Cost of paying earlier (estimate) | A comparison estimate, not a collected charge |
| Possible losses (estimate) | A planning estimate, not insurance or a collected charge |
| Confirm stock | Confirm the order's stock before packing |
| Report a problem | Record missing, damaged, late or incorrect goods for review |

Prefer these labels in controls, walkthroughs and explanations. Keep `Concept demo · sample data` and simulated-payment wording visible; simpler language does not make an estimate an observed result or a demo action a live transaction.

## Open it

Live demo: https://geethanshr.github.io/MeeshoMerchant/

GitHub Pages publishes the root of `main`. Verified pushes update the website automatically.

Double-click `index.html` in this folder. All shipped assets are local; no installation or internet is needed for the demo.

For the easiest handoff, open `outputs/merchant-demo/Meesho_Merchant_Demo.html` from the research project root, or `dist/Meesho_Merchant_Demo.html` when building from the standalone GitHub checkout. It contains the complete app, photographs and font in one file. The accompanying ZIP includes that standalone file and editable sources. Regenerate both with `python build-demo.py` from this folder after source edits.

For a consistent local preview, run `node server.mjs` from this folder and open **http://127.0.0.1:4173**. The server binds only to the local computer. `MERCHANT_PORT` can select another port. An active preview was started on port 4173 during creation.

Browser-local storage remembers demo data. Buyer and seller roles share that data in the same browser and origin. Opening the file and the server URL creates separate sessions. Other devices do not synchronise. This is a self-contained front-end prototype, not a production marketplace.

## A five-minute presentation

1. Enter as buyer. Follow the seven-step contextual spotlight walkthrough, or choose “Explore on my own.” Replay from **Walkthrough** in the desktop header or **Guide** on mobile. The seller walkthrough has six steps.
2. Open **My requests → Sage bath towels → Compare quotes**. Three routes show full cost, minimums, samples, cash timing and a separate service fee. Toggle the credit requirement: prepaid suppliers become unsuitable.
3. Choose the manufacturer quote. Simulate sample review, confirm its checklist, then place the simulated goods order. The allowances are included in comparison, not collected as payment.
4. Switch to seller. Open **Orders → Confirm capacity → Mark packed → Simulate dispatch**. Saving a request or quoting does not commit production.
5. Switch back to buyer. Open **Orders → Record received goods**. A discrepancy can be recorded without promising a refund. A received order can populate a repeat basket.
6. Show optional buying help: a proposed ₹349 for one standard buying job, or a simulated ₹1,199 monthly plan for up to four jobs. One or three jobs favour per-use. Basic discovery and self-coordination remain free.

To demonstrate the custom-sourcing challenger: buyer **My requests → New request**, select bounded customisation and supply exact specifications. Switch to seller **Buyer requests → Prepare quote**. Submit complete terms and switch back to compare. Custom quotes require sample approval. This prototype does not model a real production pool or guarantee compatible demand.

For quantity pricing: open a product, move its quantity slider or select a price-break card, then add the selected units. In **My basket**, adjust each line's slider to see its unit price, goods total, freight and payable update live. Quantities remain between minimum lot and available stock. Catalogue tiers begin at MOQ, 2×MOQ, 4×MOQ and 8×MOQ, with default discounts of 0%, 3%, 6% and 8%; tiers above stock are omitted. These are all-unit tiers: the applicable discount applies to every selected unit. Buy only the quantity already needed—a lower unit price can still require more cash and does not imply required sales growth. Request quotes keep their exact requested quantity and separate quoted terms; catalogue tiers do not alter them.

For listing management: seller **My stock → Add listing**, edit price/minimum/stock, set quantity discounts or pause a listing. Discounts may increase or stay equal as quantity rises and are capped at 30%. Switch to buyer to see the updated catalogue. Newly created listings use one of the locally shipped demo photos.

**Reset:** header question-mark button → Reset all demo activity → confirm. Only this prototype's local state is cleared; research files are unaffected.

## Included features

- 24 illustrated catalogue products across towels, bedsheets, cushion covers, table linen, kitchen linen and throws/blankets.
- Search, categories, price/minimum sorting, saved products, product detail, stock-bounded quantity sliders and seller-editable all-unit price tiers.
- Buyer basket, optional buying assistance, proposed plan comparison and simulated checkout.
- Structured buyer requests with usable quantities, specifications, deadline, budget and payment needs.
- Seller request shortlist, save/pass, clarification messages and private structured quote submission.
- Full-cost comparison, editable incumbent baseline, credit-fit checks, sample approval and clear supplier identity before a demo order.
- Capacity, packing, dispatch, buyer receipt, discrepancies and repeat baskets.
- Editable/pausable supplier stock, comparison CSV and downloadable explicitly marked demo order records.
- Seven buyer and six seller contextual spotlight steps, local persistence and repeatable reset.
- Keyboard focus, modal focus trapping, labelled fields, reduced-motion support and responsive navigation.

## Boundaries

No external users, accounts, login, real supplier verification, tax determination, payments, escrow, credit underwriting, finance interest, guarantees, inventory reservations or carrier integration. Contact detection is a simple demo regex, not secure moderation. Images represent product families, not audited exact SKUs. Role switching is deliberately unrestricted; it is not access control. Monthly activation and order confirmations are simulated and explicitly labelled. The initial tour populates a demonstration basket but creates no order.

The complete-cost example uses the project's single-assignment model: ₹18,000 goods, ₹600 freight, ₹150 sample, ₹349 procurement fee, ₹200 loss allowance and roughly ₹266 cash-timing allowance. Rounded model total ₹19,565; demo payable ₹19,099. The latter excludes allowances. Inputs and resulting savings remain assumptions.

## Files and checks

`index.html`, `styles.css`, `app.js` are the app. `server.mjs` is the optional local server. `assets/products.png` is the generated product photography atlas; `assets/products.provenance.json` records its source/prompt. Nunito Sans and its OFL license are included locally.

For developer checks, run `npm install`, `npx playwright install chromium`, then `npm start` in one terminal and `npm test` in another. Tests use port 4173 and a separate headless browser. Optional `PLAYWRIGHT_MODULE` and `CHROME_PATH` environment variables select an existing installation. `tests/demo.test.cjs` covers the connected workflows; `tests/quantity.test.cjs` covers tier maths, seller-to-buyer pricing, checkout and all spotlight steps at laptop and phone widths; `tests/offline.test.cjs` covers direct-file entry. JSON reports sit next to each test. Review screenshots are generated under `.impeccable/review/` and are excluded from Git.

Validation completed: 33 workflow checks and 63 quantity/spotlight checks passed, including connected buyer/seller transactions, credit-fit restrictions, sample gating, local persistence, reset and phone overflow checks down to 320px. Direct-file offline entry also passed with all 24 products and the local font loaded. The changed screens also received a focused visual review. These are prototype software checks, not pilot outcomes.

The prototype illustrates workflows from the project research and submission brief; interactions and demo orders are not pilot evidence. New code must preserve that distinction.

## Publishing preference

The user requests that demo changes be pushed directly to [MeeshoMerchant](https://github.com/geethanshr/MeeshoMerchant). Keep that repository scoped to demo sources, assets and demo documentation; exclude the parent project's private research and other non-demo material. The user approved making the demo repository public on 5 October 2026 to enable GitHub Pages. Keep the research project private; only this demo is published. Future platform changes should be verified, committed and pushed directly to this repository.

## Pricing alignment, 4 October 2026

Proposed buying help fees are ₹349 for one standard buying job and ₹1,199/month for up to four standard buying jobs. Four individual jobs cost ₹1,396; the plan saves ₹197. These are proposed demo prices, not observed willingness or actual payments. All simulation labels remain in place.
