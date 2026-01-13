hdoeuvre(salade).
hdoeuvre(pate).
plat(sole).
plat(thon).
plat(porc).
plat(boeuf).
dessert(glace).
dessert(fruit).

point(salade, 1).
point(pate, 6).
point(sole, 2).
point(thon, 4).
point(porc, 7).
point(boeuf, 3).
point(glace, 5).
point(fruit, 1).

repas(X, Y, Z) :-
    hdoeuvre(X),
    plat(Y),
    dessert(Z).

repasLeger(X, Y, Z) :-
    repas(X, Y, Z),
    point(X, PX),
    point(Y, PY),
    point(Z, PZ),
    PX + PY + PZ < 10.