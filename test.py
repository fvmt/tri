import lxml

import pytest

from utils import check_triangle, valid_xml, parse_response
from data_gen import gen_triangle_tc

MAX_SIDE_FOR_DYNAMIC_TEST = 5
NUMBER_OF_DYNAMIC_TESTS = 1

STATIC_TEST_DATA = [
('[1,1,1]', ('True', '2')),
('[1,2,3]', ('False', '0')),
('[1,3,2]', ('False', '0')),
('[3,2,1]', ('False', '0')),
('[2,8,1]', ('False', '0')),
('[4,5,6]', ('True', '3')),
('[2,3,2]', ('True', '1')),
('[2,2,3]', ('True', '1')),
('[3,2,2]', ('True', '1')),
('[0,0,0]', ('False', '0')),
('[-1,-1,-1]', ('False', '0')),
('[-1, 1, 1]', ('False', '0')),
('[1,-1, 1]' , ('False', '0')),
('[1,1,-1]', ('False', '0')),
('[0,1,1]', ('False', '0')),
('[1,0,1]', ('False', '0')),
('[1,1,0]', ('False', '0')),
('[1.5,2.5,4.5]', ('False', '0')),
('[1.5,1.5,1.5]', ('True', '2')),
('[1.5,1.5,1.2]', ('True', '1')),
('[1.5,2.5,3.5]', ('True', '3')),
('[-1.5, -1.5, -1.5]', ('False', '0')),
('[-1.5, 1.5, 2]', ('False', '0')),
('[0, 1.5, 1.5]', ('False', '0')),
('1,2,2', ('False', '0')),
('[a, 1, 2]', ('False', '0')),
('[1, 2, a]', ('False', '0')),
('[1, a ,2]', ('False', '0')),
('[1j,2,3]', ('False', '0')),
('[1j,1j,1j]', ('False', '0')),
]


@pytest.mark.parametrize(('sides', 'expected_result'), STATIC_TEST_DATA)
def test_triangles_static(sides, expected_result):

    main_scenario(sides, expected_result)


@pytest.mark.parametrize(('sides', 'expected_result'), [gen_triangle_tc(MAX_SIDE_FOR_DYNAMIC_TEST) for i in range(NUMBER_OF_DYNAMIC_TESTS)])
def test_triangles_dynamic(sides, expected_result):

    main_scenario(sides, expected_result)


def main_scenario(sides, expected_result):

    try:
        response = check_triangle(sides)
    except:
        pytest.fail(msg="Could not connect to service. Check connectivity.", pytrace=False)

    if not valid_xml(response):
        pytest.fail(msg="Invalid XML response", pytrace=False)
            
    actual_result = parse_response(response)
    assert actual_result == expected_result



