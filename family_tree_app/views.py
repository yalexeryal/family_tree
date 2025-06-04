from django.shortcuts import render, redirect, get_object_or_404
from models import Person, Relationship
from forms import PersonForm, RelationshipForm

def person_detail(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    relationships_from = Relationship.objects.filter(from_person=person)
    relationships_to = Relationship.objects.filter(to_person=person)

    context = {
        'person': person,
        'relationships_from': relationships_from,
        'relationships_to': relationships_to
    }
    return render(request, 'family_tree_app/person_detail.html', context)


def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect('person_list')
    else:
        form = PersonForm()

    return render(request, 'family_tree_app/person_form.html', {'form': form})


