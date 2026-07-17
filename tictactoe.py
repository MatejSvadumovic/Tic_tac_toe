import math

def isprintaj_plocu(ploca):
    print("\n")
    for i in range(3):
        # Spajamo tri polja u jedan red odvojen okomitim crtama
        red = [ploca[i*3 + j] if ploca[i*3 + j] != " " else str(i*3 + j) for j in range(3)]
        print(" " + " | ".join(red) + " ")
        if i < 2:
            print("---+---+---")
    print("\n")

# Provjera ima li pobjednika
def provjeri_stanje(ploca):
    # Moguće pobjedničke kombinacije
    pobjede = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Vodoravno
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Okomito
        [0, 4, 8], [2, 4, 6] # Dijagonalno
    ]
    
    for kombinacija in pobjede:
        if ploca[kombinacija[0]] == ploca[kombinacija[1]] == ploca[kombinacija[2]] != " ":
            return ploca[kombinacija[0]] # Vraća 'X' ili 'O'
            
    if " " not in ploca:
        return "Izjednačeno"
        
    return None # Igra još traje

def minimax(ploca, dubina, is_max):
    rezultat = provjeri_stanje(ploca)
    
    # Ako je računalo ('O') pobijedilo
    if rezultat == "O":
        return 10 - dubina
    # Ako je čovjek ('X') pobijedio
    if rezultat == "X":
        return dubina - 10
    # Ako je izjednačeno
    if rezultat == "Izjed2načeno":
        return 0

    if is_max:
        najbolji_skor = -math.inf
        for i in range(9):
            if ploca[i] == " ":
                ploca[i] = "O"
                skor = minimax(ploca, dubina + 1, False)
                ploca[i] = " "
                najbolji_skor = max(skor, najbolji_skor)
        return najbolji_skor
    else:
        najbolji_skor = math.inf
        for i in range(9):
            if ploca[i] == " ":
                ploca[i] = "X"
                skor = minimax(ploca, dubina + 1, True)
                ploca[i] = " "
                najbolji_skor = min(skor, najbolji_skor)
        return najbolji_skor

def najbolji_potez_ai(ploca):
    najbolji_skor = -math.inf
    potez = -1
    for i in range(9):
        if ploca[i] == " ":
            ploca[i] = "O"
            skor = minimax(ploca, 0, False)
            ploca[i] = " "
            if skor > najbolji_skor:
                najbolji_skor = skor
                potez = i
    return potez

# --- GLAVNA IGRA ---

def pokreni_igru():
    # Inicijalizacija prazne ploče s 9 mjesta
    ploca = [" "] * 9
    
    print("=== DOBRODOŠLI U KRIŽIĆ-KRUŽIĆ ===")
    print("1. Igraj protiv prijatelja (2. igrača)")
    print("2. Igraj protiv računala ")
    
    izbor = input("Odaberi mod (1 ili 2): ").strip()
    while izbor not in ["1", "2"]:
        izbor = input("Pogrešan unos. Odaberi 1 ili 2: ").strip()
        
    trenutni_igrac = "X" # Igrač X uvijek igra prvi
    
    while True:
        isprintaj_plocu(ploca)
        
        # Ako igra računalo i red je na 'O' u modu 2
        if izbor == "2" and trenutni_igrac == "O":
            print("Računalo (O) razmišlja...")
            potez = najbolji_potez_ai(ploca)
            ploca[potez] = "O"
        else:
            # Unos igrača
            while True:
                try:
                    potez = int(input(f"Igrač ({trenutni_igrac}), unesi broj polja (0-8): "))
                    if potez < 0 or potez > 8:
                        print("Broj mora biti između 0 i 8!")
                    elif ploca[potez] != " ":
                        print("To polje je već zauzeto! Probaj ponovno.")
                    else:
                        break
                except ValueError:
                    print("Molimo unesi ispravan broj.")
            
            ploca[potez] = trenutni_igrac
        # Provjera završetka nakon svakog poteza
        stanje = provjeri_stanje(ploca)
        if stanje:
            isprintaj_plocu(ploca)
            if stanje == "Izjednačeno":
                print("Igra je završila izjednačeno! (D)")
            else:
                print(f"Pobjednik je igrač {stanje}! (W / L)")
            break
        # Zamjena igrača
        trenutni_igrac = "O" if trenutni_igrac == "X" else "X"

if __name__ == "__main__":
    pokreni_igru()
else:
    print("Error")