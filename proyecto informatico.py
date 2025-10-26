"""Proyecto 8 “Adivina el Número”:

● La computadora elige un número al azar.
● El usuario intenta adivinarlo con pistas (“más alto” / “más bajo”).

● Contar intentos.

Proyecto 5 “Juego de Preguntas”:

● Usar una lista o diccionario con preguntas y respuestas.
● Contar cuántas acierta el jugador.
● Mostrar puntaje final.

Menu
    interactivo para elegir el proyecto a ejecutar."""

def Adivina_el_Numero():
    import random
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego!")
    print("Deberas adivinar el numero que he pensado, entre el 1 y el 100.")
    print("Tienes intentos ilimitados")
    print()
    print("¡Disfruta el juego!")
    print()

    while not adivinado:
        intento = int(input("Introduce tu numero: "))
        intentos += 1

        if intento < numero_secreto:
            print("Mas alto.")
        elif intento > numero_secreto:
            print("Mas bajo.")
        else:
            adivinado = True
            print("¡Felicidades adivinaste!, el numero era", numero_secreto, "y usaste", intentos, "intentos.")

    print("Desea seguir jugando o ir al menu?")
    continuar = input("Introduce 'jugar' para seguir jugando o 'menu' para ir al menu: ")
    if continuar.lower() == 'jugar':
        Adivina_el_Numero()
    elif continuar.lower() == 'menu':
        Menu()
    else:
        print("Opción no válida.")
        Menu()

def Juego_de_Preguntas():
    preguntas = {
        "¿Cuál es la capital de Francia?": "paris",
        "¿Cual es el planeta mas grande del sistema solar?": "jupiter",
        "¿Cual es el rio mas largo del mundo?": "nilo",
        "¿Cuantos huesos tiene el cuerpo humano?": "206",
        "¿Cual es el pais mas grande del mundo?": "rusia",
        "¿Cual es el oceano mas grande del mundo?": "pacifico",
        "¿Cuando termino la segunda guerra mundial?": "1945",
        "¿Que son los humanos, omnivoros, herbivoros o carnivoros?": "omnivoros",
        "¿Cuantas patas tiene una araña?": "8",
        "¿Cual es el animal mas rapido del mundo?": "guepardo",
        "¿Que pesa mas, un kilo de plumas o un kilo de plomo? (plumas, plomo o ninguno)": "ninguno"

    }

    puntaje = 0

    print("¡Bienvenido al juego de preguntas!")
    for pregunta, respuesta in preguntas.items():
        respuesta_usuario = input(pregunta + " ")
        if respuesta_usuario.lower() == respuesta.lower():
            print("¡Correcto!")
            puntaje += 1
        else:
            print("Incorrecto. La respuesta correcta es:", respuesta)

    print("Tu puntaje final es:", puntaje)

