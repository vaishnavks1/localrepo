# Bolt's Journal - Critical Learnings

## 2025-07-23 - Static HTML Performance Standards
**Learning:** For extremely minimal or legacy static HTML web pages, browsers default to 'Quirks Mode' if a `<!DOCTYPE html>` is missing. This introduces non-standard layout behaviors and rendering performance overhead. Specifying `<!DOCTYPE html>`, `<meta charset="UTF-8">` early in `<head>` to prevent character encoding sniffing delays, and `<link rel="icon" href="data:,">` to avoid expensive 404 network requests for favicon.ico are high-impact, lightweight optimizations.
**Action:** Always verify compatibility mode in static pages with `document.compatMode === 'CSS1Compat'` (Standards Mode) and eliminate redundant network requests for assets like favicons when not provided.
