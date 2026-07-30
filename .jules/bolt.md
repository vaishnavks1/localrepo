# Bolt's Journal

## 2024-07-30 - Standards Mode & Resource Efficiency in Static HTML
**Learning:** For extremely minimal, static HTML web projects, standard browser performance optimizations can be made without adding heavy dependencies. Specifying a proper doctype initiates Standards Mode (`CSS1Compat`) instead of Quirks Mode, leading to faster layout rendering. Declaring a charset meta tag early prevents encoding sniffing. Adding a data URI favicon stops browsers from triggering unnecessary, wasteful, and slow 404 network requests to `/favicon.ico`.
**Action:** Always include `<!DOCTYPE html>`, `<meta charset="UTF-8">`, and `<link rel="icon" href="data:,">` when preparing static web documents. Ensure any pre-existing text nodes or tags are fully preserved.
