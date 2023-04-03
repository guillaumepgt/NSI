#
# Chapitre 8 - Activité 2 - Réseau social simple
#

class Personne:
    def __init__(self, nom, annee_naissance):
        self.nom = nom
        self.annee_naissance = annee_naissance
        self.relations = {}  # clés : noms, valeurs : année de début de la relation

    def __repr__(self):
        """ La fonction appelée par `print` """
        texte = f"Personne '{self.nom}' née en {self.annee_naissance}"
        if len(self.relations) > 0:
            texte += ", connait :"
            for nom, annee in self.relations.items():
                texte += f"\n    • {nom} depuis {annee}"
        return texte


donnees_personnes = {"Rafael": 1994, "Stéphanie": 1980, "Dinesh": 1980,
                     "Margot": 1987, "Sofiane": 1985, "Lucia": 1988,
                     "Antti": 1979, "Johanna": 1980, "Ahmed": 1986,
                     "Didier": 1971, "Chimène": 1984, "Marc": 1980,
                     "Charles": 1991, "Antoine": 1991, "Maurice": 1992,
                     "Samuli": 1989, "Marlène": 1980, "Carl": 1986}

exemple_reseau = {nom: Personne(nom, annee)
                  for nom, annee in donnees_personnes.items()}

donnees_liens = {('Rafael', 'Margot'): 2021,
                 ('Dinesh', 'Antti'): 1998,
                 ('Margot', 'Lucia'): 2022,
                 ('Margot', 'Ahmed'): 2004,
                 ('Margot', 'Didier'): 2011,
                 ('Antti', 'Samuli'): 1999,
                 ('Chimène', 'Carl'): 2011,
                 ('Charles', 'Antoine'): 2021,
                 ('Samuli', 'Marlène'): 2020,
                 ('Stéphanie', 'Dinesh'): 2003,
                 ('Margot', 'Sofiane'): 2020,
                 ('Margot', 'Johanna'): 2021,
                 ('Margot', 'Charles'): 2021,
                 ('Ahmed', 'Maurice'): 2008,
                 ('Didier', 'Charles'): 2004,
                 ('Marc', 'Chimène'): 2000,
                 ('Chimène', 'Marlène'): 1992,
                 ('Antoine', 'Maurice'): 1999,
                 ('Marlène', 'Carl'): 2010,
                 }

for lien, annee in donnees_liens.items():
    nom1 = lien[0]
    nom2 = lien[1]
    p1 = exemple_reseau[nom1]
    p2 = exemple_reseau[nom2]
    if (nom1 in p2.relations) or (nom2 in p1.relations):
        print(f"/!\\ Attention, la relation {nom1} - {nom2} existe déjà !")
    if (annee < p1.annee_naissance):
        raise ValueError(
            f"L'année de relation {annee} est antérieure à la naissance de {nom1} ({p1.annee_naissance}) !")
    if (annee < p2.annee_naissance):
        raise ValueError(
            f"L'année de relation {annee} est antérieure à la naissance de {nom2} ({p2.annee_naissance}) !")
    p1.relations[nom2] = annee
    p2.relations[nom1] = annee


def duree_relation(personne1, personne2):
    for lien, annee in donnees_liens.items():
        nom1 = lien[0]
        nom2 = lien[1]
        if nom1 == personne1 and nom2 == personne2:
            return 2023 - annee
    return None


# print(duree_relation("Margot", "Charles"))

def relation_ancienne():
    plus_ancienne, relation = 2023, str
    for lien, annee in donnees_liens.items():
        if annee <= plus_ancienne:
            plus_ancienne = annee
            relation = lien
    return (relation, 2023 - plus_ancienne)


# print(relation_ancienne())

def plus_de_relation():
    relation, plus_ancienne, personne = {}, 0, str
    for lien, annee in donnees_liens.items():
        if lien[0] in relation:
            relation[lien[0]] += 1
        if lien[1] in relation:
            relation[lien[1]] += 1
        if lien[0] not in relation:
            relation[lien[0]] = 1
        if lien[1] not in relation:
            relation[lien[1]] = 1
    for lien, annee in relation.items():
        if annee >= plus_ancienne:
            plus_ancienne = annee
            personne = lien
    return personne, plus_ancienne


print(plus_de_relation())


def un():
    relation, personne = {}, []
    for lien, annee in donnees_liens.items():
        if lien[0] in relation:
            relation[lien[0]] += 1
        if lien[1] in relation:
            relation[lien[1]] += 1
        if lien[0] not in relation:
            relation[lien[0]] = 1
        if lien[1] not in relation:
            relation[lien[1]] = 1
    for lien, annee in relation.items():
        if annee >= 3:
            personne.append(lien)
    relation = {}
    for i in personne:
        for lien, annee in donnees_liens.items():
            if donnees_liens[i] == lien[0] or donnees_liens[i] == lien[1]:
                if donnees_liens[i] in relation:
                    relation[lien[0]] += 1
                if donnees_liens[i] not in relation:
                    relation[lien[0]] = 1
    personne = []
    for lien, annee in relation.items():
        if annee >= 2:
            personne.append(lien)
    relation = {}
    for i in personne:
        for lien, annee in donnees_personnes.items():
            if donnees_liens[i] in relation:
                relation[donnees_liens[i]] += annee
            if donnees_liens[i] not in relation:
                relation[donnees_liens[i]] = annee
    for lien, annee in relation.items():
        if annee / len(relation) > donnees_personnes[lien]:
            print(lien)


print(un())
