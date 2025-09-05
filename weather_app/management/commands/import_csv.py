import os
import csv_to_sqlite
from django.core.management.base import BaseCommand

class Command(BaseCommand):  
    help = "Import CSV files into SQLite using csv_to_sqlite"

    def handle(self, *args, **kwargs):
        folder_path = os.path.abspath("weather_app/data")  
        input_files = []

        for file in os.listdir(folder_path):
            if file.endswith(".txt"):  
                input_files.append(os.path.join(folder_path, file))

        if not input_files:
            self.stdout.write(self.style.ERROR("No CSV files found in 'weatherfiles/'"))
            return

        options = csv_to_sqlite.CsvOptions(
            typing_style="full",
            encoding="utf-8"  
        )

        # Convert CSV to SQLite database
        csv_to_sqlite.write_csv(input_files, "db.sqlite3", options)

        self.stdout.write(self.style.SUCCESS("CSV data successfully imported into SQLite!"))
