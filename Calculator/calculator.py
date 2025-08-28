def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b

OPERATORS = {"+": add, "-": subtract, "*": multiply, "/": divide}

def apply(op, n1, n2):
    func = OPERATORS.get(op)
    if not func:
        raise ValueError(f"Unknown operator: {op}")
    result = func(n1, n2)
    print(f"{n1} {op} {n2} = {result}")
    return result

def run():
    running = float(input("What's the first number? "))
    while True:
        print("+\n-\n*\n/")
        op = input("Pick an operation: ").strip()
        nxt = float(input("What's the next number? "))
        running = apply(op, running, nxt)

        cont = input(f"Type 'y' to continue calculating with {running}, or 'n' to start over, or 'q' to quit: ").strip().lower()
        if cont == 'y':
            continue
        elif cont == 'n':
            return run()  # restart
        else:
            break
    print("All done.")

if __name__ == "__main__":
    run()
