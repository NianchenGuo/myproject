"""
作者：郭伟伟
功能：程序可以一直运行，直到用户选择退出
版本号：V3.0
日期：2019/11/21
"""

# 汇率
USD_VS_RMB = 6.77

# 带单位的货币输入
currency_str_value = input("请输入带单位的货币金额（退出程序请输入Q)：")

i = 0

while currency_str_value != "Q":
    # 获取货币单位
    unit = currency_str_value[-3:]

    if unit == "CNY":
        # 输入的是人民币
        rmb_str_value = currency_str_value[:-3]
        # 人民币的输入转化为数字
        rmb_value = eval(rmb_str_value)
        # 汇率计算
        usd_value = rmb_value / USD_VS_RMB
        # 输出美元
        print("美元(SUD)金额是:", usd_value)

    elif unit == "USD":
        # 输入的是美元
        usd_str_value = currency_str_value[:-3]
        # 美元的输入转换为数字
        sud_value = eval(usd_str_value)
        # 汇率计算
        rmb_value = sud_value * USD_VS_RMB
        # 输出人民币
        print("人民币（CNY)金额是：", rmb_value)
    else:
        print("请输入正确的货币单位")

    print("*****************************************************")
    # 带单位的货币输入
    currency_str_value = input("请输入带单位的货币金额（退出程序请输入Q)：")

    i = i + 1
    # print("循环次数：", i)


print("程序已退出！")




