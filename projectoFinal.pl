use_module(library(date_time)).
:- dynamic sueldo/1.
:- dynamic entradas_adicionales/1.
:- dynamic libros_comprados/2.
:- dynamic libros_sugeridos/1.

libro(marcos, ['ciencia ficcion', 'drama'], 5, 'marcos de mota', date(2019,07,23), 250, usado).
libro(claudio, ['ciencia ficcion'], 4, 'marcos de mota', date(2019,01,15), 250, usado).
libro(klk, ['ciencia ficcion', 'economia'], 4, 'Edward Conard', date(2019,01,15), 250, usado).
libro('Los viajes de mario', ['ciencia ficcion', 'viaje', 'economia'], 5, 'Edward Conard', date(2019,01,15), 250, usado).


sueldo(8000).
entradas_adicionales([120,300]).

%Regla numero 1

booksXDaysOldTops(Libro,ExtraMoney,DaysOld):-retractall(libros_sugeridos),libro(Libro,_,_,Autor,ReleaseDate,Precio,_),date_get(today,Hoy),date_difference(Hoy,ReleaseDate,[years(Y),months(M),days(D)]),D =< DaysOld,appendz(libros_sugeridos(libro(Libro,Categorias,Rating,Autor,ReleaseDate,Precio,Condicion)).

%Regla numero 2
booksStarsCategoryExtraMoney(Libro, ExtraMoney, CategoriaABuscar, RatingDeseado):- retractall(libros_sugeridos),sueldo(Sueldo),Money is ((Sueldo*0.10)+ExtraMoney), libro(Libro, Categoria, Rating, _, _, Precio, _), existsInList(CategoriaABuscar, Categoria), Rating >= RatingDeseado .

existsInList(X, [X|_]).
existsInList(X, [_|Y]):- existsInList(X, Y).


%Regla numero 3
booksUsed50PercentMoreCategories(Libro,Condicion,Porcentaje):- retractall(libros_sugeridos),entradas_adicionales(Billetes),libro(Libro,Categorias,Rating,Autor,ReleaseDate,Precio,Condicion),appendz(libros_sugeridos(libro(Libro,Categorias,Rating,Autor,ReleaseDate,Precio,Condicion)).

sumarEntradasAdicionales([], 0).
sumarEntradasAdicionales([Cabeza|ListaEntradas], Total):- retractall(libros_sugeridos),sumarEntradasAdicionales(ListaEntradas, Total2), Total is Total2 + Cabeza.

%Regla numero 4
booksEconomyNoCrisisEdward(Libro, AutorBuscado):- retractall(libros_sugeridos), sueldo(Sueldo), Money is Sueldo*0.20,
    libro(Libro, Categoria, _, Autor, _, Precio, _),
    existsInList('economia', Categoria), Autor == AutorBuscado,appendz(libros_sugeridos(libro(Libro,Categorias,Rating,Autor,ReleaseDate,Precio,Condicion)).

%Regla numero 5
booksTripFiveStars(Libro):- retractall(libros_sugeridos),libro(Libro, Categoria, Rating, _, _, Precio, _), existsInList('viaje', Categoria), Rating == 5,appendz(libros_sugeridos(libro(Libro,Categorias,Rating,Autor,ReleaseDate,Precio,Condicion)).
