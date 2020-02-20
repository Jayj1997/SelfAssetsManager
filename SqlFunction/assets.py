from .dbmysql import sqlManage


class assetsManage(sqlManage):
    # 建库 查询是否存在数据库。
    def is_db_exist(self):
        con, cur = self.connect()
        is_exist = cur.execute('show databases like "{0}";'.format('selfAssetsManager'))
        if is_exist == 0:
            cur.execute('create database selfAssetsManager character set utf8mb4;')

    def is_assets_table_exist(self):
        con, cur = self.connect()
        cur.execute('use {0};'.format(self.db))
        is_exist = cur.execute('show tables like "{0}";'.format('Assets'))
        if is_exist == 0:
            # boolean会建立成功但是显示是tinyint， 所以就用1，0代表true false
            cur.execute('create table Assets('
                        '_id int(10) primary key auto_increment,'
                        'name varchar(255),'
                        'begin_with float(15),'
                        'end_with float(15),'
                        'is_end boolean,'
                        'earning_rate varchar(10),'
                        'risk_type varchar(20),'
                        'currency_type varchar(20),'
                        'begin_time datetime,'
                        'end_time datetime);')

    def input_new_assets(self, **kwargs):
        try:
            name = kwargs['name']
            begin_with = kwargs['begin_with']
            is_end = kwargs['is_end']
            risk_type = kwargs['risk_type']
            currency_type = kwargs['currency_type']
            begin_time = kwargs['begin_time']
            sql = "insert into Assets (name, begin_with, is_end, risk_type, currency_type, begin_time) values" \
                  " ('%s', '%s', '%s', '%s', '%s', '%s',);" \
                  % (name, begin_with, is_end, risk_type, currency_type, begin_time)
            result = self.execute(sql=sql)
            return result
        except Exception as e:
            print(e)
            return False

    def update_assets(self, **kwargs):
        try:
            _id = kwargs['_id']
            end_with = kwargs['end_with']
            earning_rate = kwargs['earning_rate']
            sql = "UPDATE Assets set end_with='%s', earning_rate='%s' where _id='%s';"% (end_with, earning_rate, _id)
            result = self.execute(sql)
            return result
        except Exception as e:
            print(e)
            return False

    def end_assets(self, **kwargs):
        try:
            _id = kwargs['_id']
            is_end = kwargs['is_end']
            end_time = kwargs['end_time']
            sql = "UPDATE Assets set is_end='%s', end_time='%s' where _id='%s';" % (is_end, end_time, _id)
            result = self.execute(sql)
            return result
        except Exception as e:
            print(e)
            return False

