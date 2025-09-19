def dire_bonjour(nom: str):
    return f"Bonjour, {nom} !"

def addition(a: int, b: int) -> int:
    return a + b

def afficher_liste(liste):
    return "\n".join([f"- {e}" for e in liste])

if __name__ == "__main__":
    print(dire_bonjour("Youcef"))
    print(f"La somme de 3 et 7 est {addition(3,7)}")
    print(afficher_liste(["pomme","banane","orange"]))