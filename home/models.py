from django.db import models

class UrlAddress(models.Model):
    original_url = models.CharField(max_length=300)
    changed_url = models.CharField(max_length=300)

class CSVFile(models.Model):
    csvfile = models.FileField()
    

