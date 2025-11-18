from netmiko import ConnectHandler
	
	# Paramètres de connexion
device = {
	    'device_type': 'cisco_ios',
        'host': 'sandbox-iosxr-1.cisco.com',
	    'username': 'admin',
	    'password': 'C1sco12345',
	    'port': 22
	}
	
	# Connexion SSH
net_connect = ConnectHandler(**device)
	
	# 1. Récupérer la liste des interfaces actives
output = net_connect.send_command("show ip interface brief")
with open("output.txt", "w") as f:
	    f.write(output)
	
print("Interfaces sauvegardées dans output.txt")
	
	# 2. Envoyer les commandes depuis un fichier
with open("commands.txt") as cmd_file:
	    commands = cmd_file.read().splitlines()
	
config_output = net_connect.send_config_set(commands)
print(config_output)
	
net_connect.disconnect()


def dire_salut():
  print("Salut, Git!")
  dire_salut()

def acces_netmiko():
# Affiche la date coté routeur
# Affiche les interfaces du routeur dans un fichier interfaces.txt
 print("Hello, Git!")
dire_bonjour()