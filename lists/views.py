from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
    """Handles gets and posts to the main page"""
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    
    items = Item.objects.all()
    return render(request, 'lists/home.html', {'items': items})
