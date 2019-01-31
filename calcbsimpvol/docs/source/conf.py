# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from recommonmark.parser import CommonMarkParser

source_suffix = ['.rst', '.md']

# -- Project information -----------------------------------------------------
project = 'calcbsimpvol'
copyright = '2018, Erkan Demiralay'
author = 'Erkan Demiralay'
version = '1.13.0'
release = '1.13.0'
# -- General configuration ---------------------------------------------------

# needs_sphinx = '1.0'
extensions = [
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_copybutton',
]

templates_path = ['_templates']
source_suffix = ['.rst', '.md']
master_doc = 'index'

language = None
exclude_patterns = ['_bkp']
pygments_style = None

source_parsers = {
    '.md': CommonMarkParser,
}

# -- Options for HTML output -------------------------------------------------
# html_theme = 'classic'
html_theme = 'sphinx_rtd_theme'

# html_theme_options = {}
html_static_path = ['_static']
# html_sidebars = {}
# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'calcbsimpvol'

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'calcbsimpvol.tex', 'calcbsimpvol Documentation',
     'Erkan Demiralay', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'calcbsimpvol', 'calcbsimpvol Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'calcBSImpVol', 'calcBSImpVol Documentation',
     author, 'calcBSImpVol', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------