from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStamp


class GeneratedText(TimeStamp):
    """
    Model representing a generated text entry.

    Attributes:
        user (ForeignKey): Reference to the user who generated the text.
        prompt (TextField): The input prompt provided by the user.
        generated_text (TextField): The text generated based on the input prompt.
        created_at (DateTimeField): The timestamp when the entry was created.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.TextField()
    generated_text = models.TextField()


class GeneratedImage(TimeStamp):
    """
    Model representing a generated image.

    Attributes:
        user (ForeignKey): Reference to the user who generated the image.
        prompt (TextField): The text prompt used to generate the image.
        image_url (URLField): The URL where the generated image is stored.
        created_at (DateTimeField): The timestamp when the image was created.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.TextField()
    image_url = models.URLField()
