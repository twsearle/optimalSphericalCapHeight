import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from optimalSphericalCapHeight import optimize_cap_height

def spherical_cap_coordinates(R, num_caps):
    if num_caps not in [4, 6, 8, 12]:
        raise ValueError("Number of caps must be 4, 6, 8, or 12.")

    cap_centers = []

    if num_caps == 4:  # Tetrahedron
        vertices = np.array([
            [1.0, 1.0, 1.0],
            [-1.0, -1.0, 1.0],
            [-1.0, 1.0, -1.0],
            [1.0, -1.0, -1.0]
        ])
    elif num_caps == 6:  # Octahedron
        vertices = np.array([
            [0.0, 1.0, 0.0],
            [0.0, -1.0, 0.0],
            [1.0, 0.0, 0.0],
            [-1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0],
            [0.0, 0.0, -1.0]
        ])
    elif num_caps == 8:  # Cube
        vertices = np.array([
            [1.0, 1.0, 1.0],
            [-1.0, -1.0, 1.0],
            [-1.0, 1.0, -1.0],
            [1.0, -1.0, -1.0],
            [1.0, 1.0, -1.0],
            [-1.0, -1.0, -1.0],
            [-1.0, 1.0, 1.0],
            [1.0, -1.0, 1.0]
        ])
    elif num_caps == 12:  # Icosahedron
        phi = (1 + np.sqrt(5)) / 2  # Golden ratio

        vertices = np.array([
            [0, 1, phi],
            [0, -1, phi],
            [0, 1, -phi],
            [0, -1, -phi],
            [1, phi, 0],
            [-1, phi, 0],
            [1, -phi, 0],
            [-1, -phi, 0],
            [phi, 0, 1],
            [-phi, 0, 1],
            [phi, 0, -1],
            [-phi, 0, -1]
        ])

    for vertex in vertices:
        vertex = vertex / np.linalg.norm(vertex)
        cap_centers.append(R * vertex)

    return np.array(cap_centers)

def rotation_matrix_from_vectors(vec1, vec2):
    """Calculate the rotation matrix that rotates vec1 to vec2."""
    # Ensure that the vectors are unit vectors (normalized)
    vec1 = vec1 / np.linalg.norm(vec1)
    vec2 = vec2 / np.linalg.norm(vec2)

    # Calculate the cross product and the dot product
    v = np.cross(vec1, vec2)
    c = np.dot(vec1, vec2)

    # Calculate the skew-symmetric cross product matrix
    skew_sym_matrix = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])

    # Calculate the rotation matrix
    R = np.identity(3) + skew_sym_matrix + np.dot(skew_sym_matrix, skew_sym_matrix) * (1 / (1 + c))

    return R

def plot_spherical_caps_on_sphere(R, num_caps, vector=np.array([0, 0, 1])):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    cap_centers = spherical_cap_coordinates(R, num_caps)
    cap_height = optimize_cap_height(R, num_caps)

    for center in cap_centers:
        phi = np.linspace(0, np.pi / 2, 30)
        theta = np.linspace(0, 2 * np.pi, 30)
        phi, theta = np.meshgrid(phi, theta)

        x = R * np.sin(phi) * np.cos(theta)
        y = R * np.sin(phi) * np.sin(theta)
        z = R * np.cos(phi)

        # Calculate the rotation matrix to align the cap with the vector
        cap_normal = center / np.linalg.norm(center)
        rotation_matrix = rotation_matrix_from_vectors(cap_normal, vector)

        # Rotate the cap coordinates
        x_rot, y_rot, z_rot = np.einsum('ij,jkl->ikl', rotation_matrix, np.array([x, y, z]))

        ax.plot_surface(x_rot, y_rot, z_rot, alpha=0.2)

    ax.set_xlim([-R, R])
    ax.set_ylim([-R, R])
    ax.set_zlim([-R, R])
    ax.set_aspect('auto')
    plt.show()

def plot_half_spherical_caps(R, num_caps, vector=np.array([0, 0, 1])):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    cap_centers = spherical_cap_coordinates(R, num_caps)
    cap_height = optimize_cap_height(R, num_caps)

    for c_num in range(num_caps):
        if c_num % 2 == 0: continue
        center = cap_centers[c_num]
        phi = np.linspace(0, np.pi / 2, 30)
        theta = np.linspace(0, 2 * np.pi, 30)
        phi, theta = np.meshgrid(phi, theta)

        x = R * np.sin(phi) * np.cos(theta)
        y = R * np.sin(phi) * np.sin(theta)
        z = R * np.cos(phi)

        # Calculate the rotation matrix to align the cap with the vector
        cap_normal = center / np.linalg.norm(center)
        rotation_matrix = rotation_matrix_from_vectors(cap_normal, vector)

        # Rotate the cap coordinates
        x_rot, y_rot, z_rot = np.einsum('ij,jkl->ikl', rotation_matrix, np.array([x, y, z]))

        ax.plot_surface(x_rot, y_rot, z_rot, alpha=0.2)

    ax.set_xlim([-R, R])
    ax.set_ylim([-R, R])
    ax.set_zlim([-R, R])
    ax.set_aspect('auto')
    plt.show()



def main():
    R = 1.0  # Change the radius of the sphere here
    num_caps = 4  # Change the number of caps here

    plot_spherical_caps_on_sphere(R, num_caps)
    plot_half_spherical_caps(R, num_caps)

if __name__ == "__main__":
    main()

