import os
from zipfile import ZipFile

from path import resources_path, zip_path
from pypdf import PdfReader

def test_archive():
    resources_files = os.listdir(resources_path)
    with ZipFile(zip_path, 'r') as zf:
        assert resources_files == ZipFile.namelist(zf)

def test_txt_file():
    with ZipFile(zip_path, 'r') as zf:
        with open(os.path.join(resources_path,'Hello.txt')) as txt:
            original_file = txt.read()
            assert original_file == zf.read('Hello.txt').decode()

def test_pdf_file():
    with ZipFile(zip_path, 'r') as zf:
        original_file = PdfReader(os.path.join(resources_path,'Python Testing with Pytest (Brian Okken).pdf'))
        archived_file = PdfReader(zf.open('Python Testing with Pytest (Brian Okken).pdf'))
        assert len(original_file.pages) == len(archived_file.pages)
        assert original_file.pages[3].extract_text() == archived_file.pages[3].extract_text()


def