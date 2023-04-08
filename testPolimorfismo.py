from Empleado import Empleado
from Gerente import Gerente


def Imprimir(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar())
    if isinstance(objeto,Gerente):
     print(objeto.departamento)

empleado = Empleado("Mario",2341)
Imprimir(empleado)

gerente= Gerente("Andrea", 1231, "Contable")
Imprimir(gerente)