
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="dodo-jinja2",
    version="0.9.3",
    description="add jinja2 template engine to dodo.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="tikubonn",
    author_email="https://twitter.com/tikubonn",
    url="https://github.com/tikubonn/dodo-jinja2",
    license="GPLv3",
    packages=find_packages(),
    install_requires=[
        "dodo==0.9.3",
        "jinja2==2.11.3",
    ],
    dependency_links=[
        "git+ssh://git@github.com/tikubonn/dodo.git@master#egg=dodo-0.9.3",
    ],
    entry_points={
        "dodo_init": [
            "dodo_jinja2 = dodo_jinja2:init",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
)
