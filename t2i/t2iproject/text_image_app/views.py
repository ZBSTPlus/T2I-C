from django.shortcuts import render
from django.http import HttpResponse
from .t2iapp import text_to_image
from pathlib import Path

# Create your views here.

def index(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')

        custom_image_path = Path.joinpath(Path(__file__).parent,"output.png")
        print(custom_image_path)
        image_path = text_to_image(input_text, custom_image_path)
        return render(request, 'text_image_app/index.html', {'image_path': image_path})
      
    return  render(request, 'text_image_app/index.html')


def download_image():

    image_path = Path(
        'C:/Users/dell/OneDrive/Desktop/t2i/t2iproject/text_image_app/static/images/output.png')
    if image_path.exists():
        with open(image_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename="output.png"'
            return response
    else:
        return HttpResponse("Image file not found.")

