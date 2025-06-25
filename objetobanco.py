from datetime import date

class Cuenta:
    def __init__(self, nrocuenta=0, titular='', fapertura=None, activa=False, saldo=0):
        self.nro_de_cuenta = nrocuenta
        self.titular = titular  # Este atributo almacenará el DNI del titular
        self.fecha_apertura = fapertura.strftime("%d-%m-%Y") if fapertura else date.today().strftime("%d-%m-%Y")
        self.activa = activa
        self.saldo = saldo

    def depositar(self, monto):
        if self.activa:
            if monto > 0:
                self.saldo += monto
                return True
        return False

    def extraer(self, monto):
        if self.activa:
            if monto > 0 and monto <= self.saldo:
                self.saldo -= monto
                return True
        return False

    def datos(self):
        return (f'Cuenta: {self.nro_de_cuenta}, Titular (DNI): {self.titular}, '
                f'Fecha de Apertura: {self.fecha_apertura}, '
                f'Activa: {"Sí" if self.activa else "No"}, Saldo: ${self.saldo:.2f}')

    def activar_cuenta(self):
        self.activa = True

    def desactivar_cuenta(self):
        self.activa = False

def menu():
    print("\n--- MENÚ DEL BANCO ---")
    print("1. Alta de cuenta")
    print("2. Depositar")
    print("3. Extraer")
    print("4. Búsqueda por DNI")
    print("5. Activar cuenta")
    print("6. Desactivar cuenta")
    print("7. Imprimir todas las cuentas")
    print("8. Salir")
    opcion = input("Ingrese la opción deseada: ")
    return opcion

cuentas = []

def main():
    while True:
        opcion = menu()
        
        if opcion == '1':
            nrocuenta = int(input("Ingrese el número de cuenta: "))
            dni = input("Ingrese el DNI del titular: ")
            nueva_cuenta = Cuenta(nrocuenta, dni, date.today(), True, 0)
            cuentas.append(nueva_cuenta)
                        
        elif opcion == '2':
            nrocuenta = int(input("Ingrese el número de cuenta para depositar: "))
            monto = float(input("Ingrese el monto a depositar: "))
                
        elif opcion == '3':
            nrocuenta = int(input("Ingrese el número de cuenta para extraer: "))
            monto = float(input("Ingrese el monto a extraer: "))
    
                
        elif opcion == '4':
            dni = input("Ingrese el DNI del titular a buscar: ")
            encontradas = [c for c in cuentas if c.titular == dni]
            
            if encontradas:
                print(f"\n--- CUENTAS ENCONTRADAS PARA DNI {dni} ---")
                for c in encontradas:
                    print(c.datos())
                print(f"Total de cuentas: {len(encontradas)}")
            else:
                print("No se encontraron cuentas con ese DNI.")
                
        elif opcion == '5':
            nrocuenta = int(input("Ingrese el número de cuenta a activar: "))
            
            for c in cuentas:
                if c.nro_de_cuenta == nrocuenta:
                    c.activar_cuenta()
                    print("Cuenta activada exitosamente.")
                    break
            else:
                print("Error: Cuenta no encontrada.")
                
        elif opcion == '6':
            nrocuenta = int(input("Ingrese el número de cuenta a desactivar: "))
            
            for c in cuentas:
                if c.nro_de_cuenta == nrocuenta:
                    c.desactivar_cuenta()
                    print("Cuenta desactivada exitosamente.")
                    break
            else:
                print("Error: Cuenta no encontrada.")
                
        elif opcion == '7':
            if cuentas:
                print("\n--- LISTA DE TODAS LAS CUENTAS ---")
                for c in cuentas:
                    print(c.datos())
                print(f"\nTotal de cuentas: {len(cuentas)}")
            else:
                print("No hay cuentas registradas.")
                
        elif opcion == '8':
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()