import time
import serial

# Ouvre le port série en utilisant la vitesse de 9600 bauds
ser = serial.Serial("COM2", 9600)

# Attend la réception d'une trame
trame = ser.readline(0)
time.sleep(5)
# Convertit la trame en chaîne de caractères et enlève le retour à la ligne
trame_str = trame.decode().strip()
trame_str = trame_str[0:4]

# Affiche la trame reçue
print(f"Trame reçue : {trame_str}")
print(trame)

# Ferme le port série
ser.close()