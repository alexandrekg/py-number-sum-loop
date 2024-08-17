
def main():
    result = 0
    number = 0
    while number >= 0:
        number = int(input('Digite um número positivo: '))
        result += number

    print(f'A soma total dos números digitados é: {result}')


main()