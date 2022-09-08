"""

dbconnection

mysql과 연결시키기

"""

# https://hiwony.tistory.com/entry/Dev-log-python-pymysqlerrInterfaceError-0


# 1.mysql과 연결하기
import openpyxl
import pandas as pd
import pymysql
# connect: mysql에 connect
conn = pymysql.connect(host='localhost',
                       user='kic',
                       password='1234',
                       db='fishfishing',
                       charset='utf8')
curs = conn.cursor()  # 열어주기


# 2. 테이블생성
sql = '''
CREATE TABLE extinct( 
    id int not null primary KEY, 
   name varchar(15) not NULL, 
   reason varchar(5000) not null, 
   shape varchar(5000) not null,
   ecology varchar(5000) not null,
   place varchar(5000) not null
);

'''

curs.execute(sql)  # 쿼리수행
conn.commit()  # 저장(데이터 갱신)


# 종료
conn.close()  # DB연결 열어준 거 닫기


# 3. 엑셀불러오기

extinct_data = pd.read_excel("data/멸종위기어류.xlsx")
print(extinct_data)


# 4. 불러온 파일 속 내용 insert해주기
sql = '''
INSERT INTO extinct(id, name, reason, shape, ecology, place) values(%s, %s, %s, %s, %s, %s)

'''
# 확인
len(extinct_data)
extinct_data.values[0]

for idx in range(len(extinct_data)):
    curs.execute(sql, tuple(extinct_data.values[idx]))  # 튜플형식으로 형변환하여 쿼리 수행
conn.commit()

# 종료
conn.close()


##################################################################################
# 독성어류 테이블명 posion으로 저장 후 insert로 내용 넣어주기
# 최종코드

# 1. mysql 연결
import pymysql
conn = pymysql.connect(host="localhost",  #호스트명
               user="kic",        #아이디
               password="1234",   #비밀번호
               db="fishfishing",  #접속할 db
               charset="utf8")  #인코딩형식

curs = conn.cursor()


# 2. create 테이블
sql = '''
    CREATE TABLE poison(
        id int not null primary key,
        name varchar(15) not null,
        shape varchar(5000) not null,
        ecology varchar(5000) not null,
        place varchar(5000) not null,
        eat varchar(500) not null
        );

'''

curs.execute(sql)
conn.commit()
#curs.close()


# 3. 엑셀파일 불러오기
import pandas as pd
poison_data = pd.read_excel("data/독성어류.xlsx")
poison_data.shape #데이터프레임형태



# 4. insert 구문 사용하여 엑셀데이터 저장하기
sql = '''
    INSERT INTO poison (id, name, shape, ecology, place, eat) values (%s, %s, %s, %s, %s, %s)
'''

#확인용
len(poison_data)
poison_data.values[0]

for idx in range(len(poison_data)):
    curs.execute(sql, tuple(poison_data.values[idx]))

conn.commit()
conn.close()





##################################################################################
# 일반어류 테이블명 posion으로 저장 후 insert로 내용 넣어주기
# 최종코드

# 1. mysql 연결
import pymysql
conn = pymysql.connect(host="localhost",  #호스트명
               user="kic",        #아이디
               password="1234",   #비밀번호
               db="fishfishing",  #접속할 db
               charset="utf8")  #인코딩형식

curs = conn.cursor()


# 2. create 테이블
sql = '''
    CREATE TABLE nomal(
        id int not null primary key,
        name varchar(15) not null,
        shape varchar(5000) not null,
        ecology varchar(5000) not null,
        place varchar(5000) not null,
        eat varchar(500) not null
        );

'''

curs.execute(sql)
conn.commit()
#curs.close()


# 3. 엑셀파일 불러오기
import pandas as pd
nomal_data = pd.read_excel("data/일반어류.xlsx")
nomal_data.shape #데이터프레임형태



# 4. insert 구문 사용하여 엑셀데이터 저장하기
sql = '''
    INSERT INTO nomal (id, name, shape, ecology, place, eat) values (%s, %s, %s, %s, %s, %s)
'''

#확인용
len(nomal_data)
nomal_data.values[0]

for idx in range(len(nomal_data)):
    curs.execute(sql, tuple(nomal_data.values[idx]))

conn.commit()
conn.close()






##################################################################################
# 장고와 mysql connection
# https://simbasimba.tistory.com/9

























