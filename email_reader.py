import imaplib
import email
from email.header import decode_header
import csv
import config

class EmailReader:
    def __init__(self, email, password, output_file, subject_to_filter):
        self.email = email
        self.password = password
        self.output_file = output_file
        self.mail = imaplib.IMAP4_SSL(config.IMAP_SERVER)
        self.mail.login(self.email, self.password)
        self.subject_to_filter = subject_to_filter

    def fetch_and_write_emails(self):
        self.mail.select('inbox')
        status, messages = self.mail.search(None, f'(SUBJECT "{self.subject_to_filter}")')
        if status == 'OK':
            with open(self.output_file, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Date', 'Sender', 'Subject','Content'])

                for num in messages[0].split():
                    status, data = self.mail.fetch(num, '(RFC822)')
                    if status == 'OK':
                        msg = email.message_from_bytes(data[0][1])
                        date = email.utils.parsedate_to_datetime(msg['Date']).strftime('%Y-%m-%d %H:%M:%S')
                        sender = email.utils.parseaddr(msg['From'])[1]
                        subject = decode_header(msg['Subject'])[0][0]
                        if isinstance(subject, bytes):
                            subject = subject.decode()
                        content = self.get_content_from_msg(msg)
                        writer.writerow([date, sender, subject, content])
        self.mail.logout()

    @staticmethod
    def get_content_from_msg(msg):
        content = ''
        if msg.is_multipart():
            for part in msg.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))

                # Check if the email part is text and not an attachment
                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    payload = part.get_payload(decode=True)
                    try:
                        content = payload.decode('utf-8')  # Try UTF-8 first
                    except UnicodeDecodeError:
                        content = payload.decode('iso-8859-1')  # Fall back to ISO-8859-1
                    break  # Once you find the text/plain part, exit the loop
        else:
            payload = msg.get_payload(decode=True)
            try:
                content = payload.decode('utf-8')  # Try UTF-8 first
            except UnicodeDecodeError:
                content = payload.decode('iso-8859-1')  # Fall back to ISO-8859-1
        return content

