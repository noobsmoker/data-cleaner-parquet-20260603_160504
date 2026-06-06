from setuptools import setup, find_packages

setup(
    name="data-cleaner-parquet-20260603_160504",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'data=data:main',
        ],
    },
)
