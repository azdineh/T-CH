import random

def generateRandomNumber(numbers_of_digits=4):
    if numbers_of_digits > 10:
        raise ValueError("Le nombre de chiffres ne peut pas dépasser 10 car il n'y a que 10 chiffres uniques.")
    
    # Générer la liste des chiffres possibles
    digits = list(range(1, 10))  # Chiffres de 1 à 9 pour le premier chiffre
    first_digit = random.choice(digits)  # Sélectionner le premier chiffre
    
    digits = list(range(0, 10))  # Chiffres de 0 à 9 pour les autres chiffres
    digits.remove(first_digit)  # Retirer le premier chiffre pour éviter les doublons
    
    # Générer les chiffres restants
    remaining_digits = random.sample(digits, numbers_of_digits - 1)
    
    # Combiner le premier chiffre et les chiffres restants
    random_number = [first_digit] + remaining_digits
    
    # Convertir la liste en une chaîne ou un entier
    return int("".join(map(str, random_number)))

# Exemple d'utilisation
print(generateRandomNumber())  # Par exemple : 1938
