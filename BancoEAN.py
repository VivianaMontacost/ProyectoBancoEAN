persona=                 ['clark kent', 'Bruce Wane'   ]
usuario=                 ['superman'  , 'batman'       ]
contraseña=              [1111        , 2222           ] 
numero_de_cuenta=        [ 3115996681 , 32221822       ]
tipo_de_cuenta=          [ 'corriente', 'ahorros'      ] 
dinero=                  [ 1000.00    , 1500.00        ]
rta_pregunta_de_seguridad= ['perro'     , 'murcielago'   ]   
estado_sesion=            ['cerrada'   , 'cerrada'      ] 
'''
print("Estado inicial en el banco")
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
'''
while(True): 
    sesion=False
    while(sesion==False):
        print("\n")
        print("INICIO DE SESIÓN")
        print("ingrese usuario:")
        usuario_ingresado=input()
        print("ingrese contraseña:")
        contraseña_ingresada=input()
        print(contraseña_ingresada)
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

    sesion_terminada=False
    while(sesion_terminada==False):
        print("\n")
        print("ELIJA ALGUNA TRANSACCION POR EL NUMERO:")
        print("1: Consultar saldo")
        print("2: Hacer retiro")
        print("3: Transferir dinero")
        print("4: Cerrar sesión")
        print("5: Estado todas las cuentas del banco")
        opcion=input()
        opcion=int(opcion)

        if opcion in [1,2,3,4,5]:
            indice=usuario.index(usuario_ingresado)
            if estado_sesion[indice] =='activa':
                if  opcion==1:
                    print("Saldo en cuenta",numero_de_cuenta[indice] ,":",dinero[indice] )
                if  opcion==2:
                    print("Digite el valor a retirar:")
                    valor_retiro=input()
                    valor_retiro=int(valor_retiro)
                    if valor_retiro > dinero[indice]:
                        print("Fondos insuficientes")
                    else:
                        dinero[indice]=dinero[indice]-valor_retiro
                        print("Valor retiro:",valor_retiro )
                        print("Saldo en cuenta:",dinero[indice] )
                if  opcion==3:
                    print("Digite el valor de la trasferencia:")
                    valor_trasferencia=input()
                    valor_trasferencia=int(valor_trasferencia)
                    print("Digite la cuenta de destino:")
                    numero_de_cuenta_final=input()
                    numero_de_cuenta_final=int(numero_de_cuenta_final)
                    if valor_trasferencia > dinero[indice]:
                        print("fondos insuficientes")
                    else:
                        if numero_de_cuenta_final in numero_de_cuenta:
                            indice_cta=numero_de_cuenta.index(numero_de_cuenta_final)
                            dinero[indice]=dinero[indice]-valor_trasferencia
                            dinero[indice_cta]=dinero[indice_cta]+valor_trasferencia
                            print("trasferencia exitosa al numero de cuenta:",numero_de_cuenta_final )
                            print("valor trasferencia:",valor_trasferencia)
                            print("saldo en cuenta",numero_de_cuenta[indice] ,":",dinero[indice] )
                        else: 
                            print("la cuenta de destino no existe")
                if  opcion==4:        
                    if estado_sesion[indice] =='activa':
                        estado_sesion[indice] ='cerrada'
                        print("sesion cerrada")
                    else:
                        print("sesion ya está cerrada")
                    sesion_terminada=True

                if  opcion==5:  
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
            else:
                print("sesion no activa, tramite invalido")    
        else:
            print("Opción invalida")