from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), 不要用 abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = _____
    else:
        f = _____
    return f(a, b)

def a_plus_abs_b_syntax_check():
    """检查您是否更改了 a_plus_abs_b 函数的返回语句
    >>> # 您不需要理解此测试代码。
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    # 你不需要编辑此函数。它只是用于检查你的函数是否正确



def two_of_three(i, j, k):
    """返回 m*m + n*n 的结果，其中 m 和 n 是正数 i、j 和 k 中最小的两个数。

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return _____

def two_of_three_syntax_check():
    """请检查你的 two_of_three 代码是否只包含一个返回语句

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.


def largest_factor(n):
    """返回小于 n 的最大因数

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"


def hailstone(n):
    """打印从 n 开始的序列并返回它

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"

