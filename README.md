# FRZ Generations main site

A static site: no build step, no dependencies.

## 1. Set your real domain (important)
SEO files need the site's real address. They currently use the placeholder `https://frzgenerations.netlify.app`.
Run once, with your real address, before you deploy:

    python3 set-domain.py https://your-real-domain.com

(Or find and replace `https://frzgenerations.netlify.app` in `index.html`, `404.html`, `robots.txt`, `sitemap.xml`, `llms.txt` and `llms-full.txt`.)

## 2. Deploy
Upload this folder to Netlify (drag and drop, or push to GitHub). `netlify.toml` already sets security headers, long cache for images, and correct content types.

## 3. After it is live
1. Google Search Console: add the site, verify it, then submit `/sitemap.xml`. Paste the verification tag into the commented block in the `<head>` of `index.html`.
2. Bing Webmaster Tools: add the site (you can import from Search Console) and submit the same sitemap.
3. Check structured data at https://search.google.com/test/rich-results and https://validator.schema.org/ using your live URL.
4. Test the share card by pasting your URL into WhatsApp, Instagram or the Facebook Sharing Debugger.

## What is in this folder
| File | Purpose |
|---|---|
| `index.html` | The page, with a light/dark theme switch (remembers the visitor's choice, follows their device by default), title, description, canonical, Open Graph, Twitter cards and JSON-LD (Organization, Person, WebSite, WebPage, ItemList of the six public platforms, FAQPage) |
| `sitemap.xml` | Page plus image sitemap (all logos) |
| `robots.txt` | Allows all crawlers, including AI answer engines, and points to the sitemap |
| `llms.txt`, `llms-full.txt` | Plain-language summary and Q&A for AI assistants |
| `site.webmanifest` | Installable-app metadata and icons |
| `favicon.ico`, `assets/icons/*` | Favicons and app icons made from the FRZ Generations logo |
| `assets/og-image.png` | 1200x630 social share image |
| `assets/logos/*` | All branch logos as optimised files |
| `404.html` | Branded not-found page (not indexed) |
| `netlify.toml` | Headers, caching and content types |

## Keeping SEO healthy
- The FAQ on the page and the FAQ in the JSON-LD must say the same thing. If you edit one, edit the other.
- When you change the page, update `<lastmod>` in `sitemap.xml` and `dateModified` in the JSON-LD.
- 1HOS is private, so it has no link and is not listed as an application in structured data.
- Team members are not listed in structured data on purpose, to keep students' names out of machine-readable data.
