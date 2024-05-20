import pandas as pd
from django.core.management.base import BaseCommand
from core.models import Country, Sector, Subsector, Indicator, Data, Year

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file for import')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        
        try:
            df = pd.read_csv(csv_file)  # Read the CSV file into a DataFrame
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f'File not found: {csv_file}'))
            return

        for index, row in df.iterrows():
            # Create or update instances of the Country model based on DataFrame rows
            country, created = Country.objects.get_or_create(
                name=row['Country'],
                code=row['Country_code']
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {country}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated: {country}'))

            # Create or update instances of the Sector model based on DataFrame rows
            sector, created = Sector.objects.get_or_create(
                name=row['Sector']
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {sector}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated: {sector}'))

            # Create or update instances of the Subsector model based on DataFrame rows
            subsector, created = Subsector.objects.get_or_create(
                name=row['Subsector'],
                sector=sector
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {subsector}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated: {subsector}'))

            # Create or update instances of the Indicator model based on DataFrame rows
            indicator, created = Indicator.objects.get_or_create(
                name=row['Indicator'],
                subsector=subsector
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {indicator}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated: {indicator}'))


            year, created = Year.objects.get_or_create(
                year=row['Year']
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {year}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated: {year}'))



            # Create or update instances of the Data model based on DataFrame rows
            data, created = Data.objects.get_or_create(
                rank=row['Rank'],
                amount=row['Amount'],
                year=year,
                country=country
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {data}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated: {data}'))

            # Create or update instances of the Year model based on DataFrame rows


            # Handle ManyToMany relationships for Indicator and Year models
            indicator.country.add(country)
            year.country.add(country)


