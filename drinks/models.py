from django.db import models

def upload_to(instance, medie):
    return 'images/{medie}'.format(medie=medie)

class Drink(models.Model):
    name =models.CharField(max_length=200)
    description =models.CharField(max_length=500)
    image =models.ImageField(upload_to='Images/',default='Images/None/No0img.jpg' )

    def __str__(self):
        return self.name + ':' + self.description