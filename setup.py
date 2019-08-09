from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='analysis',
      version='0.2',
      description='Analyze ',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='analysis SPI cx10wd quadcopter drone',
      url='http://github.com/yformaggio/analysis',
      author='Yannick Formaggio',
      author_email='yannick.formaggio@gmail.com',
      license='None yet',
      packages=['analysis'],
      entry_points={
          'console_scripts': ['analysis=analysis.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
