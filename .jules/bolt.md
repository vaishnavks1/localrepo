# Bolt's Journal - Critical Learnings Only

## 2024-07-22 - Optimizing Minimal Static HTML Pages
**Learning:** For extremely minimal, static HTML templates with uncontained text elements, we can significantly speed up rendering, prevent standards-quirks-mode slowdowns, and avoid wasteful favicon 404 network requests by adding proper doctype, encoding metadata, and a dummy favicon URI while carefully preserving all existing DOM elements (including text nodes).
**Action:** Always include Standard Mode DOCTYPE, UTF-8 meta element, and data-URI favicon. Ensure all raw text nodes are preserved exactly as they are.
