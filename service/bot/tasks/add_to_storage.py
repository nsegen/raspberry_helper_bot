from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger

from django.conf import settings

from pathlib import Path

from storage.models import Attachment, TYPE_BLOB, Record, TYPE_MUSIC, TYPE_PICTURE, TYPE_VIDEO, Type

logger = get_task_logger(__name__)

record_types_mapping = {
    'downloads': TYPE_BLOB,
    'music': TYPE_MUSIC,
    'video': TYPE_VIDEO,
    'photo': TYPE_PICTURE,
}


def add_folder(path):
    record_type = Type.objects.filter(
        record_type=record_types_mapping.get(path.name, TYPE_BLOB),
        name=path.name,
    ).first()
    if record_type is None:
        record_type = Type(
            record_type=record_types_mapping.get(path.name, TYPE_BLOB),
            name=path.name,
        )
        record_type.save()
    record = Record.objects.filter(record_type=record_type).first()
    if record is None:
        record = Record(record_type=record_type)
        record.save()
    for file in path.rglob('*.*'):
        print(file)
        if not Attachment.objects.filter(file=file.relative_to(settings.MEDIA_ROOT)).exists():
            attachment = Attachment(
                record=record,
            )
            attachment.file.name = file.relative_to(settings.MEDIA_ROOT)
            attachment.save()


@periodic_task(run_every=(crontab(minute="*/1")), name="add_to_storage", ignore_result=True)
def add_to_storage():
    add_folder(Path(settings.MEDIA_ROOT).joinpath('downloads'))
    for child in Path(settings.MEDIA_ROOT).joinpath('folders').iterdir():
        if child.is_dir():
            add_folder(child)

