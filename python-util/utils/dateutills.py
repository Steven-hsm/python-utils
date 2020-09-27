from datetime import datetime,timedelta

# %a	显示简化星期名称
# %A	显示完整星期名称
# %b	显示简化月份名称
# %B	显示完整月份名称
# %c	本地相应的日期和时间表示
# %d	显示当月第几天
# %H	按24小时制显示小时
# %I	按12小时制显示小时
# %j	显示当年第几天
# %m	显示月份
# %M	显示分钟数）
# %p	本地am或者pm的相应符
# %S	显示秒数）
# %U	一年中的星期数
# %w	显示在星期中的第几天，默认从0开始表示周一
# %W	和%U基本相同
# %x	本地相应日期
# %X	本地相应时间
# %y	去掉世纪的年份（00 - 99）
# %Y	完整的年份
# %Z	时区的名字（如果不存在为空字符）
# %%	‘%’字符
date_format = '%Y%m%d'


def currentStartTime(cdate):
    _detatime = datetime.strptime(cdate, date_format)
    print(_detatime)
    return int(_detatime.timestamp() * 1000)


def currentEndTime(cdate):
    _detatime = datetime.strptime(cdate, date_format)
    _endTime = int(_detatime.timestamp() * 1000)
    _endTime += 24 * 60 * 60 * 1000 - 1
    return int(_endTime)

def getBetweenDates(sDateStr, eDateStr):
    list = []
    datestart = datetime.strptime(sDateStr, date_format)
    dateend = datetime.strptime(eDateStr, date_format)
    list.append(datestart.strftime(date_format))
    while datestart < dateend:
        datestart += timedelta(days=1)
        list.append(datestart.strftime(date_format))
    return list

def nowDate():
    _detatime = datetime.now()
    _nowDate = _detatime.strftime(date_format)
    return _nowDate;

def nowDate(format):
    _detatime = datetime.now()
    _nowDate = _detatime.strftime(format)
    return _nowDate;
