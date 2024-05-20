from django.db import models
import os
from dotenv import load_dotenv

load_dotenv()

class Sector(models.Model):
    class Meta:
        managed = False
        db_table = 'core_sector' 
    
    sector = models.CharField(max_length=500, primary_key=True)

    def __str__(self):        
        return f"Sector: {self.sector};"

class Subsector(models.Model):
    class Meta:
        managed = False
        db_table = os.getenv('DB_TABLE_NAME_SUBSECTOR')
         
    
    sector = models.ForeignKey(Sector, db_column='sector', on_delete=models.CASCADE, related_name='subsector')
    subsector = models.CharField(max_length=500, primary_key=True)

    def __str__(self):        
        return f"{self.sector} Subsector: {self.subsector};"

class Indicator(models.Model):
    class Meta:
        managed = False
        db_table = os.getenv('DB_TABLE_NAME_INDICATOR')  
    
    sector = models.ForeignKey(Sector, db_column='sector', on_delete=models.CASCADE)
    subsector = models.ForeignKey(Subsector, db_column='subsector', on_delete=models.CASCADE,related_name='indicator')
    indicator = models.CharField(max_length=1000, primary_key=True)

    def __str__(self):        
        return f"{self.subsector};  Indicator: {self.indicator};"
    

class Countries(models.Model):
    class Meta:
        managed = False
        db_table = os.getenv('DB_TABLE_NAME_COUNTRIES')  
     
    year = models.IntegerField()
    indicator = models.ForeignKey(Indicator, db_column='indicator', on_delete=models.CASCADE, related_name='countryrating')
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=5)
    amount = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return f"Country: {self.country}; Year: {self.year}; Indicator: {self.indicator}; Rank: {self.rank};"





    
    
     
 
    
    





   