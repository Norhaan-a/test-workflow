# pip install pytest
# run tests with command "pytest"

# function to test
def inc(x):
    return x + 1

# run test
def test_inc():
    assert inc(3) == 4

