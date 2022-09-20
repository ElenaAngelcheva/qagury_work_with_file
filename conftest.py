import shutil
from zipfile import ZipFile, Path
import allure
import pytest
import os


@pytest.fixture(scope='session', autouse=True)
def data_preparation():
    with allure.step('create_folder'):
        os.mkdir('resources')

    with allure.step('zip_files'):
        with ZipFile(f'resources/archive.zip', mode='w') as zip_file:
            for i in os.listdir('files'):
                if '__init__.py' not in i:
                    zip_file.write(f'files/{i}')

    with allure.step('unzip_files'):
        with ZipFile('resources/archive.zip') as zip_file:
            zip_file.extractall('resources/')

    yield

    with allure.step('remove_folder'):
        shutil.rmtree('resources')
