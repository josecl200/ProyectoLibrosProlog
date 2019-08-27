% :- import(date_time).
:- use_module(library(date_time)).
:- dynamic sueldo/1.
:- dynamic entradas_adicionales/1.
:- dynamic libros_comprados/2.
:- dynamic libros_sugeridos/1.
:- dynamic combinaciones/1.
:- dynamic holding_books/1.

libroNombre('Carrion Girl (Wakeful Dead, #1)').
libroNombre('Off Script').
libroNombre('Loving Mr. Jerkface').
libroNombre('Two Cream, No Sugar').
libroNombre('The Blue Pearl Murders').
libroNombre('I Wish I May').
libroNombre('Shadrach').
libroNombre('A Thousand Miles').
libroNombre('Acrophilia').
libroNombre('Dark Paradise').
libroNombre('Perfect Imperfection').
libroNombre('My tough boy').
libroNombre('F*ckboys').
libroNombre('Fall For a Trouble').
libroNombre('Neón Awards').
libroNombre('Depressed Love').
libroNombre('Songbook').
libroNombre('Absurd Thoughts').
libroNombre('Aprils Diary').
libroNombre('Junniper').
libroNombre('Blue Royalty').
libroNombre('Larry Stylinson').
libroNombre('Broken').
libroNombre('The Secrets').
libroNombre('The Love Of My Life').
libroNombre('The Rain').
libroNombre('Death Come For Us All').
libroNombre('You').
libroNombre('13 Reasons Why').
libroNombre('A Day In The Life Of Jack').
libro('Carrion Girl (Wakeful Dead, #1)', ['drama'], 1, 'Agatha Christie', date(2006,26,05), 1950, nuevo).
libro('Off Script', ['ciencia ficcion', 'comedia', 'drama'], 4, 'William Shakespeare', date(2013,07,09), 1350, usado).
libro('Loving Mr. Jerkface', ['ciencia ficcion', 'drama', 'accion'], 4, 'Virginia Woolf', date(2019,21,11), 1450, nuevo).
libro('Two Cream, No Sugar', ['thriller', 'romance'], 5, 'Stephen King', date(2007,23,04), 1175, nuevo).
libro('The Blue Pearl Murders', ['romance'], 1, 'Stephen King', date(2016,28,01), 1450, nuevo).
libro('I Wish I May', ['accion', 'ciencia ficcion', 'comedia'], 3, 'Mark Twain', date(2002,08,12), 2000, usado).
libro('Shadrach', ['romance', 'accion', 'thriller'], 3, 'George Orwell', date(2002,25,11), 1000, nuevo).
libro('A Thousand Miles', ['romance'], 3, 'Jane Austen', date(2015,09,04), 1425, usado).
libro('Acrophilia', ['terror', 'drama'], 4, 'William Falknuer', date(2015,29,02), 825, usado).
libro('Dark Paradise', ['ciencia ficcion', 'accion'], 5, 'George Orwell', date(2019,31,09), 375, nuevo).
libro('Perfect Imperfection', ['ciencia ficcion'], 2, 'Agatha Christie', date(2006,28,02), 1850, usado).
libro('My tough boy', ['ciencia ficcion'], 3, 'Ernest Hemingway', date(2019,18,07), 250, usado).
libro('F*ckboys', ['romance'], 1, 'Jane Austen', date(2005,24,02), 1350, usado).
libro('Fall For a Trouble', ['romance', 'thriller'], 4, 'Mark Twain', date(2011,26,03), 1075, nuevo).
libro('Neón Awards', ['ciencia ficcion'], 2, 'William Falknuer', date(2010,04,01), 1775, nuevo).
libro('Depressed Love', ['thriller'], 1, 'William Falknuer', date(2018,28,10), 1350, usado).
libro('Songbook', ['ciencia ficcion', 'drama'], 2, 'Virginia Woolf', date(2010,17,11), 1350, nuevo).
libro('Absurd Thoughts', ['ciencia ficcion', 'terror', 'thriller'], 1, 'Ernest Hemingway', date(2015,01,05), 575, usado).
libro('April Diary', ['romance', 'accion', 'drama'], 4, 'George Orwell', date(2012,05,11), 900, nuevo).
libro('Junniper', ['drama'], 3, 'Mark Twain', date(2005,30,08), 1550, nuevo).
libro('Blue Royalty', ['drama', 'comedia', 'terror'], 4, 'George Orwell', date(2000,21,07), 1825, usado).
libro('Larry Stylinson', ['thriller', 'romance'], 3, 'Virginia Woolf', date(2001,12,09), 500, usado).
libro('Broken', ['accion'], 3, 'Jane Austen', date(2012,09,07), 375, usado).
libro('The Secrets', ['comedia'], 5, 'George Orwell', date(2012,11,12), 800, usado).
libro('The Love Of My Life', ['comedia', 'ciencia ficcion', 'thriller'], 3, 'George Orwell', date(2002,01,03), 300, nuevo).
libro('The Rain', ['drama'], 1, 'Stephen King', date(2005,24,02), 1850, usado).
libro('Death Come For Us All', ['comedia', 'terror'], 3, 'Agatha Christie', date(2012,06,01), 1025, usado).
libro('You', ['drama', 'accion', 'romance'], 3, 'Mark Twain', date(2011,12,03), 1425, usado).
libro('13 Reasons Why', ['terror', 'romance'], 5, 'Jane Austen', date(2001,10,10), 575, nuevo).
libro('A Day In The Life Of Jack', ['accion'], 5, 'Stephen King', date(2011,24,05), 1825, nuevo).

