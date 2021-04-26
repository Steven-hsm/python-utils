import sys
sys.path.append('../utils')
import re
import  time

import fileutils

lineArray = fileutils.readFileAsArray("log_info.log")
for line in lineArray:
    if re.match(r"(.*)请求时间(.*)",line):
        print(line)




