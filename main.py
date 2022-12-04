from clase import Account

def main():
    print("CREACION DE LA CUENTA")
    name=input("Ingrese su nombre: ")
    run=input("Ingrese su run: ")
    mail=input("Ingrese mail: ")
    password=input("Ingrese contraseña: ")
    if password!=input("Confirmar contraseña: "):
        raise Exception("LAS CONTRASEÑAS NO COINCIDEN")
    
    registro=Account(run,name,mail,password)
    registro.print()
    registro.Ingress()

if __name__=="__main__":
    main() 
    