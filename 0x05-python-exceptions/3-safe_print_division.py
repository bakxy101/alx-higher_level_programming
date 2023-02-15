#!/usr/bin/python3

def safe_print_division(a, b):
    div = None
    try:
        div = a / b
        return (div)
    except ZeroDivisionError:
        return None
    finally:
        print(f"Inside result: {div}")
        return None
