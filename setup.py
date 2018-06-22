
import sys
from setuptools import setup, find_packages

open_kwds = {}
if sys.version_info > (3,):
    open_kwds['encoding'] = 'utf-8'

setup(name='leafpy',
      version='0.2.2',
      description='Lightweight python interface to the nissan leaf.',
      classifiers=[],
      keywords='',
      author='Nate Ricklin',
      author_email='nate.ricklin@gmail.com',
      url='https://github.com/nricklin/leafpy',
      license='MIT',
      packages=find_packages(exclude=['docs','tests','examples']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['requests','pycrypto'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest','vcrpy']
)