import os 
while True :     
      print("""
      ███╗   ██╗███████╗████████╗         ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
      ████╗  ██║██╔════╝╚══██╔══╝        ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
      ██╔██╗ ██║█████╗     ██║           ██║     ███████║█████╗  ██║     █████╔╝ 
      ██║╚██╗██║██╔══╝     ██║           ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
      ██║ ╚████║███████╗   ██║ ██╗██╗██╗ ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
      ╚═╝  ╚═══╝╚══════╝   ╚═╝ ╚═╝╚═╝╚═╝  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝""")
      print("")
      input("Press Enter To Start Scan")
      os.system("color f")
      os.system("color a")
      os.system("netstat -ano")
      os.system("tasklist")
      os.system("color f")
      print("")
      input("Press Enter Clear")
      os.system("cls")