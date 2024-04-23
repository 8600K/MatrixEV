from django.core.management.base import BaseCommand, CommandParser
import csv
from datetime import datetime 
from esports.models import LolSpread 

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to CSV file')

    def handle(self, *args, **options):

        LolSpread.objects.all().delete()
        # This flushes all current objects out to make way for the new data.

        file_path = options['file_path']
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                LolSpread.objects.create(
                    team1=row['Spread1_Team'],
                    team2=row['Spread2_Team'],
                    spread1_decimal=row['Spread1_Decimal'],
                    spread2_decimal=row['Spread2_Decimal'],
                    spread1_ou=row['Spread1_Ou'],
                    spread2_ou=row['Spread2_Ou'],
                    spread1_probability=row['Spread1_Probability'],
                    spread2_probability=row['Spread2_Probability'],
                    spread1_ev=row['Spread1_Ev'],
                    spread2_ev=row['Spread2_Ev'],
                    spread1_site=row['Spread1_Site'],
                    spread2_site=row['Spread2_Site'],
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