# HAL Documentation

## Overview

To modify the website, look at the RST files in `source` (you can find 
documentation on using ReStructuredText with Sphinx [here](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)).

To modify the function contracts, you have to modify the source code of HAL (
`bin/lib/py_src` for the python contracts, and `bin/lib/include` for the C++).

### Build

To rebuild C++ contracts, run:

`doxygen && make html`

To just build the RST files and/or python contracts, just run:

`make html`

## Setup

After installing the necessary packages (see below), start by duplicating ``temp_locs.py`` and rename it to ``locs.py``. Change 
``PARENT_PATH`` in the ``hal_py_lib_path`` variable to the full path to your 
copy of the HAL repo (leave the rest of the path unchanged).

Similarly, dulpicate ``Doxyfile_temp`` and rename it to ``Doxyfile``. Search 
for the variables ``OUTPUT_DIRECTORY`` and ``INPUT``, and change ``PARENT_PATH``
to the full path to your copy of the ``Project-Hybrot.github.io`` repo and ``HAL``
repo, respectively.

## Classes/Modules

For formatting class names in text, the following feature is available: 

    .. include links.rst
    
    |CLASS|_
    
Where `CLASS` is the name of the class/module. This will automatically add the `literal` format to the name and link to its page. To add this feature for more classes and modules, see 
`source/links.rst`. 

This file can also be used for commonly linked words, such as [MaxWell](https://www.mxwbio.com/).

## Toggleable Dropdown Bar

This repo features a custom toggleable dropdown bar, as used in `channel_window.rst`
and `wave_detector.rst`. The implementation can be found in `source/_templates/page.html`
and `source/_static/custom.css`.

Example usage:

    .. container:: toggle

        .. container:: header

            Dropdown Header

        contents of dropdown


## Dependencies
- [Sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html)
- [Read the Docs](https://sphinx-rtd-theme.readthedocs.io/en/stable/installing.html)
- [Doxygen](https://doxygen.nl/manual/install.html), for automatically 
translating C++ function contracts to XML
- [Breathe](https://breathe.readthedocs.io/en/latest/index.html#download), 
which allows sphinx autodoc features to be used on the Doxygen XML output
- [MyST](https://myst-parser.readthedocs.io/en/latest/intro.html#installation), 
which allows for Sphinx to parse Markdown files
<!-- - [Sphinx Toolbox](https://pypi.org/project/sphinx-toolbox/) -->

