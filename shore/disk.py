import psutil as _psutil

def get_disk_partitions():
    partitions = _psutil.disk_partitions()
    return [partition.device for partition in partitions]
