from os.path import dirname, realpath, join
from setuptooles import setup, find_packages


CURRNET_DIR = dirname(realpath(__file__))

with open(join(CURRNET_DIR, 'README.rst')) as long_desc_file:
    long_desc = long_desc_file.read()

with open(join(CURRNET_DIR, 'requirements.txt')) as requirements:
    install_requires = [line.strip() for line in requirements]


setup(
    name="beanitor",
    version='0.1.0',
    author='shonenada',
    author_email='shonenada@gmail.com',
    url='https://github.com/shonenada/beanitor',
    zip_safe=True,
    description='A monitor for beanstalkd.',
    long_description=long_desc,
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        'Private :: Do Not Upload',
    ]
)
