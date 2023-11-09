from setuptools import setup

setup(
    name="iploc",
    version="1.1",
    description="Geolocate an IP address",
    author="Croketillo",
    author_email="croketillo@gmail.com",
    packages=["iploc"],
    install_requires=[
        "requests",
        "colorama",
    ],
    python_tag="all",
    entry_points={
    'console_scripts': [
        'iploc=iploc.iploc:main',
    ],
}, 
)
