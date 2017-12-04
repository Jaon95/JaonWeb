from flask import Flask, request, render_template
from flask.views import View

app = Flask(__name__, template_folder='../../web_develop/templates')

class BaseView(View):
    def get_template_name(self):
        raise NotImplementedError
    
    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        if request.method != 'GET':
            return 'UNSUPPORTED！'
        context = {'users':self.get_users()}
        return self.render_template(context)

class UserView(BaseView):
    def get_template_name(self):
        return 'chapter3/section1/users.html'

    def get_users(self):
        return [{
         'username':'fake',
         'avatar':'http://lorempixel.com/100/100/nature/'
    }]

app.add_url_rule('/users', view_func = UserView.as_view('uw'))

if __name__ == '__main__':
    app.run(port=9000)