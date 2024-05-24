cpu = ['get_cpu_cores', 'get_virtual_cpu_cores', 'get_max_cpu_speed', 'get_min_cpu_speed', 'get_cpu_usage']
ram = ['get_ram', 'get_available_ram', 'get_used_ram', 
       'get_swap_ram', 'get_used_swap_ram']

__all__ = cpu + ram

from cpu import *
from ram import *

_ = get_cpu_cores, get_virtual_cpu_cores, get_max_cpu_speed, get_min_cpu_speed, get_cpu_usage, \
    get_ram, get_available_ram, get_used_ram, \
    get_swap_ram, get_used_swap_ram
