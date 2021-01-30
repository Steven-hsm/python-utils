import sys
sys.path.append('../utils')
import re

import fileutils

lineArray = fileutils.readFileAsArray("log_info(7).log")
for line in lineArray:
    if re.match(r"(.*)App层接收到Hal层的原始应答(.*)\[2,60,3,1,37\](.*)\"CMD\":22(.*)ID(.*)",line):
        print(line)
    if re.match(r"(.*)App层接收到Hal层的原始应答(.*)\[2,60,3,1,37\](.*)\"CMD\":22(.*)END(.*)",line):
        print(line)
