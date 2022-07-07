from distutils.core import setup

setup(name='dmp',
      version='0.1',
      description='Dynamic Movement Primitives',
      author='Michele Ginesi',
      author_email='michele.ginesi@univr.it',
      install_requires=['numpy', 'scipy', 'matplotlib', 'tqdm'],
      packages=['dmp'])

setup(name='snsplot',
      version='0.1',
      description='Figure Style Shaping',
      author='Yan Wang',
      author_email='wangyan94maomao@gmail.com',
      install_requires=['seaborn'],
      packages=['snsplot'])
