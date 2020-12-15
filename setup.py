from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='ganntchart',
    version='1.2.3',
    description='Draw Gannt Chart with svg format',
    url='https://github.com/EdwardHong0627/gannt_chart',
    author='EdwardHong0627',
    author_email='edwardboy0627@gmail.com',
    license='MIT',
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['ganntchart'],
    keywords=['ganntchart', "scheduling"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

    ]
)
