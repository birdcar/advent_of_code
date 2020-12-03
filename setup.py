from setuptools import setup, find_packages

with open("README.md", "r") as readme_fh:
    long_description = readme_fh.read()

setup(
    name="advent-of-code-2020-@nickcannariato",
    version="0.0.1",
    author="Nick Cannariato",
    author_email="devrel@nickcannariato.dev",
    description="My solutions to Advent of Code",
    long_description=long_description,
    long_description_content_type="type/markdown",
    url="https://github.com/nickcannariato/advent_of_code_2020",
    packages=find_packages(),
    python_requires=">=3.8",
)