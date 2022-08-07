from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField(default='')
    created_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    visible = models.BooleanField()
    important = models.BooleanField()
    created_user = models.CharField(max_length=100, default='사용자')
    # created_user = models.ForeignKey("User", on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_time', 'last_modified']
