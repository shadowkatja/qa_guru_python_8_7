import os
import pathlib
from zipfile import ZipFile, ZIP_DEFLATED

import pytest

from path import tmp_path, resources_path


@pytest.fixture(scope='function', autouse=True)
def create_tmp():
    os.mkdir(tmp_path)
    yield
    os.remove(tmp_path)


@pytest.fixture(scope='function')
def create_zip(create_tmp):
    folder = pathlib.Path(resources_path)
    with ZipFile(zip_path, 'w', ZIP_DEFLATED) as zf:
        for file in folder.iterdir():
            zf.write(file, arcname=file.name)