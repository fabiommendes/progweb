from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    role_choices = [(1,'Professor'), (2,'Monitor')]

    role = models.IntegerField(choices=role_choices)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        role_map = dict(self.role_choices)
        return '%s (%s)' %(self.user.first_name, role_map[self.role])

class Discipline(models.Model):
    code = models.IntegerField("Codigo", unique=True, blank=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s (%s)' %(self.name, self.code)

class ClassRoom(models.Model):
    class_letter = models.CharField('Turma', max_length=2, blank=False)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE,
                                   related_name="class_rooms")
    class_time = models.TimeField('Horario', blank=False)

    profiles = models.ManyToManyField(Profile, related_name="class_rooms")


    def __str__(self):
        return '%s (%s)' %(self.discipline.name, self.class_letter)

    @property
    def students(self):
        return self.profiles.filter(role=2)

    @property
    def teachers(self):
        return self.profiles.filter(role=1)

