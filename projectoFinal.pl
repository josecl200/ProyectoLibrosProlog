import(date_time).
use_module(library(date_time)).
:- dynamic sueldo/1.
:- dynamic entradas_adicionales/1.
:- dynamic libros_comprados/2.
:- dynamic libros_sugeridos/1.
:- dynamic combinaciones/1.

:- dynamic holding_books/1.

libroNombre('marcos').
libroNombre('claudio').
libroNombre('klk').
libroNombre('Los viajes de mario').
libro('marcos', ['ciencia ficcion', 'drama'], 5, 'marcos de mota', date(2019,07,23), 250, usado).
libro('claudio', ['ciencia ficcion'], 4, 'marcos de mota', date(2019,01,15), 250, usado).
libro('klk', ['ciencia ficcion', 'economia'], 4, 'Edward Conard', date(2019,01,15), 250, nuevo).
libro('Los viajes de mario', ['ciencia ficcion', 'viaje', 'economia'], 5, 'Edward Conard', date(2019,01,15), 250, usado).

append([],T,T).
append([H|T],T2,[H|R]) :-
    append(T,T2,R).

sueldo(1000).
entradas_adicionales(800).

removeAllBooks():- retractall(libros_sugeridos(Libro)), retractall(holding_books(Libro)).

%Regla que devuelve todas las combinaciones posibles de una lista
combs([],[]).
combs([H|T],[H|T2]) :- combs(T,T2).
combs([_|T],T2) :- combs(T,T2).

%Regla que se asegura que la combinaciones no sobrepase el presupuesto
getCombinations(Lista,Monto,Respuesta):-combs(Lista, Respuesta), sum(Respuesta,Total), Total =< Monto.

sum([],0).
sum([CabezaLibro|CuerpoLibro],SumaTotal):- libro(CabezaLibro,_,_,_,_,Precio,_), sum(CuerpoLibro,Aux), SumaTotal is Aux+Precio.

%Regla que añade los hechos a una lista
getHoldingBooks(Libros) :- findall(X, holding_books(X), Libros).

%Regla que te dice la cantidad de libros que existen en el hecho de libro
encontrarCantidadLibros(Cantidad):- findall(Libro, libro(Libro), Libros), length(Libros, Cantidad).

%Inserta todos los libros en una lista
insertarLibrosEnLista(Libros):- findall(X, libroNombre(X), Libros).

%Regla numero 1

booksXDaysOldTops(Libros,ExtraMoney,DaysOld,Resultado,Presupuesto,Combinaciones):- removeAllBooks(), Presupuesto is ExtraMoney, 
    insertarLibrosEnLista(Libros), regla1(Libros,Presupuesto,DaysOld), getHoldingBooks(Resultado), 
    findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones).

regla1([],_,_).
regla1([CabezaLibro|CuerpoLibro], Presupuesto, DaysOld):- libro(CabezaLibro, _, _, _, ReleaseDate, Precio, _), date_get(today,Hoy),
    date_difference(Hoy,ReleaseDate,[years(_),months(_),days(D)]),
    (D =< DaysOld , Precio =< Presupuesto, assertz(holding_books(CabezaLibro)), regla1(CuerpoLibro,Presupuesto,DaysOld)) ;
    regla1(CuerpoLibro, Presupuesto, DaysOld).

%Regla numero 2


booksStarsCategoryExtraMoney(Libros, ExtraMoney, CategoriaABuscar, RatingDeseado, Resultado, Presupuesto, Combinaciones):- 
    removeAllBooks(), sueldo(Sueldo),
    Presupuesto is ExtraMoney + (Sueldo*0.10), insertarLibrosEnLista(Libros),
    regla2(Libros,Presupuesto,CategoriaABuscar,RatingDeseado), getHoldingBooks(Resultado), 
    findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones).

regla2([], _,  _, _).
regla2([CabezaLibro|CuerpoLibro], Presupuesto, CategoriaABuscar, RatingDeseado):- libro(CabezaLibro, Categoria, Rating, _, _, Precio, _), 
    (existsInList(CategoriaABuscar, Categoria), Rating >= RatingDeseado, Precio =< Presupuesto,
    assertz(holding_books(CabezaLibro)), regla2(CuerpoLibro, Presupuesto, CategoriaABuscar, RatingDeseado),!) ; 
    regla2(CuerpoLibro, Presupuesto, CategoriaABuscar, RatingDeseado).

existsInList(X, [X|_]).
existsInList(X, [_|Y]):- existsInList(X, Y).


%Regla numero 3

%Esta regla devuelve un resultado cada vez que un libro contiene mas de una categoria
findMoreThanOneCategory(Libro, Res):-holding_books(Libro), libro(Libro, Categoria, _, _, _, _, _), length(Categoria, Cantidad),
     Cantidad > 1, Res is 1. 


booksUsed50PercentMoreCategories(Libros,Condicion,Porcentaje,Resultado,Presupuesto,Combinaciones):- removeAllBooks(), entradas_adicionales(Billetes),
    Presupuesto is Billetes, insertarLibrosEnLista(Libros), regla3(Libros,Condicion,Porcentaje,Presupuesto), getHoldingBooks(Resultado),
    ((length(Resultado, Cantidad), PorCientoLibros is (Cantidad * (Porcentaje/100)),  TotalPorCiento is floor(PorCientoLibros),
    findall(Res, findMoreThanOneCategory(_, Res), TotalMoreThanOne), length(TotalMoreThanOne, Total),
    Total >= TotalPorCiento, findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones)) ; (removeAllBooks(), fail)),!.

