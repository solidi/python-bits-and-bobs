import attr


@attr.s
class C:
    a = attr.ib()


@attr.s
class D:
    a = attr.ib()
    b = attr.ib()
    c = attr.ib()
    d = attr.ib()


b = D(1, 2, 3, 4)
print(b.a)


@attr.s
class Empty(object):
    pass


print(Empty())
print(Empty() == Empty())
print(Empty() is Empty())
