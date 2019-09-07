from db import with_session
from models import UselessModel, Course, Student, Grade


@with_session
def example_service(example_argument: int, session=None):
    print(example_argument, session)
    session.add(UselessModel(number=example_argument))


@with_session
def enrolling_course(course_id: int, student_id: int, session=None):
    student = session.query(Student).get(student_id)
    course = session.query(Course).get(course_id)
    if course in student.courses:
        raise Exception('Already enrolled!')
    student.courses.append(course)

    student.enroll(course)
    course.enrolled_no += 1


@with_session
def awarding_grade(course_id: int, student_id: int, grade: int, session=None):
    session.add(
        Grade(student_id=student_id, course_id=course_id, grade=grade)
    )
