from django.db import models

# Create your models here.
class Todotask(models.Model):
    Tid = models.AutoField(primary_key=True,null=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    completedstatus=models.CharField(max_length=50, null=True, blank=True)