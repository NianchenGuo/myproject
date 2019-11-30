"""
作者：郭伟伟
功能：汇率兑换
版本号：V1.0
日期：2019/11/21
"""

# 汇率
USD_VS_RMB = 6.77

# 人民币的输入
rmb_str_value = input("请输入人民币(CNY)金额：")

# 人民币的输入转化为数字
rmb_value = eval(rmb_str_value)

# 汇率计算
usd_value = rmb_value / USD_VS_RMB

# 输出美元
print("美元(SUD)金额是:", usd_value)
