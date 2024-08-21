import importlib.util
from pathlib import Path
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
    "sphinx.ext.autodoc",
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
    "sandbox/*",
]

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

module_name = "ccg"


def run_apidoc(app):
    output_filepath = Path("api/index.md")
    build_filepath = Path(app.outdir).joinpath("api")
    if build_filepath.exists():
        return

    output_filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(output_filepath, "w") as f:
        f.write("# API Reference\n\n")
        f.write("```{toctree}\n\n")
        f.write(f"{module_name}\n")
        f.write("```")

    spec = importlib.util.find_spec(module_name)
    if spec is not None:
        module_locations = spec.submodule_search_locations
        if module_locations:
            dict_tree = _path_to_dict(module_locations[0])
    _dict_tree_to_md(dict_tree, level_max=2)


def setup(app):
    app.connect("builder-inited", run_apidoc)


def _path_to_dict(path, dict_tree={}):
    path = Path(path)
    if path.is_dir():
        if path.joinpath("__init__.py").exists():
            dict_tree[path.name] = {}
            for p in path.iterdir():
                _path_to_dict(p, dict_tree[path.name])
    else:
        if path.stem not in ["__init__", "_version"]:
            dict_tree[path.stem] = None
    return dict_tree


def _dict_tree_to_md(
    dict_tree, level=0, level_max=2, parent: str = "", api_dir="api"
):
    print(f"parent = {parent}")
    if parent == "":
        parent_dirpath = Path(api_dir)
    else:
        parent_dirpath = Path(api_dir).joinpath(parent.replace(".", "/"))
    parent_dirpath.mkdir(parents=True, exist_ok=True)
    if level <= level_max:
        for key, value in dict_tree.items():
            if parent == "":
                mod_name = key
            else:
                mod_name = f"{parent}.{key}"
            with open(parent_dirpath.joinpath(key + ".md"), "w") as f:
                f.write(f"# {mod_name}\n\n")
                f.write("```{eval-rst}\n")
                f.write(f".. automodule:: {mod_name}\n")
                f.write(f"    :members:\n")
                f.write(f"    :undoc-members:\n")
                f.write(f"    :inherited-members:\n")
                f.write("```\n\n")
                if value is not None:
                    f.write(":::{toctree}\n")
                    f.write(":caption: Submodules\n\n")
                    for child in value.keys():
                        f.write(f"{key}/{child}\n")
                    f.write(":::\n")
            if value is not None:
                _dict_tree_to_md(
                    value, level + 1, level_max, parent=mod_name
                )
    else:
        return


# %%
