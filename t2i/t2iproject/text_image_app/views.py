from django.shortcuts import render
from django.http import HttpResponse
from .t2iapp import text_to_image
from pathlib import Path

# Create your views here.

def index(request):
    if request.method == 'POST':
        # Retrieve input text from the POST request
        input_text = request.POST.get('input_text', '')
        font_size = request.POST.get('font_size', 24)
        font_color = request.POST.get('font_color', 'black')
        background_color = request.POST.get('background_color', '#FFFFFF')
        font_family = request.POST.get('font_family', 'Arial')
        
        # Define the custom image path where the generated image will be saved
        custom_image_path = Path.joinpath(Path(__file__).parent,"output.png")
        print(custom_image_path)
        
        # Call the text_to_image function to generate the image
        image_path = text_to_image(
            input_text, font_size, font_color, font_family, background_color, custom_image_path)
             
        
        # Pass the image path to the template for display
        return render(request, 'text_image_app/index.html', {'image_path': image_path})
    
    # Render the index template if the request method is GET
    return render(request, 'text_image_app/index.html')



def download_image(request):
    # Define the path to the image file
    image_path = Path(
        'C:/Users/dell/OneDrive/Desktop/t2i/t2iproject/text_image_app/static/images/output.png')
  # Check if the image file exists    
    if image_path.exists():
        # Open the image file in binary mode
        with open(image_path, 'rb') as file:
            # Create an HTTP response with the image data
            response = HttpResponse(file.read(), content_type='image/png')
            # Set the content disposition header to trigger download
            response['Content-Disposition'] = 'attachment; filename="output.png"'
            # Return the HTTP response with the image data
            return response
    else:
        # Return an HTTP response indicating that the image file was not found
        return HttpResponse("Image file not found.")
