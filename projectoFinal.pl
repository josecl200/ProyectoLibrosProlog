use_module(library(date_time)).
libro(marcos, ['ciencia ficcion', 'drama'], 5, 'marcos de mota', date(2019,07,23), 250, usado).
libro(claudio, ['ciencia ficcion'], 4, 'marcos de mota', date(2019,01,15), 250, usado).
libro(klk, ['ciencia ficcion', 'economia'], 4, 'Edward Conard', date(2019,01,15), 250, usado).
libro('Los viajes de mario', ['ciencia ficcion', 'viaje', 'economia'], 5, 'Edward Conard', date(2019,01,15), 250, usado).


sueldo(8000).
entradas_adicionales([120,300]).

%Regla numero 1

books7DaysOldTops(Libro,ExtraMoney):-libro(Libro,_,_,Autor,ReleaseDate,Precio,_),date_get(today,Hoy),date_difference(Hoy,ReleaseDate,[years(Y),months(M),days(D)]),D =< 7.

%Regla numero 2
booksStarsCategoryExtraMoney(Libro, ExtraMoney, CategoriaABuscar, RatingDeseado):- sueldo(Sueldo),
    Money is ((Sueldo*0.10)+ExtraMoney), libro(Libro, Categoria, Rating, _, _, Precio, _), existsInList(CategoriaABuscar, Categoria),    Rating >= RatingDeseado .

existsInList(X, [X|_]).
existsInList(X, [_|Y]):- existsInList(X, Y).


%Regla numero 3
booksUsed50PercentMoreCategories(Libro):- entradas_adicionales(Lista), sumarEntradasAdicionales(Lista, Money).

sumarEntradasAdicionales([], 0).
sumarEntradasAdicionales([Cabeza|ListaEntradas], Total):- sumarEntradasAdicionales(ListaEntradas, Total2), Total is Total2 + Cabeza.

%Regla numero 4
booksEconomyNoCrisisEdward(Libro, AutorBuscado):-  sueldo(Sueldo), Money is Sueldo*0.20,
    libro(Libro, Categoria, _, Autor, _, Precio, _),
    existsInList('economia', Categoria), Autor == AutorBuscado.

%Regla numero 5
booksTripFiveStars(Libro):- libro(Libro, Categoria, Rating, _, _, Precio, _), existsInList('viaje', Categoria), Rating == 5.
