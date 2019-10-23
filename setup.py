from setuptools import setup, find_packages
import os, re, codecs

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    """ Snippet from https://packaging.python.org/guides/single-sourcing-package-version/
    """
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ *= *['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

test_deps = [ 'pytest==5.2.1', ]

with open("README.md") as f:
  long_description = f.read()

setup(
    name = "toolbench",
    version = find_version('src/toolbench/__init__.py'),
    packages = find_packages('src'),
    package_dir={
        '': 'src',
#        'tests': 'tests',
    },
    #entry_points = {
    #    'console_scripts':['foobar=toolbench.foobar:main'],
    #},
    #install_requires = [ ],
    tests_require = test_deps,
    extras_require = {
        'docs': ['pdoc3'],
        'test': test_deps,
    },
    setup_requires = [ 'pytest-runner>=2.0,<3dev' ],
    author = "Sam Hiatt",
    author_email = "samhiatt@gmail.com",
    license = "LICENSE.txt",
    description = "Some handy python tools.",
    long_description = long_description,
    keywords = "python",
    url = "http://github.com/samhiatt/toolbench",  
    project_urls = {
        'Source': 'http://github.com/samhiatt/toolbench',
    },
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 3 - Alpha',
    ],

)

