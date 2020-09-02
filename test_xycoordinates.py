import pytest

@pytest.mark.parameteriza("xloc, yloc", [
        (1,2),
        (3,4),
        ])

def test_xycoordinates(xloc, yloc):
	from xycoordinates import on_line
	answer = on_line(xloc)
	assert result == expected
