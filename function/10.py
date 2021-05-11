def say_hi(name):
    print("Привет,", name)

def exchange(rate, money):
    result = money/rate
    return result

def main():
    say_hi("Аяна")
    rate = 100
    money = 3000
    a = exchange(rate, money)
    print("К выдаче", a, "тенге")

main()