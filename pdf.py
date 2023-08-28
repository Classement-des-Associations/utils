import os
import sys
from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet


class PDFManager:

    @classmethod
    def clean_all_min_pdf(cls):
        os.system("rm data/**/*.min.pdf")

    @classmethod
    def compress_file(cls, input_file: str, output_file: str):
        """Compress PDF file"""
        if not output_file:
            output_file = input_file
        try:
            # Initialize the library (you need to insert your own serial number)
            PDFNet.Initialize("<key>")
            doc = PDFDoc(input_file)
            # Optimize PDF with the default settings
            doc.InitSecurityHandler()
            # Reduce PDF size by removing redundant information and compressing data streams
            Optimizer.Optimize(doc)
            doc.Save(output_file, SDFDoc.e_linearized)
            doc.Close()
        except Exception as e:
            print("Error compress_file=", e)
            doc.Close()
