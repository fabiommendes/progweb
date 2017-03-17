from django.shortcuts import render
from django.http import HttpResponse
from trees.models import Tree


def tree_view(request, tree_id):
    tree = Tree.objects.get(id=tree_id)
    context = { 'tree': tree }
    return render(request, 'trees/tree.html', context)
    
