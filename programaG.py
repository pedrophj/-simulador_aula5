import vrep 
from pedrohj import *

j1=[]
j2=[]
j3=[]
j4=[]

# Configuração (Setup)
arduino = objeto()
for i in range(3):
	j1.append( arduino.obter("rw_joint1_"+str(i+1)) )
for i in range(3):
	j2.append( arduino.obter("rw_joint2_"+str(i+1)) )
for i in range(3):
	j3.append( arduino.obter("rw_joint3_"+str(i+1)) )
for i in range(3):
	j4.append( arduino.obter("rw_joint4_"+str(i+1)) )


arduino.setPos(j1[0], 0)
arduino.setPos(j1[1], 0)
arduino.setPos(j1[2], 90)

arduino.setPos(j2[0], 0)
arduino.setPos(j2[1], 0)
arduino.setPos(j2[2], 90)

arduino.setPos(j3[0], 0)
arduino.setPos(j3[1], 0)
arduino.setPos(j3[2], 90)

arduino.setPos(j4[0], 0)
arduino.setPos(j4[1], 0)
arduino.setPos(j4[2], 90)


angulos=[ [0,0,90] , [60,-15,90] , [60,0,90] ]
angulos2=[ [0,0,90] , [-60,-15,90] , [-60,0,90] ]

# Loop infinito
while True:
	# Pata 1
	for i in range(3):
		for k in range(3):
			arduino.setPos(j1[k],angulos[i][k])
			arduino.delay(30)
	for i in range(3):
		for k in range(3):
			arduino.setPos(j4[k],angulos2[i][k])
			arduino.delay(30)
	for i in range(3):
		for k in range(3):
			arduino.setPos(j3[k],angulos[i][k])
			arduino.delay(30)
	for i in range(3):
		for k in range(3):
			arduino.setPos(j2[k],angulos2[i][k])
			arduino.delay(30)
	arduino.delay(300)
	arduino.setPos(j1[0],-60)
	arduino.setPos(j3[0],-60)
	arduino.setPos(j2[0], 60)
	arduino.setPos(j4[0], 60)
	arduino.delay(150)