append([],T,T).
append([H|T],T2,[H|R]) :-
    append(T,T2,R).

% sueldo(1000).
% entradas_adicionales(800).

:- assertz(sueldo(0)).
:- assertz(entradas_adicionales(0)).

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
encontrarCantidadLibros(Cantidad):- findall(Libro, libro(Libro,_,_,_,_,_,_), Libros), length(Libros, Cantidad).

%Inserta todos los libros en una lista
insertarLibrosEnLista(Libros):- findall(X, libroNombre(X), Libros).

%Regla numero 1

booksXDaysOldTops(Libros,ExtraMoney,DaysOld,Resultado,Presupuesto,Combinaciones):- removeAllBooks(), Presupuesto is ExtraMoney, 
    findall(Libros, regla1(Libros,Presupuesto,DaysOld), Resultado), 
    findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones).

regla1(Libro, Presupuesto, DaysOld):- libro(Libro, _, _, _, ReleaseDate, Precio, _), date_get(today,Hoy),
    date_difference(Hoy,ReleaseDate,[years(Y),months(M),days(D)]), AnioEnDias is Y*365, MesesEnDias is M*30, 
    TotalDias is D+AnioEnDias+MesesEnDias,
    TotalDias =< DaysOld , Precio =< Presupuesto, assertz(holding_books(Libro)).

%Regla numero 2


%booksStarsCategoryExtraMoney(Libros, ExtraMoney, CategoriaABuscar, RatingDeseado, Resultado, Presupuesto, Combinaciones):- 
%    removeAllBooks(), sueldo(Sueldo),
%    Presupuesto is ExtraMoney + (Sueldo*0.10), insertarLibrosEnLista(Libros),
%    regla2(Libros,Presupuesto,CategoriaABuscar,RatingDeseado), getHoldingBooks(Resultado), 
%    findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones).

%regla2([], _,  _, _).
%regla2([CabezaLibro|CuerpoLibro], Presupuesto, CategoriaABuscar, RatingDeseado):- libro(CabezaLibro, Categoria, Rating, _, _, Precio, _), 
%    (existsInList(CategoriaABuscar, Categoria), Rating >= RatingDeseado, Precio =< Presupuesto,
%    assertz(holding_books(CabezaLibro)), regla2(CuerpoLibro, Presupuesto, CategoriaABuscar, RatingDeseado),!) ; 
%    regla2(CuerpoLibro, Presupuesto, CategoriaABuscar, RatingDeseado).

booksStarsCategoryExtraMoney(Libros, ExtraMoney, CategoriaABuscar, RatingDeseado, Resultado, Presupuesto, Combinaciones):- 
    removeAllBooks(), sueldo(Sueldo),
    Presupuesto is ExtraMoney + (Sueldo*0.10), findall(Libros, regla2(Libros,Presupuesto,CategoriaABuscar,RatingDeseado), Resultado),
    findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones).

regla2(Libro, Presupuesto, CategoriaABuscar, RatingDeseado):- libro(Libro, Categoria, Rating, _, _, Precio, _), 
    (existsInList(CategoriaABuscar, Categoria), Rating >= RatingDeseado, Precio =< Presupuesto,
    assertz(holding_books(Libro))).

existsInList(X, [X|_]).
existsInList(X, [_|Y]):- existsInList(X, Y).


%Regla numero 3

%Esta regla devuelve un resultado cada vez que un libro contiene mas de una categoria
findMoreThanOneCategory(Libro, Res):-holding_books(Libro), libro(Libro, Categoria, _, _, _, _, _), length(Categoria, Cantidad),
     Cantidad > 1, Res is 1. 


booksUsed50PercentMoreCategories(Libros,Condicion,Porcentaje,Resultado,Presupuesto,Combinaciones):- removeAllBooks(), entradas_adicionales(Billetes),
    Presupuesto is Billetes, findall(Libros, regla3(Libros,Condicion,Presupuesto), Resultado),
    ((length(Resultado, Cantidad), PorCientoLibros is (Cantidad * (Porcentaje/100)),  TotalPorCiento is floor(PorCientoLibros),
    findall(Res, findMoreThanOneCategory(_, Res), TotalMoreThanOne), length(TotalMoreThanOne, Total),
    Total >= TotalPorCiento, findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones)) ; (removeAllBooks(), fail)),!.

