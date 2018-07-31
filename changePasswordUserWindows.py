import subprocess
username = "AAECGT19"
password = "123"
subprocess.call("net users "+username+" "+password, shell = True)
#subprocess.call("net users "+username+" "+password+" /domain", shell = True)
