from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class UserModel(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
   
class add_expense(models.Model):
    # select=models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date = models.DateField()
    amount= models.DecimalField(max_digits=10,decimal_places=2, default=0)  
    type = models.CharField(max_length=10,default='expense')
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    location = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=10,null=True)
    

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,**kwargs):
        super().save(force_insert=False)

        img = Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)