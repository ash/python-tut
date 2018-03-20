def fact(n):
    f = 1
    if n > 1:
        for i in range(1, n + 1):
            f *= i
    return f

def test_fact_5():
    assert fact(5) == 120

def test_fact_6():
    assert fact(6) == 120
