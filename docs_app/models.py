from django.db import models

# Create your models here.


class Document(models.Model):
    name = models.CharField(max_length=13)
    given_amt = models.IntegerField(default=0)
    daily_amt = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=False)
    records = models.JSONField()
    
    def __str__(self):
        return self.name+'  '+str(self.given_amt)