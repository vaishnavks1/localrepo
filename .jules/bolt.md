# Bolt's Journal

## 2025-02-14 - Standardizing Static HTML Layout
**Learning:** In ultra-minimal repositories where `index.html` has no explicit `<html>`, `<head>`, or `<body>` structure and contains text nodes directly, adding these tags standardizes browser layout processes. Adding `<!DOCTYPE html>` triggers Standards Mode instead of Quirks Mode, while a data-URI favicon (`<link rel="icon" href="data:,">`) prevents redundant and wasteful 404 network requests from browsers trying to resolve `/favicon.ico`.
**Action:** When working with bare HTML, restructure it cleanly while keeping all original text nodes and content perfectly preserved.
