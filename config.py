import datetime

extensions = []
templates_path = ['_templates']

master_doc = 'index'

project = u'Syscoin Docs'
copyright = u'2018, Syscoin, http://syscoin.org'
author = u'Syscoin Team'

version = datetime.date.today().strftime('%Y-%m-%d')
release = '3.0.0'
language = None

exclude_patterns = ['_build']
pygments_style = 'sphinx'

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
html_show_sourcelink = True
htmlhelp_basename = 'Testdoc'
html_logo = '_static/images/r2_logo_128.png'
html_favicon = '_static/images/r2favicon.ico'

latex_logo = '_static/images/r2_logo.png'

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
# Changed this to a4; we're in Europe ;-)
'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
# According to this link: http://tex.stackexchange.com/questions/23078/how-can-i-automatically-center-an-image?rq=1
# all images should become centered using this package; unfortunately none of the below produces desired result :-(
# 'preamble': '\\usepackage{floatrow}\\usepackage{caption}',
# 'preamble': '\\usepackage{float}\\floatstyle{boxed}\\restylefloat*{figure}',
# 'preamble': '\\makeatletter\\g@addto@macro\\@floatboxreset\\centering\\makeatother',

# Latex figure (float) alignment
# default below is float; we want position as is: H
#'figure_align': 'htbp', 
'figure_align': 'H', 
}

latex_documents = [
  (master_doc, 'Test.tex', u'Syscoin Docs',
   u'The Syscoin team', 'manual'),
]

man_pages = [
    (master_doc, 'test', u'Syscoin Docs',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'Test', u'Syscoin Docs',
   author, 'Test', 'Syscoin Docs',
   'Miscellaneous'),
]

from recommonmark.parser import CommonMarkParser

# The suffix of source filenames.
source_suffix = ['.rst', '.md']

source_parsers = {
	'.md': CommonMarkParser,
}
