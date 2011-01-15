from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='experimentdb',
      version=version,
      description="A web based application for storage and organization of data regarding experimental data.",
      long_description = read('README.rst'),
      classifiers=[        
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Natural Language :: English',
        'Environment :: Web Environment',		
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Intended Audience :: Science/Research',
        'Topic :: Database :: Front-Ends',
        'Topic :: Scientific/Engineering :: Bio-Informatics'		
        'Topic :: Internet :: WWW/HTTP',], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='experiment, lims, data, science, data-management',
      author='Dave Bridges',
      author_email='dave.bridges@gmail.com',
      url='http://davebridges.github.com',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[ 'biopython', 'south', 'django-ajax-selects', 'pil', 'django'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
	 
