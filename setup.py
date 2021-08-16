from setuptools import setup

setup(
    name='sphinxjinja2',
    version='1.0.0',
    description='Jinja support in Sphinx',
    url='https://github.com/byran/SphinxJinja2',
    author='Byran Wills-Heath',
    author_email='byran@adgico.co.uk',
    license='MIT',
    packages=['sphinxjinja2'],
    zip_safe=False,
    install_requires=[
        'Sphinx >= 3.0.4'
    ]
)
