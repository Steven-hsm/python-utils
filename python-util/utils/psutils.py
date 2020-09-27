# 系统信息模块
import psutil

print("cpu信息:")
print(psutil.cpu_times())
print(psutil.cpu_count())

print("内存信息:")
print(psutil.virtual_memory())

print("磁盘信息:")
print(psutil.disk_partitions())
print(psutil.disk_usage("C:\\"))
print(psutil.disk_io_counters("C:\\"))

print("网络信息:")
print(psutil.net_io_counters())
print(psutil.net_if_addrs())

print("其他系统信息:")
print(psutil.users())
print(psutil.boot_time())

print("进程信息:")
print(psutil.pids())
print(psutil.Process())
