import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseCustomModel(models.Model):
    """
    Abstract model for id and timestamps.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ticket(BaseCustomModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ticket = models.TextField()
    expires_on = models.DateTimeField()
