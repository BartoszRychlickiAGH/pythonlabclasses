class Samochod:
    def __init__(self, numer_rejestracyjny, kolor, typ_pojazdu):
        self.numer_rejestracyjny = numer_rejestracyjny
        self.kolor = kolor
        self.typ_pojazdu = typ_pojazdu

    def Wjazd_na_Parking(self, Parking):
        Parking.WjazdNaParking(self.numer_rejestracyjny, self.typ_pojazdu)

    def Wyjazd_z_Parkingu(self, Parking):
        Parking.WyjazdZParkingu(self.numer_rejestracyjny, self.typ_pojazdu)

    def CarOutput(self):
        return (
            "Parametry samochodu: \n"
            + "Numer rejestracyjny: "
            + self.numer_rejestracyjny
            + "\nKolor: "
            + self.kolor
            + "\nTyp pojazdu: "
            + self.typ_pojazdu
        )


class Parking:
    def __init__(self):
        self.MaxBays = 5  # całkowita liczba miejsc
        self.TakenBays = 0  # liczba miejsc zajętych
        self.utarg = 0  # przychód z opłat parkingowych
        self.Osobowe_Rejestracje = []
        self.Cięzarowe_Rejestracje = []
        self.Jednoślad_Rejestracje = []

    def WjazdNaParking(self, numer_rejestracyjny, typ_pojazdu):
        if self.TakenBays < self.MaxBays:
            self.TakenBays += 1
            print(
                "Samochód o numerach rejestracyjnych: "
                + numer_rejestracyjny
                + " wjechał na teren parkingu"
            )
        else:
            print("Brak wolnych miejsc parkingowych")

    def Oplata(self, typ_pojazdu, numer_rejestracyjny):
        match typ_pojazdu:
            case "Jednoślad":
                if numer_rejestracyjny not in self.Jednoślad_Rejestracje:
                    self.Jednoślad_Rejestracje.append(numer_rejestracyjny)
                self.utarg += 5
                return 5
            case "Osobowe":
                if numer_rejestracyjny not in self.Osobowe_Rejestracje:
                    self.Osobowe_Rejestracje.append(numer_rejestracyjny)
                self.utarg += 10
                return 10
            case "Ciezarowe":
                if numer_rejestracyjny not in self.Cięzarowe_Rejestracje:
                    self.Cięzarowe_Rejestracje.append(numer_rejestracyjny)
                self.utarg += 30
                return 30
            case _:
                print("Wprowadzono niepoprawny typ pojazdu")

    def Info(self):
        print("Liczba zajetych miejsc: ", self.MaxBays)

    def WyjazdZParkingu(self, numer_rejestracyjny, typ_pojazdu):
        self.TakenBays -= 1
        print(
            "Samochód o numerach rejestracyjnych: "
            + numer_rejestracyjny
            + " opuścił teren parkingu"
        )
        print("Opłata wynosi:" + str(self.Oplata(typ_pojazdu, numer_rejestracyjny)))


Toyota = Samochod("KR05908", "Czarny", "Osobowe")
Nissan = Samochod("KR19405", "Czarny", "Osobowe")

Yamaha = Samochod("WW45623", "Czarny", "Jednoślad")
Suzuki = Samochod("GDA67549", "Czerwony", "Jednoślad")

Man = Samochod("DW46754", "Niebieski", "Ciezarowe")
Scania = Samochod("SK93854", "Bialy", "Ciezarowe")

parking1 = Parking()


def test1(parking1):
    Toyota.Wjazd_na_Parking(parking1)
    Nissan.Wjazd_na_Parking(parking1)
    Yamaha.Wjazd_na_Parking(parking1)
    Nissan.Wyjazd_z_Parkingu(parking1)
    print("Liczba zajetych miejsc: ", parking1.TakenBays)
    Nissan.Wjazd_na_Parking(parking1)
    Suzuki.Wjazd_na_Parking(parking1)
    Man.Wjazd_na_Parking(parking1)
    print(
        "Ilość miejsc zajętych: ",
        parking1.TakenBays,
        "\nUtarg całkowity: ",
        parking1.utarg,
    )
    Scania.Wjazd_na_Parking(parking1)
    Toyota.Wyjazd_z_Parkingu(parking1)
    Scania.Wjazd_na_Parking(parking1)
    print(
        "Ilość miejsc zajętych: ",
        parking1.TakenBays,
        "\nUtarg całkowity: ",
        parking1.utarg,
    )
    Nissan.Wyjazd_z_Parkingu(parking1)
    Yamaha.Wyjazd_z_Parkingu(parking1)
    Suzuki.Wyjazd_z_Parkingu(parking1)
    Man.Wyjazd_z_Parkingu(parking1)
    Scania.Wyjazd_z_Parkingu(parking1)
    print(
        "Ilość miejsc zajętych: ",
        parking1.TakenBays,
        "\nUtarg całkowity: ",
        parking1.utarg,
    )
    print(
        f"Wszystkie rejestracje: {parking1.Cięzarowe_Rejestracje}{parking1.Osobowe_Rejestracje}{parking1.Jednoślad_Rejestracje}"
    )
    print(f"Rejestracje samochodów ciężarowych: {parking1.Cięzarowe_Rejestracje}")


test1(parking1)
