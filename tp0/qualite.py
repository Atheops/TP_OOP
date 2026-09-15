#d n'est pas utilisé
#f n'est pas explicite
#les coefficients sont des valeurs magiques

def cout_deplacement(x_depart, y_depart, x_arrivee, y_arrivee, terrain):

    distance = ((x_arrivee - x_depart) ** 2 +
                (y_arrivee - y_depart) ** 2) ** 0.5

    cout_route = 1.0
    cout_herbe = 1.5
    cout_sable = 2.0
    cout_autre = 3.0

    if terrain == "R":
        coefficient = cout_route
    elif terrain == "H":
        coefficient = cout_herbe
    elif terrain == "S":
        coefficient = cout_sable
    else:
        coefficient = cout_autre

    return distance * coefficient
