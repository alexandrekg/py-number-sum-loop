
def main():
    result = 0
    while True:
        user_number = int(input('Digite um número positivo: '))
        if user_number < 0:
            break

        result += user_number

    print(f'A soma total dos números digitados é: {result}')


main()