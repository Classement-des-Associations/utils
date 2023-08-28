from files import FilesManager
from images import ImagesManager
from pdf import PDFManager
import logging

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    logging.info('--- Rendus Visuels ---')
    ImagesManager.clean_all_min_webp()
    VisuelManager = FilesManager("data", "visuel")
    logging.debug('Initiale size: %s',
                  VisuelManager.get_size(VisuelManager.files, True))
    logging.info("Start converting 'Rendus Visuels' to WebP")
    for file in VisuelManager.files:
        logging.debug("Converting '%s' to WebP" % file)
        ImagesManager.convert_to_webp(file)
    logging.info("End converting 'Rendus Visuels' to WebP")

    # Reload files to get new files
    VisuelManager.reload()

    logging.debug('Before compression size: %s',
                  VisuelManager.get_size(VisuelManager.get_webp_files(), True))

    logging.info('Start compressing WebP files')
    for file in VisuelManager.get_webp_files():
        logging.debug("Compressing '%s'" % file)
        ImagesManager.compress_webp(file)
    logging.info("End compressing WebP files")

    # Reload files to get new files
    VisuelManager.reload()

    logging.debug('After compression size: %s',
                  VisuelManager.get_size(VisuelManager.get_webp_files(), True))

    logging.info('--- End Rendus Visuels ---')

    logging.info('--- Rendus Ecrits ---')

    PDFManager.clean_all_min_pdf()
    RenduManager = FilesManager("data", "ecrit")

    logging.debug('Initiale size: %s',
                  RenduManager.get_size(RenduManager.get_pdf_files(), True))

    logging.info("Start compressing PDF files")
    for file in RenduManager.get_pdf_files():
        logging.debug("Compressing '%s'" % file)
        PDFManager.compress_file(file, file.replace(".pdf", ".min.pdf"))

    logging.info("End compressing PDF files")

    # Reload files to get new files
    RenduManager.reload()

    compressed_files = [file for file in RenduManager.get_pdf_files() if file.endswith(".min.pdf")]

    logging.debug('After compression size: %s',
                  RenduManager.get_size(compressed_files, True))

    logging.info('--- End Rendus Ecrits ---')
