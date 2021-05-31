#El administrador del banco tiene nombre de usuario "administrador" y clave "1234"
persona=                 ['clark kent', 'Bruce Wane'   ]
usuario=                 ['superman'  , 'batman'       ]
contraseña=              [1111        , 2222           ] 
numero_de_cuenta=        [ 3115996681 , 32221822     ]
tipo_de_cuenta=          [ 'corriente', 'ahorros'      ] 
dinero=                  [ 1000.00    , 1500.00        ]
rta_pregunta_de_seguridad= ['perro'     , 'murcielago'   ]   
estado_sesion=            ['cerrada'   , 'cerrada'      ] 

#print("Estado inicial en el banco")
#for i in list(range(0,len(persona))):
#    print("\n")
#    print("   persona:",persona[i]) 
#    print("   usuario:",usuario[i]) 
#    print("   contraseña:",contraseña[i]) 
#    print("   numero_de_cuenta:",numero_de_cuenta[i]) 
#    print("   tipo_de_cuenta:",tipo_de_cuenta[i]) 
#    print("   dinero:",dinero[i]) 
#    print("   rta_pregunta_de_seguridad:",rta_pregunta_de_seguridad[i]) 
#    print("   estado_sesion:",estado_sesion[i]) 
#    print("\n")
while(True): 
    sesion = False
    sesion_administrador = False
    while(sesion==False and sesion_administrador==False):
        print("\n")
        print("ELIJA EL NUMERO DE LA ACCION:")
        print("\n")
        print("1. INICIO DE SESIÓN")
        print("2. RECUPERAR CONTRASEÑA DE USUARIO")
        print("3. INGRESO PARA ADMINISTRADOR DEL BANCO")
    
        while(True):
            try:
                opcion=int(input())
                break
            except Exception as error:
                print("Debes digitar una opción valida")
                
        if opcion == 1:
            print("\n")
            print("INICIO DE SESIÓN")
            print("ingrese usuario:")
            usuario_ingresado=input()
            while(True):
                try:
                    contraseña_ingresada=int(input("ingrese contraseña:"))
                    if contraseña_ingresada<0:
                        raise
                    break
                except Exception as error:
                    print("Debes digitar un numero entero y que este sea mayor a 0")
            if usuario_ingresado in usuario:
                indice=usuario.index(usuario_ingresado)
                if contraseña[indice] == int(contraseña_ingresada):
                    estado_sesion[indice] ='activa'
                    print("usuario logueado")
                    sesion=True
                else:
                    print("contraseña invalida")
            else:
                print("usuario no existe")
        elif opcion == 2:
            print("\n")
            print("RECUPERACIÓN DE CONTRASEÑA")
            print("ingrese usuario:")
            usuario_ingresado=input()
            if usuario_ingresado in usuario:   
                print("Pregunta de seguridad ¿Cuál es su animal favorito?")
                print("ingrese su respuesta:")
                rta_seguridad=input()
                indice=usuario.index(usuario_ingresado)
                if rta_pregunta_de_seguridad[indice] == rta_seguridad:
                    print("La contraseña debe ser numérica")
                    while(True):
                        try:
                            contraseña_1=int(input("Digite su nueva contraseña:"))
                            if contraseña_1<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero entero y que este sea mayor a 0")
                    while(True):
                        try:
                            contraseña_2=int(input("Digite la nueva contraseña otra vez:"))
                            if contraseña_2<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero entero y que este sea mayor a 0")
                    if contraseña_1 == contraseña_2:
                        contraseña[indice] = contraseña_1
                        print("Contraseña recuperada correctamente, puede iniciar sesión con su nueva contraseña.")
                    else:
                        print("Las contraseñas no coinciden, debe realizar el proceso de nuevamente.")
                else:
                    print("Respuesta incorrecta")
                
            else:
                print("El usuario ingresado no está en nuestra base de datos")
        if opcion == 3:
            print("\n")
            print("INICIO DE SESIÓN ADMINISTRADOR DEL BANCO")
            print("ingrese usuario:")
            usuario_ingresado=str(input())
            if usuario_ingresado == "administrador":
                while(True):
                    try:
                        contraseña_ingresada=int(input("ingrese contraseña:"))
                        if contraseña_ingresada<0:
                            raise
                        break
                    except Exception as error:
                        print("Debes digitar un numero entero y que este sea mayor a 0")
                    
                if  int(contraseña_ingresada) == 1234:
                    print("\n")
                    print("Bienvenido Administrador")
                    sesion_administrador=True
                else:
                    print("contraseña de usuario administrador es invalida")
            else:
                print("usuario administrador no existe")
        else:
            print("opcion invalida")
           
            
    if sesion==True:
        indice=usuario.index(usuario_ingresado)
        print("\n")
        print("Bienvenido",persona[indice],"al banco EAN")

    while(sesion==True):
        print("\n")
        print("Está en su cuenta",tipo_de_cuenta[indice],"N°",numero_de_cuenta[indice])
        print("\n")
        print("ELIJA ALGUNA TRANSACCION POR EL NUMERO:")
        print("1: Consultar saldo")
        print("2: Consignar dinero")
        print("3: Hacer retiro")
        print("4: Transferir dinero")
        print("5: Cerrar sesión")
        #print("6: Estado todas las cuentas del banco")
        while(True):
            try:
                opcion=int(input())
                break
            except Exception as error:
                print("Debes digitar una opción valida")

        if opcion in [1,2,3,4,5]:
            if estado_sesion[indice] =='activa':
                if  opcion==1:
                    print("Saldo en cuenta",tipo_de_cuenta[indice_cta]," N°",numero_de_cuenta[indice] ,":",dinero[indice] )
                elif  opcion==2:
                    while(True):
                        try:
                            valor_consignacion=float(input("Digite el valor a consignar:"))
                            if valor_consignacion<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero y que este sea mayor a 0")
                    if valor_consignacion > 0:
                        dinero[indice] = dinero[indice] + valor_consignacion
                        print("Consignación exitosa")
                        print("Valor consignado:",valor_consignacion )
                        print("Saldo en cuenta:",dinero[indice] )       
                    else:
                        print("Error en valor ingresado")
                        
                elif  opcion==3:
                    print("Digite el valor a retirar:")
                    while(True):
                        try:
                            valor_retiro=float(input("Digite el valor a retirar:"))
                            if valor_retiro<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero y que este sea mayor a 0")
                    if valor_retiro > dinero[indice]:
                        print("Fondos insuficientes")
                    else:
                        dinero[indice]=dinero[indice]-valor_retiro
                        print("Valor retiro:",valor_retiro )
                        print("Saldo en cuenta:",dinero[indice] )
                elif  opcion==4:
                    while(True):
                        try:
                            valor_trasferencia=float(input("Digite el valor de la trasferencia:"))
                            if valor_trasferencia<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero y que este sea mayor a 0")
                    tipo_de_cuenta_final=str(input("Digite el tipo de cuenta de destino:")).lower()
                    while(True):
                        try:
                            numero_de_cuenta_final=int(input("Digite el numero de cuenta de destino:"))
                            if numero_de_cuenta_final<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero entero y que este sea mayor a 0")
                    if valor_trasferencia > dinero[indice]:
                        print("fondos insuficientes")
                    else:
                        if numero_de_cuenta_final in numero_de_cuenta:
                            indice_cta=numero_de_cuenta.index(numero_de_cuenta_final)
                            if tipo_de_cuenta_final==tipo_de_cuenta[indice_cta]:
                                dinero[indice]=dinero[indice]-valor_trasferencia
                                dinero[indice_cta]=dinero[indice_cta]+valor_trasferencia
                                print("trasferencia exitosa la cuenta",tipo_de_cuenta[indice_cta]," N°",numero_de_cuenta_final )
                                print("valor trasferencia:",valor_trasferencia)
                                print("saldo en cuenta",numero_de_cuenta[indice] ,":",dinero[indice] )
                            else:
                                print("tipo de cuenta incorrecto")
                        else: 
                            print("numero de cuenta no existe")
                elif  opcion==5:        
                    if estado_sesion[indice] =='activa':
                        estado_sesion[indice] ='cerrada'
                        print("sesion cerrada")
                    else:
                        print("sesion ya está cerrada")
                    sesion=False
                else:
                    print("opcion invalida")   
            else:
                print("sesion no activa, tramite invalido")    
        else:
            print("Opción invalida")
            
    while(sesion_administrador==True):
        print("\n")
        print("ELIJA ALGUNA OPCION:")
        print("1: Crear cuenta")
        print("2: Eliminar cuenta")
        print("3: Consultar cuenta")
        print("4: Información todas las cuentas del banco")
        print("5: Aumentar interes diario a cuentas de ahorro")
        print("6: Cerrar sesión de administrador")
 
        while(True):
            try:
                opcion=int(input())
                break
            except Exception as error:
                print("Debes digitar una opción valida")

        if opcion in [1,2,3,4,5,6]:
            if  opcion==1:
                persona_nuevo =   str(input("Ingrese nombre completo de la persona:"))
                usuario_nuevo =   str(input("Ingrese nombre de usuario de la persona:"))
                if usuario_nuevo in usuario:
                    print("El usuario ya existe, solo se permite un nombre de usuario por cuenta. Debe iniciar de nuevo el proceso.")
                else:
                     
                    while(True):
                        try:
                            contraseña_nuevo =  int(input("Ingrese contraseña numerica:"))
                            if contraseña_nuevo<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero entero y que este sea mayor a 0")
                    while(True):
                        try:
                            numero_de_cuenta_nuevo =  int(input("Ingrese numero de cuenta:"))
                            if numero_de_cuenta_nuevo<0:
                                raise
                            break
                        except Exception as error:
                            print("Debes digitar un numero entero y que este sea mayor a 0")
                    if numero_de_cuenta_nuevo in numero_de_cuenta:
                        print("El numero de cuenta ya existe, es un numero unico independiente del tipo de cuenta. Debe iniciar de nuevo el proceso.")
                    else:                   
                        tipo_de_cuenta_nuevo = str(input("Ingrese tipo de cuenta (ahorros o corriente):")).lower()
                        if tipo_de_cuenta_nuevo == "corriente" or tipo_de_cuenta_nuevo == "ahorros":
                            
                            while(True):
                                try:
                                    dinero_nuevo = float(input("Ingrese saldo inicial de la cuenta:")) 
                                    if dinero_nuevo<0:
                                        raise
                                    break
                                except Exception as error:
                                    print("Debes digitar un numero y que este sea mayor a 0")
                            rta_pregunta_de_seguridad_nuevo = str(input("Ingrese respuesta de seguridad a la pregunta ¿Cuál es su animal favorito?:"))
                            estado_sesion_nuevo = "cerrada"
                            
                            print("Los datos de la nueva cuenta fueron ingresados correctamente.")

                            persona.append(persona_nuevo)
                            usuario.append(usuario_nuevo)
                            contraseña.append(contraseña_nuevo)
                            numero_de_cuenta.append(numero_de_cuenta_nuevo)
                            tipo_de_cuenta.append(tipo_de_cuenta_nuevo)
                            dinero.append(dinero_nuevo)
                            rta_pregunta_de_seguridad.append(rta_pregunta_de_seguridad_nuevo)
                            estado_sesion.append(estado_sesion_nuevo)                         
                            
                            print("La cuenta se ha creado exitosamente.")                       
                        else:                    
                            print("Tipo de cuenta incorrecto. Debe iniciar de nuevo el proceso.")

            elif  opcion==2:
                
                while(True):
                    try:
                        numero_de_cuenta_eliminar =  int(input("Ingrese numero de cuenta a eliminar:"))
                        if numero_de_cuenta_eliminar<0:
                            raise
                        break
                    except Exception as error:
                        print("Debes digitar un numero entero y que este sea mayor a 0")
                if numero_de_cuenta_eliminar in numero_de_cuenta:
                    indice = numero_de_cuenta.index(numero_de_cuenta_eliminar)
                    persona.pop(indice)
                    usuario.pop(indice)
                    contraseña.pop(indice)
                    numero_de_cuenta.pop(indice)
                    tipo_de_cuenta.pop(indice)
                    dinero.pop(indice)
                    rta_pregunta_de_seguridad.pop(indice)
                    estado_sesion.pop(indice)  
                    print("La cuenta se ha eliminado exitosamente.") 
                else:    
                    print("El numero de cuenta no existe. Debe iniciar de nuevo el proceso.")
            elif  opcion==3:  
                print("\n")               
                while(True):
                    try:
                        numero_de_cuenta_consulta =  int(input("Digite el numero de cuenta a consultar:"))
                        if numero_de_cuenta_consulta<0:
                            raise
                        break
                    except Exception as error:
                        print("Debes digitar un numero entero y que este sea mayor a 0")
                if numero_de_cuenta_consulta in numero_de_cuenta:
                    indice_cta=numero_de_cuenta.index(numero_de_cuenta_consulta)
                    print("Estado cuenta consultada")
                    i = indice_cta
                    print("\n")
                    print("   persona:",persona[i]) 
                    print("   usuario:",usuario[i]) 
                    print("   contraseña:",contraseña[i]) 
                    print("   numero_de_cuenta:",numero_de_cuenta[i]) 
                    print("   tipo_de_cuenta:",tipo_de_cuenta[i]) 
                    print("   dinero:",dinero[i]) 
                    print("   rta_pregunta_de_seguridad:",rta_pregunta_de_seguridad[i]) 
                    print("   estado_sesion:",estado_sesion[i]) 
                    print("\n")
                else: 
                    print("numero de cuenta consultada no existe")
                            
            elif  opcion==4:  
                print("\n")
                print("Estado cuentas banco")
                for i in list(range(0,len(persona))):
                    print("\n")
                    print("   persona:",persona[i]) 
                    print("   usuario:",usuario[i]) 
                    print("   contraseña:",contraseña[i]) 
                    print("   numero_de_cuenta:",numero_de_cuenta[i]) 
                    print("   tipo_de_cuenta:",tipo_de_cuenta[i]) 
                    print("   dinero:",dinero[i]) 
                    print("   rta_pregunta_de_seguridad:",rta_pregunta_de_seguridad[i]) 
                    print("   estado_sesion:",estado_sesion[i]) 
                    print("\n")
            elif  opcion==5:  
                print("\n")
                print("Diariamente se realiza un aumento de interes del 0.0001 (0.01%) a cada cuenta de ahorro.")

                while(True):
                    try:
                        numero_confirmacion =  int(input("Para confirma incremento de hoy dijite 1, sino dijite 2:"))
                        if 2<numero_confirmacion or numero_confirmacion<1:
                            raise
                        else:   
                            break
                    except Exception as error:
                        print("Dato ingresado incorrecto") 
                        
                if numero_confirmacion==1:  
                    for i in list(range(0,len(tipo_de_cuenta))):
                        if tipo_de_cuenta[i]=="ahorros":
                            dinero[i] = dinero[i]*(1+0.0001)
                    print("Aumento por interes exitoso")
                if numero_confirmacion==2:
                    print("No se realiza aumento por interes")

                    
            elif  opcion==6:   
                sesion_administrador = False
                print("sesion administrador cerrada")

            else:
                print("Opción invalida")