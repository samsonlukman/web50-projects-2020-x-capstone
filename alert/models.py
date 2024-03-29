from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="User")
    content = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=100, blank=False)
    lga = models.CharField(max_length=100, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
    
    category = models.CharField(max_length=50, blank = False, null=False)
    

    def __str__(self):
        return f"New crime alert from {self.user} from {self.state}, {self.lga} and coordinates longitude:{self.longitude} and latitude:{self.latitude}"
