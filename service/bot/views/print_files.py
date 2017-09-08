from django.http import HttpResponseRedirect
from django.urls import reverse
# import pyipptool
import logging

logger = logging.getLogger(__name__)

config = {'ipptool_path': '/',
              'cups_uri': 'http://localhost:631/',
              'login': 'admin',
              'password': 'secr3t',
              'graceful_shutdown_time': 2,
              'timeout': 5}

# Create your views here.


def print_files(request, pk):
    
    logger.debug(request)
    return HttpResponseRedirect(
        reverse('admin:storage_attachmentproxy_changelist',)
    )
