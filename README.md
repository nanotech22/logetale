# Leo Herr static website

This is the Flask/Jinja site converted to plain HTML/CSS/JavaScript for GitHub Pages.

## Before publishing

Copy the asset folders from the old Flask project into this project so these paths exist:

- `static/css/index.css`
- `static/css/personal.css`
- `static/css/contact.css` (if you used one)
- `static/img/` (all site images)
- `static/pdf/` (CV and student-review PDFs)

The uploaded files did not include those assets, so placeholders/directories are included but not the actual files.

## Publish with GitHub Pages

1. Create a GitHub repository and put the contents of this folder at the repository root.
2. Commit and push.
3. In GitHub: **Settings -> Pages -> Build and deployment -> Deploy from a branch**.
4. Select your publishing branch (usually `main`) and `/ (root)`.
5. When the site works at the GitHub Pages URL, add your custom domain in the same Pages settings screen and update DNS at Namecheap as GitHub instructs.

## What changed

- Removed Flask, Jinja, WTForms, Flask-Mail, sitemap extension, Heroku Procfile/runtime requirements, and Python configuration.
- Replaced `url_for(...)` with relative links that work on GitHub Pages.
- Preserved the existing JavaScript used by the BibTeX buttons.
- Replaced the server-side contact form with an email link because GitHub Pages cannot run Flask or send mail.
- No API keys or server secrets are included.

## Security

The old uploaded `config.py` contained live-looking SendGrid and reCAPTCHA secrets. Rotate/revoke those credentials before doing anything else with the old repository, and remove them from Git history if that repository has ever been public.
