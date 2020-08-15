from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    # streamlit
    'streamlit==0.64.0']

setup(
    name='ColorizeFileList',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='colorize file list'
)
