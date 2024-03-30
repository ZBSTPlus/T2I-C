from PIL import Image, ImageDraw, ImageFont
import os
from io import BytesIO
import base64
from pathlib import Path
 

def text_to_image(text,font_size="24",font_color="black",font_family="Courier", background_color="#FFFFFF",image_path="output.png"):
    
    # Convert font size to integer    
    font_size=int(font_size)

    # Create a new image with the specified size and background color
    image = Image.new("RGB", (500, 200), background_color)

    # Initialize ImageDraw object for drawing on the image
    draw = ImageDraw.Draw(image)

    font_path=""
    if font_family == "Courier":
        font_path = "CourierPrime-Regular.ttf"
    elif font_family == "Montserrat":
        font_path = "Montserrat-VariableFont_wght.ttf"
    elif font_family == "Roboto":
        font_path = "Roboto-Black.ttf"
    elif font_family == "Tangerine":
        font_path = "Tangerine-Regular.ttf"
    else:
        font_path = "CourierPrime-Regular.ttf"
    
    font_path = Path.joinpath(Path(__file__).parent,font_path)

    # Load the font
    font = ImageFont.truetype(font_path, font_size)  

    # Draw text on the image
    draw.text((100, 100), text, fill=font_color, font=font)

    # Save the image to a BytesIO buffer
    buffered = BytesIO()
    image.save(buffered, format="JPEG")

    # Encode the image data to base64 string
    img_str = base64.b64encode(buffered.getvalue())

    # Save the image to the specified path
    image.save(image_path)

    # Return the base64 encoded image string
    return  img_str.decode("utf-8")