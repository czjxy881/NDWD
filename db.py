#encoding=gbk
import MySQLdb
def create(id):
    conn=MySQLdb.connect(host='localhost',user='root',passwd='asdf1234',db='test1',charset='gbk')
    cur=conn.cursor()
    try:
        cur.execute('create table `%s`(`name` VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,`pic` VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,`url` VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,`price` INT NOT NULL,`transport` INT NOT NULL,`sell` INT NOT NULL,`from` VARCHAR(256) NOT NULL)default charset=gbk '%id);
    except:
        pass
    conn.commit()
    cur.close()
    conn.close()
def add(id,s):
    conn=MySQLdb.connect(host='localhost',user='root',passwd='asdf1234',db='test1',charset='gbk')
    cur=conn.cursor()
    cur.execute("insert into %s values('%s','%s','%s',%s,%s,%s,'%s')"%(id,s[0],s[1],s[2],s[3],s[4],s[5],s[6]))
    conn.commit()
    cur.close()
    conn.close()
               
if __name__=='__main__':
    create('t7')
    add('t7',['sad','asda','asdsad',12,231,12,'淘宝'])
