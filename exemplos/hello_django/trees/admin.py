from django.contrib import admin
from trees.models import Tree, TreeSpecies, Environment


admin.site.register(Tree)
admin.site.register(TreeSpecies)
admin.site.register(Environment)

