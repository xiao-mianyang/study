from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route('/<username>')
def hello(username):
    if username =='shixiaolou':
        return 'hello {}'.format(username)
    else:
        return redirect(url_for('index'))


@app.route('/')
def index():
    course={
    'python':'lou+ python',
    'java':'java base',
    'bigdata':'spark sql',
    'teacher':'shixiaolou',
    'is_unique':False,
    'has_tag':True,
    'tags':['c','c++','docker']
}
    return render_template('index.html',course=course)


@app.route('/user/<username>')
def user_index(username):
    return 'Hello {}'.format(username)


@app.route('/courses/<coursesname>')
def courses(coursesname):
    return render_template('courses.html', coursesname=coursesname)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)


@app.route('/httptest',methods=['GET','POST'])
def get_post():
    if request.method == 'GET':
        return 'It is a get request!'
    elif request.method == 'POST':
        return 'It is a post request!'


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



