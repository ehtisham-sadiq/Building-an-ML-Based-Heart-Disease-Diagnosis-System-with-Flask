from setuptools import setup, find_packages
from typing import List


hypen_dot = "-e ."
def get_requirements(file_path:str)-> List[str]:
    
    """this function will return a list of requirements
    """
    requirements = []
    
    # reading of requirements.tx file
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if hypen_dot in requirements:
            requirements.remove(hypen_dot)
            
    return requirements
    

setup(
    name ="First-ML-Project",
    version="0.0.1",
    author="ehtisham",
    author_email="bsef19m521@pucit.edu.pk",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)