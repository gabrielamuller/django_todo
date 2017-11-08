from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm

# Create your views here.
#def get_index(request):
    #return render(request, "index.html")

def get_index(request):
    items = TodoItem.objects.all()
    return render(request, "index.html", {'items': items })

def add_item(request):
    
    if request.method == "POST":
        # Get the details from the request
        form = TodoItemForm(request.POST, request.FILES)
        # Handle saving to DB
        if form.is_valid():
            form.save()
            return redirect(get_index)
    else:
        # GET Request so just give a blank form
        form = TodoItemForm()
    return render(request, "item_form.html", { 'form': form })