"""Setup file for custom-poling module."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# with open('requirements.txt') as fp:
#     install_requires = fp.read()

setuptools.setup(
    name="custom_poling",
    description="Custom poling module",
    long_description=long_description,
    packages=setuptools.find_packages(),
    # install_requires=install_requires,
    install_requires=["matplotlib>=2.1,<3.4"],
    python_requires='>=3.6'
)
