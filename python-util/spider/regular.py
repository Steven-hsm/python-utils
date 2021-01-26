import re

myStr = "2021-01-26 00:05:00.339 [ThreadPoolTaskScheduler-1] INFO  c.l.w.pharmaux.service.impl.PharmStockService - existDrugCodes:[\"41296\",\"40764\",\"6\",\"43044\",\"44091\"]"
# 尝试从字符串的起始位置匹配一个模式
re.match("阿达", myStr)

matchGroups = re.match(r"(.*) (.*) \[(.*):(.*)", myStr, re.M | re.I)
if matchGroups:
    print(matchGroups.group())
    print(matchGroups.group(1) + ":" + matchGroups.group(4))

searchResult = re.search("339", myStr)
# 扫描整个字符串并返回第一个成功的匹配
print(searchResult.span())

# 只保留数字
phone = "1586558083@qq.com?"
digitalStr = re.sub("\\D", "", phone,count=0)
print(digitalStr)

# 将匹配的数字乘以2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

# 编译为正则表达式
pattern = re.compile(r'\d+')

# 查找所有匹配结果
pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
print(result1)

# 根据正则分割对象
pattern = re.compile(r'\d+')   # 查找数字
result2 = pattern.split('runoob 123 google 456')
print(result2)