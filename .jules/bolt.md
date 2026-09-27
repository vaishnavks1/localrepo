# Bolt's Journal - Critical Learnings

## 2026-03-27 - Minimal HTML Standards Mode and Parsing Efficiency
**Learning:** Raw text and missing standard HTML boilerplates (`<!DOCTYPE html>`, `<meta charset="UTF-8">`, favicon) force browsers into Quirks Mode (`document.compatMode === 'BackCompat'`), leading to rendering layout quirks and encoding sniffing overhead.
**Action:** Always include `<!DOCTYPE html>`, explicit charset, and empty data-URI favicon in static HTML files while preserving existing text nodes.
