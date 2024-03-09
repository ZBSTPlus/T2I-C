from django.shortcuts import render
from .forms import TextToImageForm
from .utils import generate_image

def text_to_image(request):
    if request.method == 'POST':
        form = TextToImageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            font_size = form.cleaned_data['font_size']
            image = generate_image(text, font_size)
            # Save or display the image as needed
    else:
        form = TextToImageForm()

    return render(request, 'text_converter/text_to_image.html', {'form': form})
