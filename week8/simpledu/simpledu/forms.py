from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, DataRequired
from simpledu.models import db, User
from wtforms import ValidationError
from wtforms import TextAreaField, IntergerField
from simpledu.models import Course
from wtforms.validators import URL, NumberRange


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(3, 24)])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('提交')
    
    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password=self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')


    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')




class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Length(6, 24)])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_email(self, field):
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱未注册')
            
    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')


class CourseForm(FlaskForm):
    name = String('', validators=[DataRequired(), Length(5, 32)])
    description = TextAreaField('', validators=[DataReaquired(), Length(20, 256)])
    image_url = StringField('', validators=[DataRequired(), URL()])
    author_id = IntergerField('', validators=[DataRequired(), NumberRange(min=1, message='')])
    submit = SubmitField('')


    def validate_author_id(self, field):
        if not User.query.get(field.data):
            raise ValidationError('')


    def create_course(self):
        course = Course()
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course


    def update_course(self, course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course


