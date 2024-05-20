import os
from django.conf import settings
import psycopg2
from django.core.management.base import BaseCommand
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **kwargs):

        app_name = 'ratings'
        
        temp_table_name = 'temp_table'
        
        filename = '/data.csv'#os.path.join(settings.BASE_DIR, os.getenv('FILENAME'))
    
        connection = psycopg2.connect(
            host='localhost',
            database='searchart',
            port='5430',
            user='mehran',
            password='1234'
        )

        create_temp_table_query = f"""
            CREATE TEMP TABLE {temp_table_name} (
                Year INTEGER,
                Sector VARCHAR(1000),
                Subsector VARCHAR(1000),
                Indicator VARCHAR(1000),
                Country VARCHAR(1000),
                Country_code VARCHAR(1000),
                Amount NUMERIC,
                Rank INTEGER,
                Id SERIAL PRIMARY KEY
            );
        """
        
        copy_to_temp_table_query = f"""
            COPY {temp_table_name} (Year, Sector, Subsector, Indicator, Country, Country_code, Amount, Rank, Id)
            FROM '{filename}' DELIMITER ',' CSV HEADER QUOTE '\"' ESCAPE '''';
        """
        
        create_tables_and_copy_query = f"""
            CREATE TABLE IF NOT EXISTS core_sector (
                Sector VARCHAR(500) PRIMARY KEY
            );
            
            CREATE TABLE IF NOT EXISTS core_subsector (
                Sector VARCHAR(500) REFERENCES core_sector(Sector),
                Subsector VARCHAR(500) PRIMARY KEY
            );

            CREATE TABLE IF NOT EXISTS core_indicator (
                Indicator VARCHAR(1000) PRIMARY KEY,
                Sector VARCHAR(500) REFERENCES core_sector(Sector),
                Subsector VARCHAR(500) REFERENCES core_subsector(Subsector)
            );
            
            CREATE TABLE IF NOT EXISTS core_countries (
                Year INTEGER,
                Indicator VARCHAR(1000) REFERENCES core_indicator(Indicator),
                Country VARCHAR(255),
                Country_code VARCHAR(10),
                Amount NUMERIC,
                Rank INTEGER,
                ID INTEGER PRIMARY KEY
            );
            
            INSERT INTO core_sector (Sector)
            SELECT DISTINCT ON (Sector) Sector
            FROM {temp_table_name};
            
            INSERT INTO core_subsector (Sector, Subsector)
            SELECT DISTINCT ON (Subsector) Sector, Subsector
            FROM {temp_table_name};

            INSERT INTO core_indicator (Sector, Subsector, Indicator)
            SELECT DISTINCT ON (Indicator) Sector, Subsector, Indicator
            FROM {temp_table_name};
                       
            INSERT INTO core_countries (Year, Indicator, Country, Country_code, Amount, Rank, Id)
            SELECT Year, Indicator, Country, Country_code, Amount, Rank, Id
            FROM {temp_table_name};
        """
        
        drop_temp_table_query = f"""
            DROP TABLE IF EXISTS {temp_table_name};
        """

        with connection.cursor() as cursor:
            cursor.execute(create_temp_table_query)
            self.stdout.write(self.style.SUCCESS('Temp table created successfully'))
            cursor.execute(copy_to_temp_table_query)
            self.stdout.write(self.style.SUCCESS('Data copied to temp table successfully'))
            cursor.execute(create_tables_and_copy_query)
            self.stdout.write(self.style.SUCCESS('Other tables created successfully'))
            cursor.execute(drop_temp_table_query)
            connection.commit()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
