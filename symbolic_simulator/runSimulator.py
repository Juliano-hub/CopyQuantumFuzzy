import sys
from sympy.abc import x, y, z
import Simulator

simulator = Simulator.Simulator()

#simulator.createState(4, [x])
#simulator.createState(2, [x,y])
#simulator.createState(1, [x])
#simulator.createState(3, [x,y,0])
#simulator.createState(2, [x,y])
simulator.createState(5, [x,x,y,0,0])
#simulator.createState(1, [1])
simulator.printNonZeroPosState()

print ("#######")

#simulator.executeCircuit("C-X,0-3;X,0;H,0;H,0")
#simulator.executeCircuit("V,0")
#simulator.executeCircuit("H,0")

#------------------------------------
#Toffoli:
#simulator.executeCircuit("C-X,0-1,2")
#o qubit 0 é o ultimo da lista, menos significativo
#qubit 1 é o y e qubit 2 é o x
#------------------------------------

#------------------------------------
# C-NOT:
#"C-X,CONTROLE-ALVO"
#simulator.executeCircuit("C-X,0-1")
# se qubit 0 tem valor 1, aplica X no qubit 1
#simulator.executeCircuit("C-X,1-0") 
# se qubit 1 tem valor 1, aplica X no qubit 0
#------------------------------------

#simulator.executeCircuit("C-SX,0-1")

# Circuito pais e filho modal: x^2 é armazenado no qubit 3, realiza a CRaizQuadrada entre qubit y e filho, e depois CRaizQuadrada pai^2 e filho
simulator.executeCircuit("C-X,0-1,3;C-SX,2-4;C-SX,3-4")

simulator.printNonZeroPosState()

print ("####### Measure #######")
# se qubits 111, simulator.measure([0], True): mede 11[1]
# se qubits 111, simulator.measure([1], True): mede 1[1]1
# se qubits 111, simulator.measure([2], True): mede [1]11
simulator.measure([0], True)
# python runSimulator.py