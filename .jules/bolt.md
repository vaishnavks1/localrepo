## 2025-01-22 - Static HTML Performance Optimizations
**Learning:** For extremely minimal, static HTML single-page files, several critical performance and loading speed improvements can be made with zero code complexity:
1. Adding a `<!DOCTYPE html>` preamble triggers HTML5 Standards Mode (`document.compatMode === 'CSS1Compat'`), preventing browsers from falling back to Quirks Mode, which can cause slow layout calculations and rendering inconsistencies.
2. Placing `<meta charset="UTF-8">` as the first tag inside the `<head>` prevents the browser from having to sniff character encoding, which causes re-parsing of the page and delayed rendering.
3. Specifying `<link rel="icon" href="data:,">` prevents automatic and wasteful 404 network requests for `/favicon.ico`, improving server efficiency and eliminating unnecessary latency.
**Action:** Always include these standard best-practice optimizations in static HTML structures without breaking existing text elements or styling.
