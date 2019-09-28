from flask import Flask,render_template
from flask import url_for
from flask import redirect
from flask import request

app = Flask(__name__)


@app.route('/<username>')
def hello(username):
    if username =='shixiaolou':
        return 'hello {}'.format(username)
    else:
        return redirect(url_for('index'))


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/user/<username>')
def user_index(username):
    print('User-Agent:',request.headers.get('User-Agent'))
    print('time:',request.args.get('time'))
    print('q:',request.args.get('q'))
    print('Q:',request.args.getlist('Q'))
    return 'Hello {}'.format(username)


@app.route('/coures/<coures_name>')
def get_course(course_name):
    return render_template('courses.html,course_name=coursename')


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)


@app.route('/test')
def test():
    print(url_for('index'))
    print(url_for('user_index',username='shiyanlou'))
    print(url_for('show_post',post_id=1, _external=True))
    print(url_for('show_post',post_id=2,q='python 03'))
    print(url_for('show_post',post_id=2,q='python ok'))
    print(url_for('show_post',post_id=2,_anchor='a'))
    return 'test'





if __name__ =='__main__':
    app.run()


