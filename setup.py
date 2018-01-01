from setuptools import setup

setup(name='ICPy',
      version='0.0.001',
      description='Invariant Causal Prediction for python',
      url='https://github.com/jan-glx/ICPy',
      author='Jan Gleixner',
      author_email='jan.gleixner+icpy@gmail.com',
      license='MIT',
      install_requires=[
          'numpy', 'scipy', 'scikit-learn',
      ],
      packages=['icpy'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)