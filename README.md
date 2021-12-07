# ASC_Proiect_0x00

# Introducere

**Cerința proiectului:**  Scrieți scripturi python encrypt.py/decrypt.py care iau ca parametru în linia de comandă o cheie și un fișier și realizează criptarea/decriptarea XOR folosind cheia dată. Programul va folosi cheia pentru a cripta conținutul fișierului.

---

### Membrii echipei
* Bănilean Alexandru-Ioan (grupa 152) 

* Airinei Andrei-Cristian (grupa 152)

---

# Mod de utilizare

### Mediu de lucru
- Python 3.9.0

### Metoda de rulare
Programul se rulează în modul următor, direct cu interpretatorul python:

Pentru criptare:

```
python3 encrypt.py <parola> <nume_fisier_input> <nume_fisier_output>
```
Pentru decriptare:
  
```
python3 decrypt.py <parola> <nume_fisier_input> <nume_fisier_output>
```

# Partea a doua a proiectului 

<br />

* Numele echipei noastre:  ```Enigma Otiliei```

* Numele echipei adverse:  ```TheGeeks```

* Cheia echipei adverse:  ```patriandreialex```

* [Repo-ul echipei adverse](https://github.com/AlexRus01/Proiect1_ASC)

<br />

---

- [ ] **Cerința 1:** <br /> <br /> Aflați cheia cu care a fost criptat fișierul output al echipei adverse, folosind și fișierul input.

  **Rezolvare:**

    Vom folosi proprietățile matematice ale operației XOR :

    * X ⊕ X = 0
    * 0 ⊕ X = X
    * X ⊕ Y = Y ⊕ X
    * ( X ⊕ Y ) ⊕ Z = X ⊕ ( Y ⊕ Z )

    Astfel, notând input-ul cu I, output-ul cu O și cheia cu K, în problemă apar următoarele:

    * I ⊕ K = O
    * O ⊕ K = I

    Prin urmare, obținem cheia în modul următor:

    I ⊕ O = I ⊕ I ⊕ K = ( I ⊕ I ) ⊕ K = 0 ⊕ K = K

    Am implementat ideea prezentată într-un script [decrypt_cu_input.py](https://github.com/alexbanilean/ASC_Project_0x00/blob/main/decrypt_cu_input.py) care se rulează după sintaxa:

    ```
    python3 decrypt_cu_input.py <nume_fisier_input> <nume_fisier_output>
    ```
---

- [ ] **Cerința 2:** <br /> <br /> Aflați cheia cu care a fost criptat fișierul output al echipei adverse, fără a folosi fișierul input.

   **Rezolvare:**

   Pentru rezolvare folosim faptul că lungimea cheii de criptare este între 10 și 15 caractere. Pentru fiecare lungime din acest interval, parcurgem fișierul pe bucăți de lungime **lungime_cheie** și creăm o listă de dicționare ce reține frecvența caracterelor ce apar pe pozițiile **index % lungime_cheie**, unde index este poziția curentă de parcurgere a fișierului criptat.
   
   Caracterul cu frecvența de apariție cea mai mare în fiecare dicționar îl XOR-ăm cu unul din caracterele ' ', 'a', ' i', 'e', acestea fiind caracterele ce apar [statistic](http://www.cryptogram.org/downloads/words/frequency.html) de cele mai multe ori într-un text în limba română, obținând caracterul corespunzător din posibila cheie de criptare. 
   
   La final, verificăm "potrivirea" fiecărei chei găsite prin calcularea unui procentaj între caracterele care pot apărea într-o cheie validă și numărul total de caractere din fișier, afișând-o pe cea cu procentaj maxim.

    Programul pentru rezolvare [decrypt_fara_input.py](https://github.com/alexbanilean/ASC_Project_0x00/blob/main/decrypt_fara_input.py) se rulează apelându-l în terminal după sintaxa:

    ```
    python3 decrypt_fara_input.py <nume_fisier_binar>
    ```

---

**Mențiuni:** 

Am observat că aplicând operația XOR caracter cu caracter între input-ul recuperat al echipei adverse și output-ul criptat se obține cheia doar de două ori corect, apoi apare o înșiruire de alte caractere. Acest fapt se datorează unui bug din script-ul de criptare, nici input-ul recuperat nefiind identic cu cel inițial. Prin urmare, script-ul folosit pentru rezolvarea celei de-a doua cerințe nu a găsit cheia corectă. Totuși, am folosit output-ul echipei ```The Robotors```, iar cheia folosită de aceștia este
```parola121alorap``` și am testat și cu alte output-uri.

# Articole folosite
- [Parametri din terminal](https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/)
