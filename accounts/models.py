from django.db import models
from django.contrib.auth.models import User
from accounts.utils import generate_ref_code
# Create your models here.
class Customer(models.Model):
    name = models.OneToOneField(User,null = True, on_delete = models.CASCADE)   
    phone = models.CharField(max_length=12, null = True)
    email = models.CharField(max_length=64, null = True)
    #date_created = models.DateTimeField(auto_now_add = True, null = True)
    balance = models.IntegerField (null = True)
    withdrawn = models.IntegerField(null = True)
    #code = models.CharField(max_length=12, blank = True)
    #recommended_by = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True, related_name = 'ref_by')

    def __str__(self):
        return f"{self.name.username}"   #-{self.code}


   # def get_recomended_profiles(self):
        #pass

    #def save(self, *args, **kwargs):
       # if self.code == "":
            #code = generate_ref_code()
            #self.code = code
        #super().save(*args, **kwargs)
 
