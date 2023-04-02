from setuptools import setup, find_packages
from pathlib import Path

setup(
  name='snapmlengine',
  version= '0.0.2.11',
  description='ML Helper',
  long_description=Path("README.md").read_text(encoding="utf-8"),
  long_description_content_type="text/markdown",
  url='https://github.com/midnightbot/snapmlengine',  
  author='Anish Adnani, Parth Goel',
  author_email='anishadnani00@gmail.com',
  license='MIT', 
  keywords=['python', 'coding', 'ml', 'algorithms'],
  packages=find_packages(),
  install_requires=['snapalgo', 'pandas', 'numpy', 'scikit-learn'] ,
  classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
