from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    SHIRT_SIZES = (
        ('S', 'SMALL'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shirt_size = models.CharField(max_length=1,null=True ,choices=SHIRT_SIZES)

    def __str__(self):
        return self.first_name


class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class Models(models.Model):
    Model = models.CharField(max_length=100)


class Manufacturer(models.Model):
    Brand = models.CharField(max_length=100)
    model = models.ManyToManyField(Models)
    cover = models.ImageField(null=True, blank=True)


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Best Cars')
    date_created = models.DateTimeField(auto_created=True)