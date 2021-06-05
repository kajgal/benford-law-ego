# EGO - Prawo Benforda
W celu zrealizowania zadania zdecydowałem się na napisanie skryptu w Pythonie, który pomoże mi wykonać wszystkie niezbędne.
Całość rozwiązania oparłem oczywiście o prawo Benforda, a do ustalenia współczynnika i zdecydowania czy dany zestaw testowy jest prawdopodobnie przekłamany czy wiarygodny wykorzystałem Chi-Square Test.
Do uruchomienia skryptu potrzebujemy jedynie umieszczonych w jednym folderze pliku main.py oraz folder Benford z zestawami danych. Podałbym link do githuba, ponieważ projekt tam umieściłem ale jest obecnie dla pewności prywatny. Jeśli będzie Pan chciał przetestować mój skrypt - z czego bardzo bym się cieszył. To dołączam go do maila.

### Założenia:
1. Linie z zerami są pomijane, ponieważ nie wpływa to drastycznie na ostateczny rezultat i takich linijek trafia się niewiele.
2. Przyjęty poziom istotności dla Chi-Square Testu to 0.05
3. Niesie to za sobą przyjęcie jako wartości krytycznej liczby 15.51
4. Hipoteza zerowa bzmi: Dane z testowanego pliku pasują do rozkładu Benforda
5. Druga hipoteza brzmi: Dane z testowanego pliku nie pasują do rozkładu Benforda
6. Przyjęty rozkład Benforda to [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

### Działanie skryptu:
1. W pętli otwieram każdy plik tekstowy z folderu z danymi do weryfikacji
2. Dla każdego pliku zliczam liczbę linijek z wystąpieniem zera, wykonuje rozkład zgodnie z rozkładem Benforda z pominięciem tych linijek z zerem (takie linijki rzadko się zdarzają, aczkolwiek się zdarzają, ja uczciwie losowałem spośród 800 tyś plików i też mi się czasami trafiała taka linijka)
3. Wykonuje Chi-Square Test dla zestawu danych
4. Dla każdego pliku zostaje stworzony folder o takiej samej nazwie jak plik a w nim umieszczony zostaje plik tekstowy - log z kilkoma ciekawymi informacjami oraz wykres obrazujący porównanie rozkładu dla tego zestawu i rozkładu Benforda
5. Na podstawie przeanalizowanych danych zostaje zapisany plik csv zgodnie z wytycznymi z zadania


### Prywatne obserwacje:
1. Wyszło mi, że 78 plików jest prawdopodobnie poprawnych, zaś 22 prawdopodobnie są oszukane.
2. Mój plik, który wysłałem w ramach poprzednich ćwiczeń przeszedł test uczciwości - załączam wykres wygenerowany przez mój skrypt dla tego pliku oraz plik logu.


### Pytanie:
Przy realizacji zadania poprawiłem z 10 - 15 plików i zastanawiam się czy naprawdę to są pliki podesłane przez studentów (nie wierzę, że ktoś miał problem ze stworzeniem 100 linijkowych plików z liczbą i enterem na końcu) czy może to są pliki dorzucone przez Pana żeby utrudnić trochę zadanie takim osobom jak ja? :)


### Zadanie było bardzo ciekawe i rozwijające, a wpisując się "opisy metody na tyle wyczerpujący, żeby można było go odtworzyć" chyba nic nie wpisuje się lepiej niż napisany program!
