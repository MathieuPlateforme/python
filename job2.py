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



    