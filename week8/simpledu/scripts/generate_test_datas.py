import os
import json
from random import randint
from faker import Faker
from simpledu.models import db, User, Course, Chapter

# ?? faker ????
fake = Faker()

# ????????
def iter_users():
    yield User(
        username='Jack Lee',
        email='jacklee@example.com',
        password='zxcvbnm',
        job='研发工程师'
    )

# ? datas ???????????????????????????
# ???????
def iter_courses():
    author = User.query.filter_by(username='Jack Lee').first()
    with open(os.path.join(os.path.dirname(__file__), '..', 'datas', 'courses.json')) as f:
        courses = json.load(f)
    for course in courses:
        yield Course(
            name=course['name'],
            description=course['description'],
            image_url=course['image_url'],
            author=author
        )


def iter_chapters():
    for course in Course.query:
        # ?????? 3~10 ???
        for i in range(randint(3, 10)):
            yield Chapter(
                # ?? faker ????????????
                name=fake.sentence(),
                course=course,
                # ?????????????????????
                video_url='https://labfile.oss.aliyuncs.com/courses/923/week2_mp4/2-1-1-mac.mp4',
                # ????
                video_duration='{}:{}'.format(randint(10, 30), randint(10, 59))
            )


def run():
    for user in iter_users():
        db.session.add(user)

    for course in iter_courses():
        db.session.add(course)

    for chapter in iter_chapters():
        db.session.add(chapter)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()

