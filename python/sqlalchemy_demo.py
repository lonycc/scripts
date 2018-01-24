# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

engine = create_engine('mysql+pymysql://username:password@localhost/mydb?charset=utf8')
db_session = sessionmaker(bind=engine)
db = db_session()
Base = declarative_base()

###直接操作sql###
rs = session.execute('show tables')
for r in rs.fetchall():
    print(r)

# 使用orm
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column('username', String(64), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)

user1 = User()
user1.id = 1
user1.name = 'hello'
user1.email = '123@gmail.net'
user1.password = 'password'

db.add(user1)
user2 = User(id=2, name='youmi', password='1234', email='12@you.net')
db.add(user2)
db.commit()

query = db.query(User)
query = User.query  #另一种获取方法

sql = str(query) # 执行的sql语句
sql = query.statement # 执行的sql语句

for i in query:
    print(i.name)

query.all() #返回所有对象的列表
query.first() #返回第一个对象,记录不存在时，first() 会返回 None
query.one()  # 不存在，或有多行记录时会抛出异常

names = db.query(User.name)
names.all() #每行都是一个元组

db.query(User).limit(10)
User.query.limit(10)

db.query(User).offset(5).limit(10)
User.query.offset(5).limit(10)

db.query(User).order_by('id')
db.query(User).order_by(User.id.desc())
db.query(User).order_by('id asc')
db.query(User).order_by(User.name.desc(),User.id)

db.query(User).filter(User.id == 1).scalar()
db.query(User).filter('id = 1').scalar()
db.query(User).filter(User.id > 1,User.name != 'youmi').scalar()
db.query(User).filter(User.id.in_((1,2,3))).scalar()
db.query(User).filter(or_(User.id > 1,User.name != 'youmi')).scalar()

query = User.query.join(Group, User.gid == Group.id) \
.filter(User.id != None,"is_superuser & 1 = 1") \
.order_by(User.last_edit.asc()).limit(10)

query = User.query.outerjoin(Group, User.gid == Group.id) \
.filter(User.id != None,"is_superuser & 1 = 1") \
.order_by(User.last_edit.asc()).limit(10)

db.query(User).filter(User.id == 1).update({User.name: 'tony'})

user = db.query(User).filter(User.id == 1)
user.name = 'tony'
db.flush()

db.query(User).filter(User.id == 1).delete()
db.commit()
