# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import pathlib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import locs

sys.path.insert(0, os.path.abspath(locs.hal_py_lib_path))

def setup(app):
    app.add_css_file('custom.css')

project = 'Project HAL'
copyright = """2024, Wesley Clawson, Nathan Wu, Trevor Sullivan, and Viraj Chhajed.\n\n
HAL was generously funded by the Air Force Office of Scientific Research (Grant ID: FA9550-22-1-0465)"""
author = 'Wesley Clawson, Nathan Wu, Trevor Sullivan, and Viraj Chhajed'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel',
    'breathe',
]

breathe_default_project = "HAL"

autosectionlabel_prefix_document = True

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    '_static/style.css'
]
