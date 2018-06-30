
import sys
from setuptools import setup, find_packages

open_kwds = {}
if sys.version_info > (3,):
    open_kwds['encoding'] = 'utf-8'

setup(name='leafpydome',
      version='0.2.2',
      description='Lightweight python interface to the nissan leaf based on leafpy package.',
      classifiers=[],
      keywords='',
      license='MIT',
      packages=find_packages(exclude=['docs','tests','examples']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['requests','pycryptodome'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest','vcrpy']
)