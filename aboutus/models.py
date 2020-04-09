from django.db import models

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    #image = models.ImageField(upload_to='about_us/')

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'Abous Us'

    def __str__(self):
        return self.title

class Why_Choose_Us(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name = 'Why Choose Us'
        verbose_name_plural = 'Why Choose Us'

    def __str__(self):
        return self.title

class Chef(models.Model):
    name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=30)
    bio = models.TextField()
    image = models.ImageField(upload_to = 'chef/') 

    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefs'

    def __str__(self):
        return self.name