import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitbar",
    version="2020.7.72",
    author="huqiwei",
    author_email="2607131406@qq.com",
    description="bitbar python pkg",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leohu1/bitbar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
