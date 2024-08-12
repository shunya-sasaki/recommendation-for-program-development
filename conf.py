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
language = "en"
# html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_path = ["themes"]
html_theme = "custom"
# html_theme = "basic"
exclude_patterns = ["_build", ".venv", ".mypy_cache", "Thumbs.db", ".DS_Store"]

match html_theme:
    case "custom":
        html_theme_options = {
            "git_url": "https://github.com/shunya-sasaki/"
            + "recommendation-for-program-development",
            "git_icon": "gitlab"
        }


# blockdiag
blockdiag_html_image_format = "SVG"
blockdiag_html_image_format = "SVG"
