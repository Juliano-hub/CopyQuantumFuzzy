import sys
from sympy.abc import x, y, z, N
import Simulator

simulator = Simulator.Simulator()

simulator.createState(1, [1])

#simulator.createState(5, [x,x,0,0,0])
#                        [4,3,2,1,0]
simulator.printNonZeroPosState()

simulator.createState(6, [0,0.90,0.70,0,0.60,0.25])
#                        [   5,   4,3,   2,   1,0]
print ("#######")

#------------------------------------
#Toffoli:
#simulator.executeCircuit("C-X,0-1,2")
#C-X,3-1,2,0 -> Applies X gate on qubit 3 if qubits 1 and 2 are 1 and 0 respectively
#o qubit 0 é o ultimo da lista, menos significativo
#qubit 1 é o y e qubit 2 é o x
#------------------------------------
# C-NOT:
#"C-X,CONTROLE-ALVO"
#simulator.executeCircuit("C-X,0-1")
# se qubit 0 tem valor 1, aplica X no qubit 1
#simulator.executeCircuit("C-X,1-0") 
# se qubit 1 tem valor 1, aplica X no qubit 0
#------------------------------------


#simulator.executeCircuit("C-SX,0-1")

#simulator.executeCircuit("C-SX,0-2;C-SX,1-2")

# Circuito pais e filho modal: x^2 é armazenado no qubit 3, realiza a CRaizQuadrada entre qubit y e filho, e depois CRaizQuadrada pai^2 e filho
#simulator.executeCircuit("X,3;C-X,2-3,4;C-SX,0-1;C-SX,0-2")

#simulator.executeCircuit("C-X,2-4,3;C-X,0-2;C-X,0-1")


simulator.executeCircuit("Ry1,5;C-X,5-3;Ry2,4;C-X,4-3;Ry3,2;C-X,2-0;Ry4,1;C-X,1-0")

#simulator.printNonZeroPosState()
#simulator.printPosState()

print ("####### Measure #######")
simulator.measure([0], True)
simulator.measure([3], True)
# python runSimulator.py