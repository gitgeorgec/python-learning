class A:
    def do_shomthing(self):
        print("Method Defined In: A")
class B(A):
    def do_shomthing(self):
        print("Method Defined In: `B")
class C(A):
    def do_shomthing(self):
        print("Method Defined In: C")
class D(B,C):
    def do_shomthing(self):
        print("Method Defined In: D")

# print(D.__mro__)
# print(D.mro())
help(D)