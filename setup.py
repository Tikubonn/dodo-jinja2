
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="doodoo-jinja2",
    version="0.9.1",
    description="add jinja2 template engine to doodoo.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="tikubonn",
    author_email="https://twitter.com/tikubonn",
    url="https://github.com/tikubonn/doodoo-jinja2",
    license="GPLv3",
    packages=find_packages(),
    install_requires=[
        "doodoo==0.9.1",
        "jinja2==2.10.1",
    ],
    dependency_links=[
        "git+ssh://git@github.com/tikubonn/doodoo.git@master#egg=doodoo-0.9.1",
    ],
    entry_points={
        "doodoo_init": [
            "doodoo_jinja2 = doodoo_jinja2:init",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
)
