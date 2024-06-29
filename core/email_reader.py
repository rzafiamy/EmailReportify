import imaplib
import email
from email.header import decode_header
import config
from .generator import Generator
import os
import json
import getpass
from datetime import datetime

class EmailReader:
    def __init__(self, email):
        self.email = email
        self.email_data_list = []


    def load(self, force=False):
        # check if cache file exists
        name = self.email.split('@')[0]
        try:
            if os.path.exists(f'.{name}.json') and not force:
                with open(f'.{name}.json', 'r') as file:
                    self.email_data_list = json.load(file)
            else:
                self.load_net()
        except Exception as e:
            print(f"Error: {e}")
            self.load_net()
    
    def load_net(self, box=config.MAILBOX):
        
        password = config.PASSWORD

        if not config.PASSWORD:
            password = getpass.getpass(prompt='Enter your email password: ')

        self.mail = imaplib.IMAP4_SSL(config.IMAP_SERVER)
        self.mail.login(self.email, password)
        self.mail.select(box)
        
        status, messages = self.mail.search(None, 'ALL')

        if status == 'OK':
            index = 0
            error = 0
            for num in messages[0].split():
                status, data = self.mail.fetch(num, '(RFC822)')
                if status == 'OK':
                    try:
                        msg = email.message_from_bytes(data[0][1])
                        date = email.utils.parsedate_to_datetime(msg['Date']).strftime('%Y-%m-%d %H:%M:%S')
                        sender = email.utils.parseaddr(msg['From'])[1]
                        subject = decode_header(msg['Subject'])[0][0]
                        if isinstance(subject, bytes):
                            subject = subject.decode()
                        content = self.get_content_from_msg(msg)
                        self.email_data_list.append({
                            'Date': date,
                            'Sender': sender,
                            'Subject': subject,
                            'Content': content,
                            'UID': num.decode()
                        })
                        index += 1
                        # clear console screen
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"Emails loaded: {index}, Errors: {error}, UID: {num.decode()}")

                    except Exception as e:
                        print(f"Error: {e}")
                        error += 1
            # save to cache file
            name = self.email.split('@')[0]
            Generator.generate_json(f'.{name}.json', self.email_data_list)
        else:
            print("No messages found!")
        
        self.mail.logout()

    def get_email_data(self):
        return self.email_data_list

    def get_content_from_msg(self, msg):
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
    
    def delete_emails(self, uids):
        if not config.PASSWORD:
            password = getpass.getpass(prompt='Enter your email password: ')
        
        try:
            self.mail = imaplib.IMAP4_SSL(config.IMAP_SERVER)
            self.mail.login(self.email, password)
            self.mail.select(config.MAILBOX)

            for uid in uids:
                # get the email message if uid == email['UID'] in email_data_list
                for em in self.email_data_list:
                    if uid == em['UID']:
                        datem = em['Date']
                        # Format datem to match the search query
                        datem = datetime.strptime(datem, '%Y-%m-%d %H:%M:%S').strftime('%d-%b-%Y')
                        search_query = f'(FROM "{em["Sender"]}" SENTON {datem})'

                        status, messages = self.mail.search(None, search_query)

                        if status == 'OK':
                            for num in messages[0].split():
                                status, data = self.mail.fetch(num, '(RFC822)')
                                if status == 'OK':
                                    msg = email.message_from_bytes(data[0][1])
                                    subject = decode_header(msg['Subject'])[0][0]
                                    date = email.utils.parsedate_to_datetime(msg['Date']).strftime('%Y-%m-%d %H:%M:%S')
                                    if isinstance(subject, bytes):
                                        subject = subject.decode()
                                    if subject == em['Subject'] and date == em['Date']:
                                        self.mail.store(num, '+FLAGS', '\\Deleted')
                                        print(f"Deleted: {em['Subject']} from {em['Sender']} on {em['Date']}")
                                        break
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.mail.logout()
                
                
                