# Donations
It takes me a long time to make these libraries. If you would like to support my work, Then you can follow my patreon :)

https://www.patreon.com/Schkimansky

# Library
This is a easy to use python library to get information about your system! Such as how much ram you have, Cpu cores etc.

```python
import systore
result = systore.get_disk_partitions()
print(result) # All disk partitions on your system
```

# Installation
```bash
pip install systore
```

# Documentation
These are all the functions, They are pretty much self explanatory.
More functions coming in future updates. Also, this library is based on psutils. This library is way easier than psutil too.

| Function              | Info                                              |
| --------------------- | ------------------------------------------------- |
| get_cpu_cores         | Get how many cores your cpu has.                  |
| get_virtual_cpu_cores | Virtual cores are made to increase speed of cpu.  |
| get_max_cpu_speed     | Get your cpu speed in Megahertz. (Not gigahertz). |
| get_min_cpu_speed     | Get minimum cpu speed.                            |
| get_cpu_usage         | Get current cpu usage.                            |
| get_ram               | Get how much ram you have.                        |
| get_available_ram     | Get how much ram you have available.              |
| get_used_ram          | Get how much ram you have used.                   |
| get_swap_ram          | Get how much swap ram you have.                   |
| get_used_swap_ram     | Get how much swap ram is being used currently.    |
| get_disk_partitions   | Get how many disk partitions you have.            |
| get_file_system_type  | Get the file system type of a disk partition.     |
| get_mount_point       | Get the mount point of a disk partition.          |
