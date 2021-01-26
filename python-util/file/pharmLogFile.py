import sys
sys.path.append('../utils')

import fileutils

lineArray = fileutils.readFileAsArray("log_info.log")
for line in lineArray:
    if "App层接收到Hal层的原始应答" in line:
        print(line)
