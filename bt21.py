import math
import re
from sys import float_info
from typing import Generator, Optional, Callable

from PIL import Image



WHITE = (255, 255, 255)

Color = tuple[int, int, int]
Vertex = tuple[float, float, float]
Vertex2D = tuple[float, float]
Face = tuple[Vertex, Vertex, Vertex]
Face2D = tuple[Vertex2D, Vertex2D, Vertex2D]
Normal = tuple[float, float, float]
Texture = tuple[float, float]
faceVert = tuple[int, Optional[int], Optional[int]]
IntFace = tuple[faceVert, faceVert, faceVert]


def div(numerator: float, denominator: float) -> float:
    if numerator == 0:
        return 0
    if denominator == 0:
        return float_info.max
    return numerator / denominator


def norm_face(f: Face) -> Vertex:
    v0, v2, v1 = f

    x0, y0, z0 = v0
    x1, y1, z1 = v1
    x2, y2, z2 = v2

    x = (y2 - y0) * (z1 - z0) - (z2 - z0) * (y1 - y0)
    y = (z2 - z0) * (x1 - x0) - (x2 - x0) * (z1 - z0)
    z = (x2 - x0) * (y1 - y0) - (y2 - y0) * (x1 - x0)

    return x, y, z
    
def vec_norm(v: Vertex) -> float:
    x, y, z = v
    return math.sqrt(x * x + y * y + z * z)


def angle_face(f: Face) -> float:
    v = norm_face(f)
    return cos_v(v)


def cos_v(v: Vertex) -> float:
    norm = vec_norm(v)
    return div(v[2], norm)