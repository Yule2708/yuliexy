print("¡Bienvenido a 'La Isla del Misterio'!")
print("Naufragas en una isla desconocida. A tu alrededor hay una selva densa, una playa desierta y restos de tu barco.\n")
print("INSTRUCCIONES:")
print("- Responde usando SOLO las PALABRAS CLAVE en mayúsculas")
print("- O escribe la LETRA entre paréntesis\n")

# Nivel 1 - Elección inicial
print("¿Qué dirección tomas?")
print("(S) SELVA: Explorar la densa vegetación")
print("(P) PLAYA: Recorrer la orilla")
print("(R) RESTOS: Investigar los restos del barco")

opcion = input("\nEscribe tu elección: ")

if opcion in ["s", "selva"]:
    # Nivel 2 - Rama SELVA
    print("\nAvanzas entre árboles gigantes. De repente encuentras:")
    print("(F) FRUTO: Un extraño fruto brillante")
    print("(C) CUEVA: Una cueva oscura")
    print("(G) SEGUIR: Huellas de animal que puedes seguir")
    
    opcion_selva = input("\n¿Qué investigas? ")
    
    if opcion_selva in ["f", "fruto"]:
        # Nivel 3 - Rama FRUTO
        print("\nAl comer el fruto, obtienes visión nocturna. Ves dos caminos:")
        print("(T) TEMPLO: Un templo antiguo")
        print("(A) ALDEA: Una aldea abandonada")
        
        final = input("\n¿Hacia dónde vas? ")
        if final in ["t", "templo"]:
            print("\n¡Encuentras un tesoro ancestral! Los dioses te bendicen. VIVES para contarlo. (FIN)")
        elif final in ["a", "aldea"]:
            print("\nTe atrapan tribus caníbales. Tu aventura termina aquí. (FIN)")
        else:
            print("\nTe pierdes en la oscuridad. Nunca te encuentran. (FIN)")
    
    elif opcion_selva in ["c", "cueva"]:
        # Nivel 3 - Rama CUEVA
        print("\nDentro de la cueva descubres:")
        print("(P) PINTURAS: Pinturas rupestres")
        print("(U) TUNEL: Un túnel subterráneo")
        
        cueva_opcion = input("\n¿Qué examinas? ")
        if cueva_opcion in ["p", "pinturas"]:
            print("\nDescifras un mapa secreto. ¡Encuentras la civilización perdida! (FIN)")
        elif cueva_opcion in ["u", "tunel"]:
            print("\nEl túnel colapsa. Quedas atrapado para siempre. (FIN)")
        else:
            print("\nUna criatura nocturna te ataca en la oscuridad. (FIN)")
    
    elif opcion_selva in ["g", "seguir"]:
        # Nivel 3 - Rama SEGUIR
        print("\nLas huellas te llevan a:")
        print("(A) AYUDAR: Un jaguar herido")
        print("(B) BOTE: Una cascada con un bote")
        
        huellas_opcion = input("\n¿Qué acción tomas? ")
        if huellas_opcion in ["a", "ayudar"]:
            print("\nEl jaguar te guía a un santuario seguro. ¡Eres adoptado por la manada! (FIN)")
        elif huellas_opcion in ["b", "bote"]:
            print("\nNaufragas en aguas infestadas de tiburones. (FIN)")
        else:
            print("\nPierdes el rastro y mueres de hambre. (FIN)")
    
    else:
        print("\nNo reconoces las señales de la jungla. Te conviertes en presa fácil. (FIN)")

elif opcion in ["p", "playa"]:
    # Nivel 2 - Rama PLAYA
    print("\nEn la arena encuentras una botella con un mensaje y unas extrañas construcciones de arena.")
    print("(B) BOTELLA: Abrir la botella")
    print("(I) PIRAMIDES: Examinar las construcciones")
    
    playa_opcion = input("\n¿Qué investigas? ")
    
    if playa_opcion in ["b", "botella"]:
        # Nivel 3 - Rama BOTELLA
        print("\nEl mensaje muestra coordenadas. Puedes:")
        print("(C) CONSTRUIR: Construir una balsa")
        print("(E) ESPERAR: Esperar rescate")
        
        botella_opcion = input("\n¿Qué decides? ")
        if botella_opcion in ["c", "construir"]:
            print("\n¡Llegas a una ruta comercial! Regresas a casa como héroe. (FIN)")
        elif botella_opcion in ["e", "esperar"]:
            print("\nNadie viene. Te consume la locura. (FIN)")
        else:
            print("\nLa marea alta arrastra tu campamento. (FIN)")
    
    elif playa_opcion in ["i", "piramides"]:
        # Nivel 3 - Rama PIRAMIDES
        print("\nAl excavar encuentras:")
        print("(A) ARTEFACTO: Un artefacto metálico")
        print("(T) TUNEL: Un túnel oculto")
        
        piram_opcion = input("\n¿Qué eliges? ")
        if piram_opcion in ["a", "artefacto"]:
            print("\n¡Activas un mecanismo alienígena! Te teletransportas a otra dimensión. (FIN)")
        elif piram_opcion in ["t", "tunel"]:
            print("\nDescubres una ciudad subterránea llena de oro. (FIN)")
        else:
            print("\nDespiertas a los guardianes de las arenas. (FIN)")
    
    else:
        print("\nPasividad mortal. La deshidratación te gana. (FIN)")

elif opcion in ["r", "restos"]:
    # Nivel 2 - Rama RESTOS
    print("\nEntre los escombros hallas:")
    print("(R) RADIO: Un radio averiado")
    print("(D) DIARIO: El diario del capitán")
    
    restos_opcion = input("\n¿Qué examinas? ")
    
    if restos_opcion in ["r", "radio"]:
        # Nivel 3 - Rama RADIO
        print("\nLogras transmitir SOS. ¿A quién contactas?")
        print("(G) GUARDACOSTAS: Guardacostas locales")
        print("(M) BUQUE: Buque mercante")
        
        radio_opcion = input("\n¿Qué señal envías? ")
        if radio_opcion in ["g", "guardacostas"]:
            print("\n¡Rescate exitoso! Te dan medalla al valor. (FIN)")
        elif radio_opcion in ["m", "buque"]:
            print("\nTe capturan piratas modernos. (FIN)")
        else:
            print("\nLa batería se agota. Sin segunda oportunidad. (FIN)")
    
    elif restos_opcion in ["d", "diario"]:
        # Nivel 3 - Rama DIARIO
        print("\nEl diario revela secretos de la isla:")
        print("(V) VOLCAN: Volcán activo")
        print("(L) LABORATORIO: Laboratorio secreto")
        
        diario_opcion = input("\n¿Qué investigas? ")
        if diario_opcion in ["v", "volcan"]:
            print("\nDescubres cristales de poder. ¡Controlas los elementos! (FIN)")
        elif diario_opcion in ["l", "laboratorio"]:
            print("\nCreas un mutágeno. Te transformas en criatura marina. (FIN)")
        else:
            print("\nIgnoras las advertencias. Un experimento te desintegra. (FIN)")
    
    else:
        print("\nUn remanente explosivo termina tu historia. (FIN)")

else:
    print("\nNo tomas decisión. La isla te absorbe en su eterno misterio. (FIN)")