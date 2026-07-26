# Bolt's Journal

## 2024-07-26 - Static Web Optimization
**Learning:** For extremely minimal, static single-page websites (even those with a single word or heading), missing standard components (like `<!DOCTYPE html>`, meta charset, and favicons) triggers quirks mode in modern browsers, causes unneeded DNS/network lookups (like 404s for /favicon.ico), and slows down initial rendering engine initialization.
**Action:** Always structure even the simplest html files with standards mode components and a data URI favicon to avoid wasteful network requests.
