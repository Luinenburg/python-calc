from main import *

def test_process_operation():
    for a in range(0, 100):
        for b in range(0, 100):
            assert process_operation(a, "+", b) == a+b
            if (b != 0): assert process_operation(a, "/", b) == a/b
            assert process_operation(a, "*", b) == a*b
            assert process_operation(a, "-", b) == a-b

def main():
    test_process_operation()

if __name__=="__main__":
    main()
