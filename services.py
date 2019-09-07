from db import with_session
from models import UselessModel, Course, Student


@with_session
def example_service(example_argument: int, session=None):
    print(example_argument, session)
    session.add(UselessModel(number=example_argument))


@with_session
def enrolling_course(course_id: int, student_id: int, session=None):
    student = session.query(Student).get(student_id)
    course = session.query(Course).get(course_id)
    student.courses.append(course)
    course.enrolled_no += 1
