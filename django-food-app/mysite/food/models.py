from django.db import models

# Create your models here.
class Item(models.Model):

     def __str__(self) -> str:
          return self.item_name

     item_name = models.CharField(max_length=200)
     item_desc = models.CharField(max_length=200)
     item_price = models.IntegerField()
     item_image = models.CharField(max_length=500, default='https://th.bing.com/th/id/R.59b8493ce8bc3e21038d9b85a44b6133?rik=VwcGq4PVCk2dvA&riu=http%3a%2f%2fwww.ukvisitorguide.cn%2fwp-content%2fuploads%2f2015%2f11%2fFood-placeholder.jpg&ehk=vLfv4oTMqt4NGoXjvXIWptKQZN3aCyg9btfYCj4%2b3Lc%3d&risl=&pid=ImgRaw&r=0')