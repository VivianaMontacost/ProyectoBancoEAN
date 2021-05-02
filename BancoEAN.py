import pandas as pd
d = {'persona':                    ['clark kent', 'Bruce Wane'   ]
     ,'usuario':                   ['superman'  , 'batman'       ]
     ,'contrasena':                [1111        , 2222           ] 
     ,'numero de cuenta':          [ 3115996681 , 32221822       ]
     ,'tipo de cuenta':            [ 'corriente', 'ahorros'      ] 
     ,'dinero':                    [ 1000.00    , 1500.00        ]
     ,'rta pregunta de seguridad': ['perro'     , 'murcielago'   ]   
     }
df = pd.DataFrame(data=d)
print("Bienvenidos al Banco EAN:")
print()
def inicio_sesion(usuario,contraseña,base_banco_EAN):
    if usuario in base_banco_EAN["usuario"].values:
        indice=base_banco_EAN[base_banco_EAN['usuario']==usuario].index.tolist()[0]
        if base_banco_EAN.loc[[indice],["contraseña"]]["contraseña"].values[0]==contraseña:
            base_banco_EAN.loc[[indice],["estado_sesion"]]='activa'
            print("usuario logueado")
        else:
            print("contraseña invalida")
    else:
        print("usuario no existe")