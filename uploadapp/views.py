import re
import io
import base64

from django.core.files import File
from django.shortcuts import render

from .forms import StoreImageForm


def upload_canvas(request):
    form = StoreImageForm()
    if request.method == 'POST':
        image_base64 = request.POST.get('image_base64', '')
        res = re.match(r'^([^,]*),(.*)$', image_base64)
        if res:
            ext = re.match(r'^data:image/(.+);base64$', res.groups()[0]).groups()[0]
            image = base64.b64decode(res.groups()[-1])
            buf = io.BytesIO(image)
            form = StoreImageForm(files={'upload_file': File(buf, name=f'name.{ext}')})
            try:
                form.is_valid()
            except Exception as err:
                return render(request, 'form.html', {'message': err, 'form': form})
            instance = form.save()
            return render(request, 'form.html', {'message': 'Image Uploaded Successfuly', 'form': form})
        return render(request, 'form.html', {'message': 'Image Upload Failed', 'form': form})
    return render(request, 'form.html', {'message': 'Upload Image...', 'form': form})
