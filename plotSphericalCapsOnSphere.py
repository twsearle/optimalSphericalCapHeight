import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from optimalSphericalCapHeight import optimize_cap_height

def spherical_cap_coordinates(R, num_caps):
    cap_height = optimize_cap_height(R, num_caps)
    cap_theta = np.linspace(0, 2 * np.pi, num_caps, endpoint=False)
    cap_phi = np.arccos(cap_height / R)

    cap_centers_x = R * np.sin(cap_phi) * np.cos(cap_theta)
    cap_centers_y = R * np.sin(cap_phi) * np.sin(cap_theta)
    cap_centers_z = R * np.cos(cap_phi)

    cap_centers = np.column_stack((cap_centers_x, cap_centers_y, cap_centers_z))

    return cap_centers

def plot_spherical_caps_on_sphere(R, num_caps):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    phi = np.linspace(0, np.pi, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    phi, theta = np.meshgrid(phi, theta)

    x = R * np.sin(phi) * np.cos(theta)
    y = R * np.sin(phi) * np.sin(theta)
    z = R * np.cos(phi)

    cap_centers = spherical_cap_coordinates(R, num_caps)

    for center in cap_centers:
        ax.plot_surface(x + center[0], y + center[1], z + center[2], color='b', alpha=0.4)

    ax.set_xlim([-R, R])
    ax.set_ylim([-R, R])
    ax.set_zlim([-R, R])
    ax.set_aspect('auto')
    plt.show()

def main():
    R = 1.0  # Change the radius of the sphere here
    num_caps = 4  # Change the number of caps here

    plot_spherical_caps_on_sphere(R, num_caps)

if __name__ == "__main__":
    main()

