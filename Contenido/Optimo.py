import re


class Optimo:
    lst = []
    #REGLAS SIN USAR
    #2
    #3
    #4
    #5
    #6
    #7

    def __init__(self, lst):
        self.lst = lst
        self.mirilla_regla_m()
    def mirilla_regla_m(self):
        contador = 0
        novo_lista = []
        for cada in self.lst:
            #print(cada)
            if cada.find("=") != -1 and contador > 1:
                div:str = cada.split("=")
                p0=div[0].strip()
                p1 = div[1].replace(";","").strip()

                if self.mirilla_regla_1(p0,p1,contador):
                    pass
                elif self.mirilla_regla_8_11(p0,p1,contador):
                    pass
                elif self.mirilla_regla_12_15(p0,p1,contador):
                    pass
                elif self.mirilla_regla_16_18(p0,p1,contador):
                    pass
                #elif self.repetidos(novo_lista):
                    #pass
                else:
                    novo_lista.append(self.lst[contador])
                    self.repetidos(novo_lista)
                    #print("")

                #elif self.mirilla_regla_8_11(p0,p1,contador,cada):
                #    pass
            else:
                novo_lista.append(self.lst[contador])

            contador = contador + 1
        self.lst = novo_lista

    def repetidos(self,lst_novo):
        tama=len(lst_novo)
        if tama > 2:
            if lst_novo[-1] ==lst_novo[-2]:
                lst_novo.pop(tama-1)
                return False

        return False

    def mirilla_regla_16_18(self,p0,p1,contador):
        subp = p1.split("*")
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_a = f1 == '0'
            param_b = f2 == '0'
            if param_a or param_b:
                self.lst[contador] = p0 + "=0;"
                return False

            param_a = f1 == '2'
            param_b = f2 == '2'
            if param_a:
                self.lst[contador] = p0 + "=" + f2 +" + "+f2 + ";"
                return False
            elif param_b:
                self.lst[contador] = p0 + "=" +  f1 +" + "+f1+ ";"
                return False

        subp = p1.split("/")
        if len(subp) > 1:
            f1 = subp[0].strip()
            param_a = f1 == '0'
            if param_a:
                self.lst[contador] = p0 + "=0;"
                return False

        return False

    def mirilla_regla_12_15(self,p0,p1,contador):
        subp =p1.split("+")
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_a= f1 == '0'
            param_b= f2 == '0'
            if param_a :
                self.lst[contador]=p0+"="+f2+";"
                return False
            elif param_b :
                self.lst[contador]=p0+"="+f1+";"
                return False

        subp = p1.split("-")
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_a = f1 == '0'
            param_b = f2 == '0'
            if param_a:
                self.lst[contador] = p0 + "=" + f2+";"
                return False
            elif param_b:
                self.lst[contador] = p0 + "=" + f1+";"
                return False

        subp = p1.split("*")
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_a = f1 == '1'
            param_b = f2 == '1'
            if param_a:
                self.lst[contador] = p0 + "=" + f2+";"
                return False
            elif param_b:
                self.lst[contador] = p0 + "=" + f1+";"
                return False

        subp = p1.split("/")
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_b = f2 == '1'
            if param_b:
                self.lst[contador] = p0 + "=" + f1+";"
                return False

        return False

    def mirilla_regla_8_11(self,p0,p1,contador):
        subp =p1.split("+")
        f0 = p0.strip()
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_a= f0==f1 or f0==f2
            param_b= f1 == '0' or f2 =='0'
            if param_a and param_b:
                return True

        subp = p1.split("-")
        f0 = p0.strip()
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_a = f0 == f1 or f0 == f2
            param_b = f1 == '0' or f2 == '0'
            if param_a and param_b:
                return True

        subp = p1.split("*")
        f0 = p0.strip()
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_a = f0 == f1 or f0 == f2
            param_b = f1 == '1' or f2 == '1'
            if param_a and param_b:
                return True

        subp = p1.split("/")
        f0 = p0.strip()
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_a = f0 == f1 or f0 == f2
            param_b = f1 == '1' or f2 == '1'
            if param_a and param_b:
                return True

        return False



    def mirilla_regla_1(self,p0,p1,contador):
        div_an: str = self.lst[contador - 1].split("=")
        if len(div_an) == 2:
            a0 = div_an[0].strip()
            a1 = div_an[1].replace(";", "").strip()
            if p0 == a1 and p1 == a0:
                return True
        return False


    def codigo_optimizado(self):
        return self.lst
