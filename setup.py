from setuptools import setup, find_packages

__version__ = '0.4.2'
project_name = 'pywinrm'

# PyPi supports only reStructuredText, so pandoc should be installed
# before uploading package
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = ''

setup(
    name=project_name,
    version=__version__,
    description='Python library for Windows Remote Management',
    long_description=long_description,
    keywords='winrm ws-man devops ws-management'.split(' '),
    author='Alexey Diyan',
    author_email='alexey.diyan@gmail.com',
    url='http://github.com/diyan/pywinrm/',
    license='MIT license',
    packages=find_packages(),
    package_data={'winrm.tests': ['*.ps1']},
    install_requires=['xmltodict', 'requests>=2.9.1', 'requests_ntlm>=0.3.0', 'six'],
    extras_require={
        'credssp': ['requests-credssp>=1.0.0'],
        'kerberos:sys_platform=="win32"': ['winkerberos>=0.5.0'],
        'kerberos:sys_platform!="win32"': ['pykerberos>=1.2.1,<2.0.0']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Clustering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration'
    ],
)
