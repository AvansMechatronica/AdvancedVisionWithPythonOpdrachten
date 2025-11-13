"""
camera_optics_calculator.py

Calculator for basic camera optics quantities.
Units: millimeters (mm) for distances; nanometers (nm) for wavelength when needed.
"""

import math

def image_distance(f, s):
    denom = (1.0 / f) - (1.0 / s)
    if abs(denom) < 1e-12:
        return float('inf')
    return 1.0 / denom

def magnification(s_prime, s):
    return s_prime / s

def fov_deg(f, sensor_dim):
    return 2.0 * math.degrees(math.atan(sensor_dim / (2.0 * f)))

def diagonal(w, h):
    return math.sqrt(w*w + h*h)

def hyperfocal(f, N, c):
    return (f*f) / (N * c) + f

def dof_near_far(s, f, N, c):
    H = hyperfocal(f, N, c)
    near = (H * s) / (H + (s - f))
    denom_far = (H - (s - f))
    if denom_far <= 0:
        far = float('inf')
    else:
        far = (H * s) / denom_far
    dof = None if math.isinf(far) else (far - near)
    return H, near, far, dof

def airy_disk_diameter_mm(wavelength_nm, N):
    lam_mm = wavelength_nm * 1e-6
    return 2.44 * lam_mm * N

def airy_disk_in_pixels(airy_mm, pixel_size_mm):
    if pixel_size_mm <= 0:
        return float('nan')
    return airy_mm / pixel_size_mm

def aperture_diameter(f, N):
    return f / N

def example():
    f = 25.0
    sensor_w = 6.4
    sensor_h = 4.8
    s = 500.0
    N = 4.0
    c = 0.02
    wavelength_nm = 550.0
    pixel_size_mm = 0.0022

    s_prime = image_distance(f, s)
    M = magnification(s_prime, s)
    fov_h = fov_deg(f, sensor_w)
    fov_v = fov_deg(f, sensor_h)
    fov_d = fov_deg(f, diagonal(sensor_w, sensor_h))
    H, near, far, dof = dof_near_far(s, f, N, c)
    airy_mm = airy_disk_diameter_mm(wavelength_nm, N)
    airy_px = airy_disk_in_pixels(airy_mm, pixel_size_mm)

    out = {
        's_prime_mm': s_prime,
        'M': M,
        'fov_h_deg': fov_h,
        'fov_v_deg': fov_v,
        'fov_d_deg': fov_d,
        'H_mm': H,
        'near_mm': near,
        'far_mm': far,
        'DOF_mm': dof,
        'airy_mm': airy_mm,
        'airy_px': airy_px
    }
    return out

if __name__ == "__main__":
    res = example()
    for k,v in res.items():
        print(f"{k}: {v}")


# --- Additional functions for computing required sensor size / sampling ---
def required_magnification_for_resolution(h_obj, pixels_per_detail, pixel_size_mm):
    \"\"\"Minimum magnification M so that an object detail of size h_obj (mm) covers at least pixels_per_detail pixels on the sensor, given pixel pitch in mm.\"\"\"
    if h_obj <= 0:
        raise ValueError('h_obj must be > 0')
    return (pixels_per_detail * pixel_size_mm) / h_obj

def achievable_magnification(f, s):
    \"\"\"Magnification M = s' / s using thin-lens formula.\"\"\"
    s_prime = image_distance(f, s)
    if math.isinf(s_prime):
        return float('inf')
    return s_prime / s

def required_sensor_width_for_scene(scene_width_mm, f, s):
    \"\"\"Compute required physical sensor width (mm) so that the given scene width at object distance fits on the sensor.\n    Uses magnification M = s'/s and sensor_width = M * scene_width_mm.\"\"\"
    M = achievable_magnification(f, s)
    if math.isinf(M):
        return float('inf')
    return M * scene_width_mm

def required_sensor_pixels(sensor_width_mm, pixel_size_mm):
    if pixel_size_mm <= 0:
        return float('nan')
    return sensor_width_mm / pixel_size_mm

# Example new usage
def example_sensor_calc():
    # Given:
    f = 25.0
    s = 500.0
    scene_width = 1000.0  # mm (1 meter wide scene at that distance)
    smallest_detail = 5.0  # mm
    pixel_size = 0.0022  # mm
    pixels_per_detail = 2  # Nyquist-ish requirement

    req_M = required_magnification_for_resolution(smallest_detail, pixels_per_detail, pixel_size)
    ach_M = achievable_magnification(f, s)
    req_sensor_w = required_sensor_width_for_scene(scene_width, f, s)
    req_sensor_px = required_sensor_pixels(req_sensor_w, pixel_size)

    return {
        'required_M_for_detail': req_M,
        'achievable_M': ach_M,
        'required_sensor_width_mm_for_scene': req_sensor_w,
        'required_sensor_pixels_for_scene': req_sensor_px
    }

if __name__ == \"__main__\":
    print(\"--- previous example ---\")
    res = example()
    for k,v in res.items():
        print(f\"{k}: {v}\")
    print(\"--- sensor sizing example ---\")
    res2 = example_sensor_calc()
    for k,v in res2.items():
        print(f\"{k}: {v}\")
