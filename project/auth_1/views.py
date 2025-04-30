from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from auth_1.tasks import process_image

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()

            # Call the Celery task to process the image
            process_image.apply_async(args=[image.id])

            return redirect('image_processing:upload_success')
    else:
        form = ImageUploadForm()

    return render(request, 'upload_image.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')
