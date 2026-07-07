## 2024-05-22 - [Optimizing Skeleton Repositories]
**Learning:** Even in a minimal skeleton repository, there are foundational performance wins.
1. Adding `<!DOCTYPE html>` ensures the browser uses "no-quirks mode," which is the fastest and most modern rendering path.
2. Adding `<link rel="icon" href="data:,">` eliminates a redundant 404 network request for `/favicon.ico` that browsers make by default.
**Action:** When faced with an empty or minimal project, implement these foundational optimizations to set a performant baseline.
