from distutils.core import setup

setup(name='pyfmm',
      version='0.0.1',
      description='Python implementation of Fast Multipole Method for spin dynamics',
      author='Ryan Pepper',
      author_email='ryan.pepper@soton.ac.uk',
      url='www.github.com/ryanpepper/spinfmm',
      packages=['pyfmm'],
      install_requires = [
        'pytest >= 2.8',
        'numpy',
        'hypothesis'
      ],
      classifiers = [
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: BSD',
      ],
)
