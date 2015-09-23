from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    jmlItem = Item.objects.count()

    if(jmlItem > 4):
        comment = 'oh tidak'
    elif(jmlItem == 0):
        comment = 'yey, waktunya berlibur'
    else:
        comment = 'sibuk tapi santai'

    return render(request, 'home.html', {'items': items, 'comment' : comment})
