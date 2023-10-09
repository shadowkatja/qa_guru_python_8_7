import os
from zipfile import ZipFile

from path import resources_path, zip_path


def test_archive():
    resources_files = os.listdir(resources_path)
    with ZipFile(zip_path, 'r') as zf:
        # check that all files are in archive
        assert resources_files == ZipFile.namelist(zf)

#def test_txt():
