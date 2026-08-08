# Bolt's Journal

## 2025-02-14 - Standardizing Static HTML Document Structure for Performance
**Learning:** For static HTML sites, omission of a DOCTYPE triggers Quirks Mode in browsers, which degrades rendering performance. Additionally, the lack of a specified charset early in the document forces the browser to perform charset sniffing, stalling parsing. Finally, missing favicon files result in wasteful 404 network requests, costing valuable round-trips and server load.
**Action:** Always structure even the simplest HTML files with `<!DOCTYPE html>`, `<meta charset="UTF-8">`, and a lightweight data-URI favicon `<link rel="icon" href="data:,">` to prevent these inefficiencies.
