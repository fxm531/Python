'''
名称：电话本
版本：1.0
作者：九韵
功能：输入姓名查找电话
'''
import sys
print('''|----欢迎进入通讯录程序---|
|---1.查询联系人资料---|
|---2.增加新的联系人---|
|---3.删除已有联系人---|
|---4.退出通讯录程序---|
''')
address = {}
def chaxun():
    name = input('请输入要查询的人物姓名，按回车确认：')
    if name not in address.keys():
        print('查无此人!')
        tongxunlu()
    else:
        print('{0}：电话是{1}'.format(name,address[name]))
        tongxunlu()
def zengjia():
    name = input('请输入要增加的联系人姓名，按回车确定：')
    if name in address.keys():
        panduan = input('联系人已经存在，是否更新？Y?N:')
        if panduan == 'Y':
            phone_num = int(input('请输入联系人电话，按回车确认：'))
            address[name] = phone_num
        else:
            tongxunlu()
    else:
        phone_num = int(input('请输入联系人电话，按回车确认：'))
        address[name] = phone_num
        tongxunlu()
def shanchu():
    name = input('请输入要删除的联系人姓名，按回车确认：')
    address.pop(name)
    tongxunlu()
def tuichu():
    print('感谢您使用通讯录程序，欢迎下次再见！')
    sys.exit()
def tongxunlu():
    choice = int(input('请输入相关指令代码(阿拉伯数字)，按回车确认：'))
    if choice == 1:
        chaxun()
    elif choice == 2:
        zengjia()
    elif choice == 3:
        shanchu()
    elif choice == 4:
        tuichu()
    else:
        choice = int(input('指令错误，请重新输入，按回车确认：'))
tongxunlu()
