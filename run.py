from Assets.assetsManage import assets_manage
# import os

print('欢迎使用个人资产管理工具，此工具目标为全平台集合、投资采取长线投资策略, 具有一定技术要求的收益帮助计算工具，'
      '不会推出推荐使用者具体投资方案的功能 \n 现阶段为version 0 爬虫自动化、算法参考、可视化界面等功能暂未添加， 功能还在开发中\n')
init = assets_manage()
while True:
    print('1: 插入新的资产投资信息 \n 2: 更新当日资产信息\n 3: 买入卖出资产更新 \n 4: 查询全部投资资产 \n '
          '5: 按id查询投资资产情况 \n 6: 按sql条件查询资产 sql条件暂需要自己编写 \n 7: 退出 \n')
    choose = int(input('请输入选项 \n'))
    if choose == 1:
        init.insert_new_assets()
    elif choose == 7:
        print('感谢参与测试， 欢迎留下改进措施')
        break
    else:
        print('其它功能施工中')
    # os.system('cls')
