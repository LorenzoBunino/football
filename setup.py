import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name='football',
    version='0.1',
    author='Lorenzo Bunino',
    author_email="bunino.lorenzo@gmail.com",
    description="Analyze a season\'s worth of match data, provide insights",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lorenzobunino/football",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'football = football.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pandas>=1.2.0'],
    python_requires='>=3.6'
)
