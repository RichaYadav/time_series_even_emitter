from django.db import models

class Event(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    metric = models.CharField(max_length=50)
    value = models.FloatField()

    def __str__(self):
        return f"{self.metric}: {self.value} at {self.timestamp}"

