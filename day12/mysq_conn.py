import  pymysql
#pip3 install pymysql

# 创建连接
conn = pymysql.connect(host='192.168.239.141', port=3306, user='root', passwd='alex3714', db='oldboydb')
# 创建游标
cursor = conn.cursor()
# 执行SQL，并返回收影响行数
#effect_row = cursor.execute("select * from student")
# print(cursor.fetchone())
# print(cursor.fetchone())
# print('-------------------')
# print(cursor.fetchall())
data = [
    ("N1","2015-05-22","M"),
    ("N2", "2015-05-21", "M"),
    ("N3", "2015-05-23", "M")
]
cursor.executemany("insert into student(name,register_date,gendar) values(%s,%s,%s)", data)
conn.commit()