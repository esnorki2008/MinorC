class Optimo:
    def __init__(self):
        pass

    def quitar_etiquetas_sin_saltos(self,lst:[]):
        salida = []
        etiquetas = []
        saltos = []
        for cada in lst :
            if cada.find(":") != -1:
                etiquetas.append(cada)
            elif cada.find("goto") != -1:
               saltos.append((cada.split("goto")[1]).replace(";","").strip())

        eti_perm = []
        eti_perm.append("main:")
        for eti in etiquetas:
            for sal in saltos:
                if eti.find(sal)!=-1:
                    eti_perm.append(eti)
                    break


        for cada in lst :
            if cada.find(":") != -1:
                for eq in eti_perm:
                    if eq ==cada:
                        salida.append(cada)
                        break
            else:
                salida.append(cada)

        return salida