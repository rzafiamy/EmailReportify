import argparse
from email_reader import EmailReader

def main():
    parser = argparse.ArgumentParser(description='Read Emails and write to CSV all emails with a specific subject (date, sender, subject, content).')
    parser.add_argument('--email', help='Email address to log in.', required=True)
    parser.add_argument('--subject', help='Subject to filter emails.', default='Bugs', required=True)

    parser.add_argument('--output', help='Output CSV file name.', default='emails.csv')

    args = parser.parse_args()

    # Ask for password
    password = input('Enter password: ')

    reader = EmailReader(args.email, password, args.output, args.subject)
    reader.fetch_and_write_emails()

if __name__ == '__main__':
    main()