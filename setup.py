import setuptools

from jsonly import __version__

setuptools.setup(
    name="jsonly",
    version=__version__,
    license="MIT",
    author="VoidAsMad",
    author_email="star@devksy.xyz",
    description="JSON 데이터 관리 라이브러리",
    long_description=open("README.md", "rt", encoding="UTF8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/VoidAsMad/jsonly",
    packages=setuptools.find_packages(),
    python_requires=">=3.10",
)
