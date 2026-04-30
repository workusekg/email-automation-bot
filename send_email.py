import os
import smtplib
from email.message import EmailMessage

def send_mail():
    # These secrets will be managed in GitHub Settings
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    
    msg = EmailMessage()
    msg['Subject'] = "Automated Browser-Based Email"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = "RECIPIENT@EXAMPLE.COM" # <--- CHANGE THIS TO YOUR EMAIL
    msg.set_content("Success! This was sent entirely from the GitHub cloud.")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    send_mail()
