import math

def spherical_cap_surface_area(R, h):
    return 2 * math.pi * R * h

def total_surface_area_of_caps(R, h, num_caps):
    return num_caps * spherical_cap_surface_area(R, h)

def optimize_cap_height(R, num_caps, tolerance=1e-6):
    h_min = 0.0
    h_max = R
    h_mid = (h_min + h_max) / 2.0

    while h_max - h_min > tolerance:
        h_mid = (h_min + h_max) / 2.0
        total_area = total_surface_area_of_caps(R, h_mid, num_caps)

        if total_area > 4 * math.pi * R * R:
            h_max = h_mid
        else:
            h_min = h_mid

    return h_mid

def phi_from_height(h, R):
    return 2* math.asin(h / (2*R))

def arc_length_from_phi(phi, R):
    return 2 * math.pi * R * math.sin(phi)

def main():
    R = 1.0  # You can change the radius of the sphere here

    num_caps_list = [2, 4, 6, 8, 12, 20]

    print(f"For a sphere with radius R = {R}:")
    for num_caps in num_caps_list:
        cap_height = optimize_cap_height(R, num_caps)
        phi = phi_from_height(cap_height, R)
        arc_length = arc_length_from_phi(phi, R)
        print(f"Number of Caps: {num_caps}, Optimal Cap Height Fraction: {cap_height:.6f}"
              f", phi: {math.degrees(phi):.6f}, L: {arc_length:.6f}")

if __name__ == "__main__":
    main()

