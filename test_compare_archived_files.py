import os
from zipfile import ZipFile

from openpyxl.reader.excel import load_workbook

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


def test_xlsx_file():
    with (ZipFile(zip_path, 'r') as zf):
        original_file = load_workbook(os.path.join(resources_path,'file_example_XLSX_50.xlsx'))
        archived_file = load_workbook(zf.open('file_example_XLSX_50.xlsx'))
        for worksheet in original_file.sheetnames:
            original_sheet = original_file[worksheet]
            archived_sheet = archived_file[worksheet]
        for row in range(1, original_sheet.max_row + 1):
            for col in range(1, original_sheet.max_column + 1):
                original_cell = original_sheet.cell(row, col)
                archived_cell = archived_sheet.cell(row, col)
                if original_cell.value == archived_cell.value:
                    result = True
                else:
                    result = False
                    break
        assert result == True
