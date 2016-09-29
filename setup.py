from setuptools import find_packages, setup

setup(
    name='coral_client',
    version='1.1.0',
    packages=find_packages(),
    url='https://bitbucket.org/yuceali/coral_client',
    license='GPL',
    author='Ali Osman Yuce',
    author_email='aliosmanyuce@gmail.com',
    description='Hotelspro.com api client',
    install_requires=['requests'],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)