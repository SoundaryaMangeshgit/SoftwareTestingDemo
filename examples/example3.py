def if_triangle(a: int, b: int, c: int) -> int:
    if a + b > c:
        return True
    if b + c > a:
        return True

    if c + a > b:
        return True
    else:
        return False
