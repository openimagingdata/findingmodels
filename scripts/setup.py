from setuptools import setup, find_packages

setup(
    name='findingmodels',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here, e.g., 'numpy', 'pandas'
    ],
    entry_points={
        'console_scripts': [
            'findingmodels=findingmodels.main:main',  # Replace with your actual module and function
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)