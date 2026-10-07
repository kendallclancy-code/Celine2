import json
import os
from email.mime.text import MIMEText
import smtplib

MAX_PRICE = 350

sample_listings = [
    {
        "date": "2026-10-16",
        "section": "Lower Bowl",
        "price": 299,
        "qty": 2,
        "url": "https://example.com"
    }
]

def load_seen():
    try:
        with open("known_listings.json", "r") as f:
            return json.load(f)
    except Exception:
        return []

def save_seen(data):
    with open("known_listings.json", "w") as f:
        json.dump(data, f)

def send_email(listing):
    body = f"""
Celine Dion ticket found

Date: {listing['date']}
Section: {listing['section']}
Price: €{listing['price']}
Quantity: {listing['qty']}

Link:
{listing['url']}
"""
    msg = MIMEText(body)
    msg["Subject"] = "🚨 Celine Dion Paris Ticket Alert"
    msg["From"] = os.environ["EMAIL_USER"]
    msg["To"] = os.environ["EMAIL_TO"]

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(
            os.environ["EMAIL_USER"],
            os.environ["EMAIL_PASSWORD"]
        )
        server.send_message(msg)

def main():
    seen = load_seen()

    for listing in sample_listings:
        key = f"{listing['date']}-{listing['section']}-{listing['price']}"
        if (
            listing["qty"] >= 2
            and listing["price"] <= MAX_PRICE
            and key not in seen
        ):
            send_email(listing)
            seen.append(key)

    save_seen(seen)

if __name__ == "__main__":
    main()
