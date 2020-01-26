from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, 'Item has been added to List')
            return render(request, 'index.html', {'all_items': all_items})

        else:
            all_items = List.objects.all
            messages.Failure('entry is empty')
            return render(request, 'index.html', {'all_items': all_items})


    else:
        all_items = List.objects.all
        return render(request, 'index.html', {'all_items': all_items})

def delete(request, List_id):
    item = List.objects.get(pk=List_id)
    item.delete()
    messages.success(request, ('Item has been deleted'))
    return redirect("index")


def cross(request, List_id):
    item = List.objects.get(pk=List_id)
    item.completed = True
    item.save()
    return redirect("index")


def uncross(request, List_id):
    item = List.objects.get(pk=List_id)
    item.completed = False
    item.save()
    return redirect('index')


def edit(request, List_id):
    if request.method == 'POST':
        item = List.objects.get(pk=List_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('item Has been Edited'))
            return redirect('index')
        else:
            item = List.objects.get(pk=List_id)
            messages.MessageFailure(request, ('Entry is empty'))
            return render(request, 'edit.html')

    else:
        item = List.objects.get(pk=List_id)
        return render(request, 'edit.html', {'item': item})
