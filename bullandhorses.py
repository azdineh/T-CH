import random

def generate_secret_number():
    """Génère un nombre secret à quatre chiffres sans répétition."""
    digits = random.sample(range(10), 4)
    return ''.join(map(str, digits))

def get_feedback(secret, guess):
    """Renvoie le nombre de taureaux et de chevaux."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(x), guess.count(x)) for x in set(guess)) - bulls
    return bulls, cows

def play_game():
    """Joue une partie du jeu de taureaux et chevaux."""
    secret_number = generate_secret_number()
    attempts = 0

    print("Bienvenue dans le jeu de Taureaux et Chevaux!")
    print("Devinez un nombre à 4 chiffres sans chiffres répétés.")

    while True:
        guess = input("Entrez votre proposition (4 chiffres) : ")

        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Veuillez entrer un nombre valide à 4 chiffres sans répétition.")
            continue

        attempts += 1
        bulls, cows = get_feedback(secret_number, guess)

        if bulls == 4:
            print(f"Félicitations! Vous avez deviné le nombre {secret_number} en {attempts} tentatives.")
            break
        else:
            print(f"{bulls} taureau(x) et {cows} cheval(aux).")

if __name__ == "__main__":
    play_game()