#!/usr/bin/env python


def problem():
    """
    问题：
    
    从某个可迭代对象中分解出N个元素，当这个可迭代对象的长度超过N时，会出现“分解的值过多（too many values to unpack）的异常”
    """
    pass


def solution():
    """
    解决方案：

    可以用“*表达式”来解决这个问题。
    """
    case1()
    case2()
    case3()
    case4()


def case1():
    """
    case1: 元组处理，drop first and last

    >>> a = (1, 2, 3, 4, 5, 6, 7)
    >>> first, *middle, last = a
    >>> middle
    [2, 3, 4, 5, 6]
    """
    a = (1, 2, 3, 4, 5, 6, 7)
    first, *middle, last = a
    print(middle)


def case2():
    """
    case2: 列表处理

    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> first, *middle, last = a
    >>> middle
    [2, 3, 4, 5, 6]
    """
    a = [1, 2, 3, 4, 5, 6, 7]
    first, *middle, last = a
    print(middle)


def case3():
    """
    case3: 字符串处理
    
    >>> line = 'nobody:*:-2:-2:Inprivileged User:/var/empty:/usr/bin/false'
    >>> uname, *fields, homedir, sh = line.split(':')
    >>> uname
    'nobody'
    >>> homedir
    '/var/empty'
    >>> sh
    '/usr/bin/false'
    """
    line = 'nobody:*:-2:-2:Inprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(':')
    print(uname)
    print(homedir)
    print(sh)


def case4():
    """
    case4: 丢弃一些分解元素

    >>> record = ('ACME', 50, 123.45, (12, 18, 2012))
    >>> name, *_, (*_, year) = record
    >>> name
    'ACME'
    >>> year
    2012
    """
    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record
    print(name)
    print(year)


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

