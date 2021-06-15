from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("mlvc"),
    autoescape=select_autoescape()
)
