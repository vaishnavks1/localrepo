## 2025-08-10 - HTML standards mode and data-URI favicon optimization
**Learning:** In a minimal web page missing proper document scaffolding, browsers run in Quirks Mode and automatically attempt to fetch `favicon.ico`, resulting in a wasteful, high-latency 404 network request.
**Action:** Always wrap minimal HTML content with a valid HTML5 doctype declaration (`<!DOCTYPE html>`) to trigger Standards Mode and add `<link rel="icon" href="data:,">` to instantly resolve and prevent the wasteful favicon 404 network request.
