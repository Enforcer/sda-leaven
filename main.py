from db import engine, Base, with_session
from services import enrolling_course
from models import Student, Course

def create_schema():
    Base.metadata.create_all(engine)


def teardown_schema():
    Base.metadata.drop_all(engine)


@with_session
def insert_initial_data(session):
    print('Insert initial data', session)
    student = Student(student_no='AZB123', first_name='John', last_name='Doe')
    course = Course(name='Maths', exam_type='speaking', enrolled_no=0)
    session.add(student)
    session.add(course)
    session.commit()

    return (student.id, course.id)


if __name__ == '__main__':
    create_schema()
    try:
        student_id, course_id = insert_initial_data()
        # Call your services!
        enrolling_course(course_id, student_id)
    finally:
        teardown_schema()
