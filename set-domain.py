#!/usr/bin/env python3
"""Usage: python3 set-domain.py https://your-real-domain.com
Rewrites the placeholder domain in every SEO file (canonical, Open Graph, JSON-LD, sitemap, robots, llms)."""
import sys, pathlib
OLD = "https://frzgenerations.netlify.app"
if len(sys.argv) != 2 or not sys.argv[1].startswith("http"):
    sys.exit("Usage: python3 set-domain.py https://your-real-domain.com")
new = sys.argv[1].rstrip("/")
root = pathlib.Path(__file__).parent
for name in ["index.html", "404.html", "robots.txt", "sitemap.xml", "llms.txt", "llms-full.txt"]:
    p = root / name
    if p.exists():
        s = p.read_text(encoding="utf-8")
        p.write_text(s.replace(OLD, new), encoding="utf-8")
        print("updated", name)
print("Done. Domain is now", new)
