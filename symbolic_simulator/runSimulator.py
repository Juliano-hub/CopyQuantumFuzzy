import sys
from sympy.abc import x, y, z
import Simulator

simulator = Simulator.Simulator()

#simulator.createState(4, [x])
#simulator.createState(2, [x,y])
#simulator.createState(1, [x])
#simulator.createState(3, [x,y,z])


#simulator.createState(5, [x,x,y,0,0])
simulator.createState(3, [x,y,0])
simulator.printNonZeroPosState()

print ("#######")

#simulator.executeCircuit("C-X,0-3;X,0;H,0;H,0")
#simulator.executeCircuit("C-SX,1-2;C-SX,0-2")
#simulator.executeCircuit("V,0")
#simulator.executeCircuit("H,0")

#circuito pais e filho
#simulator.executeCircuit("Toffoli, 0-1-2")
simulator.printNonZeroPosState()

print ("####### Measure #######")

simulator.measure([0], True)
# python runSimulator.py