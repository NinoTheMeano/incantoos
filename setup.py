import setuptools


setup_info = {
    "name": "incantoos",
    "version": "1.0.0",
    "author": "NinoTheMeano",
    "author_email": "ninosdeveloping@gmail.com",
    "description": "IncantoOS Is intended to give ",
    "url": "https://github.com/ro-py/ro.py",
    "packages": setuptools.find_packages(),
    "classifiers": [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: AsyncIO",
        "Topic :: Internet :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Software Development :: Libraries"
    ],
    "project_urls": {
        "Discord": "https://discord.com/users/255125932447236096"
    },
    "python_requires": '>=3.9',
    "install_requires": [
        "httpx>=0.21.0",
        "python-datetime>=2.8.0"
    ]
}


setuptools.setup(**setup_info)