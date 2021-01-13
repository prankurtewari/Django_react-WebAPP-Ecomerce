from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField( max_length=50,default='')
    description=models.CharField( max_length=250,default='')
    #created_at=models.DateTimeField(  auto_now_add=True,default='')
    #updated_at=models.DateTimeField( auto_now=True,default='')



    def __str__(self):
        return self.name

