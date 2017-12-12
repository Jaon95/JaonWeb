from mako.template import Template
from mako.lookup import TemplateLookup 
from itertools import repeat


lookup = TemplateLookup(directories=['F:\\pystudy\\FlaskStudy\\template\\mako\\'])
print(lookup.get_template('index.html').render())