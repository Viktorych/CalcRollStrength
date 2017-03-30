import math
import pickle


class Рarameter():
    """Единичный параметр расчета"""
    def __init__(self, id, name, value, ed_izm, types):
        super().__init__()
        self.Id=id# Идентификатор параметра
        self.Name=name#Наименование
        self.Value=value#Значение
        self.Ed_izm=ed_izm#Единица измерения "m<sup>3</sup>"
        self.Type=types # 0-группа, 1-переменная
    def __str__(self):
        return "key={}, Name={}, Value={}, Ed_izm={}, Тип={}".format(self.Id,self.Name,self.Value, self.Ed_izm, self.Type)
    def strConsol(self):
        """Печать параметра в консоль"""
        if self.Type==0:
            return "{}".format(self.Name)
        else:
            return "    {} = {} {}".format(self.Name,self.Value, self.Ed_izm)


class Рarameters:
    """Список параметров расчета"""
    def __init__(self):
        super().__init__()
        self.List = { \
            "qB"    :Рarameter(1,"qВ материала",                1470.00,   "MPa", 1), \
            "Dpp"   :Рarameter(1,"Диаметр перднего подшипника", 0.00,      "mm",1),\
            "Lpp"   :Рarameter(2, "Длина переднего подшипника", 45.00,     "mm", 1), \
            "Dzp"   :Рarameter(3, "Диаметр заднего подшипника", 0.00,      "mm", 1), \
            "Lzp"   :Рarameter(4, "Длина заднего подшипника",   27.00,     "mm", 1), \
            "Dvsr"  :Рarameter(5, "Cредний диаметр валка",      85.00,     "mm", 1), \
            "P"     :Рarameter(6, "Усилие прокатки", 15, "kH", 1), \
            "Dku"   :Рarameter(6, "Диаметр калибрующего участка", 16.00,   "mm", 1), \
            "Lku"   :Рarameter(6, "Длина калибрующего участка", 37.50,   "mm", 1), \
            "Dou"   :Рarameter(6, "Диаметр обжимного участка",  10.00,     "mm", 1), \
            "Lou"   :Рarameter(6, "Длина обжимного участка",    27.5,   "mm", 1), \
            }#параметры для расчетов

        self.ListCalc = {\
            "Dbv"   :Рarameter(8, "Длина бочки валка, Lв", 0, "mm", 1), \
            "L1"    :Рarameter(9, "Длина l1", 0, "mm", 1), \
            "L2"    :Рarameter(10, "Длина l2", 0, "mm", 1), \
            "L"     :Рarameter(10, "Длина l", 0, "mm", 1),\
            "Dsr"   :Рarameter(10, "Диаметр Dср", 0, "mm", 1), \
            "R2": Рarameter(8, "Реакция в опоре 2", 0, "kH", 1), \
            "R1": Рarameter(9, "Реакция в опоре 1", 0, "kH", 1), \
            "Mizg": Рarameter(10, "Изгибающий момент", 0, "kH*m", 1), \
            "Nizg": Рarameter(10, "Напряжение изгиба в бочке вала", 0, "MPa", 1), \
            "Mkruch": Рarameter(10, "Расчет вала на кручение", 0, "kH*m", 1), \
            "Mkruch2": Рarameter(10, "Расчет вала на кручение 2", 0, "MPa", 1), \
            "Mrez": Рarameter(10, "Результирующее напряжение", 0, "MPa", 1), \
            "Usl":Рarameter(10, "Условие", 0, "MPa", 1), \
            "Rezult": Рarameter(10, "Результат", 0, "", 1), \
            }#Расчитанные параметры
        self.ListIndexParam=[]
        for k in self.List.keys():
            self.ListIndexParam.append(self.List[k])
        self.htmlResult=["<b style='color:#00ff00'>Условие выполняется</span></b>", \
                     "<b style='color:#ff0000'>Условие не выполняется</span></b>"]
        self.strResult = ["Условие выполняется", \
                           "Условие не выполняется"]
        self.Result=0


    def __str__(self, *args, **kwargs):
        str="Параметры для расчетов:\n"
        for k in self.List.keys():
            str="{} {}\n".format (str, self.List[k].strConsol())
        str=str+"Расчетные параметры:\n"
        for k in self.ListCalc.keys():
            str = "{} {}\n".format(str, self.ListCalc[k].strConsol())
        str="{} {}".format(str,self.strResult[self.Result])
        return str

    def strWin(self, *args, **kwargs):
        str="<b>Параметры для расчетов:</b><br>"

        for k in self.List.keys():
            str="{} &nbsp;&nbsp;&nbsp;&nbsp; {}</b><br>".format (str, self.List[k].strConsol())
        str=str+"<b>Расчетные параметры:</b><br>"
        for k in self.ListCalc.keys():
            str = "{} &nbsp;&nbsp;&nbsp;&nbsp;{}<br>".format(str, self.ListCalc[k].strConsol())
        str = "{} {}".format(str, self.htmlResult[self.Result])
        return str


    def Calc (self):
        """Расчеты"""
        qB=self.List["qB"].Value
        Dpp=self.List["Dpp"].Value
        Lpp=self.List["Lpp"].Value
        Dzp=self.List["Dzp"].Value
        Lzp=self.List["Lzp"].Value
        Dvsr=self.List["Dvsr"].Value
        Dku=self.List["Dku"].Value
        Lku=self.List["Lku"].Value
        Dou=self.List["Dou"].Value
        Lou=self.List["Lou"].Value
        P=self.List["P"].Value
        Dbv=Lku+Lou
        self.ListCalc["Dbv"].Value=Dbv
        L1=(Lpp/2)+Lou
        self.ListCalc["L1"].Value = L1
        L2=(Lzp/2)+Lku
        self.ListCalc["L2"].Value = L2
        L= L1+L2
        self.ListCalc["L"].Value = L
        Dsr=(Dou+Dku)/2
        self.ListCalc["Dsr"].Value = Dsr
        R2=(P*L2)/(L1+L2)
        self.ListCalc["R2"].Value = round(R2,2)
        R1=P-R2
        self.ListCalc["R1"].Value = round(R1, 2)
        Mizg=R1*(L1/1000)
        self.ListCalc["Mizg"].Value = round(Mizg, 2)
        Nizg=(Mizg/(0.1*(Dvsr/1000)**3))/1000
        self.ListCalc["Nizg"].Value = round(Nizg, 2)
        #=0,5*B10*(1+(D20/D9))
        Mkruch= 0.5*P*(1+((Dsr/1000)/(Dvsr/1000)))
        self.ListCalc["Mkruch"].Value = round(Mkruch, 2)
        #=B31 / (0, 2 * (D9) ^ 3)
        Mkruch2 = (Mkruch / (0.2 * (Dvsr/1000)**3))/1000
        self.ListCalc["Mkruch2"].Value = round(Mkruch2, 2)
        #SQRT((B28) ^ 2 + 0, 75 * (B32) ^ 2)
        Mrez=(math.sqrt((Nizg*1000) ** 2 + 0.75 * (Mkruch2*1000)** 2))/1000
        self.ListCalc["Mrez"].Value = round(Mrez, 2)
        Usl=qB/4
        self.ListCalc["Usl"].Value = round(Usl, 2)
        if Mrez<Usl :
            self.ListCalc["Rezult"].Value = "{} меньше {}".format(round(Mrez, 2),round(Usl, 2))
            self.Result=0
        else:
            self.ListCalc["Rezult"].Value = "{} больше {}".format(round(Mrez, 2), round(Usl, 2))
            self.Result = 1


    def SaveResult (self, file):
        with open(file, 'w', encoding="utf-8", errors="surrogateescape") as f:
            f.write(self.__str__())

    def Save(self, file):
        #ouf = open('datafile.dat', 'w')
        #marshal.dump(self, ouf,1)
        #ouf.close()
        with file:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(self, file, pickle.HIGHEST_PROTOCOL)
        #print(self)

    def Load(self, file):
        #ouf = open('datafile.dat', 'w')
        #marshal.dump(self, ouf,1)
        #ouf.close()
        # fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        #
        # if fname[0]:
        #     # #f = open(fname[0], 'r')
        #     #
        #     # with f:
        #     #     data = f.read()
        #     #     self.textEdit.setText(data)
        #     f = open(fname[0], 'rb')
        with  file:
                # The protocol version used is detected automatically, so we do not
                # have to specify it.
            #print (file)
            new = pickle.load(file)
        self.List=new.List
        #print (self)

    def Print(self):
        """Вывод в консоль"""
        print (self)


