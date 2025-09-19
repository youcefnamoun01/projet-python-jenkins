from app.main import dire_bonjour, addition, afficher_liste

def test_dire_bonjour():
    assert dire_bonjour("Alice") == "Bonjour, Alice !"

def test_addition():
    assert addition(3, 7) == 10
    assert addition(-2, 5) == 3

def test_afficher_liste():
    result = afficher_liste(["pomme", "banane"])
    assert result == "- pomme\n- banane"