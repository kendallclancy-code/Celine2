# Celine Dion Paris Ticket Monitor

Configured for:
- 2 tickets together
- Oct 16, 2026 preferred
- Oct 17, 2026 backup
- Max €350 per ticket
- Email alerts via Gmail

## Setup

1. Create a private GitHub repository.
2. Upload all files from this package.
3. In GitHub:
   Settings -> Secrets and Variables -> Actions
4. Add:
   - EMAIL_USER
   - EMAIL_PASSWORD (Gmail App Password)
   - EMAIL_TO
5. Go to Actions and enable workflows.
6. Run 'Celine Ticket Monitor' once manually to test.

Note: Replace the sample data source in monitor.py with a real inventory source when ready.
