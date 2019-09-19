class ImportedCar:
    def max_speed(self):
        pass

### HenesseyVenonGT atinge 270.49 MPH
class HennesseyVenonGT(ImportedCar):
    def max_speed(self):
        # Velocidade dos carros americanos geralmente é medida em MPH (milhas por hora)
        return 270.49

class ImportedCarForBrazilAdapter():
    def __init__(self, adaptee: HennesseyVenonGT) -> None:
        self.adaptee = adaptee

    def max_speed(self):
        return self.adaptee.max_speed() * 1.60934

if __name__ == "__main__":
    hennessey_car = HennesseyVenonGT()
    print("Velocidade máxima de um Hennessey Venon GT é de: {}".format(hennessey_car.max_speed()))

    adapter = ImportedCarForBrazilAdapter(hennessey_car)
    print("Para outros países que usam KM/H, a velocidade máxima de um Hennessey Venon GT é de: {}".format(
        adapter.max_speed()))