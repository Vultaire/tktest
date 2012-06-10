from distutils.core import setup
import py2exe

version = "0.1"

setup(
    name="tkinter_test",
    version="0.1",
    author="Paul Goins",
    author_email="general@vultaire.net",
    description="Tkinter py2exe test program",
    scripts=["tktest.py"],

    # py2exe-specific
    windows=[
        "tktest.py",
        ],
    zipfile=None,
    options={
        "py2exe": {
            "bundle_files": 1,
            },
        },
    )
