from distutils.core import setup
import py2exe

setup(console=["pygame1.py"],
      data_files=[("bitmaps",
                   ["snakehead2.png", "apple.png"])],
)