regla3(Libro,CondicionABuscar, Presupuesto):- libro(Libro,_,_,_,_,Precio,Condicion),
    (Condicion == CondicionABuscar, Precio =< Presupuesto, assertz(holding_books(Libro))).


%Regla numero 4

notName(FraseABuscar, Libro):- atomic_list_concat(Lista,' ',Libro),
	not(existsInList(FraseABuscar,Lista)).

booksEconomyNoCrisisEdward(Libros, PorCiento, AutorBuscado, CategoriaABuscar, FraseABuscar, Resultado, Presupuesto, Combinaciones):- 
    removeAllBooks(), sueldo(Sueldo), Presupuesto is (Sueldo * (PorCiento/100)),
    findall(Libros, regla4(Libros, Presupuesto, AutorBuscado, CategoriaABuscar, FraseABuscar), Resultado),
    findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones).

regla4(Libro, Presupuesto, AutorBuscado, CategoriaABuscar, FraseABuscar):- 
    libro(Libro, Categoria, _, Autor, _, Precio, _),
    (existsInList(CategoriaABuscar, Categoria), Autor == AutorBuscado, notName(FraseABuscar, Libro),
    Precio =< Presupuesto, assertz(holding_books(Libro))).

%Regla numero 5

booksTripFiveStars(Libros, CategoriaABuscar, RatingDeseado, Resultado, Presupuesto, Combinaciones):- removeAllBooks(), 
    sueldo(Sueldo), Presupuesto is Sueldo,
    findall(Libros, regla5(Libros, Presupuesto, CategoriaABuscar, RatingDeseado), Resultado),
    findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones).

regla5(Libro, Presupuesto, CategoriaABuscar, RatingDeseado):- 
    libro(Libro, Categoria, Rating, _, ReleaseDate, Precio, _), (existsInList(CategoriaABuscar, Categoria), Rating == RatingDeseado,
    Precio =< Presupuesto, date_get(today,Hoy), date_difference(Hoy,ReleaseDate,[years(Y),months(M),days(_)]), 
    Y == 0, M == 0, assertz(holding_books(Libro))).


%Regla numero 6 (Libros nuevos o usados que cuesten menos de una cantidad pero que aun se puedan comprar con mi sueldo)

booksConditionCheap(Libros, CondicionABuscar, PrecioMaximo, Resultado, Presupuesto, Combinaciones):-  removeAllBooks(), 
    sueldo(Sueldo), Presupuesto is Sueldo, findall(Libros, regla6(Libros, CondicionABuscar, PrecioMaximo, Presupuesto), Resultado),
    getHoldingBooks(Resultado), findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones).

regla6(Libro, CondicionABuscar, PrecioMaximo, Presupuesto):- libro(Libro, _, _, _, _, Precio, Condicion),
    (Condicion == CondicionABuscar, Precio =< PrecioMaximo, Precio =< Presupuesto, assertz(holding_books(Libro))).


%Regla numero 7 (Obtener los libros de un autor con un rating especifico teniendo como presupuesto mi sueldo mas mis entradas adicionales)

booksAuthorBest(Libros, AutorBuscado, RatingDeseado, Resultado, Presupuesto, Combinaciones):- removeAllBooks(), sueldo(Sueldo), 
    entradas_adicionales(Entradas), Presupuesto is Sueldo+Entradas, 
    findall(Libros, regla7(Libros, AutorBuscado, RatingDeseado, Presupuesto), Resultado),
    getHoldingBooks(Resultado), findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones).

regla7(Libro, AutorBuscado, RatingDeseado, Presupuesto):- libro(Libro,_,Rating,Autor,_,Precio,_),
    AutorBuscado == Autor, Rating == RatingDeseado, Precio =< Presupuesto, assertz(holding_books(Libro)).


%Regla numero 8 (Obtener los libros de un autor que no pasen de un precio especificado que hallan salido antes de un año especifico)

booksAuthorCheaperThanX(Libros, AutorBuscado, PrecioDeseado, Presupuesto, AnioBuscado, Resultado, Combinaciones):-removeAllBooks(),sueldo(Sueldo),
entradas_adicionales(Clavo), Presupuesto is Sueldo+Clavo, 
findall(Libros, regla8(Libros, AutorBuscado, PrecioDeseado, Presupuesto, AnioBuscado), Resultado),
getHoldingBooks(Resultado),findall(X, getCombinations(Resultado, Presupuesto, X), Combinaciones).

regla8(Libro,AutorBuscado,PrecioDeseado,Presupuesto,AnioBuscado):- libro(Libro,_,_,AutorBuscado,Fecha,Precio,_),
    Precio =< PrecioDeseado, Precio =< Presupuesto, date_extract(Fecha,year(Y)), Y =< AnioBuscado, assertz(holding_books(Libro)).
