from pyswip import Prolog
import itertools

def main():
    prolog = Prolog()
    prolog.consult("projectoFinal")

    #regla1(prolog,500,200)
    #regla2(prolog, 300, "'drama'", 3)
    #regla3(prolog, "usado", 50)
    regla4(prolog, 50, "marcos de mota", "ciencia ficcion", "hola")



def regla1(prolog, extramoney, days):
    finalList = []
    list(prolog.query("booksXDaysOldTops(Libros,"+str(extramoney)+","+str(days)+",Resultado,Presupuesto)"))
    booklist = getBookList(prolog)

    combinationList = getCombinations(booklist)

    # Verifica cuales combinaciones son validas
    for combination in combinationList:
        preciototal = 0
        for item in combination:
            for search in prolog.query("libro('%s', Categoria, Rating, Autor, Fecha, Precio, Condicion)" % item):
                preciototal += search["Precio"]
        for queryResult in prolog.query("booksStarsCategoryExtraMoney(Libros,"+str(extramoney)+","+str(days)+",Resultado,Presupuesto)"):
            if preciototal <= queryResult["Presupuesto"]:
                if len(combination) is not 0:
                    finalList.append(combination)
    print(finalList)


def regla2(prolog, extramoney, categoria, rating):
    booklist = []
    finalList = []
    list(prolog.query("booksStarsCategoryExtraMoney(Libros, "+str(extramoney)+", "+categoria+", "+str(rating)+", Resultado, Presupuesto)"))
    for search in prolog.query("holding_books(X)"):
        booklist.append(search["X"])
        #print(search["X"])

    combinationList = getCombinations(booklist)

    #Verifica cuales combinaciones son validas
    for combination in combinationList:
        preciototal = 0
        for item in combination:
            for search in prolog.query("libro('%s', Categoria, Rating, Autor, Fecha, Precio, Condicion)" % item):
                preciototal += search["Precio"]
        for queryResult in prolog.query("booksStarsCategoryExtraMoney(Libros, "+str(extramoney)+", "+categoria+", "+str(rating)+", Resultado, Presupuesto)"):
            if preciototal <= queryResult["Presupuesto"]:
                if len(combination) is not 0:
                    finalList.append(combination)
    print(finalList)

def regla3(prolog, condicion, porcentaje):
    booklist = []
    finalList = []
    list(prolog.query("booksUsed50PercentMoreCategories(Libros,"+condicion+","+str(porcentaje)+",Resultado,Presupuesto)"))
    for search in prolog.query("holding_books(X)"):
        booklist.append(search["X"])
        #print(len(list(search["Categoria"])))

    combinationList = getCombinations(booklist)
    # Verifica cuales combinaciones son validas
    for combination in combinationList:
        preciototal = 0
        for item in combination:
            for search in prolog.query("libro('%s', Categoria, Rating, Autor, Fecha, Precio, Condicion)" % item):
                preciototal += search["Precio"]

        for queryResult in prolog.query("booksUsed50PercentMoreCategories(Libros,"+condicion+","+str(porcentaje)+",Resultado,Presupuesto)"):
            if preciototal <= queryResult["Presupuesto"]:
                if len(combination) is not 0:
                    finalList.append(combination)
    print(finalList)


def regla4(prolog, porciento, autor, categoria, frase):
    finalList = []
    list(prolog.query("booksEconomyNoCrisisEdward(Libros, "+str(porciento)+", '%s', '%s', '%s', Resultado, Presupuesto)"
                      % (autor, categoria, frase)))
    booklist = getBookList(prolog)

    combinationList = getCombinations(booklist)
    for combination in combinationList:
        preciototal = 0
        for item in combination:
            for search in prolog.query("libro('%s', Categoria, Rating, Autor, Fecha, Precio, Condicion)" % item):
                preciototal += search["Precio"]

        for queryResult in prolog.query("booksEconomyNoCrisisEdward(Libros, "+str(porciento)+", '%s', '%s', '%s', Resultado, Presupuesto)"
                      % (autor, categoria, frase)):
            if preciototal <= queryResult["Presupuesto"]:
                if len(combination) is not 0:
                    finalList.append(combination)
    print(finalList)


def regla5(prolog, categoria, rating, meses):
    finalList = []
    list(prolog.query("booksTripFiveStars(Libros, '%s', "+str(rating)+", "+str(meses)+", Resultado, Presupuesto)") % categoria)
    booklist = getBookList(prolog)

    combinationList = getCombinations(booklist)

    for combination in combinationList:
        preciototal = 0
        for item in combination:
            for search in prolog.query("libro('%s', Categoria, Rating, Autor, Fecha, Precio, Condicion)" % item):
                preciototal += search["Precio"]

        for queryResult in prolog.query("booksTripFiveStars(Libros, '%s', "+str(rating)+", "+str(meses)+", Resultado, Presupuesto)")\
                           % categoria:
            if preciototal <= queryResult["Presupuesto"]:
                if len(combination) is not 0:
                    finalList.append(combination)
    print(finalList)


def regla6(prolog, condicion, precio):
    finalList = []
    list(prolog.query("booksConditionCheap(Libros , "+condicion+", "+str(precio)+", Resultado, Presupuesto)"))
    booklist = getBookList(prolog)

    combinationList = getCombinations(booklist)

    for combination in combinationList:
        preciototal = 0
        for item in combination:
            for search in prolog.query("libro('%s', Categoria, Rating, Autor, Fecha, Precio, Condicion)" % item):
                preciototal += search["Precio"]

        for queryResult in prolog.query("booksConditionCheap(Libros , "+condicion+", "+str(precio)+", Resultado, Presupuesto)"):
            if preciototal <= queryResult["Presupuesto"]:
                if len(combination) is not 0:
                    finalList.append(combination)
    print(finalList)


def regla7(prolog, autor, rating):
    finalList = []
    list(prolog.query("booksAuthorBest(Libros, '%s', "+rating+", Resultado, Presupuesto)") % autor)
    booklist = getBookList(prolog)

    combinationList = getCombinations(booklist)

    for combination in combinationList:
        preciototal = 0
        for item in combination:
            for search in prolog.query("libro('%s', Categoria, Rating, Autor, Fecha, Precio, Condicion)" % item):
                preciototal += search["Precio"]

        for queryResult in prolog.query("booksAuthorBest(Libros, '%s', "+rating+", Resultado, Presupuesto)") % autor:
            if preciototal <= queryResult["Presupuesto"]:
                if len(combination) is not 0:
                    finalList.append(combination)
    print(finalList)


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



main()