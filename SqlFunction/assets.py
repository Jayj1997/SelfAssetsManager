from SqlFunction.dbmysql import sqlManage


class assetsManage(sqlManage):
    # 建库 查询是否存在数据库。
    # 建库建表没必要写出错控制 except后没库没表也没有继续运行的必要了
    def is_db_exist(self):
        print('查询数据库是否存在中···')
        con, cur = self.connect()
        is_exist = cur.execute('show databases like "{0}";'.format('selfAssetsManager'))
        if is_exist == 0:
            cur.execute('create database selfAssetsManager character set utf8mb4;')

    def is_assets_table_exist(self):
        print('查询表是否存在中···')
        con, cur = self.connect()
        cur.execute('use {0};'.format(self.db))
        is_exist = cur.execute('show tables like "{0}";'.format('Assets'))
        if is_exist == 0:
            # boolean会建立成功但是显示是tinyint， 所以就用1，0代表true false
            """
            _id 自增键 用来记录投资资产
            name 用来记录投资的项目名称
            begin_with 记录初买入时投入金额，加仓也会影响begin_money
            unit_price 购买单价 每次更新会改变
            end_with 记录结束时的金额
            is_end 记录是否此项目结束投资
            risk_type 风险类型 零风险（银行存款、货币基金（余额宝、微信）、基金、股票、期货（玩期货就不要整长期投资了、除非是黄金期货）
            currency_type 货币类型 （美元、人民币等)
            begin_time 开始投资时间
            end_time 结束投资时间
            is_fixed 是否是定期（自动结束）
            由于初版没有加入爬虫项目，所以不能得知每次金额是多少，所以定投项目暂时先创表、不操作
            is_timing 是否定投
            timing_date 定投日期
            timing_money 定投金额
            """
            cur.execute('create table Assets('
                        '_id int(10) primary key auto_increment,'
                        'name varchar(255),'
                        'begin_with float(10, 2),'
                        'unit_price float(10, 2),'
                        'end_with float(10, 2),'
                        'is_end boolean,'
                        'risk_type varchar(20),'
                        'currency_type varchar(20),'
                        'begin_time datetime,'
                        'end_time datetime,'
                        'is_fixed boolean,'
                        'is_timing boolean,'
                        'timing_date varchar(20),'
                        'timing_money float(10, 2));')

    def input_new_assets(self, **kwargs):
        try:
            name = kwargs['name']
            begin_with = kwargs['begin_with']
            unit_price = kwargs['unit_price']
            is_end = kwargs['is_end']
            risk_type = kwargs['risk_type']
            currency_type = kwargs['currency_type']
            begin_time = kwargs['begin_time']
            is_fixed = kwargs['is_fixed']
            end_time = kwargs['end_time']

            sql = "insert into Assets (name, begin_with, unit_price, is_end, risk_type, currency_type, begin_time, " \
                  "is_fixed, end_time) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" \
                  % (name, begin_with, unit_price, is_end, risk_type, currency_type, begin_time, is_fixed, end_time)
            self.execute(sql=sql)
            return True
        except Exception as e:
            print(e, '资产表建立失败，请修复重新插入新资产')
            return False

    def update_assets(self, **kwargs):
        try:
            _id = kwargs['_id']
            unit_price = kwargs['unit_price']
            end_with = kwargs['end_with']

            sql = "UPDATE Assets set unit_price='%s', end_with='%s' where _id='%s';" % (unit_price, end_with, _id)
            self.execute(sql)
            return True
        except Exception as e:
            print(e, '资产更新失败，请修复错误重新更新')
            return False

    def end_assets(self, **kwargs):
        try:
            # 结束时记得更新一次资产
            _id = kwargs['_id']
            is_end = kwargs['is_end']
            end_time = kwargs['end_time']
            sql = "UPDATE Assets set is_end='%s', end_time='%s' where _id='%s';" % (is_end, end_time, _id)
            self.execute(sql)
            return True
        except Exception as e:
            print(e, '资产结束失败，请修复错误重新结束')
            return False

    def buy_in_out(self, **kwargs):
        try:
            _id = kwargs['_id']
            begin_with = kwargs['begin_time']
            unit_price = kwargs['unit_price']
            end_with = kwargs['end_with']
            sql = "UPDATE Assets set begin_with='%s', unit_price='%s', end_with='%s' where _id='%s';" % \
                  (begin_with, unit_price, end_with, _id)
            self.execute(sql)
            return True
        except Exception as e:
            print(e)
            return False

    def find_all_assets(self):
        sql = "select * from Assets;"
        result = self.fetchall(sql)
        if result:
            return result
        else:
            print('查询失败，请修复错误后再次查询')

    def find_assets_by_id(self, _id):
        sql = "select * from Assets where _id = '{0}'".format(_id)
        result = self.execute(sql)
        if result:
            return result
        else:
            print('id输入错误')

    def find_with_limits(self, limits):
        sql = 'select * from Assets where {0};'.format(limits)
        result = self.fetchall(sql)
        if result:
            return result
        else:
            print('查询失败，请修复条件后再次查询')


