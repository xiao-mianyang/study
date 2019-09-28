from flask import Flask,render_template,url_for,redirect,request,session
from datetime import timedelta

app = Flask(__name__)

app.config.update({
    'SECRET_KEY': 'HAHA'})


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


@app.route('/register',methods=['GET','POST'])
def register():
    print('method:',request.method)
    print('name:',request.form.get('name'))
    print('password:',request.form.get('password'))
    print('hobbies:',request.form.getlist('hobbies'))
    print('age:',request.form.get('age',default=18))
    return 'registered successfully!'


@app.route('/test')
def test():
    print(url_for('index'))
    print(url_for('user_index',username='shiyanlou'))
    print(url_for('show_post',post_id=1, _external=True))
    print(url_for('show_post',post_id=2,q='python 03'))
    print(url_for('show_post',post_id=2,q='python ok'))
    print(url_for('show_post',post_id=2,_anchor='a'))
    return 'test'

@app.route('/set_session')
def set_session():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=35)
    session['username']='shixiaolou'
    return 'Session Ready!'

@app.route('/get_session')
def get_session():
    value = session['username']
    return 'Get Session!{}'.format(value)


@app.route('/del_session')
def del_session():
    print('--------------', session)
    value = session.pop('username')
    return 'Del Session!'.format(value)


if __name__ =='__main__':
    app.run()