def Besarse():
    print("""
                       .,;;x+nxnnnn,,.
                   .;XXHHMM!!%M??!!?MXMX;,
                  ;!X?XXXXdXXTS!!!?MM!HXMX.
               .<!MH@MM??????M88BB8$$MURMM!;
             .!XMM!!!!MMMMXWWW@@H?????R$U?$Xx
            ;!!??!!!!"';!XX?M$$NWX'<:<'??M!R5!;
           <!!!!'' ;;!!!!!!??T$$$$H!!!!!:':`!M!!;
          <!!!!';XH!!!!!!'!!!!XMRT?!!'<'':.  4H!';
         !'''<';X!!!''  ..  `'"TTM%!':<>.XXh .!' <;;
        !! '<''J!!!'  :Xx ! ..:<!!!!!'' X$$5X'</'!!!!
       <'`'''  ''     !!XxL<!H!!!!!!!''X$$$$X:;<X!!!!'
       ' <''      .X! !!>XX'' '!'uuuid$$$$$5P:?M!>!-'
      '!!''`  .id$d5XL`X%!?XsuJJ$$$$F????XX!`<!'!'';>));<!!!!;;-.
      ':''.<X55$$$$$X!:!!Xd3$$$$$$$$X-x> `!'    .;!!?;;<XXX!!!!!!!:
       .;!XX5$$$$$$$X?!!HX$$$$33X$$$F;,,;!"    :);,,,`''<!!!!!!!!!!!:.
  :sL :!XXXd$$$$$$$$F'!!X53XXX3JJJXSX!XXX    <:JX$$$$$$o.';<<!XX!!X!!!!
 xX$3`!5$$55$$$$$$$5!`!!3$$3333X??SX!XX$!   .XYX$$$$$$$$$h <;<!!?!!!!X!!
'!X3$%<555XX55$$$$$!!:`!?X$3XXt3$3XXL?"?>  'XF""?$$$$$$$P"!!!!);<!!!XXX!h
X.XX3X,?dXXXdd$55$XX!!!.!!XXXdX?<"?X!' ,uuc$$f:h;?$$$$C" :!!XHXX!;!X!!HX!.
fX!X%''<??HX5X5ddXXbi:''`!!X$$X!h; "'  ?3$$$C.`?t$$$$$!``!!?XHHX!!;;t!XH!!
:'''sL'i `X555$5X??X?`    `!X$dXf"    =JUX3$$$$$$$$$$$$r `!?!!!!!!!!!X!!!!
; 'c`$ $b:`XX$$5!!'`       `'??'    .'??$33$$$$$$$$$$$$ :,:,)!':':'!<!)!!!
's $:?k`$L:`!X5!:<!     :          xx)Xx3$3$$$$$$$$$$C ''!!!!XXXXX!!!!!!!!
 4,?h`$ ?$ :!?XXX'     '!<::.     `X$$$$2$$$$$$$$$$$$L. < `!!!!!??!!!!!!!X
.`b'$,$h`$h .!XRXX!.  ' !X5HX!,    `"?T?$$$$$$$$$$$$5d":>` ::`'"!!!!!!!XXH
>`$`$h`$L?$h`'XXXdXX  '-!55$XXXHx:     `'"?5$$$$$5??$bh?)h>~ <!!:.`'!!!!??
! XF)$i$$$$$.<&X$$X!   :XXX$$$$55XX:.   );,(((()idX3u.?(:    ;!!!!!:<<(:<!
X !$X$$$$$$$F!`X$$5!  >X!555$$$$$$XX!:  !X5$J5X$$$$$$$$X':;:;;!!!!!XX;!X!;
$.`33X$$$$$$b!>!X5X .<U5$5$$$$$$$$$$hX: `X$$$$$$$$?????".:;!!;;!XXX!!?;!H!
d! X$$$$$$$5f'L!!?' !JJ$$$$$$5$$$$$$$X! '!X$2??,xndMMMMr'::!!!<!X!?!?X!;?!
X!:?3$$$$$$5fxX`!' <X55$$$$$$$XXX5X5X!!  `?;nHMMMMMMMMMF::;!!!!;;!!;!!XXt;
?U! "X$$$$$X !T'' X5$$$$$5$$$5XXXXX!!''.nMMMMMMMMPP")JWx :;!!X<!;:!!;!XHH1
X!.. <XF",e ecc: <X6X$$5$$$$$55X!!`,xnMMMMMMPP))ndMMMMMM:`:;!XX!!)<!?!!HH5
!!X' .,xdP";$$$;<ST5$55$$$$$$$$5! 4MMMMMP?)ndMMMMMMMMMMMMx :;!XX!!;!!!!XHH
!',xW$$P",??",uu,"$555XX$$5$$??!' `P"(xdMMMMMMMMMMMMMMMMMMh :;!!!!!'!/!?X!
  !$$$$znsd$$$P"` ?XX?XXS9$555?'  :nMMMMMMMMMMMMMMMMMMMMMMMh `;!!!X!:!!!H!
 <H$$$5X$$$$Xud8$$ ?Xd5$$X?T?'',mMM?MMMMMMMMMMMMMMMMMMMMMMMMX ;!:X?!%`!!!!
.!X$$$$$$$5$X$P"',.`?Xd??!" uXbXnmnMMMMMMMMMMMMMMMMMMMMMMMMMM>:<;<!!X!:!!'
!!XX$$$$X$$d$ndd$P" !!?!':MMMMMMMMMMMSMMMMMMMMMMMMMMMMMMMMMMM> `;:!!H!!:!'
!!X$X$$$$$$U$$F",yc <'':MMMMMMMMMM2MMMMMMMMMMMMMMMMMMMMMMMMMM>`;:;;!!!!!;'
!!X$$$$$$$$$$$$P?"" .xMMMMMMMHMCMMMMMMSMMMMMMMMMXMMMMMMMTMMMM'.:;::'''''''
!??$$$$$$$P'`..nnMMxMMMMMMHMMMMMMM?XMMMMMMMSXHMMMMMMNHHUWMMMM :(;;''!!'''
!!!>>>'`..nnMMMMM)MMMMMMhMMMMMMSHMMMMMMSHHMMMMMMM2HXWSMMMMMMM `'''`'
      nHMMMMMMM?dMMMMM!MMMMTXMMMMMSXMMMMMMMMMNTX5XSMMMMMMMMMM
`. .  MMMMMMMP)MMMMMMXMMMMMMMMMSMMMMMMMMMT?!XXHMMMMMTMMMMMMM!
;:  . !MMMMMMXMMMMHMMMMMMMMHSMMMMMMMMM?!XX!M?!XXHWMMMMMMMMMMf
,;.`  `?MMMF(MMMMMMMMMMMHSMMMMMMM?!XX!M?XXHHMMMMMMMMMMMMMMMM
;:.:  . ` ''!?MMMMMMMMHMMMMMP?!X!??XX!!?????!?MMMUMMMMMMMMMP
;.:;  ..`    ~?MMMMMHMMM"())n!SX!!??!!XXHHMHMMMMMMMMMMMXMMM'
;;`.`   . `.   `?T""!)!+MSM!!??!!!!?"?""<'!SMMMMMMM?MMHMMMM
;;,;:`,: .:  .`  -=""'?""````  ..::::)X!!!xn2MMMMMMMMPSTTPT""")

def Menu():
    print("1. Proyecto 8 “Adivina el Número”")
    print("2. Proyecto 5 “Juego de Preguntas”")
    print("3. Besarse")
    eleccion = input("Elige el proyecto a ejecutar (1, 2 o 3): ")
    print()
    if eleccion == '1':
        Adivina_el_Numero()
    elif eleccion == '2':
        Juego_de_Preguntas()
    elif eleccion == '3':
        Besarse()
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
        Menu()

Menu()