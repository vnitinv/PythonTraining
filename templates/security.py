import yaml
from jinja2 import Template

data = yaml.load(open('data.yaml'))

tmpl = Template(open('security.j2').read())
conf = tmpl.render(data)
print conf
