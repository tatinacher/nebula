from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

class Character(models.Model):
    name = models.CharField(max_length=255)
    mother = models.ManyToManyField('self', symmetrical = True, blank = True)
    father = models.ManyToManyField('self', symmetrical = True, blank = True)
    children = models.ManyToManyField('self', symmetrical = True, blank = True)
    linked_to = models.ManyToManyField('self', symmetrical = True, blank = True)
    brothers = models.ManyToManyField('self', symmetrical = True, blank = True)
    sisters = models.ManyToManyField('self', symmetrical = True, blank = True)
    description = models.TextField(blank = True)
    nature = models.ForeignKey('Nature', on_delete=models.CASCADE, blank = True)
    images = models.ManyToManyField('Image', symmetrical = True, blank = True)
    def __str__(self):
        return '%s' % (self.name)

class Nature(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True)
    def __str__(self):
        return '%s' % (self.name)

class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/images/', blank = True)
    description = models.TextField(blank = True)
    def __str__(self):
        return '%s' % (self.name)