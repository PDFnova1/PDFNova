# PDFNova — Final Production Integration Package

## Architecture
- `frontend/index.html`: Blogger-compatible application frontend.
- `backend/`: FastAPI processing service.
- `docker-compose.yml`: reproducible backend deployment.
- Backend secrets stay server-side.

## Important deployment requirement
Replace `https://YOUR-BACKEND-DOMAIN.example.com` in the frontend CONFIG with the real HTTPS API origin before publishing. Also set the backend CORS allow-list to the real Blogger/custom domain.

## Correctness policy
Browser tools remain browser tools. Advanced conversions/security/OCR/AI do not claim success when the backend is unavailable. OCR and layout reconstruction are inherently document-dependent; the service should not promise pixel-perfect preservation for arbitrary scanned documents.

## Production checklist
- HTTPS on backend
- Strong API key or authenticated user/session layer
- Exact CORS origins (never `*` with credentials)
- Reverse proxy/WAF and rate limiting
- Object/temp storage lifecycle cleanup
- Monitoring and error logging without document content
- Virus/malware scanning if accepting untrusted files at scale
- Legal/privacy/retention policy published on the site
- Configure AdSense/analytics IDs only after deployment
