from pathlib import Path
from setuptools import setup, find_packages

_here = Path(__file__).resolve().parent
# read the contents of README file
# with open(_here.joinpath('README.md'), "r", encoding='utf-8') as f:
#     long_desc = f.read()
long_desc = ""


with open(_here.joinpath("requirements.txt"), "r", encoding="utf-8") as f:
    all_reqs = [
        x
        for x in f.read().split("\n")
        if x.strip() and not x.startswith("#") and not x.startswith("-")
    ]

install_requires = [x.strip() for x in all_reqs if "git+" not in x]
dependency_links = [
    x.strip().replace("git+", "") for x in all_reqs if x.startswith("git+")
]

setup(
    name="TODO",
    version="0.0.1",
    description="TODO",
    python_requires=">=3.8",
    install_requires=install_requires,
    dependency_links=dependency_links,
    packages=find_packages(),
    license="MIT License",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    author="TODO",
    author_email="TODO",
    url="TODO",
    download_url="TODO",
    extras_require={"dev": ["pytest", "pytest-pep8", "pytest-cov", "tox"]},
    keywords=["TODO"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Debuggers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
