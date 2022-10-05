

def calc_tax(bill, tax):
    return round((bill * tax)/100.00,2)

print(calc_tax(177.00,24))
print(calc_tax(122.00,17))

# Scope === === === #
# Built-in
# Global
# Enclosing
# Local

global_v = 'global'

def fn1():
    enclosed_v = 'enclosed'
    def fn2():
        local_v = 'local'
        print('access to: ', global_v)
        print('access to: ', enclosed_v)
        print('access to: ', local_v)
    fn2()
fn1()


