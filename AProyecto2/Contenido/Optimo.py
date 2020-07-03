import re


class Optimo:
    lst = []
    lst_reglas_usadas = []
    #REGLAS SIN USAR
    #3
    #4
    #5
    #6
    #7
    #19
    #21
    #22
    #23
    #24
    def __init__(self, lst ,reglas_usadas):
        self.lst = lst
        self.lst_reglas_usadas = reglas_usadas
        self.mirilla_regla_2_20()
        self.mirilla_regla_m()
        #print(id(self.lst_reglas_usadas))
        
    
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
                else:
                    novo_lista.append(self.lst[contador])
                    self.repetidos(novo_lista)
            else:
                novo_lista.append(self.lst[contador])

            contador = contador + 1
        self.lst = novo_lista

    def mirilla_regla_2_20(self):
        return
        contador = 0
        novo_lista = []
        vigilar = None
        pre_vigilar = None
        for cada in self.lst:
            if cada.find("goto") != -1 and cada.find(";") != -1 and cada.find("if") == -1:
                reemp :str=cada.replace("goto","")
                reemp = reemp.replace(";","")
                reemp = reemp.strip()
                vigilar = reemp
                pre_vigilar = cada
            elif cada.find(":") != -1:
                reemp :str=cada.replace(":","")
                reemp = reemp.strip()
                if vigilar != reemp  :
                    if vigilar is not None:
                        novo_lista.append(pre_vigilar)
                    novo_lista.append(self.lst[contador])
                    self.regla_aplicada("Regla 20",contador)
                elif reemp.find("retornos")!=-1:
                    novo_lista.append(self.lst[contador])
                    self.regla_aplicada("Regla 20",contador)
                else:
                    self.regla_aplicada("Regla 2",contador)
                vigilar = None
            else:
                if vigilar is None:
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
                self.regla_aplicada("Regla 17",contador)
                return False

            param_a = f1 == '2'
            param_b = f2 == '2'
            if param_a:
                self.lst[contador] = p0 + "=" + f2 +" + "+f2 + ";"
                self.regla_aplicada("Regla 16",contador)
                return False
            elif param_b:
                self.lst[contador] = p0 + "=" +  f1 +" + "+f1+ ";"
                self.regla_aplicada("Regla 16",contador)
                return False

        subp = p1.split("/")
        if len(subp) > 1:
            f1 = subp[0].strip()
            param_a = f1 == '0'
            if param_a:
                self.lst[contador] = p0 + "=0;"
                self.regla_aplicada("Regla 18",contador)
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
                self.regla_aplicada("Regla 12",contador)
                return False
            elif param_b :
                self.lst[contador]=p0+"="+f1+";"
                self.regla_aplicada("Regla 12",contador)
                return False

        subp = p1.split("-")
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_a = f1 == '0'
            param_b = f2 == '0'
            if param_a:
                self.lst[contador] = p0 + "=" + f2+";"
                self.regla_aplicada("Regla 13",contador)
                return False
            elif param_b:
                self.lst[contador] = p0 + "=" + f1+";"
                self.regla_aplicada("Regla 13",contador)
                return False

        subp = p1.split("*")
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_a = f1 == '1'
            param_b = f2 == '1'
            if param_a:
                self.lst[contador] = p0 + "=" + f2+";"
                self.regla_aplicada("Regla 14",contador)
                return False
            elif param_b:
                self.lst[contador] = p0 + "=" + f1+";"
                self.regla_aplicada("Regla 14",contador)
                return False

        subp = p1.split("/")
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_b = f2 == '1'
            if param_b:
                self.lst[contador] = p0 + "=" + f1+";"
                self.regla_aplicada("Regla 15",contador)
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
                self.regla_aplicada("Regla 8",contador)
                return True

        subp = p1.split("-")
        f0 = p0.strip()
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_a = f0 == f1 or f0 == f2
            param_b = f1 == '0' or f2 == '0'
            if param_a and param_b:
                self.regla_aplicada("Regla 9",contador)
                return True

        subp = p1.split("*")
        f0 = p0.strip()
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_a = f0 == f1 or f0 == f2
            param_b = f1 == '1' or f2 == '1'
            if param_a and param_b:
                self.regla_aplicada("Regla 10",contador)
                return True

        subp = p1.split("/")
        f0 = p0.strip()
        if len(subp) > 1:
            f1 = subp[0].strip()
            f2 = subp[1].strip()
            param_a = f0 == f1 or f0 == f2
            param_b = f1 == '1' or f2 == '1'
            if param_a and param_b:
                self.regla_aplicada("Regla 11",contador)
                return True

        return False



    def mirilla_regla_1(self,p0,p1,contador):
        div_an: str = self.lst[contador - 1].split("=")
        if len(div_an) == 2:
            a0 = div_an[0].strip()
            a1 = div_an[1].replace(";", "").strip()
            if p0 == a1 and p1 == a0:
                self.regla_aplicada("Regla 1",contador)
                return True
        return False

    def regla_aplicada(self,regla,contador):
        enli = "en linea "+str(contador)
        pos_val=""
        if contador < len(self.lst):
            pos_val=self.lst[contador]
        valuar=(regla,enli,pos_val)
        self.lst_reglas_usadas.append(valuar)

    def codigo_optimizado(self):
        return self.lst
