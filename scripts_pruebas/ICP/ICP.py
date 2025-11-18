import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import KDTree

def transform_matrix_2d(tx, ty, r, degrees=True):
    """
    Build a 3x3 homogeneous transformation matrix for 2D transformations.

    Parameters
    ----------
    tx, ty : float
        Translation along x and y.
    r : float
        Rotation about the z-axis (in degrees or radians).
    degrees : bool, optional
        If True (default), r is in degrees. If False, it is in radians.

    Returns
    -------
    T : (3,3) ndarray
        Homogeneous transformation matrix:
            [ cos(r) -sin(r)  tx ]
            [ sin(r)  cos(r)  ty ]
            [   0       0      1 ]
    """
    if degrees:
        r = np.deg2rad(r)

    c, s = np.cos(r), np.sin(r)
    T = np.array([[c, -s, tx],
                  [s,  c, ty],
                  [0,  0,  1]])
    return T


def transform_points(A, T):
    n = A.shape[0]
    ones = np.ones((n, 1))
    A_hom = np.hstack([A, ones])            # (n, 3)
    A_transformed = (T @ A_hom.T).T         # (n, 3)
    return A_transformed[:, :2]  


x = np.linspace(1, 10, 20)
y = 1/x*np.sin(x)+10

ref = np.column_stack((x, y))

np.random.seed(0)

points_to_align = ref.copy()
points_to_align[:,1] = points_to_align[:,1] + np.random.normal(0, .05, size=points_to_align[:,1].shape)


T = transform_matrix_2d(5, 5, 45, degrees=True)

transformed_poins = transform_points(points_to_align, T)


f, ax = plt.subplots()
ax.plot(ref[:,0], ref[:,1], '-o')
ax.plot(points_to_align[:,0], points_to_align[:,1], '-o')
ax.plot(transformed_poins[:,0], transformed_poins[:,1], '-o')

ax.set_aspect('equal')

plt.show()






tree = KDTree(transformed_poins)
distances, indices = tree.query(ref)



f, ax = plt.subplots()

ax.plot(ref[:,0], ref[:,1], '-o')
ax.plot(transformed_poins[:,0], transformed_poins[:,1], '-o')

for i, idx in enumerate(indices):
    plt.plot([transformed_poins[i, 0], ref[idx, 0]], [transformed_poins[i, 1], ref[idx, 1]], 'k', alpha=0.2)

ax.set_aspect('equal')
plt.show()