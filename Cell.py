import os
from termcolor import colored as c
import sys
import re


filename = sys.argv[0]
filetype = filename[-3:]



while True:
    error1 = "' is not a valid cell command."
    error2 = "No such valid file or directory."
    cmd = input("Cell>> ")
    
    if cmd == "file open":
        filedir = input("   File>> ")
        try:
            os.startfile(filedir)
        except:
            print(c(error2, "red"))
    elif cmd == "file new":
        dirn = input("  Directory>> ")
        try:
            nfile = open(dirn+"/Untitled.cell", "w")
            editn = input("  Untitled.cell>> ")
            nfile.write(editn)
            nfile.close()
        except:
            print(c(error2, "red"))
    elif cmd == "file open txt":
        diro = input("  File>> ")
        try:
            ofiler = open(diro, "r")
            ofilea = open(diro, "a")
            ofilere = ofiler.read()
            inputo = input("  "+diro+">> "+ofilere)
            ofilea.write(inputo)
            ofiler.close()
            ofilea.close()
        except:
            print(c(error2, "red"))
    elif cmd == "file open cell":
        diroc = input("  File>> ")
        try:
            ofilerc = open(diroc, "r")
            ofileac = open(diroc, "a")
            ofilerec = ofilerc.read()
            inputoc = input("  "+diroc+">> "+ofilerec)
            ofileac.write(inputoc)
            ofilerc.close()
            ofileac.close()
        except:
            print(c(error2, "red"))
    elif cmd == "file read":
        dirr = input("  File>> ")
        try:
            rfile = open(dirr, "r")
            readfile = rfile.read()
            input("  "+dirr+">> "+readfile)
            rfile.close()
        except:
            print(c(error2, "red"))
    elif cmd == "":
        pass
    elif cmd == " ":
        pass
        
    elif cmd[:5] == "label":
        lbl = re.sub(r'.', '', cmd, count = 6)
        print(lbl)
    elif cmd[:6] == "input ":
        inp = re.sub(r'.', '', cmd, count = 7)
        input(inp)
    elif cmd[:11] == "input_label":
        inl = re.sub(r'.', '', cmd, count = 12)
        inl_result = input(inl)
        print(inl_result)
    elif cmd[:6] == "system":
        sysf = re.sub(r'.', '', cmd, count = 7)
        os.startfile("C:\\Windows\\"+sysf)
    elif cmd == "system notepad":
        os.startfile("C:\\Windows\\notepad.exe")
    elif cmd == "system explorer.exe":
        os.startfile("C:\\Windows\\explorer.exe")
    elif cmd == "cell test":
        os.startfile("Cell.py")
    elif cmd == "cell kill":
        exit()
    elif cmd == "cell restart":
        try:
            os.startfile("Cell.py")
        except:
            os.startfile("Cell.exe")
        exit()
       
    elif cmd == "cell about":
        print("""                                                                                                    
                            .:~!!777777777777777777!!!!!!!!!!!!!!!!!!!!!!!~^:.                          
                          :!7????????????????77777777777777777777777777777777!~.                        
                         ~?????????????????777777777777777777777777777777777777!^                       
                        .!??????7!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!7777777~                      
                      .7??????7~^~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^~~~~~~!777777~.                    
                     ^???????!~~~~^^^^~~~~~~~~~~~~~~~^^~!7?JYYYYYJ?7!~^^~~~~!777777!:                   
                    ~???????!~~~~!77??????77~~~~~~~^~?YPGBBBBBBBBBBBGPY7~^~~~!7777777:                  
                  .!???????~~~~^?555YYJJJ???!~~~~^!YGBBBBBBBBBBBBBBBBBBBPJ~^~~~7777777^                 
                 .7??????7~~~~~^755Y?!!!!!!!~~~~~?GBBBBBBBBBBBBBBBBBBBBBBBP7^~~~!777777~.               
                ^???????7~~~~~~~^!7!^^~~~~~~~~~~Y#BBBBBBBBBBBBBBBBBBBBBBBBBB?^~~~!777777!.              
               ~???????!~^^~~~~~~^^^~~~~~~~~~~^J#BBBBBBBBBBBBBBBBBBBBBBBBBBBB7^~~~!7777777:             
             .!J??????!^~!?JJJJJ?7!~~~~~~~~~~~~G#BBBBBBBBBBBBBBBBBBBBBBBBBBBB5^~~~~~7777777^            
            .7J?????7~^!JYYYYYYYYYYJ?!~^~~~~~~!B#B#BBBBBBBBBBBBBBBBBBBBBBBBBBP~~~~~~~!777777~.          
           ^?J?????7~^7Y5YYYYYYYYYYYYJJ7~^~~~~~G#####BBBBBBBBBBBBBBBBBBBBBBBB5~~~~~~~~!777777!.         
          ~JJ?????!~^755YYYYYYYYYYYYYJJYJ7~^~~^J#########BBBBBBBBBBBBBBBBBBBB7^~~~~~~~~!7777777:        
        .!JJJ??J?!~~~Y55YYYYYYYYYYYYYYJJJJJ7~^~~5###########BBBBBBBBBBBBBBBBJ^~~~~~~~~~~~7777777^       
       .7JJJJJJ?~~~^?55555YYYYYYYYYYYYYYJJJJJ7~^~JB#############BBBBBBBBB#G?^~~~~~~~~~~~~~!777777~.     
      :?JJJJJJ7~~~~~Y555555YYYYYYYYYYYYYYJJJJJJ!~^!5B###################GY~^~~~7?7!~~~~~~~~!777777!.    
     .?JJJJJ?!~~~~^!55555555YYYYYYYYYYYYYYJJJJJJ?~^^!JPB############BG5?~^~~~^~????7~~~~~~~~!777777!    
     :JJJJJJ7^~~~~^7555555555YYYYYYYYYYYYYYJJJJJJJ7~^^^~7?JY5PP55YJ?!~^^~~^~~7?JJ?7~~~~~~~~~~!777777.   
     .JJJJJJ?~^~~~^!55555555555YYYYYYYYYYYYYYJJJJJJJ?!~~^^^^^^^^^^^^^~~~~~?YYYYYJ7~~~~~~~~~~~777777!.   
      ~JJJJJJ?!~~~~~555555555555YYYYYYYYYYYYYYJJJJJJJJJ??77!!~~~~~~~~~~~~~?555Y?~^~~~~~~~~~!7777777:    
       ^JJJJJJJ7~~~^JP55555555555YYYYYYYYYYYYYYJJJJJJJJJJJJJJ??77!~~~~~~~~~~77!~~~~~~~~~~~!777777!:     
        :?JJJJJJ7~~~!5555555555555YYYYYYYYYYYYYYJJJJJJJJJJJJJJJJ????7!~~~~~~^^~~~~~~~~~~~7777777!.      
         .7JJJJJJ?~^^7P5555555555555YYYYYYYYYYYYYYJJJJJJJJJJJJJJ???????7~~~~~~~~~~~~~~~~7777777~        
           !JJJJJJ?!^^75P555555555555YYYYYYYYYYYYYYJJJJJJJJJJJJJJ????????!~~~~~~~~~~~~!7777777^         
            ^JJJJJJJ7~^!5P555555555555YYYYYYYYYYYYYYJJJJJJJJJJJJJJ????????~~~~~~~~~~~!7777777:          
             :?JJJJJJ7~^!YP555555555555YYYYYYYYYYYYYYJJJJJJJJJJJJJJ???????~~~~~~~~~~7777777!.           
              .7JJJJJJ?~^~J5P555555555555YYYYYYYYYYYYYYJJJJJJJJJJJJJJ????7~~~~~~~~~7777777~             
                !JJJJJJ?!^^!YPP55555555555YYYYYYYYYYYYYYJJJJJJJJJJJJJJJJ7~~~~~~~~!7777777^              
                 ^JJJJJJJ7~^~7Y555555555555YYYYYYYYYYYYYYJJJJJJJJJJJJJ?!~~~~~~~~!7777777:               
                  :?JJJJJJ7~^^~!J55555555555YYYYYYYYYYYYYYJJJJJJJJJJ?!~~~~~~~~~7?7777?!.                
                   .7JJJJJJ?~^~^^~7JY55555555YYYYYYYYYYYYYYYJJJJJJ7!~^~~~~~~~~7?7777?~                  
                     !JJJJJJ?!^~~~^^~!?JYY5555555YYYYYYYYYYYYJ?7!~~~~~~~~~~~!7???7??^                   
                      ~JJJJJJJ7~~~~~~^^^~~!77??JJJJJJJJJ??77!~~^^~~~~~~~~~~!??????7:                    
                       :?JJJJJJ7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~7??????7.                     
                        .7JJJJJJJ???????????????????????????????777777777???????!.                      
                          ~?JJJJJJJJJJJJJJJ???????????????????????????????????7^                        
                           .^!??JJJJJJJJJJJJJJ????????????????????????????77~:                          
                                                            
                                                                                                    
""")
        if filetype == ".py":
            input(("""            Cell Terminal v1.0 [Open Source]  AdV.(c) All rights reserved
                """ ))
                
        if filetype == "exe":
            input(("""                 Cell Terminal v1.0 [Stable]  AdV.(c) All rights reserved
                """))
    
    else:
        er1 = "'" + cmd + error1
        print(c(er1, "red"))

