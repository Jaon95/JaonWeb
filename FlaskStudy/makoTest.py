from mako.template import Template
from mako.lookup import TemplateLookup 

template = Template('hello ${name} !')
print(template.render(name = 'xiaoming'))

lookup = TemplateLookup(directories=['FlaskStudy/template'])

template = Template('<%include file="makoTest.html"/>', lookup=lookup)
print(template.render(name = 'xiaoming'))

print(lookup.get_template('makoTest.html').render(name = 'xiaoming'))