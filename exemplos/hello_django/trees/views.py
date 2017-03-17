from django.shortcuts import render
from django.http import HttpResponse
from trees.models import Tree


def tree_view(request, tree_id):
    tree = Tree.objects.get(id=tree_id)
    context = { 'tree': tree }
    return render(request, 'trees/tree-detail.html', context)


def tree_list(request):
    context = {'tree_list': Tree.objects.all()}
    return render(request, 'trees/tree-list.html', context)
    
