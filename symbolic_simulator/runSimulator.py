import sys
from sympy.abc import x, y
import Simulator

simulator = Simulator.Simulator()

#simulator.createState(4, [x])

simulator.createState(2, [x,y])

simulator.printNonZeroPosState()

print ("#######")

#simulator.executeCircuit("C-X,0-3;X,0;H,0;H,0")
simulator.executeCircuit("C-V,0-1")
simulator.printNonZeroPosState()

simulator.measure([0], True)
# python runSimulator.py