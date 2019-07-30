from pyswip import Prolog
import itertools

def main():
    prolog = Prolog()
    prolog.consult("projectoFinal")

    #regla1(prolog,500,200)
    regla2(prolog, 1000, "'ciencia ficcion'", 3)
    #regla3(prolog, "usado", 50)
    #regla4(prolog, 50, "marcos de mota", "ciencia ficcion", "hola")



def regla1(prolog, extramoney, days):
    finalList = []
    result = list(prolog.query("booksXDaysOldTops(Libros,"+str(extramoney)+","+str(days)+",Resultado,Presupuesto, Combinaciones)"))
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
   # print(finalList)
    return booklist, result


def regla2(prolog, extramoney, categoria, rating):
    booklist = []
    finalList = []
    result = list(prolog.query("booksStarsCategoryExtraMoney(Libros, "+str(extramoney)+", "+categoria+", "+str(rating)+", Resultado, Presupuesto, Combinaciones)"))
    for search in prolog.query("holding_books(X)"):
        booklist.append(search["X"])
    for search in prolog.query("booksStarsCategoryExtraMoney(Libros, "+str(extramoney)+", "+categoria+", "+str(rating)+", Resultado, Presupuesto, Combinaciones)"):
        print(search["Combinaciones"])


    combinationList = getCombinations(booklist)

    #Verifica cuales combinaciones son validas
    for combination in combinationList:
        preciototal = 0
        for item in combination:
            for search in prolog.query("libro('%s', Categoria, Rating, Autor, Fecha, Precio, Condicion)" % item):
                preciototal += search["Precio"]
        for queryResult in prolog.query("booksStarsCategoryExtraMoney(Libros, "+str(extramoney)+", "+categoria+", "+str(rating)+", Resultado, Presupuesto, Combinaciones)"):
            if preciototal <= queryResult["Presupuesto"]:
                if len(combination) is not 0:
                    finalList.append(combination)
    #print(finalList)
    return booklist, result

def regla3(prolog, condicion, porcentaje):
    booklist = []
    finalList = []
    result = list(prolog.query("booksUsed50PercentMoreCategories(Libros,"+condicion+","+str(porcentaje)+",Resultado,Presupuesto, Combinaciones)"))
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

        for queryResult in prolog.query("booksUsed50PercentMoreCategories(Libros,"+condicion+","+str(porcentaje)+",Resultado,Presupuesto, Combinaciones)"):
            if preciototal <= queryResult["Presupuesto"]:
                if len(combination) is not 0:
                    finalList.append(combination)
    #print(finalList)
    return booklist, result


def regla4(prolog, porciento, autor, categoria, frase):
    finalList = []
    result = list(prolog.query("booksEconomyNoCrisisEdward(Libros, "+str(porciento)+", '%s', '%s', '%s', Resultado, Presupuesto, Combinaciones)"
                      % (autor, categoria, frase)))
    booklist = getBookList(prolog)

    combinationList = getCombinations(booklist)
    for combination in combinationList:
        preciototal = 0
        for item in combination:
            for search in prolog.query("libro('%s', Categoria, Rating, Autor, Fecha, Precio, Condicion)" % item):
                preciototal += search["Precio"]

        for queryResult in prolog.query("booksEconomyNoCrisisEdward(Libros, "+str(porciento)+", '%s', '%s', '%s', Resultado, Presupuesto, Combinaciones)"
                      % (autor, categoria, frase)):
            if preciototal <= queryResult["Presupuesto"]:
                if len(combination) is not 0:
                    finalList.append(combination)
    #print(finalList)
    return booklist, result


def regla5(prolog, categoria, rating, meses):
    finalList = []
    result = list(prolog.query("booksTripFiveStars(Libros, '%s', "+str(rating)+", "+str(meses)+", Resultado, Presupuesto, Combinaciones)") % categoria)
    booklist = getBookList(prolog)

    combinationList = getCombinations(booklist)

    for combination in combinationList:
        preciototal = 0
        for item in combination:
            for search in prolog.query("libro('%s', Categoria, Rating, Autor, Fecha, Precio, Condicion)" % item):
                preciototal += search["Precio"]

        for queryResult in prolog.query("booksTripFiveStars(Libros, '%s', "+str(rating)+", "+str(meses)+", Resultado, Presupuesto, Combinaciones)")\
                           % categoria:
            if preciototal <= queryResult["Presupuesto"]:
                if len(combination) is not 0:
                    finalList.append(combination)
    #print(finalList)
    return booklist, result


def regla6(prolog, condicion, precio):
    finalList = []
    result = list(prolog.query("booksConditionCheap(Libros , "+condicion+", "+str(precio)+", Resultado, Presupuesto, Combinaciones)"))
    booklist = getBookList(prolog)

    combinationList = getCombinations(booklist)

    for combination in combinationList:
        preciototal = 0
        for item in combination:
            for search in prolog.query("libro('%s', Categoria, Rating, Autor, Fecha, Precio, Condicion)" % item):
                preciototal += search["Precio"]

        for queryResult in prolog.query("booksConditionCheap(Libros , "+condicion+", "+str(precio)+", Resultado, Presupuesto, Combinaciones)"):
            if preciototal <= queryResult["Presupuesto"]:
                if len(combination) is not 0:
                    finalList.append(combination)
    #print(finalList)
    return booklist, result


def regla7(prolog, autor, rating):
    finalList = []
    result = list(prolog.query("booksAuthorBest(Libros, '%s', "+rating+", Resultado, Presupuesto, Combinaciones)") % autor)
    booklist = getBookList(prolog)

    combinationList = getCombinations(booklist)

    for combination in combinationList:
        preciototal = 0
        for item in combination:
            for search in prolog.query("libro('%s', Categoria, Rating, Autor, Fecha, Precio, Condicion)" % item):
                preciototal += search["Precio"]

        for queryResult in prolog.query("booksAuthorBest(Libros, '%s', "+rating+", Resultado, Presupuesto, Combinaciones)") % autor:
            if preciototal <= queryResult["Presupuesto"]:
                if len(combination) is not 0:
                    finalList.append(combination)
    print(finalList)
    return booklist, result


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