from django.db import models
from django.urls import reverse
# Create your models here.

class Person(models.Model):
    AGE_RANGE = [
        ('A', '18 - 30'),
        ('B', '31 - 43'),
        ('C', '44 - 56'),
        ('D', '57 - 69'),
        ('E', '70 +'),
    ]
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    age_range = models.CharField(default='A', help_text="Tell us your age (in years) so we can personalize your experience!", choices=AGE_RANGE)
    gender = models.CharField(default='F', max_length=1, choices=GENDER_CHOICES)
    fitness_goals = models.TextField(help_text="Your Fitness Goals: What are you aiming for?", max_length=100)
    lifestyle = models.TextField(help_text="Could you share what your typical fitness routine involves?", max_length=200, blank=True, null=True)
      
    class Meta():
        ordering = ['gender', 'age_range', 'fitness_goals', 'lifestyle']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('person-detail', args=[str(self.id)])
    def __str__(self) -> str:
        return f'{self.age_range}, {self.fitness_goals.title()}, {self.lifestyle.title()}, {self.gender}'

