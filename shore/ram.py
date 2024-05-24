import psutil as _psutil
from functools import lru_cache

@lru_cache
def get_ram():
    virtual_mem = _psutil.virtual_memory()    
    return virtual_mem.total

def get_available_ram():
    virtual_mem = _psutil.virtual_memory()    
    return virtual_mem.available
