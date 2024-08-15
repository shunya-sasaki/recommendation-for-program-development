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
    "sphinx_design",
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

language = "en"
# html_theme = "sphinx_rtd_theme"
# html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_path = ["themes"]
html_theme = "custom"
exclude_patterns = [
    ".DS_Store",
    ".venv",
    ".mypy_cache",
    "_build",
    "Thumbs.db",
    "README.md",
]
togglebutton_hint = ""
togglebutton_hint_hide = ""

match html_theme:
    case "custom":
        html_theme_options = {
            "globaltoc_collapse": False,
            "globaltoc_includehidden": False,
            "globaltoc_maxdepth": 2,
            "git_url": "https://github.com/shunya-sasaki/"
            + "recommendation-for-program-development",
            "git_icon": "github",
        }
