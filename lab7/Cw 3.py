# Przewoźnik chce przewieźć grupę k turystów z miasta A do miasta B, między tymi miastami jest wiele miast, i
# pomiędzy tymi miastami jeżdżą autobusy o różnej pojemności. Mamy Graf połączeń w postaci trójek [x,y,c],
# x-y miasta, c - pojemność autobusu na tej trasie. Przewodnik musi wyznaczyć wspólną trasę dla wszystkich turystów,
# musi w związku z tym ich podzielić na grupki tak, żeby każda grupka mogła przebyć trase bez rozdzielania się, podaj
# algorytm który wylicza na ile grupek trzeba podzielić turystów (największa przepustowość ale bez Dijkstry żeby było
# śmiesznie)

#Перевезення з міста А до міста Б туристів кількості К, по дорозі їздять автобуси, кожне ребро це певна кількість
#туристів, які тут можна перевезти
#Перевізник має знайти трасу, щоб перевезти 15 туристів, поділивши туристів на групи (шукаємо такий варіант, щоб
#впихнути якнайбільше на них людей)

#Sortowaniwe względem wagi
#{A}, {B}, {C}, {D}, {E}, {F}