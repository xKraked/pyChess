from pieces import *
from config import *

class Echiquier:
    def __init__(self):
        
        Cn = Cavalier('noir')
        Cb = Cavalier('blanc')
        Fn = Fou('noir')
        Fb = Fou('blanc')
        Tn = Tour('noir')
        Tb = Tour('blanc')
        Dn = Dame('noir')
        Db = Dame('blanc')
        Rn = Roi('noir')
        Rb = Roi('blanc')
        Pn = Pion('noir')
        Pb = Pion('blanc')
        O = Vide()

                       
        self.tab = [[Tb,Cb,Fb,Db,Rb,Fb,Cb,Tb],
                    [Pb,Pb,Pb,Pb,Pb,Pb,Pb,Pb],
                    [O ,O ,O ,O ,O ,O ,O ,O ],
                    [O ,O ,O ,O ,O ,O ,O ,O ],
                    [O ,O ,O ,O ,O ,O ,O ,O ],
                    [O ,O ,O ,O ,O ,O ,O ,O ],
                    [Pn,Pn,Pn,Pn,Pn,Pn,Pn,Pn],
                    [Tn,Cn,Fn,Dn,Rn,Fn,Cn,Tn]]
    
    def __repr__(self):
        return str(self.tab[7])+'\n'+str(self.tab[6])+'\n'+str(self.tab[5])+'\n'+str(self.tab[4])+'\n'+str(self.tab[3])+'\n'+str(self.tab[2])+'\n'+str(self.tab[1])+'\n'+str(self.tab[0])+'\n'
        
    #Cette fonction transforme une position sur l'écran (en pixels) en position sur l'échiquier
    def transfertCoordonnees(self, pos = ()):
    
        x = pos[0]
        y = pos[1]

        i = int(x/TAILLE_CASE)
        j = 7-int((y - ORIGINE_Y)/TAILLE_CASE)

        return (i,j)
    
    #Cette fonction permet de déplacer une pièce dans l'échiquier
    def deplacerPiece(self, pos_i = (), pos_f = ()):
           
        x = pos_i[0]
        y = pos_i[1]
        xf = pos_f[0]
        yf = pos_f[1]
        
        self.tab[yf][xf] = self.tab[y][x]
        self.tab[y][x] = Vide()
    
    #Cette fonction retourne la liste des mouvements (x,y) possibles grâce à la fonction libertes de chaque pièce
    def mouvPossibles(self, pos=()):
       
        x = pos[0]
        y = pos[1]
        piece = self.tab[y][x]

        #La classe Vide ne possède pas de libertes : on retourne une liste vide
        if piece.estPiece():
            return piece.libertes(pos, self.tab)
        else:
            return []
    
