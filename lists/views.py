from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from lists.forms import ItemForm
from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'lists/home.html', {'form': ItemForm()})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            new_item_text = request.POST['text']
            item = Item.objects.create(text=new_item_text, list=list_)
            return redirect(list_)
        else:
            return render(request, 'lists/list.html', {'list': list_, 'form': form})
    else:
        pass
    return render(request, 'lists/list.html', {'list': list_, 'form': ItemForm()})

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        new_item_text = request.POST['text']
        Item.objects.create(text=new_item_text, list=list_)
        return redirect(list_)
    else:
        return render(request, 'lists/home.html', {"form": form})
