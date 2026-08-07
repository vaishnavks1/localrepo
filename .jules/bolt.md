## 2025-08-07 - Avoid Wasteful Favicon Requests and Encoding Sniffing
**Learning:** For static HTML websites, specifying standard HTML structures helps trigger Standards Mode (`document.compatMode === 'CSS1Compat'`), while adding `<meta charset="UTF-8">` prevents browser encoding-sniffing. Also, using `<link rel="icon" href="data:,">` prevents wasteful default favicon.ico 404 network requests, which can block or delay initial paint.
**Action:** Always structure minimal static web pages properly with standard head attributes and data-URI icons.
