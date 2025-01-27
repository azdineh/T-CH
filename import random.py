import random

def generateRandomNumber(numbers_of_digits=4):
    digits = list(range(1,10))
    random.shuffle(digits)
    return digits[:4]

def get_bulls_and_cows(secret_code, guess):
    bulls = sum(s == g for s, g in zip(secret_code, guess))
    cows = sum(min(secret_code.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def main():
    secret_code = generateRandomNumber()
    attempts = 0

    print("Bienvenue au jeu de Chevaux et Taureaux!")
    print("Essayez de deviner le code secret de 4 chiffres.")

    while True:
        guess = input("Entrez votre supposition: ")
        if len(guess) != 4 or not guess.isdigit():
            print("Veuillez entrer exactement 4 chiffres.")
            continue

        guess = [int(d) for d in guess]
        attempts += 1

        bulls, cows = get_bulls_and_cows(secret_code, guess)
        print(f"Bulls: {bulls}, Cows: {cows}")

        if bulls == 4:
            print(f"Félicitations! Vous avez deviné le code en {attempts} tentatives.")
            break

if __name__ == "__main__":
    main()