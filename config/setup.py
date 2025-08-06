from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements from the given file path.
    '''
    requirements=[]
    with open('./requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
    name='RS-MIGA',
    version='0.1',
    author='Giorgio Casoni',
    author_email='giorgio.casoni.03@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)