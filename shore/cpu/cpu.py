import psutil as _psutil

def get_cpu_cores(): 
    """
    Returns the number of cpu cores in your computer.
    """
    return _psutil.cpu_count(logical=False)
def get_virtual_cpu_cores(): 
    """
    Returns the number of virtual cpu cores in your computer.
    Virtual cores are used to make a cpu more like a GPU to increase its speed.
    """
    return _psutil.cpu_count(logical=True)

