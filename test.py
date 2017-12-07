from jinja2 import FileSystemLoader, Environment
from datetime import datetime

loader = FileSystemLoader('F:\\pystudy\\FlaskStudy\\template')
template = Environment(loader=loader).get_template('hello_macro.html')

print(template.render(time = datetime.now()))

print(datetime.now())