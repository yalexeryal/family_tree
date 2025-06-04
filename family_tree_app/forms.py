from django import forms
from models import Person, Relationship

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'surname', 'birth_date', 'death_date']

class RelationshipForm(forms.ModelForm):
    class Meta:
        model = Relationship
        fields = ['from_person', 'to_person', 'relationship_type', 'description']