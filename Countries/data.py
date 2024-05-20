# import psycopg2

# conn = psycopg2.connect(
#     host="localhost",
#     database="searchart",
#     user="mehran",
#     password=1234,
#     port=5430
# )

# print('salam')

# cur = conn.cursor()



# import csv

# with open('updated_searchart_data.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
#     for row in spamreader:
#         row=row[0].split(',')
#         with conn.cursor() as cur:
            
#             try:
#                 cur.execute(
#                     "INSERT INTO core_country (name, code) VALUES (%s, %s)",
#                     (row[4], row[5])
#                 )

#             except Exception as e:
#                 # Handle other exceptions if necessary

#                 conn.rollback()  # Roll back the transaction to avoid committing the failed insertion

#             # Commit the transaction for successful insertions
#             conn.commit()

            
#             sector_name = row[1]
            

#             try:
#                 # Attempt to insert the new sector
#                 cur.execute(
#                     "INSERT INTO core_sector (name) VALUES (%s)",
#                     (sector_name)
#                 )

#             except Exception as e:
#                 # Handle other exceptions if necessary

#                 conn.rollback()  # Roll back the transaction to avoid committing the failed insertion

#             # Commit the transaction for successful insertions
#             conn.commit()


#             sector_name = row[1]
#             subsector_name = row[2]

#             try:
#                 # Attempt to insert the new subsector with the determined sector_id
#                 cur.execute(
#                     "INSERT INTO core_subsector (name, sector_id) SELECT %s, id FROM core_sector WHERE name = %s",
#                     (subsector_name, sector_name)
#                 )

#             except Exception as e:
#                 # Handle other exceptions if necessary

#                 conn.rollback()  # Roll back the transaction to avoid committing the failed insertion

#             # Commit the transaction for successful insertions
#             conn.commit()


            
#             # row_values = row[0].split(',')  # Sətri vergüllərdən ayırırıq və listdə saxlayırıq



#             # # Indicator adını verilənlərin siyahısından yaradırıq
#             # if len(row_values) >= 4:
#             #     indicator_names = row_values[3].split(',')  # Indicator adını vergüllərdən ayırırıq və listdə saxlayırıq

#             #     for indicator_name in indicator_names:
#             #         try:
#             #             # Attempt to insert the new indicator
#             #             cur.execute(
#             #                 "INSERT INTO core_indicator (name, subsector_id) SELECT %s, id FROM core_subsector WHERE name = %s",
#             #                 (indicator_name, subsector_name)
#             #             )

#             #         except psycopg2.errors.UniqueViolation as e: 
#             #             # Handle the case where a duplicate indicator name is encountered
#             #             # You can choose to skip the insertion or update the existing record here
#             #             print(f"Duplicate indicator name: {indicator_name}. Skipping insertion or updating existing record.")
                        
#             #             conn.rollback()  # Roll back the transaction to avoid committing the failed insertion

#             #         # Commit the transaction for successful insertions
#             #         conn.commit()
#             # else:
#             #         try:
#             #             # Attempt to insert the new indicator
#             #             cur.execute(
#             #                 "INSERT INTO core_indicator (name, subsector_id) SELECT %s, id FROM core_subsector WHERE name = %s",
#             #                 (row[3], subsector_name)
#             #             )

#             #         except psycopg2.errors.UniqueViolation as e: 
#             #             # Handle the case where a duplicate indicator name is encountered
#             #             # You can choose to skip the insertion or update the existing record here

                        
#             #             conn.rollback()  # Roll back the transaction to avoid committing the failed insertion

#             #         # Commit the transaction for successful insertions
#             #         conn.commit()
                
                      
            
            

#             # Create the 'year' table
#             try:
#                 year = int(row[0])
#             except ValueError:
#                 year = None

#             try:
#                 cur.execute(
#                     "INSERT INTO core_data (year) VALUES (%s)",
#                     (year)
#                 )

#             except Exception as e:
#                 # Handle other exceptions if necessary
#                 conn.rollback()  # Roll back the transaction to avoid committing the failed creation

#             # ...


        
        
#             try:
#                 rank = int(row[7])
#             except ValueError:
#                 rank = None

#             try:
#                 amount = float(row[6])
#             except ValueError:
#                 amount = None

#             try:
#                 cur.execute(
#                     "INSERT INTO core_data (rank, amount) VALUES (%s, %s)",
#                     (rank, amount)
#                 )

#             except Exception as e:
#                 # Handle other exceptions if necessary

#                 conn.rollback()  # Roll back the transaction to avoid committing the failed insertion

#             # Commit the transaction for successful insertions
#             conn.commit()



# conn.close()





