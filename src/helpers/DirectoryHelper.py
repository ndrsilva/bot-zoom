"""..."""
from os import listdir
from os import path


class DirectoryHelper:
    """..."""

    def __init__(self, dir_file: str) -> None:
        """..."""

        self.__dir = dir_file

    def list_files_type(self, extension: str) -> list:
        """..."""

        list_all = self.__list_files_all()
        list_files = [file for file in list_all
                      if file.lower().endswith(extension)]

        return list_files

    def __list_files_all(self) -> list:
        """..."""

        list_files = [path.join(self.__dir, nome)
                      for nome in listdir(self.__dir)]

        return list_files


# Test
# if __name__ == '__main__':
#     directory_helper = DirectoryHelper(r'.\temp\x')
#     print(directory_helper.list_files_type('txt'))


