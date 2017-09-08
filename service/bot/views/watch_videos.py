from django.shortcuts import render
from storage.models.attachment import Attachment
# import pyipptool
import logging

logger = logging.getLogger(__name__)


def watch_videos(request, pk):
    
    videos = [
      request.build_absolute_uri(attachment.file.url).replace('http', 'https') for attachment in Attachment.objects.filter(record__pk=pk)
    ]

    return render(request, 'videos.html', {
      'videos': videos
    })
