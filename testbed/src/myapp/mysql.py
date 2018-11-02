#! /usr/bin/python
# encoding utf-8

import MySQLdb

class table():
    def __init__(self,host,port,account,pwd,database,encoding,tablename):
        self.db = MySQLdb.connect(host,port,account,pwd,database,charset=encoding)
        self.cursor = self.db.cursor()
        self.tablename = tablename

        # create table if not exist
        if not self.cursor.execute("show tables like '%s'" %self.tablename):
            sql = """create table %s (
                id int not null primary key auto_increment,
                username   char(20) not null unique,
                password   char(100)
              )""" % self.tablename
            self.cursor.execute(sql)
            self.db.commit()
            #print "table '%s' has been created successfully" %self.tablename

    def query_user(self, username=None):
        if username:
            sql = "select * from %s where username='%s'" %(self.tablename,username)
        else:
            sql = "select * from %s"% (self.tablename)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def add_user(self, username, password):
        result = self.query_user(username)
        if not result:
            sql = "insert into %s(username,password) values('%s','%s')" %(self.tablename, username, password)
            self.cursor.execute(sql)
            self.db.commit()
            #print "user '%s' has been created successfully" %username
            return 1
        else:
            # print "user '%s' exists" %username
            return 0

    def delete_user(self, username):
        result = self.query_user(username)
        if result:
            sql = "delete from %s where username='%s'" %(self.tablename,username)
            self.cursor.execute(sql)
            self.db.commit()
            #print "user '%s' has been deleted successfully" %username
            return True
        else:
            #print "user '%s' doesn't exist" % username
            return False

    def query_password(self, username):
        result = self.query_user(username)
        if result:
            return result[0][2]
        else:
            #print "user '%s' doesn't exist" % username
            return 0

    def update_password(self, username, password):
        result = self.query_user(username)
        if result:
            sql = "update %s set password='%s' where username='%s'" %(self.tablename,password,username)
            self.cursor.execute(sql)
            self.db.commit()
            #print "password of the user '%s' has been updated successfully" %username
            return 1
        else:
            #print "user '%s' doesn't exist" % username
            return 0

    def close_table(self):
        self.db.close()
        #print "close table successfully"

if __name__ == '__main__':
    table_instance = table("mysql_for_flask", 3306, "flask", "flask", "flask",'utf8',"users")
    #print table_instance.query_user("1")
    table_instance.add_user("A","cisco123!")
    # table_instance.add_user("B","cisco123!")
    # table_instance.add_user("C", "cisco123!")
    # table_instance.add_user("D", "cisco123!")
    # table_instance.delete_user("A")
    # table_instance.update_password("B", "1234567890")
    #print table_instance.query_password("admin")
    table_instance.close_table()