import pytest

@pytest.mark.parametrize("coords, m, b", [
        ([(1,2),(4,8)], 2, 0),
        ([(3,6),(6,12)], 2, 0),                  
        ])

def test_define_line(coords, m, b):
	from xycoordinates import define_line
	result = define_line(coords)
	assert result == (m, b)

@pytest.mark.parametrize("m, b, x, y", [
        (2, 0, 10, 20),
        (2, 0, 5, 10),                  
        ])

def test_solve_y(m, b, x, y):
        from xycoordinates import solve_y
        result = solve_y(m, b, x)
        assert result == y
