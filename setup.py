import sys
from glob import glob
from setuptools import setup, Extension
from distutils.command.build import build


with open('README.md') as f:
    long_description = f.read()

include_dirs = ['scripts','src']
library_dirs = ['lib']
libraries = ['aec', 'stdc++']
define_macros = []
extra_compile_args = []

sources = (
    glob('scripts/echo_canceller.cpp') +
    ['scripts/athenaaec.i']
)

swig_opts = (
    ['-c++'] +
    ['-I' + h for h in include_dirs]
)


setup(
    name='athenaaec',
    version='0.1.1',
    description='Python bindings of athenaaec library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Yihui Xiong',
    author_email='yihui.xiong@hotmail.com',
    maintainer='Yihui Xiong',
    maintainer_email='yihui.xiong@hotmail.com',
    url='https://github.com/xiongyihui/athenaaec-python',
    download_url='https://pypi.python.org/pypi/athenaaec',
    packages=['athenaaec'],
    ext_modules=[
        Extension(
            name='athenaaec._athenaaec',
            sources=sources,
            swig_opts=swig_opts,
            include_dirs=include_dirs,
            library_dirs=library_dirs,
            libraries=libraries,
            define_macros=define_macros,
            extra_compile_args=extra_compile_args
        )
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: C++'
    ],
    license='BSD',
    keywords=['athenaaec', 'acoustic echo cancellation'],
    platforms=['Linux'],
    package_dir={
        'athenaaec': 'scripts'
    }
)