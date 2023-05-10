import csv 
from datetime import date
from django.conf import settings
from django.core.management.base import BaseCommand
from plot.models import Sales

MONTH_MAP = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12,
}

class Command(BaseCommand):
    help = 'load data from csv file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'Data' / 'SalesForCourse_quizz_table.csv'

        with open(datafile, 'r')as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                dt = date(
                    year=int(row['year']),
                    month=MONTH_MAP[row['Month']],
                    day = 1,
                )
                Sales.objects.get_or_create(date=dt, revenue=row['Revenue'])
            
            



