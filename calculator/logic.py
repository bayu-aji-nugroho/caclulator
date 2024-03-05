class operation():

    def __init__(self) -> None:
        self.__mainvalue = 0
        self.ind = 0
        self.index = 0
        self.datasementara = 0
        self.valueInLabel = " "
        self.status = ""

    def onclick(self,value):#value adalah value dari masing masing widget
        self.ind +=1
        if type(value) == int:
            if self.ind > 1:
                self.datasementara = self.datasementara*10 + value
                self.output(self.datasementara)
            else:
                self.output(value)
                self.datasementara +=value
        elif value == "CE":
            self.mainvalue,self.datasementara,self.status,self.index= 0,0,"",0
            self.output(self.datasementara)
        elif value == "=":
            self.mainOperation(self.status)
            self.output(self.__mainvalue)
            self.datasementara,self.status,self.ind = 0,"",0

        elif value =="<-":
            self.datasementara /=10
            self.datasementara = int(self.datasementara)
            self.output(self.datasementara)
        else: 
            self.index +=1
            self.output(value)
            self.algoritma(self.index,value)
            self.datasementara = 0
            self.ind = 0

    
    
    def output(self,newText:str) -> str:
            self.valueInLabel = newText

    def algoritma(self,no,Status):
        if(no==1):#maksudnya program ini dijalankan saat setelah AC
            self.__mainvalue = self.datasementara
            self.status = Status
        else:
            self.mainOperation(self.status)
            self.status = Status

    def mainOperation(self,op):
        match op:
            case "+":self.__mainvalue += self.datasementara
            case "-":self.__mainvalue -= self.datasementara
            case "x":self.__mainvalue *= self.datasementara
            case "/":
                try:#untuk mengatur koma dibelakang angka setelah pembagian
                    val = self.__mainvalue / self.datasementara
                    if (int(val)<float(val)):
                        self.__mainvalue /= self.datasementara
                    elif(int(val)== float(val)):
                        self.__mainvalue /= self.datasementara
                        self.__mainvalue = int(self.__mainvalue)
                except:
                    self.__mainvalue = "tidak bisa dibagi"
    