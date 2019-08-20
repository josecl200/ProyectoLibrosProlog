from pyswip import Prolog
import itertools

#def main():
    #prolog = Prolog()
    #prolog.consult("projectoFinal")
    #print("Hola")

    #regla1(prolog,500,200)
    #booknames, combinaciones = regla2(prolog, 1000, "'ciencia ficcion'", 3)
    #regla3(prolog, "usado", 50)
    #regla4(prolog, 50, "marcos de mota", "ciencia ficcion", "hola")
    #print(combinaciones[0][0])


def getProlog():
    prolog = Prolog()
    prolog.consult("projectoFinal")
    prolog.query("['librosComprados.txt']")
    return prolog

def buyBook(prolog, bookname):
    fecha = ""
    for result in prolog.query("date_get(today, Hoy)"):
        fecha = result["Hoy"]

    prolog.assertz("libros_comprados('"+bookname+"', "+fecha+")")
    prolog.query("tell('librosComprados.txt'), listing(libros_comprados), told")

def regla1(prolog, extramoney, days):
    combinaciones = []
    result = list(prolog.query("booksXDaysOldTops(Libros,"+str(extramoney)+","+str(days)+",Resultado,Presupuesto, Combinaciones)"))
    booklist = getBookList(prolog)
    for search in result:
        for i in range(0, len(search["Combinaciones"])):
            combinacion = []
            for j in range(0, len(search["Combinaciones"][i])):
                combinacion.append(search["Combinaciones"][i][j])
            combinaciones.append(combinacion)
    return booklist, combinaciones



def regla2(prolog, extramoney, categoria, rating):
    booklist = []
    combinaciones = []
    result = list(prolog.query("booksStarsCategoryExtraMoney(Libros, "+str(extramoney)+", '"+categoria+"', "+str(rating)+", Resultado, Presupuesto, Combinaciones)"))
    for search in prolog.query("holding_books(X)"):
        booklist.append(search["X"])
    for search in result:
        for i in range(0, len(search["Combinaciones"])):
            combinacion = []
            for j in range(0, len(search["Combinaciones"][i])):
                combinacion.append(search["Combinaciones"][i][j])
            combinaciones.append(combinacion)
    return booklist, combinaciones

def regla3(prolog, condicion, porcentaje):
    booklist = []
    combinaciones = []
    result = list(prolog.query("booksUsed50PercentMoreCategories(Libros,"+condicion+","+str(porcentaje)+",Resultado,Presupuesto, Combinaciones)"))
    for search in prolog.query("holding_books(X)"):
        booklist.append(search["X"])
        #print(len(list(search["Categoria"])))

    for search in result:
        for i in range(0, len(search["Combinaciones"])):
            combinacion = []
            for j in range(0, len(search["Combinaciones"][i])):
                combinacion.append(search["Combinaciones"][i][j])
            combinaciones.append(combinacion)
    return booklist, combinaciones


def regla4(prolog, porciento, autor, categoria, frase):
    combinaciones = []
    result = list(prolog.query("booksEconomyNoCrisisEdward(Libros, "+str(porciento)+", '%s', '%s', '%s', Resultado, Presupuesto, Combinaciones)"
                      % (autor, categoria, frase)))
    booklist = getBookList(prolog)

    for search in result:
        for i in range(0, len(search["Combinaciones"])):
            combinacion = []
            for j in range(0, len(search["Combinaciones"][i])):
                combinacion.append(search["Combinaciones"][i][j])
            combinaciones.append(combinacion)
    return booklist, combinaciones


def regla5(prolog, categoria, rating):
    combinaciones = []
    result = list(prolog.query("booksTripFiveStars(Libros, '%s', "+str(rating)+", Resultado, Presupuesto, Combinaciones)") % categoria)
    booklist = getBookList(prolog)

    for search in result:
        for i in range(0, len(search["Combinaciones"])):
            combinacion = []
            for j in range(0, len(search["Combinaciones"][i])):
                combinacion.append(search["Combinaciones"][i][j])
            combinaciones.append(combinacion)
    return booklist, combinaciones

def regla6(prolog, condicion, precio):
    combinaciones = []
    result = list(prolog.query("booksConditionCheap(Libros , "+condicion+", "+str(precio)+", Resultado, Presupuesto, Combinaciones)"))
    booklist = getBookList(prolog)

    for search in result:
        for i in range(0, len(search["Combinaciones"])):
            combinacion = []
            for j in range(0, len(search["Combinaciones"][i])):
                combinacion.append(search["Combinaciones"][i][j])
            combinaciones.append(combinacion)
    return booklist, combinaciones


def regla7(prolog, autor, rating):
    combinaciones = []
    result = list(prolog.query("booksAuthorBest(Libros, '%s', "+rating+", Resultado, Presupuesto, Combinaciones)") % autor)
    booklist = getBookList(prolog)

    for search in result:
        for i in range(0, len(search["Combinaciones"])):
            combinacion = []
            for j in range(0, len(search["Combinaciones"][i])):
                combinacion.append(search["Combinaciones"][i][j])
            combinaciones.append(combinacion)
    return booklist, combinaciones


def regla8(prolog, autor, precioDeseado, anioBuscado):
    combinaciones = []
    result = list(prolog.query("booksAuthorCheaperThanX(Libros,'"+autor+"', "+str(precioDeseado)+", Presupuesto, "+anioBuscado+", Resultado, Combinaciones)"))
    booklist = getBookList(prolog)

    for search in result:
        for i in range(0, len(search["Combinaciones"])):
            combinacion = []
            for j in range(0, len(search["Combinaciones"][i])):
                combinacion.append(search["Combinaciones"][i][j])
            combinaciones.append(combinacion)
    return booklist, combinaciones


#Funcion que retorna la lista de libros
def getBookList(prolog):
    booklist = []
    for search in prolog.query("holding_books(X)"):
        booklist.append(search["X"])
    return booklist

#Funcion que retorna todas las combinaciones posibles de una lista
def getCombinations(booklist):
    combinationList = []
    for L in range(0, len(booklist) + 1):
        for subset in itertools.combinations(booklist, L):
            # print(list(subset))
            combinationList.append(list(subset))
    return combinationList

def getBoughtBooks(prolog):
    booklist=[]
    for search in prolog.query("libros_comprados(Libro,_)"):
        booklist.append(search["Libro"])
    return booklist

def getCategories(prolog):
    categorias=[]
    for sol in prolog.query("libro(_,Categories,_,_,_,_,_)"):
        for cat in sol["Categories"]:
            if str(cat) not in categorias:
                categorias.append(str(cat))
        
    return categorias


def setSalary(prolog, salary):
    prolog.retractall("sueldo/1")
    prolog.assertz("sueldo(%s)" % str(salary))    

def getSalary(prolog):
    salary = 0
    for sol in prolog.query("sueldo(Cualto)"):
        salary = sol["Cualto"]

    return salary

def setClavo(prolog, clavo):
    prolog.retractall("entradas_adicionales/1")
    prolog.assertz("entradas_adicionales(%s)" % str(clavo))
    

def getClavo(prolog):
    clavo = 0
    for sol in prolog.query("entradas_adicionales(Cualto)"):
        clavo = sol["Cualto"]

    return clavo



#main()