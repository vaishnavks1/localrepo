# Bolt's Journal

## 2025-05-18 - HTML document structure standards and charset optimization
**Learning:** Adding standard HTML5 DOCTYPE prevents Quirks Mode parsing overhead and layout inconsistencies, while specifying `<meta charset="UTF-8">` within the first 1024 bytes avoids browser encoding detection buffering. Adding an inline favicon data URI prevents automatic 404 network requests for `/favicon.ico`.
**Action:** Always structure minimal HTML documents with DOCTYPE, meta charset, and favicon URI to maximize document parsing and loading efficiency.
