from django.shortcuts import render, redirect
from .forms import ToDoForm, InputForm
from .models import ToDo

# Create your views here.
def to_do(request):
    form = InputForm()
    context = {"form":form}
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            todo = ToDo.objects.create(title=form_data["title"], description=form_data["description"], 
            state=form_data["state"], date=form_data["date"],)

    return render(request, "todo/todo.html",context)

def to_do_list(request):
    to_dos = ToDo.objects.all()
    context = {"to_dos":to_dos}
    return render(request, "todo/todo_list.html",context)

def to_do_update(request, id):
    
    to_do = ToDo.objects.get(id=id) 
    data_dict = {"title":to_do.title, "description":to_do.description, "state":to_do.state, "date":to_do.date}
    form = InputForm(data_dict)
    context = {"form":form}
    
    if request.method == "GET":
        return render(request, "todo/update.html",context)
    elif request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            to_do.title = form_data["title"]
            to_do.description = form_data["description"]
            to_do.state = form_data["state"]
            to_do.date = form_data["date"]
            to_do.save()
            return redirect("list")
            

def to_do_delete(request, id):

    to_do = ToDo.objects.get(id=id)
    to_do.delete()

    return redirect("list")