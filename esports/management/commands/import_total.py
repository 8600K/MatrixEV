from django.core.management.base import BaseCommand, CommandParser
import csv
from datetime import datetime 
from esports.models import LolTotal

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to CSV file')


    def handle(self, *args, **options):

        LolTotal.objects.all().delete()
        # This clears all previous data entries out! 

        file_path = options['file_path']
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                LolTotal.objects.create(
                    team1=row['Total1_Team'],
                    team2=row['Total2_Team'],
                    total1_decimal=row['Total1_Decimal'],
                    total2_decimal=row['Total2_Decimal'],
                    total_over=row['Total_Over'],
                    total_under=row['Total_Under'],
                    total1_probability=row['Total1_Probability'],
                    total2_probability=row['Total2_Probability'],
                    total1_ev=row['Total1_Ev'],
                    total2_ev=row['Total2_Ev'],
                    total1_site=row['Total1_Site'],
                    total2_site=row['Total2_Site'],
                    date=row['Date_Time']
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