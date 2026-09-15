from abc import ABC, abstractmethod

# --- CLASE ABSTRACTA PADRE ---
class Personaje(ABC):
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    @abstractmethod
    def atacar(self, objetivo):
        pass

    @abstractmethod
    def hacer_sonido(self):
        pass

# --- CLASE HIJA: STEVE ---
class Steve(Personaje):
    def __init__(self):
        super().__init__("Steve", 100)
        self.daño_base = 8  # Daño de ataque de Steve

    def atacar(self, objetivo):
        print(f"¡{self.nombre} ataca a {objetivo.nombre} con su espada!")
        objetivo.vida -= self.daño_base
        print(f"-> ¡Le has hecho {self.daño_base} de daño a {objetivo.nombre}!")

    def hacer_sonido(self):
        print(f"{self.nombre}: ¡Oof! (Sonido de esfuerzo)")

# --- CLASE INTERMEDIA: MOB ---
class Mob(Personaje):
    def __init__(self, nombre, vida, daño_base, sonido, forma_de_ataque, drop):
        super().__init__(nombre, vida)
        self.daño_base = int(daño_base)
        self.__arma = None  
        self.sonido = sonido
        self.forma_de_ataque = forma_de_ataque
        self.drop = drop

    @property
    def arma(self):
        return self.__arma

    @arma.setter
    def arma(self, nueva_arma):
        self.__arma = nueva_arma  # Formato: ("Nombre del arma", daño_extra)

    @property
    def daño(self):
        daño_extra = self.__arma[1] if self.__arma else 0
        return self.daño_base + daño_extra

# --- CLASES HIJAS DE MOB ---
class Zombie(Mob):
    def __init__(self):
        super().__init__("Zombie", 20, 3, "Groooaaannn", "Muerde", "Carne podrida")

    def atacar(self, objetivo):
        print(f"¡{self.nombre} {self.forma_de_ataque} a {objetivo.nombre}!")
        objetivo.vida -= self.daño
        print(f"-> {objetivo.nombre} recibe {self.daño} de daño.")

    def hacer_sonido(self):
        print(f"{self.nombre} gime: {self.sonido}")

class Esqueleto(Mob):
    def __init__(self):
        super().__init__("Esqueleto", 15, 4, "Clack clack", "Dispara flechas", "Huesos")

    def atacar(self, objetivo):
        print(f"¡{self.nombre} {self.forma_de_ataque} a {objetivo.nombre}!")
        objetivo.vida -= self.daño
        print(f"-> {objetivo.nombre} recibe {self.daño} de daño.")

    def hacer_sonido(self):
        print(f"{self.nombre} cruje: {self.sonido}")

class Creeper(Mob):
    def __init__(self):
        super().__init__("Creeper", 10, 8, "Sssssss", "Explota", "Pólvora")

    def atacar(self, objetivo):
        print(f"¡{self.nombre} corrió hacia {objetivo.nombre} y {self.forma_de_ataque}!")
        objetivo.vida -= self.daño
        print(f"-> {objetivo.nombre} recibe {self.daño} de daño.")

    def hacer_sonido(self):
        print(f"{self.nombre} sisea: {self.sonido}")


# --- INICIALIZACIÓN DEL JUEGO ---
steve = Steve()
mobs = [Zombie(), Esqueleto(), Creeper()]

# Equipar armas a los mobs
mobs[0].arma = ("Espada de Hierro", 2)
mobs[1].arma = ("Arco Encantado", 3)
mobs[2].arma = ("TNT Extra", 4)

print("=== ¡COMIENZA LA BATALLA MINECRAFT! ===")

# --- COMBATE INTERACTIVO ---
while steve.vida > 0 and len(mobs) > 0:
    print("\n--- ESTADO ACTUAL ---")
    print(f" Tu vida (Steve): {steve.vida}")
    print("Elige a qué mob quieres atacar:")
    
    # Mostrar menú de mobs vivos
    for i, mob in enumerate(mobs):
        arma_nombre = mob.arma[0] if mob.arma else "Sin arma"
        print(f"  [{i + 1}] {mob.nombre} (Vida: {mob.vida}) | Arma: {arma_nombre}")
    
    opcion = input("\nIngresa el número del mob (o escribe 'salir'): ")
    
    if opcion.lower() == 'salir':
        print("¡Te has retirado de la batalla con cobardía!")
        break
        
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(mobs):
        print(" Opción inválida. Inténtalo de nuevo.")
        continue
        
    indice_elegido = int(opcion) - 1
    mob_objetivo = mobs[indice_elegido]
    
    print("\n--- TURNO DE STEVE ---")
    steve.atacar(mob_objetivo)
    
    # Comprobar si el mob murió
    if mob_objetivo.vida <= 0:
        print(f"\n ¡Has derrotado a {mob_objetivo.nombre}! Obtuviste su drop: {mob_objetivo.drop}")
        mobs.pop(indice_elegido)  # Eliminar mob de la lista de vivos
    else:
        print("\n--- TURNO DEL ENEMIGO ---")
        mob_objetivo.hacer_sonido()
        mob_objetivo.atacar(steve)
        
    # Comprobar si Steve murió
    if steve.vida <= 0:
        print("\nGAME OVER : ¡Steve ha perdido toda su vida y ha muerto!")
        break

# Fin del juego si todos los mobs murieron
if len(mobs) == 0 and steve.vida > 0:
    print("\n ¡VICTORIA! Has derrotado a todos los mobs del mundo de Minecraft.")