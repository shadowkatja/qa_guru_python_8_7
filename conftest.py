import pathlib

import pytest
import os
from path import tmp_path, resources_path
from zipfile import ZipFile, ZIP_DEFLATED


@pytest.fixture(scope='function', autouse=True)
def create_tmp():
    os.mkdir(tmp_path)
    yield
    os.remove(tmp_path)

@pytest.fixture(scope='function')
def create_zip(create_tmp):
    folder = pathlib.Path(resources_path)
    zip_path = os.path.join(tmp_path, 'archive.zip')
    with ZipFile(zip_path, 'w', ZIP_DEFLATED) as zf:
        for file in folder.iterdir():
            zf.write(file, arcname=file.name)