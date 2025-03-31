#1) implementacja forda-fulkersona

#2) znaleźć maksymalny przepływ w grafie nieskierowanym -> przerobić na skierowany (obie nowe krawędzie mają wagę pierwotnej)
#   -> w reprezentacji macierzonwej od razu tak jest, listowej też

#3) mamy gotowy algorytm forda-fulkersona, mamy wiele źródeł i wiele ujść -> dodajemy wspólne źródło i wspólne ujście ->
# implementacja redukcji,dana lista tupli

#4) spójność krawędziowa - ile minimalnie krawędzi trzeba zniszczyć, żeby go rozspójnić -> graf o wagach 1,ff, wybieramy
# jedno źródło, musimy sprawdzić wszystkie ujścia (w grafie skierowanym trzeba sprawdzić każdy z każdym)

#5) skojarzenie - dodajemy źródło do jednego ze zbiorów, ujście do drugiego,ff -> poprawne bo do każdego wierzchołka
# z A wchodzimy maksymalnie raz i z każdego z B wychodzimy maksymalnie raz

#6) znaleźć skojarzenie w drzewie - graf dwudzielny - na każdym poziomie "zmienia się kolor" -> BFS: dzielimy na zbiory,ff

#7) dany graf skierowany, maksymalna liczba ścieżek, które nie dzielą między sobą wierzchołków -> każdy wierzchołek
# dzielimy na dwa, do jednego wchodzą, z drugiego tylko wychodzą krawędzie, pomiędzy nimi dwie krawędzie - jedna o wadze 1,
# druga o wadze 0, reszta krawędzi w grafie skierowanym ma wagę 1, s i t może zostać

#8) formuły logiczne (określić wartościowanie -> wart poszczególnych zmiennych - normalnie problem NP trudny)
#   -> postać normalna koniunkcyjna, każda zmienna występuje dokładnie dwa razy (raz z negacją, raz be) -> krawędź
#   skierowana w grafie to implikacja (mamy więcej zmiennych niż alternatyw), skojarzenie maksymalne pomiędzy
#   A={a,~a,...} B=((a v b),(b v ~c),...) -> bierzemy te krawędzie, które są w maksymalnym skojarzeniu
#   lub: b) wierzchołkami klauzule, wagi - zmienne bez negacji, trzeba nadać skierowanie tak, by na każdy wierzchołek
#   wskazywała przynajmniej jedna krawędź, jeśli mamy drzewo, to nie da się znaleźć takiego wartościowania, jeśli cykl,
#   to łączymy w kółko, zamieniamy cykl w wierzchołek i uruchamiamy DFS

