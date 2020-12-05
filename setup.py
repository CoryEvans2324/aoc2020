from setuptools import find_packages, setup


with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

setup(
    name='aoc2020',
    author='Cory Evans',
    author_email="cory.evans@mailbox.org",
    url="https://github.com/CoryEvans2324",
    install_requirements=requirements,
    include_package_data=True
)
