# pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc='left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

"""
ms: set the size of the marker
mec: set the color of the edge of the markers
mfc: set the color inside the edge of the markers
"""

plt.plot(x, y, marker='*', ms=5, mec='b', mfc='b', linestyle='dotted')
plt.show()