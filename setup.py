from setuptools import setup, find_packages

setup(
    name="file-organizer-cli",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'file-organizer=file_organizer:main',
        ],
    },
    author="Your Name", # Ganti dengan nama Anda
    author_email="your.email@example.com", # Ganti dengan email Anda
    description="A CLI tool to organize and clean files.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eidolon1302/cli-mad", # Pastikan ini URL repo Anda
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyfiglet',
    ],
)