# import psycopg2
# import csv

# # Establish a database connection
# conn = psycopg2.connect(
#     host="localhost",
#     database="searchart",
#     user="mehran",
#     password="1234",  # Make sure your password is a string
#     port=5430
# )

# # Create a cursor
# cur = conn.cursor()

# # Read data from CSV file
# with open('updated_searchart_data.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
#     for row in spamreader:
#         row = row[0].split(',')
        
#         # Insert into core_country
#         try:
#             cur.execute(
#                 "INSERT INTO core_country (name, code) VALUES (%s, %s)",
#                 (row[4], row[5])
#             )
#             conn.commit()
#         except Exception as e:
#             conn.rollback()
#             # Handle other exceptions if necessary

#         sector_name = row[1]

#         # Insert into core_sector
#         try:
#             cur.execute(
#                 "INSERT INTO core_sector (name) VALUES (%s)",
#                 (sector_name,)
#             )
#             conn.commit()
#         except Exception as e:
#             conn.rollback()
#             # Handle other exceptions if necessary

#         subsector_name = row[2]

#         # Insert into core_subsector
#         try:
#             cur.execute(
#                 "INSERT INTO core_subsector (name, sector_id) SELECT %s, id FROM core_sector WHERE name = %s",
#                 (subsector_name, sector_name)
#             )
#             conn.commit()
#         except Exception as e:
#             conn.rollback()
#             # Handle other exceptions if necessary

#         country_names = row[4:]  # Index 4 onwards for country_names

#         if len(row) >= 4:
#             indicator_names = row[3].split(',')  # Split indicator names by commas and store them in a list

#             for indicator_name in indicator_names:
#                 # Insert into core_indicator
#                 try:
#                     cur.execute(
#                         "INSERT INTO core_indicator (name, subsector_id) SELECT %s, id FROM core_subsector WHERE name = %s",
#                         (indicator_name, subsector_name)
#                     )
#                     conn.commit()
#                 except Exception as e:
#                     conn.rollback()
#                     # Handle other exceptions if necessary

#                 # Retrieve indicator_id
#                 try:
#                     cur.execute(
#                         "SELECT id FROM core_indicator WHERE name = %s",
#                         (indicator_name,)
#                     )
#                     fetch_result = cur.fetchone()
#                     if fetch_result is not None:
#                         indicator_id = fetch_result[0]
#                     else:
#                         indicator_id = None
#                         # Handle the case where no rows were retrieved

#                     for country_name in country_names:
#                         # Insert into core_country
#                         try:
#                             cur.execute(
#                                 "INSERT INTO core_country (name, code) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING",
#                                 (country_name, "code_here")
#                             )
#                             conn.commit()
#                         except Exception as e:
#                             conn.rollback()
#                             # Handle other exceptions if necessary

#                         # Retrieve country_id
#                         try:
#                             cur.execute(
#                                 "SELECT id FROM core_country WHERE name = %s",
#                                 (country_name,)
#                             )
#                             fetch_result = cur.fetchone()
#                             if fetch_result is not None:
#                                 country_id = fetch_result[0]
#                             else:
#                                 country_id = None
#                                 # Handle the case where no rows were retrieved

#                             # Create a ManyToMany relationship between the indicator and country
#                             try:
#                                 cur.execute(
#                                     "INSERT INTO core_indicator_country (indicator_id, country_id) VALUES (%s, %s)",
#                                     (indicator_id, country_id)
#                                 )
#                                 conn.commit()
#                             except Exception as e:
#                                 conn.rollback()
#                                 # Handle other exceptions if necessary

#                         except Exception as e:
#                             conn.rollback()
#                             # Handle other exceptions if necessary

#                 except Exception as e:
#                     conn.rollback()
#                     # Handle other exceptions if necessary

#         else:
#             # Handle the case where there is no indicator name
#             pass

#         # Insert into core_data (year)
#         try:
#             year = int(row[0]) if row[0] else None
#             cur.execute(
#                 "INSERT INTO core_data (year) VALUES (%s)",
#                 (year,)
#             )
#             conn.commit()
#         except Exception as e:
#             conn.rollback()
#             # Handle other exceptions if necessary

#         # Insert into core_data (rank, amount)
#         try:
#             rank = int(row[7]) if row[7] else None
#             amount = float(row[6]) if row[6] else None
#             cur.execute(
#                 "INSERT INTO core_data (rank, amount) VALUES (%s, %s)",
#                 (rank, amount)
#             )
#             conn.commit()
#         except Exception as e:
#             conn.rollback()
#             # Handle other exceptions if necessary

# # Close the database connection
# conn.close()


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
