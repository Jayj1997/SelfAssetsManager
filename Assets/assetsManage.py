from SqlFunction.assets import assetsManage
from datetime import datetime


class assets_manage(assetsManage):
    def insert_new_assets(self):
        name = input('请输入新资产的项目名称：\n')
        begin_with = datetime.now()
        is_end = 0
        risk_type = input('请输入风险类型:')
