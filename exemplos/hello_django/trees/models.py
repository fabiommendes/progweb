from django.db import models
from .managers import TreeSpeciesQuerySet, TreeQuerySet 


class Environment(models.Model):
    """
    A natural environment (e.g.: Amazonia, Cerrado, Mata Atlantica, etc)
    """
    name = models.CharField(max_length=100)
    avg_rain = models.FloatField(blank=True, null=True)
    avg_temperature = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class TreeSpecies(models.Model):
    """
    #TODO: documentar
    """
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    objects =  TreeSpeciesQuerySet.as_manager() 
    
    def __str__(self):
        return self.name
        

class Tree(models.Model):
    """
    #TODO: documentar
    """
    age = models.IntegerField()
    species = models.ForeignKey(TreeSpecies)
    lat = models.FloatField(null=True)
    lon = models.FloatField()
    height = models.FloatField()
    is_threatened = models.BooleanField(default=False)
    objects = TreeQuerySet.as_manager()

    def __str__(self):
        return '%s (%.2f, %.2f)' % (self.species, self.lat, self.lon)
        
        
    
