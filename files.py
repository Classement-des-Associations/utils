import os


class FilesManager:
    path = ""
    type = None
    files = list()

    def __init__(self, path, type):
        self.type = type
        self.path = path
        self.files = self.retrieve(path, type)

    def retrieve(self, path, type):
        """
        Get all files in path
        """
        data = []
        for root, _, files in os.walk(path):
            for file in files:
                if type in file:
                    data.append(os.path.join(root, file))
        return data

    def reload(self):
        """
        Reload files
        """
        self.files = self.retrieve(self.path, self.type)

    def get_size(self, files, human_readable=False):
        """
        Get size of all files
        """
        size = 0
        for file in files:
            size += os.path.getsize(file)
        return human_readable and self.__convert_size_to_humain_readable(size) or size

    def __convert_size_to_humain_readable(self, size):
        """
        Convert size to human readable
        """
        if size < 1024:
            return str(size) + " octets"
        elif size < 1048576:
            return str(round(size / 1024, 2)) + " Ko"
        elif size < 1073741824:
            return str(round(size / 1048576, 2)) + " Mo"
        elif size < 1099511627776:
            return str(round(size / 1073741824, 2)) + " Go"
        else:
            return str(round(size / 1099511627776, 2)) + " To"

    def __get_files_by_ext(self, type):
        """
        Get all files by extension
        """
        files = []
        for file in self.files:
            if file.endswith(type):
                files.append(file)
        return files

    def get_webp_files(self):
        """
        Get all WebP files in path
        """
        return self.__get_files_by_ext(".webp")

    def get_pdf_files(self):
        """
        Get all PDF files in path
        """
        return self.__get_files_by_ext(".pdf")
