import argparse
from tabulate import tabulate
import config
from core.email_reader import EmailReader
from core.generator import Generator  # Assuming you have a Generator module for output formats

def main():
    parser = argparse.ArgumentParser(description='Read Emails and print in a table format.')
    parser.add_argument('--email', help='Email address to log in.', required=True, default=config.EMAIL)
    parser.add_argument('--filter', action='append', help='Filter emails by Subject, Sender, or Date. Use format "key=value".')
    parser.add_argument('--sort', choices=['Date', 'Sender'], help='Sort emails by Date or Sender.')
    parser.add_argument('--output', help='Output CSV, JSON, or XML file to write the emails.')
    args = parser.parse_args()

    reader = EmailReader(args.email)
    reader.load()
    email_list = reader.get_email_data()

    if args.filter:
        for filter_str in args.filter:
            filter_key, filter_value = filter_str.split('=')
            filter_key = filter_key.capitalize()
            email_list = [email for email in email_list if filter_value in email[filter_key]]

    if args.sort:
        email_list.sort(key=lambda x: x[args.sort])

    if not args.output:
        # Print emails in a table format

        # Prepare data for tabulation
        table_data = []
        for email in email_list:
            table_data.append([email['Date'], email['Sender'], email['Subject'][:50], email['Content'][:50]])

        # Print table using tabulate
        headers = ['Date', 'Sender', 'Subject', 'Content']
        print(tabulate(table_data, headers=headers, tablefmt='grid'))
    else:
        # Output emails to a file based on the specified format
        output_file_extension = args.output.split('.')[-1]

        if output_file_extension not in ['csv', 'json', 'xml']:
            raise ValueError("Unsupported output format. Supported formats are: 'csv', 'json', 'xml'")

        if output_file_extension == 'csv':
            Generator.generate_csv(args.output, email_list)
        elif output_file_extension == 'json':
            Generator.generate_json(args.output, email_list)
        elif output_file_extension == 'xml':
            Generator.generate_xml(args.output, email_list)

if __name__ == '__main__':
    main()
