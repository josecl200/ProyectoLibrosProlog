import(date_time).
use_module(library(date_time)).
:- dynamic sueldo/1.
:- dynamic entradas_adicionales/1.
:- dynamic libros_comprados/2.
:- dynamic libros_sugeridos/1.
:- dynamic combinaciones/1.

:- dynamic holding_books/1.

libroNombre(marcos).
libroNombre(claudio).
libroNombre(klk).
libroNombre('Los viajes de mario').
libro(marcos, ['ciencia ficcion', 'drama'], 5, 'marcos de mota', date(2019,07,23), 250, usado).
libro(claudio, ['ciencia ficcion'], 4, 'marcos de mota', date(2019,01,15), 250, usado).
libro(klk, ['ciencia ficcion', 'economia'], 4, 'Edward Conard', date(2019,01,15), 250, nuevo).
libro('Los viajes de mario', ['ciencia ficcion', 'viaje', 'economia'], 5, 'Edward Conard', date(2019,01,15), 250, usado).


sueldo(100).
entradas_adicionales(300).

removeAllBooks():- retractall(libros_sugeridos(Libro)), retractall(holding_books(Libro)).

combs([],[]).
combs([H|T],[H|T2]) :- combs(T,T2).
combs([_|T],T2) :- combs(T,T2).


%Regla numero 1

booksXDaysOldTops(Libro,ExtraMoney,DaysOld):-removeAllBooks(),libro(Libro,_,_,Autor,ReleaseDate,Precio,_),date_get(today,Hoy),
    date_difference(Hoy,ReleaseDate,[years(Y),months(M),days(D)]),
    D =< DaysOld ,assertz(libros_sugeridos(Libro)).

%Regla numero 2

%Regla que añade los hechos a una lista
getHoldingBooks(Libros) :- findall(X, holding_books(X), Libros).

%Regla que te dice la cantidad de libros que existen en el hecho de libro
encontrarCantidadLibros(Cantidad):- findall(X, libro(Libro), Libros), length(Libros, Cantidad).

%Inserta todos los libros en una lista
insertarLibrosEnLista(Libros):- findall(X, libroNombre(X), Libros).

booksStarsCategoryExtraMoney(Libros, ExtraMoney, CategoriaABuscar, RatingDeseado, Resultado):- removeAllBooks(), sueldo(Sueldo),
    Presupuesto is ExtraMoney + (Sueldo*0.10), insertarLibrosEnLista(Libros),
    regla2(Libros,Presupuesto,CategoriaABuscar,RatingDeseado), getHoldingBooks(Resultado).

regla2([], _,  _, _).
regla2([CabezaLibro|CuerpoLibro], Presupuesto, CategoriaABuscar, RatingDeseado):- libro(CabezaLibro, Categoria, Rating, _, _, Precio, _), 
    (existsInList(CategoriaABuscar, Categoria), Rating >= RatingDeseado, Precio =< Presupuesto,
    assertz(holding_books(CabezaLibro)), regla2(CuerpoLibro, Presupuesto, CategoriaABuscar, RatingDeseado),!) ; 
    regla2(CuerpoLibro, Presupuesto, CategoriaABuscar, RatingDeseado).

%regla2(Libro, Presupuesto, CategoriaABuscar, RatingDeseado):- libro(Libro, Categoria, Rating, _, _, Precio, _), not(libros_sugeridos(Libro)),
%   existsInList(CategoriaABuscar, Categoria), Rating >= RatingDeseado,
%    NewPresupuesto is Presupuesto - Precio, write(Libro),((NewPresupuesto > 0, assertz(libros_sugeridos(Libro)),
%    regla2(NewLibro, NewPresupuesto, CategoriaABuscar, RatingDeseado)) ; (NewPresupuesto =< 0, !)).

%regla2(Libro, Presupuesto, CategoriaABuscar, RatingDeseado):- libro(Libro, Categoria, Rating, _, _, Precio, _),
%    not(holding_books(Libro)), encontrarCantidadLibros(Cantidad)
%    existsInList(CategoriaABuscar, Categoria), Rating >= RatingDeseado, assertz(holding_books(Libro)).

existsInList(X, [X|_]).
existsInList(X, [_|Y]):- existsInList(X, Y).


%Regla numero 3

%extractPercentBooks([], CantidadLibros, CantidadPorCiento, CantidadTotal).
%extractPercentBooks([CabezaLibro|CuerpoLibro], CantidadLibros, CantidadPorCiento, CantidadTotal):- 
%    libro(CabezaLibro,Categoria,_,_,_,_,_), length(Categoria, CantidadCategorias), CantidadCategorias > 1,
%    assertz() 

booksUsed50PercentMoreCategories(Libros,Condicion,Porcentaje,Resultado):- removeAllBooks(), entradas_adicionales(Billetes),
    Presupuesto is Billetes, insertarLibrosEnLista(Libros), regla3(Libros,Condicion,Porcentaje,Presupuesto), getHoldingBooks(Resultado).
    %length(Resultado, Cantidad), PorCientoLibros is (Cantidad * (Porcentaje/100)), write(PorCientoLibros).

regla3([],_,_,_).
regla3([CabezaLibro|CuerpoLibro],Condicion,Porcentaje, Presupuesto):- libro(CabezaLibro,Categorias,Rating,Autor,ReleaseDate,Precio,Condicion),
    (Condicion == usado, Precio =< Presupuesto, assertz(holding_books(CabezaLibro)), regla3(CuerpoLibro,Condicion,Porcentaje, Presupuesto),!) ;
    regla3(CuerpoLibro,Condicion,Porcentaje, Presupuesto).


%Regla numero 4

booksEconomyNoCrisisEdward(Libros, PorCiento, AutorBuscado, CategoriaABuscar, FraseABuscar, Resultado):- removeAllBooks(),
    sueldo(Sueldo), Presupuesto is (Sueldo * (PorCiento/100)), insertarLibrosEnLista(Libros), getHoldingBooks(Resultado).

regla4([],_,_,_,_).
regla4([CabezaLibro|CuerpoLibro], Presupuesto, AutorBuscado, CategoriaABuscar, FraseABuscar):- libro(Libro, Categoria, _, Autor, _, Precio, _),
    (existsInList(CategoriaABuscar, Categoria), Autor == AutorBuscado, Precio =< Presupuesto, assertz(holding_books(CabezaLibro)),
    regla4(CuerpoLibro, Presupuesto, AutorBuscado, CategoriaABuscar, FraseABuscar),!) ; 
    regla4(CuerpoLibro, Presupuesto, AutorBuscado, CategoriaABuscar, FraseABuscar).

%Regla numero 5

booksTripFiveStars(Libros, CategoriaABuscar, RatingDeseado, CantidadMeses):- removeAllBooks(), sueldo(Sueldo), insertarLibrosEnLista(Libros),

regla5([],_,_,_,_).
regla5([CabezaLibro|CuerpoLibro], Presupuesto, CategoriaABuscar, RatingDeseado, CantidadMeses):- 
    libro(Libro, Categoria, Rating, _, _, Precio, _), (existsInList(CategoriaABuscar, Categoria), Rating == RatingDeseado,
    Precio =< Presupuesto, assertz(holding_books(CabezaLibro)), regla5(CuerpoLibro, Presupuesto, CategoriaABuscar, RatingDeseado, CantidadMeses))
    ; regla5(CuerpoLibro, Presupuesto, CategoriaABuscar, RatingDeseado, CantidadMeses).