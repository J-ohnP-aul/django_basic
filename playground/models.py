from django.db import models

# Create your models here.
class Topic(models.Model):
  text = models.CharField(max_length=200)
  date_added = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.text
  
class Entry(models.Model):
  # somthng specific learned about a topic
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  text = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    verbose_name_plural = 'entries'
    
  def __str__(self):
    '''rtn string rep of model'''
    return self.text[:50] + "..."
  
  