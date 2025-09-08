from setuptools import setup, find_packages

setup(
    name="amazon_pricepal",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    entry_points={
        "console_scripts": [
            "amazon-price-finder=cli:main"
        ]
    },
    description="Amazon price getter package",
    author="Your Name",
)