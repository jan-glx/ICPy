from setuptools import setup

setup(name='pertInv',
      version='0.0.001',
      description='Invariant Causal Prediction for python',
      url='https://github.com/PMBio/pertInv',
      author='Jan Gleixner',
      author_email='jan.gleixner@gmail.com',
      license='MIT',
      install_requires=[
          'numpy',
      ],
      packages=['pertInv'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)