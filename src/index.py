from varasto import Varasto

def tulostatiedot(varasto, varaston_nimi):
    print(f"{varaston_nimi}: {varasto}")

def getterit(varasto, varaston_nimi):
    print(str(varasto) + "getterit:")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")

def setterit(varasto, varaston_nimi):
    print(f"{varaston_nimi} setterit:")
    print("Lisätään 50.7")
    varasto.lisaa_varastoon(50.7)
    tulostatiedot(varasto, varaston_nimi)
    print("Otetaan 3.14")
    varasto.ota_varastosta(3.14)
    tulostatiedot(varasto, varaston_nimi)

def ongelmat_luonti():
    print("Luontiin liittyviä virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def ongelmat_lisays(varasto, varaston_nimi):
    print("Lisäämiseen liittyviä virhetilanteita")
    tulostatiedot(varasto, varaston_nimi)
    print(f"{varaston_nimi}.lisaa_varastoon(1000.0)")
    varasto.lisaa_varastoon(1000.0)
    tulostatiedot(varasto, varaston_nimi)

    print(f"{varaston_nimi}.lisaa_varastoon(-666.0)")
    varasto.lisaa_varastoon(-666.0)
    tulostatiedot(varasto, varaston_nimi)

def ongelmat_otto(varasto, varaston_nimi):
    print("Ottamiseen liittyviä virhetilanteita:")
    tulostatiedot(varasto, varaston_nimi)
    print(f"{varaston_nimi}.ota_varastosta(1000.0)")
    saatiin = varasto.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    tulostatiedot(varasto,varaston_nimi)

    print(f"{varaston_nimi}.otaVarastosta(-32.9)")
    saatiin = varasto.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    tulostatiedot(varasto, varaston_nimi)

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    tulostatiedot(mehua, "mehua")
    tulostatiedot(olutta, "olutta")

    getterit(mehua, "mehua")
    getterit(olutta, "olutta")

    setterit(mehua, "mehua")
    setterit(olutta, "olutta")

    ongelmat_luonti()

    ongelmat_lisays(mehua, "mehua")
    ongelmat_lisays(olutta, "olutta")

    ongelmat_otto(mehua, "mehua")
    ongelmat_otto(olutta, "olutta")

if __name__ == "__main__":
    main()