regla3([],_,_,_).
regla3([CabezaLibro|CuerpoLibro],CondicionABuscar,Porcentaje, Presupuesto):- libro(CabezaLibro,_,_,_,_,Precio,Condicion),
    (Condicion == CondicionABuscar, Precio =< Presupuesto, assertz(holding_books(CabezaLibro)), 
    regla3(CuerpoLibro,CondicionABuscar,Porcentaje, Presupuesto),!) ;
    regla3(CuerpoLibro,CondicionABuscar,Porcentaje, Presupuesto).


%Regla numero 4

notName(FraseABuscar, Libro):- atomic_list_concat(Lista,' ',Libro),
	not(existsInList(FraseABuscar,Lista)).

booksEconomyNoCrisisEdward(Libros, PorCiento, AutorBuscado, CategoriaABuscar, FraseABuscar, Resultado, Presupuesto, Combinaciones):- 
    removeAllBooks(), sueldo(Sueldo), Presupuesto is (Sueldo * (PorCiento/100)), insertarLibrosEnLista(Libros),
    regla4(Libros, Presupuesto, AutorBuscado, CategoriaABuscar, FraseABuscar),
    getHoldingBooks(Resultado), findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones).

regla4([],_,_,_,_).
regla4([CabezaLibro|CuerpoLibro], Presupuesto, AutorBuscado, CategoriaABuscar, FraseABuscar):- 
    libro(CabezaLibro, Categoria, _, Autor, _, Precio, _),
    (existsInList(CategoriaABuscar, Categoria), Autor == AutorBuscado, notName(FraseABuscar, CabezaLibro),
    Precio =< Presupuesto, assertz(holding_books(CabezaLibro)),
    regla4(CuerpoLibro, Presupuesto, AutorBuscado, CategoriaABuscar, FraseABuscar),!) ; 
    regla4(CuerpoLibro, Presupuesto, AutorBuscado, CategoriaABuscar, FraseABuscar).

%Regla numero 5

booksTripFiveStars(Libros, CategoriaABuscar, RatingDeseado, CantidadMeses, Resultado, Presupuesto, Combinaciones):- removeAllBooks(), 
    sueldo(Sueldo), Presupuesto is Sueldo, insertarLibrosEnLista(Libros),
    regla5(Libros, Presupuesto, CategoriaABuscar, RatingDeseado, CantidadMeses),
    getHoldingBooks(Resultado), findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones).

regla5([],_,_,_,_).
regla5([CabezaLibro|CuerpoLibro], Presupuesto, CategoriaABuscar, RatingDeseado, CantidadMeses):- 
    libro(CabezaLibro, Categoria, Rating, _, _, Precio, _), (existsInList(CategoriaABuscar, Categoria), Rating == RatingDeseado,
    Precio =< Presupuesto, assertz(holding_books(CabezaLibro)), regla5(CuerpoLibro, Presupuesto, CategoriaABuscar, RatingDeseado, CantidadMeses))
    ; regla5(CuerpoLibro, Presupuesto, CategoriaABuscar, RatingDeseado, CantidadMeses).


%Regla numero 6 (Libros nuevos o usados que cuesten menos de una cantidad pero que aun se puedan comprar con mi sueldo)

booksConditionCheap(Libros, CondicionABuscar, PrecioMaximo, Resultado, Presupuesto, Combinaciones):-  removeAllBooks(), 
    sueldo(Sueldo), Presupuesto is Sueldo,
    insertarLibrosEnLista(Libros), regla6(Libros, CondicionABuscar, PrecioMaximo, Presupuesto), getHoldingBooks(Resultado),
    findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones).

regla6([], _, _, _).
regla6([CabezaLibro|CuerpoLibro], CondicionABuscar, PrecioMaximo, Presupuesto):- libro(CabezaLibro, _, _, _, _, Precio, Condicion),
    (Condicion == CondicionABuscar, Precio =< PrecioMaximo, Precio =< Presupuesto, assertz(holding_books(CabezaLibro)),
    regla6(CuerpoLibro, CondicionABuscar, PrecioMaximo, Presupuesto), !) ; regla6(CuerpoLibro, CondicionABuscar, PrecioMaximo, Presupuesto).


%Regla numero 7 (Obtener los libros de un autor con un rating especifico teniendo como presupuesto mi sueldo mas mis entradas adicionales)

booksAuthorBest(Libros, AutorBuscado, RatingDeseado, Resultado, Presupuesto, Combinaciones):- removeAllBooks(), sueldo(Sueldo), 
    entradas_adicionales(Entradas), Presupuesto is Sueldo+Entradas, insertarLibrosEnLista(Libros),
    regla7(Libros, AutorBuscado, RatingDeseado, Presupuesto), getHoldingBooks(Resultado),
    findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones).

regla7([], _, _, _).
regla7([CabezaLibro|CuerpoLibro], AutorBuscado, RatingDeseado, Presupuesto):- libro(CabezaLibro,_,Rating,Autor,_,Precio,_),
    (AutorBuscado == Autor, Rating == RatingDeseado, Precio =< Presupuesto, assertz(holding_books(CabezaLibro)),
    regla7(CuerpoLibro, AutorBuscado, RatingDeseado, Presupuesto), !) ; regla7(CuerpoLibro, AutorBuscado, RatingDeseado, Presupuesto).

