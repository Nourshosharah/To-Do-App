from django.db import models
from django.utils import timezone
import datetime
from datetime import datetime


# Create your models here.
class TO_DO(models.Model):
    text=models.TextField(max_length=500)
    date=models.DateTimeField(null=True, blank=True, default=datetime.now)
# Create your models here.
    def __str__(self):
        return self.text

