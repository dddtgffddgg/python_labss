from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///teachers.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Position(Base):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'Position(id={self.id}, name={self.name})'

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    institute = Column(String)

    teachers = relationship('Teacher', back_populates='department')

    def __repr__(self):
        return f'Department(id={self.id}, name={self.name}, institute={self.institute})'

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    birth_date = Column(Date)
    position_id = Column(Integer, ForeignKey('positions.id'))
    department_id = Column(Integer, ForeignKey('departments.id'))

    position = relationship('Position')
    department = relationship('Department', back_populates='teachers')

    def __repr__(self):
        return f'Teacher(id={self.id}, full_name={self.full_name}, birth_date={self.birth_date})'

Base.metadata.create_all(engine)

position1 = Position(name='Профессор')
position2 = Position(name='Доцент')
session.add_all([position1, position2])
session.commit()

department1 = Department(name='Кафедра 1', institute='Институт 1')
department2 = Department(name='Кафедра 2', institute='Институт 2')
session.add_all([department1, department2])
session.commit()

teacher1 = Teacher(full_name='Иванов Иван Иванович', birth_date=datetime(1980, 5, 10), position=position1, department=department1)
teacher2 = Teacher(full_name='Петров Петр Петрович', birth_date=datetime(1990, 3, 15), position=position2, department=department1)
teacher3 = Teacher(full_name='Сидоров Сидор Сидорович', birth_date=datetime(1985, 8, 20), position=position2, department=department2)
session.add_all([teacher1, teacher2, teacher3])
session.commit()

# Запросы
teachers = session.query(Teacher).join(Position).join(Department).all()
for teacher in teachers:
    age = datetime.now().year - teacher.birth_date.year
    print('ФИО преподавателя:', teacher.full_name)
    print('Возраст преподавателя:', age)
    print('Название кафедры:', teacher.department.name)
    print('Должность преподавателя:', teacher.position.name)
    print()

departments = session.query(Department).all()
for department in departments:
    teacher_count = session.query(Teacher).filter_by(department_id=department.id).count()
    print('Название кафедры:', department.name)
    print('Число преподавателей на кафедре:', teacher_count)
    print()
