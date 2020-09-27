import psutil

def printDiskUsage():
    disk_part = psutil.disk_partitions();
    for part in disk_part:
        usage = psutil.disk_usage(part.device)
        total = round(usage.total/1024/1024/1024,2)
        used = round(usage.used/1024/1024/1024,2)
        percent = usage.percent;
        print(part.device)
        print("总大小:" + str(total) + "GB")
        print("已使用:" + str(used) + "GB")
        print("占比:" + str(percent))

        print()

printDiskUsage()