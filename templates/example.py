from jinja2 import Template


tmpl = Template(open('replace_sys_syslog.j2').read())
conf = tmpl.render(conf=open('system:syslog').read())
print conf
