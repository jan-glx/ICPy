from setuptools import setup

setup(name='ICPy',
      version='0.0.003',
      description='Invariant Causal Prediction for python',
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
