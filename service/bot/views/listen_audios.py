from django.http import HttpResponseRedirect
from django.urls import reverse
# import pyipptool
import logging

logger = logging.getLogger(__name__)


def listen_audios(request, pk):
    
    logger.debug(request)
    return HttpResponseRedirect(
        reverse('admin:storage_attachmentproxy_changelist',)
    )
