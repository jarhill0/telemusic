from setuptools import setup

setup(name='telemusic',
      version='0.1.7',
      packages=['telemusic'],
      entry_points={
          'console_scripts': [
              'telemusic = telemusic:main',
          ],
      },
      install_requires=['pawt',
                        'python-vlc',
                        'youtube-dl'],
      dependency_links=['http://github.com/jarhill0/pawt/tarball/master']
      )
