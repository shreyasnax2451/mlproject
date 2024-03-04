from setuptools import find_packages, setup

HYPEN_E = '-e .'
def get_requirements(file_path:str) -> list[str]:
    with open(file_path, 'r') as require_file:
        requirements = require_file.read().split('\n')

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    return requirements

setup(
    name='mlproject',
    version='1.0.0',
    author='Shreyas',
    author_email='shreyasnax2451@gmail',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)