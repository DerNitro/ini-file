========
INI-FILE
========

A small utility for get value from .ini files

Install
---------
::

    git clone https://github.com/DerNitro/ini-file
    cd ini-file
    python3 setup.py install



Usage
-------------
::

    usage: ini-file [-h] [--version] [--section SECTION] [--key KEY] [--sep SEP] file [file ...]

    positional arguments:
      file               .ini files

    optional arguments:
      -h, --help         show this help message and exit
      --version          show program's version number and exit
      --section SECTION  file section
      --key KEY          key
      --sep SEP          string inserted between values, default a "=" (equally).

