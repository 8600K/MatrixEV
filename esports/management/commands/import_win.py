from django.core.management.base import BaseCommand, CommandParser
import csv
from datetime import datetime 
from esports.models import LolWin

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to CSV file')

    def handle(self, *args, **options):

        LolWin.objects.all().delete()
        # This flushes all data entries out to make way for the new data.

        file_path = options['file_path']
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                LolWin.objects.create(
                    team1=row['Win1_Team'],
                    team2=row['Win2_Team'],
                    win1_decimal=row['Win1_Decimal'],
                    win2_decimal=row['Win2_Decimal'],
                    win1_probability=row['Win1_Probability'],
                    win2_probability=row['Win2_Probability'],
                    win1_ev=row['Win1_Ev'],
                    win2_ev=row['Win2_Ev'],
                    win1_site=row['Win1_Site'],
                    win2_site=row['Win2_Site'],
                    date = row['Date_Time']
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))

# Documentation! 
# Create model in models.py.
# Make migrations etc.
# Create import.py
# Using Command(BaseCommand) lets us run this command from the terminal.
# py manage.py import_win esports\resources\csv\Win_Dataframe.csv 
# Where import_win is the name of the file, and then we provide the relative file path to the csv file. 
# Thanks for coming to my Ted Talk