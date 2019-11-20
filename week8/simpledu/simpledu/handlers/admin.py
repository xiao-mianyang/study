from flask import Blueprint
from flask import render_template
from simpledu.decorators import admin_required
from flask import request, current_app
from simpledu.models import Course
from flask import redirect, url_for, flash
from simpledu.forms import CourseForm



admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')

@admin.route('/courses')
@admin_required
def courses():
    page = request.args.get('page', default=1, type=int)
    pagination = Course.query.paginate(
       page=page,
       per_page=current_app.config['ADMIN_PER_PAGE'],
       error_out=False
     )
    return render_template('admin/courses.html', pagination=pagination)

@admin.route('/courses/create', methods=['GET', 'POST'])
@admin_required
def create_course():
    form = CourseForm()
    if form.validate_on_submit():
        form.create_course()
        flash('', 'success')
        return redirect(url_for('admin.courses'))
    return render_template('admin/create_course.html', form=form)


