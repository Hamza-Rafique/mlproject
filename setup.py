import setuptools
from setuptools import find_packages  # Explicit import for clarity

def readme():
    """Read the README.md file for the long description."""
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

setuptools.setup(
    name='mlproject',
    version='0.0.1',
    author='Hamza Rafqiue',  
    author_email='hamzarafique964@gmail.com',  
    description='A short description of your machine learning project',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Hamza-Rafique/mlproject', 
    packages=find_packages(exclude=['tests.*', '*.tests', '*.test']),  # Exclude tests
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify minimum Python version required
    install_requires=[
         'numpy', 'pandas', 'seaborn'
    ],
    extras_require={
        # Optional dependencies (e.g., 'dev': ['pytest', 'mypy'])
    },
    entry_points={
        'console_scripts': [
            'mlproject=mlproject.cli:main',  # Example entry point (replace with your script)
        ],
    },
)
