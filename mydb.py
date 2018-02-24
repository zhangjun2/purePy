# -*- coding:utf-8 -*-
_author__ = 'ZHANGJUN'
import mysql.connector

# 连接配置第一种方式，连接配置，Ip 端口，用户名，密码，数据库名称，字符编码
mysql_config = {
	"host": '172.18.50.11',
	'port': 3306,
	'user': 'wanjiaweb',
	'passwd': 'web@123456',
	'db': 'wanjiaweb',
	'charset': 'utf8'

}
# 第二种连接配置方式
# con = mysql.connector.connect(
# 	host='172.18.50.11',
# 	port=3306,
# 	user='wanjiaweb',
# 	passwd='web@123456',
# 	db='wanjiaweb'
# )
con = mysql.connector.connect(**mysql_config)
cur = con.cursor()


# cur.execute('select * from t_address_info')

# cur.execute('select * from %s  WHERE DISTRICT_CODE= %s' % ('t_address_info', '2080'))
# cur.execute('select * from %s  WHERE PROVINCE_CODE= %s' % ('t_address_info', '2080'))
# result = cur.fetchall()  # 查询全部
# result = cur.fetchmany(10)  # 查询部分
# result = cur.fetchone()  # 查询一条 ,这时result为一个tuple，
# print(len(result))
# for x in result:
# 	print(x)
# con.commit()
# cur.close()


def execute_query(query, size=1):
	query_set = []
	if isinstance(query, str):
		cur.execute(query)
		if size == 1:
			query_set = cur.fetchone()
		else:
			query_set = cur.fetchmany(10)
	return query_set


if __name__ == '__main__':
	result = execute_query('select * from t_address_info')
	print(result)
