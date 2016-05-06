try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='plib',
    version='0.0.2',
    description='Password generator for humans',
    long_description=readme,
    url='https://github.com/pypa/sampleproject',
    author='Hjalti',
    author_email='hjalti@dyraklam.is',
    license='MIT',
    packages=['plib'],
    package_data={
        'plib' : ['words.txt']
    },
    entry_points={
        'console_scripts': [
            'pword=plib.pword:main',
            'rpass=plib.pword:rpass_main',
        ],
    },
)
