from calcbsimpvol.examples.example1 import calcbsimpvol_ex1
from calcbsimpvol.examples.example2 import calcbsimpvol_ex2
from pytest import approx

from numpy import asarray, nan

expect_ex_1 = asarray([
    [nan, nan, 0.20709362, 0.21820954, 0.24188675],
    [nan, 0.22279836, 0.20240934, 0.21386148, 0.23738982],
    [nan, 0.22442837, 0.19870480, 0.21063506, 0.23450013],
    [nan, 0.22188111, 0.19564657, 0.20798285, 0.23045406]
])

expect_ex_2 = asarray([
    [nan, nan, 0.20632041, 0.21805647, 0.24672859],
    [nan, 0.22571652, 0.20213163, 0.21393441, 0.23734226],
    [0.29522239, 0.22556393, 0.19872376, 0.21099555, 0.23484719],
    [nan, 0.22188111, 0.19564657, 0.20794493, 0.23099783]
])

MOE = 1/100000


def test_example_1():
    assert approx(calcbsimpvol_ex1(), abs=MOE, nan_ok=True, ) == expect_ex_1


def test_example_2():
    assert approx(calcbsimpvol_ex2(), abs=MOE, nan_ok=True, ) == expect_ex_2
