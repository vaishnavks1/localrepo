# Bolt's Journal - Critical Learnings

## 2025-08-22 - Standards Mode and Favicon Data-URI for Minimal HTML
**Learning:** Barebone HTML files without `<!DOCTYPE html>`, `<meta charset="UTF-8">`, or a favicon link cause browsers to render in Quirks Mode, perform encoding sniffing, and issue 404 network requests for `/favicon.ico`.
**Action:** Always include `<!DOCTYPE html>`, early `<meta charset="UTF-8">`, and `<link rel="icon" href="data:,">` while preserving any raw text nodes present in the initial markup.
