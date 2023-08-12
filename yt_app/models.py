from django.db import models
from website_app.models import *

# Create your models here.


class Youtube(models.Model):
    channel_name = models.CharField(max_length=100, blank=True, null=True)
    website_associated = models.ForeignKey(Website, on_delete=models.PROTECT)





class YoutubeIdeas(models.Model):

    IDEAONLY = "IDEAONLY"
    SCRIPTED = "SCRIPTED"
    FILMED = "FILMED"
    EDITED = "EDITED"
    UPLOADREADY = "UPLOADREADY"

    VIDEO_CREATION_CHOICES = [
        (IDEAONLY, "Idea Stage"),
        (SCRIPTED, "Script Completed"),
        (FILMED, "Filming Completed"),
        (EDITED, "Edit Completed"),
        (UPLOADREADY, "Upload Ready"),
        
    ]

    main_idea = models.CharField(max_length=200, blank=True, null=True)
    ideas_keywords = models.TextField(max_length=1000, blank=True, null=True)
    idea_expansion = models.TextField(max_length=1000, blank=True, null=True)
    video_creation_status = models.CharField(
        max_length=15,
        choices=VIDEO_CREATION_CHOICES,
        default=IDEAONLY,
    )
    video_channel = models.ForeignKey(Youtube, on_delete=models.PROTECT, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('yt_app:yt_detail', args=[str(self.id)])
    

    def __str__(self):
        return self.main_idea 

