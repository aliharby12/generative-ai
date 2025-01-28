from django.db import models
import uuid
from django.utils import timezone
from typing import Type


class TimeStamp(models.Model):
    """
    Abstract base model that provides self-updating 'created_at' and 'updated_at' fields,
    along with a unique UUID for each instance.

    Attributes:
        uuid (UUIDField): Unique identifier for each instance, generated automatically.
        created_at (DateTimeField): Timestamp indicating when the instance was created, set automatically.
        updated_at (DateTimeField): Timestamp indicating when the instance was last updated, set automatically.
    """

    uuid: models.UUIDField = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True
    )
    created_at: models.DateTimeField = models.DateTimeField(
        default=timezone.now, editable=False
    )
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        abstract: bool = True
