from distutils.core import setup

with open('README.md') as f:
    long_description = ''.join(f.readlines())

setup(name='Schrodinger',
    version='0.01',
    description='Wave function basis set',
    long_description=long_description,
    author='Eric Holmgren',
    author_email='eholmgr2@u.rochester.edu',
    packages=['schrod'],
    entry_points=
    {
        'console_scripts': ['schrod=schrod.schrod:start']
    }
    )