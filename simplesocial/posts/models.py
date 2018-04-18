from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group
from djago.contrib.auth import get_user_model
import misaka
# Create your models here.
#POSTS MODELS.PY

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(related_name='posts')
    created_at = models.DateTimeField(auto_now=True) #post time is auto generated
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misake.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username':self.username
                                                'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message'] #every message is uniquely linked to the user
