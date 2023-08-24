# this app exports each individual powerpoint slide into .JPG files into an output folder
import os
from pptx import Presentation
from PIL import Image

def save_slides_as_images(pptx_path, output_folder):
    presentation = Presentation(pptx_path)

    for slide_number, slide in enumerate(presentation.slides, start=1):
        slide_image = Image.new('RGB', slide.dimensions)
        slide.draw(slide_image)

        image_filename = os.path.join(output_folder, f"slide_{slide_number:02}.jpg")
        slide_image.save(image_filename, 'JPEG')

if __name__ == "__main__":
    
    script_folder = os.path.dirname(os.path.abspath(__file__))
    
    pptx_file_path = os.path.join(script_folder, "H:\DCS SUPPORTIVE STUFF\DCS KNEEBOARD\F18 - Kneeboard_Supplementary_Info - Copy.pptx")
    output_folder_path = os.path.join(script_folder, "H:\DCS SUPPORTIVE STUFF\DCS KNEEBOARD\Kneeboard_Output\test")

    save_slides_as_images(pptx_file_path, output_folder_path)
    
    
    