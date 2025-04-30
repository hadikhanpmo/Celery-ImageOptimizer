from celery import shared_task
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.base import ContentFile
from .models import Image

@shared_task
def process_image(image_id):
    # Get the image object from the database
    image = Image.objects.get(id=image_id)

    # Open the uploaded image
    img = PILImage.open(image.image)
    img.thumbnail((100, 100))

    # Save the image to a new file in memory
    thumb_io = BytesIO()
    img.save(thumb_io, img.format)
    thumb_file = ContentFile(thumb_io.getvalue(), name=f"thumb_{image.image.name}")

    # Save the resized image back to the model (you can save it to a new field or replace)
    image.image.save(f"thumb_{image.image.name}", thumb_file)
    image.processed = True
    image.save()

    return f"Image {image_id} processed successfully!"
