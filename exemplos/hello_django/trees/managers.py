from django.db import models


class TreeSpeciesQuerySet(models.QuerySet):
    def by_name(self, name):
        """
        Filter trees by name or scientific name.
        """
        filter = self.filter
        species_by_name = filter(name__contains=name)
        species_by_sci_name = filter(scientific_name__contains=name)
        return species_by_name | species_by_sci_name


class TreeQuerySet(models.QuerySet):
    def by_name(self, name):
        """
        Filter trees by name or scientific name.
        """
        from .models import TreeSpecies
        
        species = TreeSpecies.objects.by_name(name)
        return self.filter(species__in=species)
        
