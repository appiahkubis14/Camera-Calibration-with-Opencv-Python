import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


calibration_data = np.load(r'C:\Users\Samuel\Desktop\CODES\PYTHON\progress project\references\Basic-Augmented-reality-course-opencv\calib_data\MultiMatrix.npz')
dist = calibration_data['distCoef']


indices = np.arange(len(dist))

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')


ax.scatter(indices, np.zeros_like(dist), dist, c=dist, cmap='viridis', s=100)
# ax.axline(dist , len(dist))


ax.set_xlabel('Coefficient Index')
ax.set_ylabel('Zero')
ax.set_zlabel('Coefficient Value')
ax.set_title('3D Plot of the Camera Distortion Coefficients')


cbar = plt.colorbar(ax.collections[0], ax=ax, orientation='vertical')
cbar.set_label('Coefficient Value') 

plt.show()




