from django.db import models
from multiselectfield import MultiSelectField
from django.urls import reverse

CATEGORIES = (
    ('is_tiring', 'Ciężki'),
    ('is_impact', 'Druzgoczący'),
    ('is_experimental', 'Eksperymentalny'),
    ('is_shrapnel', 'Odłamkowy'),
    ('is_pummeling', 'Ogłuszający'),
    ('is_defensive', 'Parujący'),
    ('is_slow', 'Powolny'),
    ('is_precise', 'Precyzyjny'),
    ('is_armour_pisercing', 'Przebijający zbroję'),
    ('is_special', 'Specjalny'),
    ('is_fast', 'Szybki'),
    ('is_snare', 'Unieruchamiający'),
    ('is_balanced', 'Wyważony'),
    ('is_unreliable', 'Zawodny')
)

GROUP = [
    ('Zwykła', ('Zwykła')),
    ('Długi Łuk', ('Długi Łuk')),
    ('Dwuręczna', ('Dwuręczna')),
    ('Kawaleryjska', ('Kawaleryjska')),
    ('Korbacz', ('Korbacz')),
    ('Kusza', ('Kusza')),
    ('Mechaniczna', ('Mechaniczna')),
    ('Palna', ('Palna')),
    ('Parująca', ('Parująca')),
    ('Proca', ('Proca')),
    ('Rzucana', ('Rzucana')),
    ('Szermiercza', ('Szermiercza')),
    ('Unieruchamiająca', ('Unieruchamiająca')),
]

AVAILABILITY = [
    ('-', ('-')),
    ('przeciętna', ('przeciętna')),
    ('duża', ('duża')),
    ('mała', ('mała')),
    ('rzadka', ('rzadka')),
    ('sporadyczna', ('sporadyczna')),
    ('znikoma', ('znikoma')),
]

RELOAD = [
    (0,(0)),
    (1,(1)),
    (2,(2)),
    (3,(3)),
    (4,(4)),
    (5,(5)),
    (6,(6)),
    (7,(7)),
    (8,(8)),
    (9,(9)),
    (10,(10)),
]

# Create your models here.
class Weapon(models.Model):
    name        = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    cost_gc     = models.IntegerField()
    cost_s      = models.IntegerField(default=0, blank=True, null=True)
    cost_p      = models.IntegerField(default=0, blank=True, null=True)
    enc         = models.IntegerField()
    group       = models.CharField(
        max_length=30,
        choices=GROUP,
        default=('Ordinary', ('Zwykła'))
    )
    damage        = models.IntegerField()
    is_melee      = models.BooleanField(default=True)
    is_two_handed = models.BooleanField(default=False)
    is_damage_strength_depend = models.BooleanField(default=True)
    short_range   = models.IntegerField(default=0, blank=True, null=True)
    long_range    = models.IntegerField(default=0, blank=True, null=True)
    reload_in_actions = models.IntegerField(
        choices=RELOAD,
        default=0,
        blank=True,
        null=True
    )
    #reload_in_actions = models.IntegerField(default=0, blank=True, null=True)
    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY,
        default=('przeciętna', ('przeciętna')),
    )
    qualities = MultiSelectField(choices=CATEGORIES, max_length=180, null=True, blank=True)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_qualities(self):
        return str(self.qualities) if self.qualities else 'brak'

    def get_cost(self):
        price = ''
        if self.cost_gc:
            price += f'{self.cost_gc} zk '
        if self.cost_s:
            price += f'{self.cost_s} s '
        if self.cost_p:
            price += f'{self.cost_p} p'

        if price == '':
            return '-'
        return price

    def get_cost_in_p(self):
        price = 0
        if self.cost_gc:
            price += 240 * self.cost_gc
        if self.cost_s:
            price += 12 * self.cost_s
        if self.cost_p:
            price += self.cost_p
        return price

    def get_range(self):
        return f'{self.short_range}/{self.long_range if self.long_range else "-"}'

    def get_damage(self):
        if self.is_damage_strength_depend:
            if self.damage > 0:
                return f'S+{self.damage}'
            if self.damage < 0:
                return f'S{self.damage}'
            return 'S'
        return f'{self.damage}'            

    def get_absolute_url(self):
        return reverse('warhammer:warhammer-weapons:weapon-detail', kwargs={'id':self.id})