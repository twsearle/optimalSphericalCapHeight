import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def cap_surface_area(R, h):
    return 2 * np.pi * R * h

def total_surface_area_of_caps(R, h, num_caps):
    return num_caps * cap_surface_area(R, h)

def optimize_cap_height(R, num_caps, tolerance=1e-6):
    h_min = 0.0
    h_max = R
    h_mid = (h_min + h_max) / 2.0
    
    while h_max - h_min > tolerance:
        h_mid = (h_min + h_max) / 2.0
        total_area = total_surface_area_of_caps(R, h_mid, num_caps)
        
        if total_area > 4 * np.pi * R * R:
            h_max = h_mid
        else:
            h_min = h_mid
    
    return h_mid

def spherical_cap_coordinates(R, num_caps):
    cap_height = optimize_cap_height(R, num_caps)
    cap_theta = np.linspace(0, 2 * np.pi, num_caps, endpoint=False)
    cap_phi = np.arccos(cap_height / R)

    cap_centers_x = R * np.sin(cap_phi) * np.cos(cap_theta)
    cap_centers_y = R * np.sin(cap_phi) * np.sin(cap_theta)
    cap_centers_z = R * np.cos(cap_phi)

    return cap_centers_x, cap_centers_y, cap_centers_z

def plot_spherical_caps_on_sphere(R, num_caps):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    phi = np.linspace(0, np.pi, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    phi, theta = np.meshgrid(phi, theta)

    x = R * np.sin(phi) * np.cos(theta)
    y = R * np.sin(phi) * np.sin(theta)
    z = R * np.cos(phi)

    cap_centers_x, cap_centers_y, cap_centers_z = spherical_cap_coordinates(R, num_caps)

    for i in range(num_caps):
        ax.plot_surface(x + cap_centers_x[i], y + cap_centers_y[i], z + cap_centers_z[i], color='b', alpha=0.4)

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

