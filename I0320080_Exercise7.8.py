import sys


def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)


def main():
    bil = int(input("Masukkan bilangan= "))

    if bil < 0:
        print("ERROR")
        sys.exit(1)

    print("%d! = %d" % (bil, faktorial(bil)))


if __name__ == "__main__":
    main()