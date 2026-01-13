

% actions.pl
% Définit les actions possibles dans le monde des blocs.

% action(Env, move(B,X,Y)) : déplacer B de X vers Y.
action(Env, move(B, X, Y)) :-
	member(on(B, X), Env),
	member(clear(B), Env),
	member(clear(Y), Env),
	member(block(B), Env),
	member(block(X), Env),
	member(block(Y), Env),
	B \== X, B \== Y, X \== Y.

% action(Env, moveToTable(B,X)) : déplacer B de X vers la table.
action(Env, moveToTable(B, X)) :-
	member(on(B, X), Env),
	member(clear(B), Env),
	member(block(B), Env),
	member(block(X), Env),
	B \== X.

% actionsPossibles(Env, R) : R est la liste de toutes les actions valides.
actionsPossibles(Env, R) :-
	findall(Action, action(Env, Action), R).

%% Exemple d'utilisation :
%% ?- Env = [on(b, table), on(a, table), on(c, a), clear(b), clear(c), block(a), block(b), block(c)],
%%    actionsPossibles(Env, R).
%% R = [move(b, table, c), move(c, a, b), moveToTable(c, a)].

