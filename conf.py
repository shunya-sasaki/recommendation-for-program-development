import platform

# OS Identification
platform_name = platform.system()  # Windows, Darwin, Linux

project = "Recommendation for Program Development"
copyright = "2024, Shunya Sasaki"
author = "Shunya Sasaki"

extensions = [
    "myst_parser",
    "sphinx.ext.napoleon",
    "sphinx.ext.imgmath",
    "sphinx.ext.ifconfig",
    "sphinx.ext.imgconverter",
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
]
language = "ja"
# html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_path = ["themes"]
html_theme = "custom"
exclude_patterns = ["_build", ".venv", ".mypy_cache", "Thumbs.db", ".DS_Store"]

# blockdiag
blockdiag_html_image_format = "SVG"
blockdiag_html_image_format = "SVG"
