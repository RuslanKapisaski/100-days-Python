from setuptools import setup

APP = ['01.intorduction.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],
    'frameworks': [
        '/opt/homebrew/Caskroom/miniconda/base/envs/100-days-Python/lib/libffi.8.dylib',
        '/opt/homebrew/Caskroom/miniconda/base/envs/100-days-Python/lib/libtk8.6.dylib',
        '/opt/homebrew/Caskroom/miniconda/base/envs/100-days-Python/lib/libtcl8.6.dylib',
    ],
    'resources': ['tomato.png'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)