#!/usr/bin/env python


def problem():
    """
    问题：
    
    把一个包含N个元素的元组或序列，分解为N个单独的变量
    """
    pass


def solution():
    """
    解决方案：

    任何序列（或可迭代的对象）都可以通过一个简单的赋值操作来分解为单独的变量。
    唯一的要求是变量的总数和结构要与序列相吻合。
    """
    case1()
    case2()
    case3()
    case4()


def case1():
    """
    case1:

    >>> p = (4, 5)
    >>> x, y = p
    >>> x
    4
    >>> y
    5
    """
    p = (4, 5)
    x, y = p
    print(x)
    print(y)


def case2():
    """
    case2:
    

    >>> data = ['ACME', 50, 91.1, (2012, 12, 21)]
    >>> name, shares, price, date = data
    >>> name
    'ACME'
    >>> date
    (2012, 12, 21)
    >>> name, shares, price, (year, month, day) = data 
    >>> year
    2012
    >>> day
    21
    """
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print(name)
    print(date)

    name, shares, price, (year, month, day) = data
    print(year)
    print(month)
    print(day)


def case3():
    """
    case3: 分解可迭代的对象

    
    >>> s = 'Hello'
    >>> a, b, c, d, e = s
    >>> a
    'H'
    >>> e
    'o'
    """
    s = 'Hello'
    a, b, c, d, e = s
    print(a)
    print(e)


def case4():
    """
    case4: 选一个用不到的变量名，可以丢弃某些值

     
    >>> data = ['ACME', 50, 91.1, (2012, 12, 21)]
    >>> _, shares, price, _ = data
    >>> shares
    50
    >>> price
    91.1
    """
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    _, shares, price, _ = data
    print(shares)
    print(price)


def print_doc():
    print(problem.__doc__)
    print(solution.__doc__)
    print(case1.__doc__)
    print(case2.__doc__)
    print(case3.__doc__)
    print(case4.__doc__)


if __name__ == '__main__':
    print_doc()
    # solution()

