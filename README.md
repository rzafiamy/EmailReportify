# EmailReportify

**EmailReportify** is a powerful Python application designed to search through your email inbox for emails matching a specific subject pattern and compile a detailed report in CSV format. This tool is particularly useful for users who need to track emails about specific topics, such as "Bug" reports, and organize this information outside their email clients for further analysis or record-keeping.

## Features

- **Flexible Email Search**: Specify any subject pattern to search for in your inbox.
- **Comprehensive Reporting**: Generates a CSV report containing the date, sender, subject, and content of each matching email.
- **Secure Access**: Utilizes your email credentials securely without storing them.
- **Easy Configuration**: Simple setup with minimal configuration required.

## Setup

### Prerequisites

- Python 3.x installed on your system.
- Access to an email account with IMAP support.

### Installation

1. Clone or download the EmailReportify repository to your local machine.
2. Navigate to the EmailReportify directory.
3. There are no external dependencies required beyond the Python Standard Library, so no need for a `requirements.txt` file.

## Configuration

Before running EmailReportify, you need to set up the necessary configuration:

1. Open the `config.py` file in a text editor.
2. Update the `IMAP_SERVER` variable to match your email provider's IMAP server address. For example, for Gmail users: `IMAP_SERVER = 'imap.gmail.com'`.

## Usage

To use EmailReportify, run the `manager.py` script with the necessary arguments. Here's how you can do it:

```
python manager.py --email YOUR_EMAIL --output OUTPUT_FILE.csv --subject "SUBJECT_PATTERN"
```

Replace the following:
- `YOUR_EMAIL` with your email address.
- `OUTPUT_FILE.csv` with the desired output CSV file name.
- `SUBJECT_PATTERN` with the subject pattern you want to search for.

### Example

```
python manager.py --email example@gmail.com --output bugs_report.csv --subject "Bug"
```

This command searches for emails with the subject containing "Bug" and generates a CSV report named `bugs_report.csv`.

## Security Note

Your email and password are used only for logging into your email account to fetch emails and are not stored or used for any other purposes. However, ensure you keep your credentials secure and consider using app-specific passwords if your email provider supports them.

## License

EmailReportify is open-source software licensed under the MIT License.