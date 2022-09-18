import threading
import random


alreadyTested = []
passedNumbers = []
failedNumbers = []


def calculate(x):
    res1 = (2/x) * (x*x)  # 2/x is rounded down so it fails sometimes
    res2 = 2*x
    if res1 == res2: passedNumbers.append([x, res1, res2])
    else: failedNumbers.append([x, res1, res2])


def main():
    for i in range(1000000):
        x = random.randint(1, 1000)
        if x not in alreadyTested:
            alreadyTested.append(x)
            threading.Thread(target=calculate, args=(x,)).start()
    dir = "(2divX)mul(XmulX) same as 2x Test"
    with open(f"{dir}/passedNumbers.txt", "w") as f: f.write(str(passedNumbers))
    with open(f"{dir}/failedNumbers.txt", "w") as f: f.write(str(failedNumbers))


if __name__ == '__main__':
    main()
