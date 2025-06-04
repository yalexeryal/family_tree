from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    birth_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='Дата рождения')
    death_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name='Дата смерти')
    place_birth = models.CharField(max_length=100, null=True, blank=True, verbose_name='Место рождения')
    place_death = models.CharField(max_length=100, null=True, blank=True, verbose_name='Место смерти')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'{self.surname} {self.first_name}'

    class Meta:
        db_table = 'человек'
        verbose_name = 'Люди'
        verbose_name_plural = 'People'


class Relationship(models.Model):
    PERSON_CHOICES = [
        ('Parent', 'Родитель'),
        ('Child', 'Дети'),
        ('Sibling', 'Брат/Сестра'),
        ('Spouse', 'Супруг'),
        ('Grandparent', 'Дед/Бабушка'),
        ('Grandchild', 'Внук/Внучка'),
        ('Cousin', 'Двоюродный братья/сестра'),
        ('Aunt_Uncle', 'Тетя/Дядя'),
        ('Nephew_Niece', 'Племянник/Племянница'),
        ('In_law', 'Свояки(Теща, тесть, свекр, свекровь)'),
        ('Godparent', 'Крещеные родители'),
        ('Godchild', 'Крещеные дети'),
        ('Matchmaker', 'Сват/Сваха'),
        ('Friend', 'Друг'),
        ('Relative', 'Родственники'),
        ('Acquaintance', 'Знакомые'),
        ('Other', 'Другое')
    ]

    from_person = models.ForeignKey(Person, related_name='relationships_from' ,on_delete=models.CASCADE, verbose_name='От кого')
    to_person = models.ForeignKey(Person, related_name='relationships_to', on_delete=models.CASCADE, verbose_name='К кому')
    relationship_type = models.CharField(max_length=50, choices=PERSON_CHOICES, verbose_name='Тип родства')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.from_person} - {self.to_person} ({self.relationship_type})'



    class Meta:
        db_table = 'отношение'
        verbose_name = 'Отношение'
        verbose_name_plural = 'Relationships'
