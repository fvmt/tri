import random


def gen_triangle_tc(max_side):

    a, b, c = [random.randint(-max_side, max_side) for _ in range(3)]
    payload_style = str([a, b, c]).replace(" ", "")
    return payload_style, get_expected_result((a,b,c))


def get_expected_result(sides):

    a, b, c = sides
    is_triangle = a + b > c and a + c > b and c + b > a
    is_isosceles = a == b or b == c or a == c
    is_equilateral = a == b and b == c
    if is_triangle:
        tri_type = 3
    if is_isosceles:
        tri_type = 1
    if is_equilateral:
        tri_type = 2
    if not is_triangle:
        tri_type = 0

    return str(is_triangle), str(tri_type)

    


