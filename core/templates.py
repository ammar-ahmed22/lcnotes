from jinja2 import Environment, FileSystemLoader
from .utils import write_file

__env = Environment(loader=FileSystemLoader('templates'))

def render(template_name, **context) -> str:
    template = __env.get_template(template_name)
    return template.render(**context)

def render_to_file(template_name, path, **context) -> None:
    content = render(template_name, **context)
    write_file(path, content)
