from setuptools import setup, find_packages


install_required = [l.strip() for l in open("requirements.txt", "r")]


metadata = {
    'name': 'beanitor',
    'version': '0.1',
    'packages': find_packages(),
    'author': 'shonenada',
    'author_email': 'shonenada@gmail.com',
    'url': "https://github.com/shonenada/beanitor",
    'zip_safe': True,
    'platforms': ['all'],
    'package_data': {"": ['*.html', '*.jpg', '*.png', '*.css', '*.js',
                     '*.ico', '*.coffee', '*.less', '*.stylus']},
    'install_requires': install_required,
    'description': 'A monitor for beanstalkd.'}


if __name__ == '__main__':
    setup(**metadata)
