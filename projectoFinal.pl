import(date_time).
use_module(library(date_time)).
:- dynamic sueldo/1.
:- dynamic entradas_adicionales/1.
:- dynamic libros_comprados/2.
:- dynamic libros_sugeridos/1.

:- dynamic holding_books/1.

libro(marcos, ['ciencia ficcion', 'drama'], 5, 'marcos de mota', date(2019,07,23), 250, usado).
libro(claudio, ['ciencia ficcion'], 4, 'marcos de mota', date(2019,01,15), 250, usado).
libro(klk, ['ciencia ficcion', 'economia'], 4, 'Edward Conard', date(2019,01,15), 250, usado).
libro('Los viajes de mario', ['ciencia ficcion', 'viaje', 'economia'], 5, 'Edward Conard', date(2019,01,15), 250, usado).


sueldo(100).
entradas_adicionales([120,300]).

removeAllBooks():- retractall(libros_sugeridos(Libro)), retractall(holding_books(Libro)).

combs([],[]).
combs([H|T],[H|T2]) :- combs(T,T2).
combs([_|T],T2) :- combs(T,T2).

%Regla numero 1

booksXDaysOldTops(Libro,ExtraMoney,DaysOld):-removeAllBooks(),libro(Libro,_,_,Autor,ReleaseDate,Precio,_),date_get(today,Hoy),
    date_difference(Hoy,ReleaseDate,[years(Y),months(M),days(D)]),
    D =< DaysOld ,appendz(libros_sugeridos(Libro)).

%Regla numero 2

%Regla que añade los hechos a una lista
getHoldingBooks(Libros) :- findall(X, holding_books(Libro), Libros).

%Regla que te dice la cantidad de libros que existen en el hecho de libro
encontrarCantidadLibros(Cantidad):- findall(X, libro(Libro), Libros), length(Libros, Cantidad).

booksStarsCategoryExtraMoney(Libro, ExtraMoney, CategoriaABuscar, RatingDeseado):- removeAllBooks(), sueldo(Sueldo),
    Presupuesto is ExtraMoney + (Sueldo*0.10), regla2(Libro,Presupuesto,CategoriaABuscar,RatingDeseado).

regla2(Libro, Presupuesto, CategoriaABuscar, RatingDeseado):- libro(Libro, Categoria, Rating, _, _, Precio, _), not(libros_sugeridos(Libro)),
   existsInList(CategoriaABuscar, Categoria), Rating >= RatingDeseado,
    NewPresupuesto is Presupuesto - Precio, write(Libro),((NewPresupuesto > 0, assertz(libros_sugeridos(Libro)),
    regla2(NewLibro, NewPresupuesto, CategoriaABuscar, RatingDeseado)) ; (NewPresupuesto =< 0, !)).

%regla2(Libro, Presupuesto, CategoriaABuscar, RatingDeseado):- libro(Libro, Categoria, Rating, _, _, Precio, _),
%    not(holding_books(Libro)), encontrarCantidadLibros(Cantidad)
%    existsInList(CategoriaABuscar, Categoria), Rating >= RatingDeseado, assertz(holding_books(Libro)).

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
