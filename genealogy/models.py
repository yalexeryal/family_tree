from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    death_date = models.DateField(null=True, blank=True, verbose_name='Дата смерти')


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Relationship(models.Model):
    PERSON_CHOICES = [
        ('Parent', 'Родитель'),
        ('Child', 'Ребенок'),
        ('Sibling', 'Брат/Сестра'),
        ('Spouse', 'Супруг/Супруга'),
        ('Grandparent', 'Дедушка/Бабушка'),
        ('Grandchild', 'Внук/Внучка'),
        ('Cousin', 'Двоюродный брат/сестра'),
        ('Uncle_Aunt', 'Дядя/Тётя'),
        ('Nephew_Niece', 'Племянник/Племянница'),
        ('In_Law', 'Свойственник (Свёкор, Тесть, и т.д.)'),
        ('Godparent', 'Крёстный родитель'),
        ('Godchild', 'Крестник'),
        ('Matchmaker', 'Сват/Сваха'),
        ('Friend', 'Друг'),
        ('Acquaintance', 'Знакомый'),
        ('Other', 'Другое'),
    ]

    from_person = models.ForeignKey(Person, related_name='relationships_from', on_delete=models.CASCADE, verbose_name='От кого')
    to_person = models.ForeignKey(Person, related_name='relationships_to', on_delete=models.CASCADE, verbose_name='К кому')
    relationship_type = models.CharField(max_length=20, choices=PERSON_CHOICES, verbose_name='Тип родства')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return f"{self.from_person} - {self.relationship_type} - {self.to_person}"
