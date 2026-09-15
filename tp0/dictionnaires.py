pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

def quantite_piece(pieces_stock,modele,piece):
  return pieces_stock[modele][piece]

assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10


def consommer_piece(pieces_stock, modele, piece, nbcons):
    pieces_stock[modele][piece] = pieces_stock[modele][piece] - nbcons

consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7

def ajouter_modele(pieces_stock, modele, moteurs, capteurs, roues): 
    pieces_stock[modele] = { "moteurs": moteurs, "capteurs": capteurs, "roues": roues }

ajouter_modele(pieces_stock, "ModeleC", moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == {"moteurs": 4, "capteurs": 10, "roues": 16}


def total_pieces(pieces_stock):

    totaux = {"moteurs": 0,"capteurs": 0,"roues": 0}

    for modele in pieces_stock:
        totaux["moteurs"] = totaux["moteurs"] + pieces_stock[modele]["moteurs"]
        totaux["capteurs"] = totaux["capteurs"] + pieces_stock[modele]["capteurs"]
        totaux["roues"] = totaux["roues"] + pieces_stock[modele]["roues"]

    return totaux

totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}

