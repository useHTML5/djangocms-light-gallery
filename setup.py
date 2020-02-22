from setuptools import setup, find_packages

setup(name='djangocms-light-gallery',
      version='0.4',
      description='Light Gallery plugin for django CMS',
      url='https://github.com/andyklimczak/djangocms-light-gallery',
      author='Andy Klimczak',
      author_email='andyklimczak@fastmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      long_description=open('README.rst').read(),
      install_requires=[
          'django>=2.2',
          'django-cms>=3.5',
          'django-filer',
          'django-sekizai',
          'easy-thumbnails'
      ],
      zip_safe=False)
