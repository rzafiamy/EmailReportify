import json
from collections import Counter

class EmailStatistics:
    def __init__(self, emails):
        self.emails = emails

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            emails = json.load(f)
        return cls(emails)

    def compute_statistics(self):
        total_emails = len(self.emails)
        
        senders_counter = Counter(email['Sender'] for email in self.emails)
        top_senders = senders_counter.most_common(10)  # Top 5 senders
        
        subjects_counter = Counter(email['Subject'] for email in self.emails)
        common_subjects = subjects_counter.most_common(10)  # Top 5 common subjects
        
        # Add more statistics as needed
        
        return {
            'Total Emails': total_emails,
            'Top Senders': top_senders,
            'Common Subjects': common_subjects,
            # Add more statistics here
        }

    def print_statistics(self):
        statistics = self.compute_statistics()
        
        print("Email Statistics:")
        for stat_name, stat_value in statistics.items():
            print(f"{stat_name}:")
            if isinstance(stat_value, list):
                for item in stat_value:
                    print(f"  - {item[0]}: {item[1]}")
            else:
                print(f"  {stat_value}")