from django.db import models


class Post(models.Model):
    id = models.AutoField(primary_key=True,
                          db_column='id')
    title = models.CharField(max_length=255,
                             null=False,
                             blank=False,
                             db_column='title')
    content = models.TextField(null=False,
                               blank=True,
                               db_column='content')
    image = models.ImageField(upload_to='images/',
                              null=True,
                              blank=True,
                              db_column='image')
    create_at = models.DateTimeField(default=None,
                                     null=False,
                                     blank=False,
                                     db_column='create_at')
    update_at = models.DateTimeField(default=None,
                                     null=True,
                                     blank=True,
                                     db_column='update_at')