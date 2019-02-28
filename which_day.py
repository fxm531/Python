from datetime import datetime
in_day_str = input('请按照格式输入年月日(yyyy/mm/dd)：')
in_day = datetime.strptime(in_day_str,'%Y/%m/%d')

def is_leap_year(year):
    '''
    判断是否为闰年
    '''
    is_leap = False
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        is_leap == True
    return is_leap
def main():
    '''
    主函数
    '''
    year = in_day.year
    month = in_day.month
    day = in_day.day
    month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year) and month > 2:
        month_day[1] = 29
    days = sum(month_day[:month-1])+day
    print('这是{0}年第{1}天'.format(year,days))
if __name__ == '__main__':
    main()