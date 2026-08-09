## 2025-08-09 - Static HTML Performance Standards
**Learning:** Minimal, unformatted static HTML pages lack doctype, charset, and favicon definitions. This forces browsers into Quirks Mode (rendering slower), delays processing due to character encoding sniffing, and wastes network requests on a non-existent `/favicon.ico` yielding 404 errors.
**Action:** Always wrap minimal HTML content in valid HTML5 structures, specify standard charset early, and use inline data-URI favicons to guarantee immediate CSS1Compat mode, fast parsing, and zero redundant network requests.
