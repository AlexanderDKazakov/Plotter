from distutils.core import setup
setup(
    name = 'plotter',
    packages = ['plotter'],
    version = '1.2.2',
    license='MIT',
    description = 'Plotter based on Veusz[https://github.com/veusz/veusz].',
    author = 'Alexander Kazakov, Varvara Prokacheva',
    author_email = 'alexander.d.kazakov@gmail.com',
    url = 'https://github.com/AlexanderDKazakov/Plotter',
    download_url = 'https://github.com/AlexanderDKazakov/Plotter/archive/v1.2.2.tar.gz',
    keywords = ['store', 'pickle'],
    install_requires=[
        'Storer',
        'numpy',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
