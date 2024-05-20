import os
import django
import csv

# Manually configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Countries")  # Replace "your_project.settings" with your actual project's settings module
django.setup()

# Now you can import your models and use them
from core.models import Country, Sector, Subsector, Indicator, Year, Data

# Read data from CSV file
with open('updated_searchart_data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    for row in spamreader:
        row = row[0].split(',')

        # Create or get the Country instance
        country_name = row[4]
        country, created = Country.objects.get_or_create(name=country_name, code=row[5])

        # Create or get the Sector instance
        sector_name = row[1]
        sector, created = Sector.objects.get_or_create(name=sector_name)

        # Create or get the Subsector instance
        subsector_name = row[2]
        subsector, created = Subsector.objects.get_or_create(name=subsector_name, sector=sector)

        # Create or get the Indicator instance(s)
        indicator_names = row[3].split(',')
        for indicator_name in indicator_names:
            indicator, created = Indicator.objects.get_or_create(name=indicator_name, subsector=subsector)
            indicator.country.add(country)

        # Create or get the Year instance
        year = int(row[0]) if row[0] else None
        year, created = Year.objects.get_or_create(year=year)
        year.country.add(country)

        # Create the Data instance
        rank = int(row[7]) if row[7] else None
        amount = float(row[6]) if row[6] else None

        data_instance = Data.objects.create(rank=rank, amount=amount, country=country)
