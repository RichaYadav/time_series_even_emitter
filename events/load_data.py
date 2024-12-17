import csv
from datetime import datetime
from events.models import Event

csv_file_path = 'events/sample_time_series_data.csv'

def load_csv_data():
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Event.objects.create(
                timestamp=datetime.fromisoformat(row['timestamp']),
                metric=row['metric'],
                value=float(row['value'])
            )

load_csv_data()
