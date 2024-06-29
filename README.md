# EmailReportify

EmailReportify provides functionality to read, filter, sort, and output email data from an IMAP server. It supports generating statistics and exporting emails to CSV, JSON, or XML formats based on user-specified criteria.

### Features

- **Email Retrieval and Display**
  - Fetches emails from the specified email account using IMAP.
  - Displays email data in a tabular format on the console using `tabulate`.

- **Filtering and Sorting**
  - Filters emails based on Subject, Sender, or Date criteria provided by the user.
  - Sorts filtered emails by Date or Sender.

- **Output Options**
  - Outputs filtered and sorted emails to CSV, JSON, or XML files.
  - Supports different file formats for exporting data.

- **Statistics Generation**
  - Computes and displays statistics about the email data set, including total email count, top senders, and common subjects.

### Usage

To use the tool, follow these steps:

1. **Requirements**
   - Python 3.x
   - Required Python packages (`argparse`, `tabulate`, etc.) which can be installed using `pip`.

2. **Setup**
   - Clone the project repository.
   - Install dependencies using `pip install -r requirements.txt` (if provided).

3. **Running the Tool**
   - Navigate to the project directory.
   - Execute the script `python manager.py --email <email_address> --filter <filter_criteria> --sort <sort_criteria> --output <output_file>`.

   **Arguments:**
   - `--email`: Required. Email address to log in.
   - `--filter`: Optional. Filter emails by Subject, Sender, or Date. Use format "key=value". Can be specified multiple times.
   - `--sort`: Optional. Sort emails by Date or Sender.
   - `--output`: Optional. Output CSV, JSON, or XML file to write the emails.
   - `--delete`: Delete email filtered

4. **Examples**

   - **Display emails in tabular format:**
     ```
     python manager.py --email user@example.com
     ```

   - **Filter and sort emails, output to CSV file:**
     ```
     python manager.py --email user@example.com --filter Sender=johndoe@example.com --sort Date --output filtered_emails.csv
     ```

   - **Generate statistics only:**
     ```
     python manager.py --email user@example.com --output stats.json
     ```

### Structure

The project is structured as follows:

- **`manager.py`**: Main script handling email retrieval, filtering, sorting, and output functionalities.
- **`core/email_reader.py`**: Module for handling IMAP email retrieval.
- **`core/generator.py`**: Module for generating CSV, JSON, and XML outputs.
- **`core/stats.py`**: Module for computing email statistics.
- **`config.py`**: Configuration file for storing constants and configurations.

### Dependencies

- **Python Libraries**:
  - `argparse`: For parsing command-line arguments.
  - `tabulate`: For formatting data into tables.
  - Additional libraries may be required based on specific functionalities and modules used.

### Notes

- Ensure proper configuration (`config.py`) with IMAP server details and other necessary constants.
- Handle authentication securely by prompting for the password using `getpass`.
- Customize and extend functionalities as per project requirements.

### License

This project is licensed under the MIT License. See `LICENSE` file for details.

---

This README provides an overview of the email handling and analysis tool, guiding users on installation, usage, and customization. It aims to facilitate efficient email data management and analysis tasks using Python.