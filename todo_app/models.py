from django.db import models

# Create your models here.


class Bucket(models.Model):
  name = models.CharField(max_length=120)
  
  def _str_(self):
    return self.name
    

class Todo(models.Model):
  bucket = models.ForeignKey(
        Bucket, related_name="bucket", on_delete=models.CASCADE
    )
  title = models.CharField(max_length=120)
  description = models.TextField()
  is_done = models.BooleanField(default=False)

  def _str_(self):
    return self.title



