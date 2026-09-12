# Bolt Journal - Critical Learnings

## 2024-09-20 - Standard HTML5 Doctype, Charset, and Data-URI Favicon
**Learning:** Raw HTML snippets without `<!DOCTYPE html>` force browsers into Quirks Mode (`BackCompat`), which uses legacy rendering algorithms. Adding explicit `<!DOCTYPE html>`, `<meta charset="UTF-8">`, and a data-URI favicon `<link rel="icon" href="data:,">` switches the engine to Standards Mode (`CSS1Compat`), prevents charset detection delays, and eliminates 404 favicon network requests.
**Action:** Always ensure minimal entry HTML documents declare standard DOCTYPE, UTF-8 charset, and inline data-URI favicon when external favicon assets are absent.
