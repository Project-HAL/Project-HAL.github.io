# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import pathlib
import sys
import os

sys.path.insert(0, os.path.abspath("/home/mxwbio/Desktop/HAL/bin/lib/py_src"))

project = 'Project HAL'
copyright = '2024, Wesley Clawson, Nathan Wu, Trevor Sullivan, and Viraj Chhajed'
author = 'Wesley Clawson, Nathan Wu, Trevor Sullivan, and Viraj Chhajed'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    '_static/style.css'
]