from setuptools import setup, find_packages
import platform

install_requires = []
if platform.system() == 'Windows':
    install_requires.append('pywin32')

setup(
    name='PyScriptingHost',
    version='0.0.1',
    author='Fj',
    author_email='fj.mail@gmail.com',
    packages=find_packages(),
    scripts=['bin/pyscriptinghost-client.py'],
    url='http://pypi.python.org/pypi/PyScriptingHost/',
    license='LICENSE.txt',
    description='Manage periodically running tasks.',
    install_requires=install_requires,
    zip_safe=True,
)
