from django.shortcuts import render, get_object_or_404, redirect
from .models import Person, Relationship
from .forms import PersonForm, RelationshipForm


def person_detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    relationships_from = Relationship.objects.filter(from_person=person)
    relationships_to = Relationship.objects.filter(to_person=person)

    context = {
        'person': person,
        'relationships_from': relationships_from,
        'relationships_to': relationships_to,
    }
    return render(request, 'genealogy/person_detail.html', context)


def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'genealogy/person_form.html', {'form': form})
