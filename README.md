# NetCheck

A tool to extract a list of all open connection ports, a list of processes and programs running on the computer, and check if there are any suspicious programs connected

How do I determine what port an application is using?
How do I determine what application is using a specific port?

(1) list all the connections  listening ports

Active Connections

Proto  Local Address          Foreign Address        State           PID
TCP    192.168.1.3:5053       51.102.4.150:1177      LISTENING       1136 <===


(2)list of the processes and programs running on the computer

Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
trojen.exe               ===> 1136 Console                    1        364 K


In the output column "Local Address", locate the port number of interest. Note the PID (Process ID) that corresponds to the port
