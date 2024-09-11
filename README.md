# HAL Documentation

## Setup

Start by duplicating ``temp_locs.py`` and rename it to ``locs.py``. Change 
``PARENT_PATH`` in the ``hal_py_lib_path`` variable to the full path to your 
copy of the ``HAL`` repo (leave the rest of the path unchanged).

Similarly, dulpicate ``Doxyfile_temp`` and rename it to ``Doxyfile``. Search 
for the variables ``OUTPUT_DIRECTORY`` and ``INPUT``, and change ``PARENT_PATH``
to the full path to your copy of the ``Project-Hybrot.github.io`` repo and ``HAL``
repo, respectively.

## Build

To build C++ documentation (Doxygen XML), run:

`doxygen`

Then, to build the `html` files, run:

`make `


## Dependencies
- [Sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html)
- [Read the Docs](https://sphinx-rtd-theme.readthedocs.io/en/stable/installing.html)
- [Doxygen](https://doxygen.nl/manual/install.html), for automatically 
translating C++ function contracts to XML
- [Breathe](https://breathe.readthedocs.io/en/latest/index.html#download), 
which allows sphinx autodoc features to be used on the Doxygen XML output
<!-- - [Sphinx Toolbox](https://pypi.org/project/sphinx-toolbox/) -->

