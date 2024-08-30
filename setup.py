from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_require(file:str)->List[str]:
  """
  this file will return list of requirements
  """
  requirements=[]
  with open(file) as file:
    requirements = file.readlines()
    requirements = [req.replace("\n","") for req in requirements]

    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)
    


setup(
  name='ML_project1',
   version='0.0.1',
   author='saqlain',
   author_email='ssmak786@gmail.com',
   packages=find_packages(),
   install_requires=get_require('requirements.txt')

)