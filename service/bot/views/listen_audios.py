from django.http import HttpResponseRedirect
from django.urls import reverse
from storage.models import Record, Attachment
import logging

logger = logging.getLogger(__name__)


def listen_audios(request, pk):
    
    attachment = Attachment.objects.filter(record__pk=pk).first()
    playsound(attachment.file.path, attachment.extension)
    logger.debug(attachment)
    return HttpResponseRedirect(
        reverse('admin:storage_attachmentproxy_changelist',)
    )
