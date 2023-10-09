import filecmp
import os
from zipfile import ZipFile

from path import resources_path, zip_path


# check that all files are in archive
def test_archive():
    resources_files = os.listdir(resources_path)
    with ZipFile(zip_path, 'r') as zf:
        assert resources_files == ZipFile.namelist(zf)

def test_files():
    with ZipFile(zip_path, 'r') as zf:
        # check txt
        with open(os.path.join(resources_path,'Hello.txt')) as txt:
            original_file = txt.read()
            assert original_file == zf.read('Hello.txt').decode()


