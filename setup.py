import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name         = 'vplotter',
    version      = '1.4.0',
    author       = 'Alexander D. Kazakov, Varvara M. Prokacheva',
    author_email = 'alexander.d.kazakov@gmail.com',
    description  = 'Plotter is a minimalistic handler to use plotting engines. See details for engine availability.',
    license      = 'MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url          = 'https://github.com/AlexanderDKazakov/Plotter',
    packages     =  setuptools.find_packages(),
    keywords     = ['plot'],
    classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      ],
    python_requires='>=3.7',
    install_requires=[
        'storer',
        'numpy',
        'pygnuplot',
        'pandas'
      ],
)

