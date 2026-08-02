## 2025-08-02 - Initial Setup and Minimal HTML Performance Insights
**Learning:** For extremely minimal HTML static websites (like this project containing only "vaishnav" text), adding standard tags can improve parsing speed, prevent browser quirks (quirks mode vs standards mode), and avoid unnecessary network favicon request errors.
**Action:** Always add <!DOCTYPE html>, UTF-8 charset, and a inline data URI favicon to avoid extra roundtrips and ensure standard rendering mode without introducing external files.
