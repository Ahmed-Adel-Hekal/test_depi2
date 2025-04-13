from setuptools import find_packages, setup
from typing import List


def requirement_parser(path:str)->List[str]:
    with open(path) as f :
        req = f.readlines()
    req = [i.replace("\n","") for i in req]
    if "-e ." in req : 
        req.remove('-e .')
    return req 



setup(
    name='depi_test_2',
    version="0.0.1",
    author="Hekal",
    author_email="ahmedadelhekal@gmail.com",
    packages=find_packages(),
    install_requires=requirement_parser("requirements.txt")
)