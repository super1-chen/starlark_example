import pathlib
from jinja2 import Template

def load_template():
    
    with open(pathlib.Path(__file__).resolve().parent / "template/data.j2") as fp:
        template = Template(fp.read())
    return template.render(model_name="test1/")
    