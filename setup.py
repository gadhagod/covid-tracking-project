import setuptools

setuptools.setup(
    name='covid-tracking-project',
    version='0.1',
    author='Aarav Borthakur',
    author_email='gadhaguy13@gmail.com',
    description='A python wrapper for the Covid Tracking Project API',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gadhagod/covid-tracking-project',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)