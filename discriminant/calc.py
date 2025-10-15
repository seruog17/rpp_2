from typing import Tuple


def discriminant(a: float, b: float, c: float) -> float:
    """
    Вычисляет дискриминант D = b^2 - 4ac
    """
    return b * b - 4 * a * c


def roots_info(a: float, b: float, c: float) -> Tuple[str, float]:
    """
    Возвращает кортеж: (тип_корней, D)
    тип: "two" (D>0), "one" (D==0), "complex" (D<0)
    """
    d = discriminant(a, b, c)
    if d > 0:
        return "two", d
    if d == 0:
        return "one", d
    return "complex", d
