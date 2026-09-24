# PDFNova deployment

## 1. Backend
- Copy `backend/.env.example` to `backend/.env`.
- Set a long random `PDFNOVA_API_KEY`.
- Set `CORS_ORIGINS` to your exact Blogger/custom domain(s).
- `docker compose up -d --build`.
- Put the service behind HTTPS (reverse proxy/CDN/WAF).
- Verify `GET /health` returns `{"ok":true,...}`.

## 2. Frontend
In `frontend/index.html`, replace:
`https://YOUR-BACKEND-DOMAIN.example.com`
with your HTTPS backend origin.

Never put the backend provider's private API keys in this file.

## 3. Blogger
- Back up the existing Blogger theme.
- Import `Blogger_PDFNova_Theme.xml` in Blogger Theme > Restore/Upload.
- Before publishing, replace the placeholder canonical domain in the theme if present.
- Verify mobile and desktop views.

## 4. Operational safeguards
- Use rate limiting at the reverse proxy.
- Limit concurrent conversions and CPU/memory.
- Keep uploaded files temporary; do not log file contents.
- Add malware scanning before allowing public uploads at scale.
- Configure backups/monitoring for the backend configuration, not user documents.
- Publish privacy, retention and acceptable-use policies.

## 5. Important accuracy note
No document converter can guarantee identical formatting for every arbitrary PDF, especially scans with unusual fonts, handwriting, tables, multi-column layouts, or complex vector graphics. PDFNova should show the actual conversion result and never claim 100% fidelity.
