class foo():
    def __eq__(self, other):
        return False



f = foo()
q = foo()

print(f.__eq__('4'))


print(f is q)
print(f == q)

if 'vance' in locals():
    print(True)
else:
    print(None)