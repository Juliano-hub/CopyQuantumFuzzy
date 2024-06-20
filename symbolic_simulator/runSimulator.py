import sys
from sympy.abc import x, y, z
import Simulator

simulator = Simulator.Simulator()

#simulator.createState(4, [x])
#simulator.createState(2, [x,y])
#simulator.createState(1, [x])
#simulator.createState(3, [x,y,z])


#simulator.createState(5, [x,x,y,0,0])
simulator.createState(2, [x,y])
#simulator.createState(5, [x,x,0,y,0])
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
#C - lista de portas/qubits - controles
#"C-X,0-1" - porta X no qubit 0 / 1 é a parte do controle - controle em 1
simulator.executeCircuit("C-X,0-1")
#------------------------------------

#circuito pais e filho
#simulator.executeCircuit("C-X,0-1,2")

#simulator.executeCircuit("C-X,0-1,2;C-SX,2-4;C-SX,3-4")
#simulator.executeCircuit("C-X,0-1,2;C-SX,3-4;C-SX,2-4")

simulator.printNonZeroPosState()

print ("####### Measure #######")

simulator.measure([0], True)
# python runSimulator.py