## 2024-08-13 - Standards Mode, Meta UTF-8, and Favicon 404 Optimization
**Learning:** For extremely minimal, static HTML templates (such as just an un-wrapped text node and a tag), browsers default to "Quirks Mode" (`document.compatMode === 'BackCompat'`), which reduces CSS rendering efficiency and causes non-standard parsing. Additionally, omitting standard viewport/charset/favicon declarations leads to encoding-sniffing parsing pauses and wasteful favicon.ico 404 network requests.
**Action:** Always wrap minimal HTML content with a proper HTML5 document structure:
1. `<!DOCTYPE html>` to trigger Standards Mode.
2. `<meta charset="UTF-8">` placed in the first 1024 bytes of the document to optimize tokenization and prevent parsing pauses due to character encoding sniffing.
3. `<link rel="icon" href="data:,">` to avoid wasteful network roundtrips caused by 404s for favicon.ico.
