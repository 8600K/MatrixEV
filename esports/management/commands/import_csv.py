from django.core.management.base import BaseCommand, CommandParser
import csv
from datetime import datetime 
from esports.models import Lol 

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Lol.objects.create(
                    team1=row['Team1'],
                    team2=row['Team2'],
                    spread1=row['Spread1'],
                    spread2=row['Spread2'],
                    win1=row['Win1'],
                    win2=row['Win2'],
                    total1=row['Total1'],
                    total2=row['Total2'],
                    date=row['DateTime']
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))

        