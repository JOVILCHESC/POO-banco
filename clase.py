class Account:
    def __init__(self,run,name,mail,password):
        self.run=run
        self.name=name
        self.mail=mail
        self.balance=0
        self.password=password
    
    def Ingress(self):
        option=int(input("Desea ingresar dinero a su cuenta?(presione(1))para continuar (0)para detener la operacion: "))
        while option!=0:
            
            if option==1:
                new_balance=int(input("Cuanto dinero desea ingresar?: "))
                if new_balance>0:
                    print("Se ha agregado dinero a su cuenta")
                    self.balance=self.balance+new_balance
                    print("Tu nuevo saldo es: "+str(self.balance))
            else:
                print("Debe ingresar un numero valido")
            option=int(input("Desea ingresar dinero a su cuenta?(presione(1))para continuar (0)para detener la operacion: "))
    def print(self):
        print("DATOS DEL CLIENTE")
        print("El nombre del cliente es: "+str(self.name))
        print("El saldo inicial del cliente es: "+str(self.balance))
        print("El run del cliente es: "+str(self.run))
        print("El mail ingresado es: "+str(self.mail))
        
    