from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .form import PersonForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required()
def person_list(request):
    valueSearch = request.GET.get('search', None)

    if valueSearch:
        persons = Person.objects.all()
        persons = persons.filter(first_name=valueSearch)
    else:
        persons = Person.objects.all()
    return  render(request, 'CRUD.html', {'Persona': persons})

@login_required()
def person_new(request):
    form = PersonForm(request.POST or  None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form_new.html', {'form': form})
@login_required()
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)#Vai pegar o objeto person, onde a primary key é igual a ''Id'', que passamos na função
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)#Form vai ser instanciado por person

    if form.is_valid():
        form.save()
        return  redirect('person_list')


    return  render(request, 'person_form.html', {'form': form})

@login_required()
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect('person_list')




