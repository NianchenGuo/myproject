"""
作者：郭伟伟
功能：将汇率兑换功能封装到函数中
版本号：V4.0
日期：2019/11/21

已经接触到的函数：print(). input(). eval()

"""


def convert_currency(im, er):
    """
    汇率兑换函数
    """
    out = im * er
    return out


# 汇率
USD_VS_RMB = 6.77

# 带单位的货币输入
currency_str_value = input("请输入带单位的货币金额：")

unit = currency_str_value[-3:]

if unit == "CNY":
    exchange_rate = 1 / USD_VS_RMB
elif unit == "USD":
    exchange_rate = USD_VS_RMB
else:
    exchange_rate = -1
if exchange_rate != -1:
    in_money = eval(currency_str_value[:-3])
    out_money = convert_currency(in_money, exchange_rate)
    print("转换后的金额：", out_money)
else:
    print("不支持该种货币！")






