from setuptools import setup, find_packages

setup(
    name='Distutils',
    version='1.0',
    description='python lab2',
    author='StepanovMS',
    author_email='stepanov@mail.ru',
    url='https://github.com/MatveySTEP/6403stepanovms',
    packages=find_packages(),
    install_requires=[
        'meteostat',
        'openpyxl',
        'numpy',
        'jupyterlab',
    ],
    python_requires='>=3.12',
)
