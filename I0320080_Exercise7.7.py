def panggil(func):
    return func


def helloworld():
    return "HELLO WORLD"


def main():
    daftarnama = ["Adi, Cahyo, budi, Dedi"]
    print("Keadaan awal")
    print(daftarnama)

    print("\nMenggunakan sorted():")
    print(sorted(daftarnama))

    daftarnama.sort(key=lambda n: n.lower())

    print("\nKeadaan akhir:")
    print(daftarnama)


if __name__ == "__main__":
    main()