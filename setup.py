from setuptools import setup
from io import open # for python 2

with open("README.md", "r", encoding="utf-8") as fh:
      long_description = fh.read()

setup(name='ICPy',
      version='0.0.005',
      description='Invariant Causal Prediction for python',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/jan-glx/ICPy',
      author='Jan Gleixner',
      author_email='jan.gleixner+icpy@gmail.com',
      license='MIT',
      install_requires=[
          'numpy', 'scipy', 'scikit-learn',
      ],
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*,<4',
      packages=['icpy'],
      test_suite='tests',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
      ],
      keywords = ['statistics', 'casual-inference'],
      include_package_data=True,
      zip_safe=False)
