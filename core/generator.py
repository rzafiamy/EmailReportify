import csv
import json
import xml.etree.ElementTree as ET

class Generator:
    @staticmethod
    def generate_csv(output_file, data):
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Date', 'Sender', 'Subject', 'Content'])
            for email_data in data:
                writer.writerow([
                    email_data['Date'],
                    email_data['Sender'],
                    email_data['Subject'],
                    email_data['Content']
                ])

    @staticmethod
    def generate_json(output_file, data):
        with open(output_file, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)

    @staticmethod
    def generate_xml(output_file, data):
        root = ET.Element('Emails')
        for email_data in data:
            email_elem = ET.SubElement(root, 'Email')
            ET.SubElement(email_elem, 'Date').text = email_data['Date']
            ET.SubElement(email_elem, 'Sender').text = email_data['Sender']
            ET.SubElement(email_elem, 'Subject').text = email_data['Subject']
            ET.SubElement(email_elem, 'Content').text = email_data['Content']
        
        tree = ET.ElementTree(root)
        tree.write(output_file, encoding='utf-8', xml_declaration=True)
