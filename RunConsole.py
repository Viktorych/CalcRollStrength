from CRS import Parametrs
if __name__ == '__main__':
    param=Parametrs.Рarameters()#Создание класса
    param.Calc()#расчет
    param.Print()#вывод в консоль
    param.SaveToFile("Результат расчета.txt") #сохранение в файл
