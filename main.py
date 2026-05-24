#README.md 를 먼저 보고 시작할것

# x,y,z 값을 포함한 클래스
class Vector3:
    x : float = 0
    y : float = 0
    z : float = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # 클래스를 str 로 변환할 때 반환할 값
    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    # 덧셈 예제
    def __add__(self, other):
        if isinstance(other, Vector3):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z

            return Vector3(x,y,z)

        else:
            raise TypeError(f"TypeError: unsupported operand type(s) for +: 'Vector3' and {type(other).__name__}")

    #TODO Vector3 클래스끼리 사칙연산이 가능하게 하고 연산할 때 잘못된 값이 오면 오류를 내뱉기
    # tip : 사칙연산 등을 할 때 클래스를 새로 만들어서 반환함
    # .
    # [덧셈] [이미 구현함]
    # Vector3(31.4, 0.3, 21.7) + Vector3(0, 32, 1.4) == Vector3(31.4, 32.3, 23.1)
    # .
    # [뺄셈]
    # Vector3(31.4, 0.3, 21.7) - Vector3(0, 32, 1.4) == Vector3(31.4, -31.7, 20.3)
    # .
    # [곱셈]
    # Vector3(2, 4, 6) * Vector3(3, 5, 7) == Vector3(6, 20, 42)
    # .
    # [나눗셈]
    # Vector3(30, 20, 10) / Vector3(5, 4, 2) == Vector3(6, 5, 5)
    # .
    # [나머지(mod)]
    # Vector3(31, 65, 100) % Vector3(10, 32, 9) == Vector3(1, 1, 1)

# 실행 시작

# tip : print를 할 때 str이 아닌 것은 자동으로 str로 변환함
print(Vector3(0, -1.3, 4) + Vector3(2, 3, 6))
print(Vector3(10, 5.5, -2) - Vector3(3, 1.5, 7))
print(Vector3(2, -4, 1.5) * Vector3(3, 0.5, -2))
print(Vector3(20, -9, 15) / Vector3(5, 3, -5))
print(Vector3(31, 65, 100) % Vector3(10, 32, 9))