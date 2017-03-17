from django.db import models


class Tree(models.Model):
    age = models.IntegerField()
    species = models.CharField(max_length=200)
    lat = models.FloatField(null=True)
    lon = models.FloatField()
    height = models.FloatField()
    is_threatened = models.BooleanField(default=False)
    
    def __str__(self):
        return '%s (%.2f, %.2f)' % (self.species, self.lat, self.lon)
