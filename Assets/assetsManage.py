from SqlFunction.assets import assetsManage
from datetime import date, datetime


class assets_manage(assetsManage):
    def __init__(self):

        super().__init__()
        self.is_db_exist()
        self.is_assets_table_exist()

    def insert_new_assets(self):
        try:
            name = input('\n请输入新资产的项目名称：')
            begin_with = float(input('\n请输入初次购买时投资金额：\n'))
            unit_price = float(input('\n请输入初次购买时单位价值:\n'))
            is_end = 0
            risk_type = input('\n请输入风险类型(零风险/基金/股票/黄金):\n')
            currency_type = input('\n请输入货币类型(人民币/美元等)：\n')
            begin_time = input('\n是否是今天购买的资产呢？是请输入1 否请输入日期如2020-1-1: \n')
            if begin_time == '1':
                begin_time = date.today()
            else:
                begin_time = datetime.strptime(begin_time, '%Y-%m-%d')
            end_time = datetime.strptime('2099-1-1', '%Y-%m-%d')
            is_fixed = int(input('\n是否是定期类型呢？，是请填1 不是填0，后续版本会更新定期自动结算: \n'))
            if is_fixed == 1:
                end_time = input('请输入定期结束时间 如2020-1-1: \n')
                end_time = datetime.strptime(end_time, '%Y-%m-%d')

            result = self.input_new_assets(name=name, begin_with=begin_with, unit_price=unit_price, is_end=is_end,
                                           risk_type=risk_type, currency_type=currency_type, begin_time=begin_time,
                                           is_fixed=is_fixed, end_time=end_time)
            if result:
                print('添加新资产成功')
        except Exception as e:
            print(e, '请确认输入信息是否正确')

    def update_earned_spider(self):
        # 添加爬虫程序, 查询投资增值减值
        pass

    def update_earned_manually(self):
        # 手动更新价值
        pass

    def update_assets_change(self):
        # 增持减持更新
        pass

    def find_all_assets(self):
        pass

    def find_assets_with_limits(self):
        pass

    def end_my_assets(self):
        # 结束资产
        pass


"""
要做的还有很多，比如确定是否是今天买入的资产
不是的话要爬取当日的价格和今天的价格，不如先直接自己填入购买价和时间
爬虫方面还要手动提供url 要找到一个综合提供信息的网站 motherfuck
"""
