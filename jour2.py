class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.prenom + " " + self.nom)
    
    def GetNom(self):
        return self.nom

    def GetPrenom(self):
        return self.prenom

    def SetNom(self, nom):
        self.nom = nom

    def SetPrenom(self, prenom):
        self.prenom = prenom

class Livre:
    def __init__(self ,titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def print():
        print("Le titre du livre est " + self.titre + " et à été écris par " + self.auteur)

class Auteur(Personne):
    
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvres = []
    
    def listerOeuvre(self):
        for oeuvre in self.oeuvres:
            print(oeuvre.titre)
    def ecrireUnLivre(self, titre):
        self.oeuvres.append(Livre(titre, self))

class Client(Personne):
    
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvres = []
    
    def listerOeuvre(self):
        for oeuvre in self.oeuvres:
            print(oeuvre.titre)
    def ecrireUnLivre(self, titre):
        self.oeuvres.append(Livre(titre, self))

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.oeuvres:
            if livre.titre == titre:
                if titre in self.catalogue:
                    self.catalogue[titre] += quantite
                else:
                    self.catalogue[titre] = quantite

    def inventaire(self):
        print("Inventaire du catalogue de la bibliothèque ", self.nom)
        for titre, quantite in self.catalogue.items():
            print("Titre: ", titre, " Quantité: ", quantite)

    def louer(self, client, titre):
        if titre in self.catalogue and self.catalogue[titre] > 0:
            livre = Livre(titre, None)
            client.collection.append(livre)
            self.catalogue[titre] -= 1

    def rendreLivres(self, client):
        for livre in client.collection:
            titre = livre.titre
            if titre in self.catalogue:
                self.catalogue[titre] += 1
            else:
                self.catalogue[titre] = 1
        client.collection = []

#p1 = Personne("Doe", "John")
#p2 = Personne("Doe", "Jane")
#p3 = Personne("Doe", "Jack")

#p1.SePresenter()
#p2.SePresenter()
#p3.SePresenter()

#p1.SetNom("Ruiz")
#p1.SetPrenom("Mathieu")

#p1.ecrireUnLivre("Livre 1")
#p1.ecrireUnLivre("Livre 2")
#p1.ecrireUnLivre("Livre 3")

#p1.listerOeuvre()

auteur1 = Auteur("Tolstoï", "Léon")
auteur2 = Auteur("Hugo", "Victor")

livre1 = auteur1.ecrireUnLivre("Guerre et Paix")
livre2 = auteur1.ecrireUnLivre("Anna Karénine")
livre3 = auteur2.ecrireUnLivre("Les Misérables")
livre4 = auteur2.ecrireUnLivre("Notre-Dame de Paris")

bibliotheque1 = Bibliotheque("Bibliothèque municipale")

bibliotheque1.acheterLivre(auteur1, "Guerre et Paix", 5)
bibliotheque1.acheterLivre(auteur1, "Anna Karénine", 3)

print("Inventaire de", bibliotheque1.nom , ":" , bibliotheque1.inventaire()) 



    