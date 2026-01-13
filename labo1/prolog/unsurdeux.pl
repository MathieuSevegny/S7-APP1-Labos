unSurDeux([],[]).
unSurDeux([_],[]).

unSurDeux([_,X|Liste],[X|Res]) :- unSurDeux(Liste,Res).