import pymysql


# 获取数据库版本
def getdbversion(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    return cursor.fetchone()


# 执行sql
def execute(db, sql):
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    return cursor.fetchall()


# 连接数据库
db = pymysql.connect(host="10.2.6.14", user="user", passwd="Lachesis-mh_1024", db="test", port=3306)
print("Database version : %s" % getdbversion(db))

# 使用预处理语句创建表
sql_drop = "DROP TABLE IF EXISTS EMPLOYEE"
sql_crate = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
execute(db, sql_drop)
execute(db, sql_crate)

db.close()
