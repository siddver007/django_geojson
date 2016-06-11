from django.db import models

# Model/ Relation for Providers
class Provider(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100 , primary_key = True)
    phone_number = models.CharField(max_length = 100)
    language = models.CharField(max_length = 100)
    currency = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

# Model/ Relation for Regions/ Polygons
class Region(models.Model):
	email = models.CharField(max_length = 100)
	price = models.FloatField()
	provider = models.CharField(max_length = 100)
	geodata = models.TextField()     

