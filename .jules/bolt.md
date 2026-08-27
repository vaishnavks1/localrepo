# Bolt's Journal

## 2024-09-20 - HTML Standards Mode and Encoding Initialization
**Learning:** Minimal static HTML files lacking DOCTYPE render in Quirks Mode, slowing layout parsing and triggering default browser favicon 404 network probes.
**Action:** Always declare `<!DOCTYPE html>`, early `<meta charset="UTF-8">`, and inline data-URI favicon in static HTML templates.
