# NetCheck
A tool to extract a list of all open connection ports, a list of processes and programs running on the computer, and check if there are any suspicious programs connected


      ███╗   ██╗███████╗████████╗         ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
      ████╗  ██║██╔════╝╚══██╔══╝        ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
      ██╔██╗ ██║█████╗     ██║           ██║     ███████║█████╗  ██║     █████╔╝
      ██║╚██╗██║██╔══╝     ██║           ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗
      ██║ ╚████║███████╗   ██║ ██╗██╗██╗ ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
      ╚═╝  ╚═══╝╚══════╝   ╚═╝ ╚═╝╚═╝╚═╝  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝

    Press Enter To Start Scan

    Active Connections

    Proto  Local Address          Foreign Address        State           PID
    TCP    192.168.1.3:5053       51.102.4.150:1177      LISTENING       1136
    TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
  
    Image Name                     PID Session Name        Session#    Mem Usage
    ========================= ======== ================ =========== ============
    System Idle Process              0 Services                   0          4 K
    trojen.exe                    1136 Console                    1      1,744 K



How do I determine what port an application is using?
How do I determine what application is using a specific port?

# list all the connections  listening ports
    Active Connections

     Proto  Local Address          Foreign Address        State           PID
     TCP    192.168.1.3:5053       51.102.4.150:1177      LISTENING       1136 <===

# list of the processes and programs running on the computer

     Image Name                     PID Session Name        Session   Mem Usage
     ========================= ======== ================ =========== ============
     trojen.exe               ===> 1136 Console                    1     1,744 K

In the output column "Local Address", locate the port number of interest. Note the PID (Process ID) that corresponds to the port





