import setuptools
import classifier as c

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name=c.APP_NAME,
    version=c.APP_VERSION,
    author=c.APP_AUTHOR,
    license_files=('LICENSE'),
    description=c.APP_DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=c.APP_URL,
    project_urls={
        'Documentation': 'https://github.com/FoxtrotCore/ftuv2',
        'Bug Tracking': 'https://github.com/FoxtrotCore/ftuv2/issues'
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    install_requires=[
    ],
    extras_require={
        "dev": [
            "setuptools",
            "wheel",
            "flake8",
            "twine",
            "sphinx",
            "sphinx_rtd_theme",
        ]
    },
    python_requires='>=3.9.0',
    entry_points={
        "console_scripts": [
            f'{c.APP_NAME} = classifier.__main__:main'
        ]
    }
)
