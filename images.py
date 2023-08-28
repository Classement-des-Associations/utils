import logging
import os
from PIL import Image
from pdf2image import convert_from_path  # import library


class ImagesManager:
    def clean_all_min_webp():
        """
        Clean all WebP files in path
        """
        os.system("rm -rf data/**/*.webp")

    def __pdf_to_webp(pdf_file):
        """
        Convert a PDF file to a WebP file using PIL
        """
        images = convert_from_path(pdf_file)  # Read pdf file
        for image in images:
            image.save(os.path.splitext(pdf_file)[0] + ".webp", "WEBP")

    def __image_to_webp(png_file):
        """
        Convert an files to a WebP file using PIL
        """
        image = Image.open(png_file)
        image.save(os.path.splitext(png_file)[0] + ".webp", "WEBP")

    @classmethod
    def convert_to_webp(cls, file):
        """
        Convert a file to a WebP file using PIL
        """
        try:
            if file.endswith(".pdf"):
                cls.__pdf_to_webp(file)
            # else if end with png or jpg or jpeg or gif
            elif file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".gif"):
                cls.__image_to_webp(file)
            else:
                logging.info("File type not supported")
        except Exception as e:
            logging.error(e)

    @classmethod
    def compress_webp(cls, file):
        """
        Compress a WebP file using PIL to 512x512 with a quality of 80%
        """
        try:
            if file.endswith(".webp"):
                image = Image.open(file)
                image.thumbnail((512, 512), Image.ANTIALIAS)
                image.save(file, "WEBP", quality=80)
            else:
                logging.info("File type not supported")
        except Exception as e:
            logging.error(e)
