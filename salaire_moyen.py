def salaire_moyen_condition(employes, champ, valeur):
    liste_salaire = []
    for i in range(len(employes)):
        if employes[i][champ] == valeur:
            liste_salaire.append(employes[i][salaire])
    salaire_moyen = sum(liste_salaire)/len(liste_salaire)
    return salaire_moyen

employes = [
{'experience': 5, 'etudes': 3, 'sexe': 'F', 'salaire': 2400},
{'experience': 3, 'etudes': 3, 'sexe': 'M', 'salaire': 2550},
{'experience': 5, 'etudes': 5, 'sexe': 'F', 'salaire': 2500},
{'experience': 3, 'etudes': 5, 'sexe': 'M', 'salaire': 2800},
{'experience': 2, 'etudes': 5, 'sexe': 'F', 'salaire': 2300},
{'experience': 2, 'etudes': 3, 'sexe': 'M', 'salaire': 2700}
]