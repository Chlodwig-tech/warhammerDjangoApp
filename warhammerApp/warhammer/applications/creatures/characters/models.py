from django.db import models
from django.urls import reverse

# Create your models here.
from ..creature import Creature

class Character(Creature):
    
    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f'{self.name}'

    def get_s(self):
        return f'{self.K // 10}'

    def get_wt(self):
        return f'{self.Odp // 10}'
    
    def get_absolute_url(self):
        return reverse('warhammer:warhammer-characters:warhammer-characters-detail', kwargs={'id':self.id})