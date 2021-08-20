# JKTools_python
Python tools 

## Run
```console
$ ./Report_MemBW_rocprof.py 
Report_MemBW_rocprof.py -i <input csv file>

$ ./Report_MemBW_rocprof.py -i sample.csv 
Input CSV filename = sample.csv
 
Kernel name: void triad_kernel<double>(double*, double const*, double const*) [clone .kd]
 ---------- Memory Bandwidth (GB/s): 943.9176903325856

Kernel name: void dot_kernel<double>(double const*, double const*, double*, unsigned int) [clone .kd]
 ---------- Memory Bandwidth (GB/s): 705.3718164660054

````

## Bug report and requests
Send bug reports and feature requests to JaeHyuk Kwack (jkwack@anl.gov).
