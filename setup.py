from setuptools import setup, find_packages
from setuptools.command.install import install
import os
import io

SETUP_DIR = os.path.dirname(os.path.abspath(__file__))


def readfile(filename, split=False):
    with io.open(filename, encoding="utf-8") as stream:
        if split:
            return stream.read().split("\n")
        return stream.read()


plugin_readme = readfile("README.rst", split=True)[3:]  # skip title
plugin_license = readfile("LICENSE")
plugin_dependencies = [
    "setuptools",
    "PySide6",
    "opencmiss.utils",
    "opencmiss.zinc",
    "opencmiss.zincwidgets"
]


class InstallCommand(install):

    def run(self):
        install.run(self)
        # Automatically install requirements from requirements.txt
        import subprocess
        subprocess.call(['pip', 'install', '-r', os.path.join(SETUP_DIR, 'requirements.txt')])


setup(name='mapclientplugins.datamapstep',
    version='0.1.0',
    description='',
    long_description='\n'.join(plugin_readme) + plugin_license,
    classifiers=[
      "Development Status :: 3 - Alpha",
      "License :: OSI Approved :: Apache Software License",
      "Programming Language :: Python",
    ],
    cmdclass={'install': InstallCommand,},
    author='Mahyar Osanlouy',
    author_email='',
    url='',
    license='APACHE',
    packages=find_packages(exclude=['ez_setup',]),
    namespace_packages=['mapclientplugins'],
    include_package_data=True,
    zip_safe=False,
    install_requires=plugin_dependencies,
    )
