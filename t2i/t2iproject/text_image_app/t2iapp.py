from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, image_path="output.png"):
    # Create a new image with the specified size and background color
    image = Image.new('RGB', (1000, 800), (255, 255, 255))
    
    # Initialize ImageDraw object
    draw = ImageDraw.Draw(image)
    
    # Use a default font if font_path is not provided
    font = ImageFont.truetype("arial.ttf", 16)
    
    # Calculate text position to center it in the image
    # text_width, text_height = draw.textsize(text, font)
    # x = (image_size[0] - text_width) // 2
    # y = (image_size[1] - text_height) // 2
    
    # Draw the text on the image
    draw.text((100, 100), text, font=font, fill="white")
    
    # Save the resulting image
    image.save(image_path)

    #Show the resulting image
    image.show()

# Example usage:
text = input()

