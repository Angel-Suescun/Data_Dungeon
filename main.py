import pygame
from config import *
from estructuras.lista import Lista
from estructuras.arreglo import Arreglo
from game.jugador import Jugador
from game.mapa import Mapa
from game.variacionesEnemigos import Esqueleto, Bruja, Golem
from estructuras.cola import Cola
from game.objetos.mision import Mision
from game.objetos.variacionesBuff import *
from game.objetos.variacionesHabilidad import *
from game.objetos.variacionesObjetos import *
from estructuras.nodo import Nodo

jugador = Jugador("Heroe", RUTA_JUGADOR)
mapa = Mapa()
mapa.agregar_ubicacion("Entrada", "assets/images/entrada.png")
mapa.agregar_ubicacion("Sala", "assets/images/sala.png")
mapa.conectar_ubicaciones("Entrada", "Sala")
mapa.establecer_ubicacion_inicial("Entrada")
jugador.posicion_actual = mapa.obtener_ubicacion_actual()
# Inicializar enemigos
enemigos = Lista()
enemigos.agregar(Esqueleto("Esqueleto", 50, mapa.grafo.vertices["Sala"], jugador.inventario, Lista(), Cola(), "assets/images/esqueleto.png"))
enemigos.agregar(Bruja("Bruja", 30, mapa.grafo.vertices["Sala"], jugador.inventario, Lista(), Cola(), "assets/images/bruja.png"))
enemigos.agregar(Golem("Golem", 80, mapa.grafo.vertices["Sala"], jugador.inventario, Lista(), Cola(), "assets/images/golem.png"))

jugador.agregar_mision(Mision("Derrota al Esqueleto", "Derrota al esqueleto en la sala.", False))
jugador.agregar_mision(Mision("Encuentra la Bruja", "Encuentra a la bruja en la sala.", False))
jugador.agregar_mision(Mision("Derrota al Golem", "Derrota al golem en la sala.", False))
jugador.agregar_mision(Mision("Recoge el tesoro", "Recoge el tesoro en la sala.", False))
jugador.agregar_mision(Mision("Habla con el anciano", "Habla con el anciano en la entrada.", False))
jugador.agregar_mision(Mision("Resuelve el acertijo", "Resuelve el acertijo del anciano.", False))

# Habilidades del jugador
golpe_pesado = GolpePesado()
curacion_rapida = CuracionRapida()
doble_golpe = DobleGolpe()
invisibilidad = Invisibilidad()
escudo_energetico = EscudoEnergetico()
regeneracion = Regeneracion()
carga_relampago = CargaRelampago()
ataque_basico = AtaqueBasico()
congelacion = Congelacion()
aumento_velocidad = AumentoVelocidad()
maestria_armas = MaestriaArmas()
jugador.agregar_habilidad("Raíz", ataque_basico)
jugador.agregar_habilidad("Raíz", golpe_pesado)
jugador.agregar_habilidad(ataque_basico, curacion_rapida)
jugador.agregar_habilidad(ataque_basico, doble_golpe)
jugador.agregar_habilidad(ataque_basico, invisibilidad)
jugador.agregar_habilidad(curacion_rapida, escudo_energetico)
jugador.agregar_habilidad(doble_golpe, regeneracion)
jugador.agregar_habilidad(invisibilidad, carga_relampago)
jugador.agregar_habilidad(escudo_energetico, congelacion)
jugador.agregar_habilidad(regeneracion, aumento_velocidad)
jugador.agregar_habilidad(carga_relampago, maestria_armas)
print("Habilidades del jugador:")
jugador.arbol_habilidades.mostrar()

#objetos del jugador
pocion_salud = Pocion("Poción de Salud", "Restaura 50 puntos de salud.", "assets/images/pocion_salud.png", 50)
pocion_mana = Pocion("Poción de Maná", "Restaura 30 puntos de maná.", "assets/images/pocion_mana.png", 30)
llave_oro = Llave("Llave de Oro", "Abre puertas doradas.", "assets/images/llave_oro.png", "Oro")
llave_plata = Llave("Llave de Plata", "Abre puertas plateadas.", "assets/images/llave_plata.png", "Plata")
espada = Arma("Espada de Hierro", "Causa 10 puntos de daño.", "assets/images/espada.png", 10)

# Agregar objetos al inventario del jugador
jugador.agregar_item(pocion_salud)
jugador.agregar_item(pocion_mana)
jugador.agregar_item(llave_oro)
jugador.agregar_item(llave_plata)
jugador.agregar_item(espada)

# Mostrar inventario del jugador
jugador.mostrar_inventario()

# Buffs del jugador
buff_velocidad = BuffVelocidad()
buff_fuerza = BuffFuerza()
buff_defensa = BuffDefensa()
buff_invisibilidad = BuffInvisibilidad()
buff_regeneracion = BuffRegeneracion()
jugador.buff_activos.encolar(buff_velocidad)
jugador.buff_activos.encolar(buff_fuerza)
jugador.buff_activos.encolar(buff_defensa)
jugador.buff_activos.encolar(buff_invisibilidad)
jugador.buff_activos.encolar(buff_regeneracion)
# Mostrar buffs activos
print("Buffs activos del jugador:")
print(jugador.buff_activos)


# Inicializa Pygame
pygame.init()
pantalla = pygame.display.set_mode(TAMANIO_PANTALLA)
pygame.display.set_caption("Data Dungeon - La Leyenda del Héroe Perdido")
clock = pygame.time.Clock()

# Cargar y configurar icono
try:
    icono = pygame.image.load(RUTA_ICONO)
    pygame.display.set_icon(icono)
except pygame.error:
    print("No se pudo cargar el icono, continuando sin él...")

# Cargar imágenes del jugador
try:
    imagen_jugador_original = pygame.image.load(jugador.ruta_imagen)
    imagen_jugador_original = pygame.transform.scale(imagen_jugador_original, (40, 40))
    imagen_jugador_izquierda = pygame.transform.flip(imagen_jugador_original, True, False)
except pygame.error:
    print("No se pudo cargar la imagen del jugador, usando rectángulo...")
    imagen_jugador_original = None
    imagen_jugador_izquierda = None

# Cargar imágenes de las habitaciones
imagenes_habitaciones = {}
for ubicacion in ["Entrada", "Sala"]:
    vertice = mapa.grafo.vertices[ubicacion]
    try:
        imagen = pygame.image.load(vertice.ruta)
        imagen = pygame.transform.scale(imagen, TAMANIO_PANTALLA)
        imagenes_habitaciones[ubicacion] = imagen
    except pygame.error:
        print(f"No se pudo cargar la imagen de {ubicacion}")
        imagenes_habitaciones[ubicacion] = None

# Cargar imágenes de enemigos
imagenes_enemigos = {}
imagenes_habilidades = {}  # Inicializar aquí el diccionario

for i in range(enemigos.obtener_tamano()):
    enemigo = enemigos.obtener_elemento(i)
    try:
        imagen = pygame.image.load(enemigo.ruta)
        imagen = pygame.transform.scale(imagen, (60, 60))
        imagenes_enemigos[enemigo.nombre] = imagen
    except pygame.error:
        print(f"No se pudo cargar la imagen del {enemigo.nombre}")
        imagenes_enemigos[enemigo.nombre] = None

# Cargar imágenes de habilidades
habilidades_para_cargar = [
    ("Ataque Básico", ataque_basico),
    ("Golpe Pesado", golpe_pesado),
    ("Curación Rápida", curacion_rapida),
    ("Doble Golpe", doble_golpe),
    ("Invisibilidad", invisibilidad),
    ("Escudo Energético", escudo_energetico),
    ("Regeneración", regeneracion),
    ("Carga Relámpago", carga_relampago),
    ("Congelación", congelacion),
    ("Aumento Velocidad", aumento_velocidad),
    ("Maestría Armas", maestria_armas)
]

for nombre, habilidad in habilidades_para_cargar:
    try:
        imagen = pygame.image.load(habilidad.ruta_imagen)
        imagen = pygame.transform.scale(imagen, (50, 50))
        imagenes_habilidades[nombre] = imagen
    except (pygame.error, AttributeError):
        print(f"No se pudo cargar la imagen de {nombre}, usando icono por defecto")
        # Crear una imagen por defecto (círculo con texto)
        superficie = pygame.Surface((50, 50), pygame.SRCALPHA)
        color_habilidad = (100, 150, 200) if habilidad.desbloqueada else (80, 80, 80)
        pygame.draw.circle(superficie, color_habilidad, (25, 25), 24)
        pygame.draw.circle(superficie, (255, 255, 255), (25, 25), 24, 2)
        imagenes_habilidades[nombre] = superficie

# Variables del juego
pos_jugador_x = 400
pos_jugador_y = 500
velocidad = 3
mirando_izquierda = False
rect_jugador = pygame.Rect(pos_jugador_x, pos_jugador_y, 40, 40)

# Variables de enemigos y combate
enemigos_activos = []
tiempo_movimiento_enemigos = 0
intervalo_movimiento = 120  # frames entre movimientos
enemigo_seleccionado = None
en_combate = False
turno_jugador = True
mensaje_combate = ""
tiempo_mensaje_combate = 0

# Sistema de experiencia y nivel
experiencia_jugador = 0
nivel_jugador = 1
experiencia_necesaria = 100

# Variables de UI
mostrar_dialogo = True
dialogo_actual = 0
mostrar_inventario = False
mostrar_habilidades = False
mostrar_misiones = False
fuente_dialogo = pygame.font.SysFont("Arial", 16)
fuente_titulo = pygame.font.SysFont("Arial", 24, bold=True)
fuente_pequena = pygame.font.SysFont("Arial", 12)

# Variables para tooltips y árbol de habilidades visual
pos_mouse = (0, 0)
habilidad_hover = None
tooltip_timer = 0

# Historia y diálogos
dialogos_historia = [
    "🏰 Bienvenido a Data Dungeon, valiente héroe...",
    "📜 Has llegado a las ruinas de un antiguo castillo",
    "⚔️ Se dice que dentro habitan criaturas místicas",
    "💎 Y que un gran tesoro aguarda al final...",
    "🚪 Usa WASD o las flechas para moverte",
    "🎯 Presiona ESPACIO para interactuar",
    "📋 Presiona I para inventario, H para habilidades, M para misiones",
    "⚔️ Haz clic en un enemigo para atacar",
    "🎮 ¡Que comience la aventura!"
]

# Inicializar enemigos activos para la Sala
def inicializar_enemigos_sala():
    global enemigos_activos
    enemigos_activos = []
    posiciones_iniciales = [(150, 200), (500, 300), (650, 150)]
    
    for i in range(min(enemigos.obtener_tamano(), 3)):
        enemigo = enemigos.obtener_elemento(i)
        enemigo_data = {
            'enemigo': enemigo,
            'x': posiciones_iniciales[i][0],
            'y': posiciones_iniciales[i][1],
            'rect': pygame.Rect(posiciones_iniciales[i][0], posiciones_iniciales[i][1], 60, 60),
            'direccion_x': 1 if i % 2 == 0 else -1,
            'direccion_y': 1 if i % 3 == 0 else -1,
            'vivo': True
        }
        enemigos_activos.append(enemigo_data)

# Zonas especiales (puertas de transición)
zona_puerta_sala = pygame.Rect(375, 50, 50, 30)  # Puerta arriba en la entrada

# Estados del juego
jugador_en_combate = False
mensaje_transicion = ""
tiempo_mensaje = 0

def dibujar_dialogo(pantalla, texto, y_pos):
    """Dibuja un cuadro de diálogo en la pantalla"""
    # Fondo del diálogo
    dialogo_rect = pygame.Rect(50, y_pos, TAMANIO_PANTALLA[0] - 100, 60)
    pygame.draw.rect(pantalla, (0, 0, 0, 180), dialogo_rect)
    pygame.draw.rect(pantalla, COLOR_BORDES, dialogo_rect, 2)
    
    # Texto del diálogo
    texto_surface = fuente_dialogo.render(texto, True, COLOR_TEXTO)
    pantalla.blit(texto_surface, (60, y_pos + 20))

def dibujar_hud(pantalla):
    """Dibuja la interfaz de usuario"""
    # Información del jugador
    vida_texto = f"❤️ Vida: {jugador.vida}/{jugador.vida}"
    ubicacion_texto = f"📍 Ubicación: {mapa.obtener_ubicacion_actual()}"
    nivel_texto = f"⭐ Nivel: {nivel_jugador} | XP: {experiencia_jugador}/{experiencia_necesaria}"
    
    vida_surface = fuente_dialogo.render(vida_texto, True, COLOR_TEXTO)
    ubicacion_surface = fuente_dialogo.render(ubicacion_texto, True, COLOR_TEXTO)
    nivel_surface = fuente_dialogo.render(nivel_texto, True, COLOR_TEXTO)
    
    pantalla.blit(vida_surface, (10, 10))
    pantalla.blit(ubicacion_surface, (10, 35))
    pantalla.blit(nivel_surface, (10, 85))
    
    # Barra de experiencia
    exp_rect = pygame.Rect(10, 110, 200, 10)
    pygame.draw.rect(pantalla, (50, 50, 50), exp_rect)
    exp_fill = int((experiencia_jugador / experiencia_necesaria) * 200)
    if exp_fill > 0:
        pygame.draw.rect(pantalla, (0, 255, 255), pygame.Rect(10, 110, exp_fill, 10))
    
    # Mostrar habilidades desbloqueadas
    habilidades_desbloqueadas = sum(1 for h in [ataque_basico, golpe_pesado, curacion_rapida, doble_golpe, invisibilidad] if h.desbloqueada)
    habilidades_texto = f"🗡️ Habilidades: {habilidades_desbloqueadas}/11"
    hab_surface = fuente_dialogo.render(habilidades_texto, True, COLOR_TEXTO)
    pantalla.blit(hab_surface, (10, 60))
    
    # Mostrar controles
    controles = "I: Inventario | H: Habilidades | M: Misiones | 1: Curar | 2: Invisibilidad"
    ctrl_surface = fuente_pequena.render(controles, True, COLOR_TEXTO)
    pantalla.blit(ctrl_surface, (10, TAMANIO_PANTALLA[1] - 25))
    
    # Mostrar mensaje de combate
    if tiempo_mensaje_combate > 0 and mensaje_combate:
        combate_surface = fuente_dialogo.render(mensaje_combate, True, (255, 255, 0))
        pantalla.blit(combate_surface, (300, 10))

def dibujar_inventario(pantalla):
    """Dibuja la barra de inventario en la parte inferior"""
    if not mostrar_inventario:
        return
    
    # Fondo del inventario
    inv_rect = pygame.Rect(50, TAMANIO_PANTALLA[1] - 150, TAMANIO_PANTALLA[0] - 100, 100)
    pygame.draw.rect(pantalla, (0, 0, 0, 200), inv_rect)
    pygame.draw.rect(pantalla, COLOR_BORDES, inv_rect, 2)
    
    # Título
    titulo = fuente_titulo.render("🎒 INVENTARIO", True, COLOR_TEXTO)
    pantalla.blit(titulo, (60, TAMANIO_PANTALLA[1] - 145))
    
    # Instrucciones
    instruccion = fuente_pequena.render("Click en un objeto para usarlo", True, (150, 150, 150))
    pantalla.blit(instruccion, (60, TAMANIO_PANTALLA[1] - 125))
    
    # Dibujar items
    x_offset = 60
    y_offset = TAMANIO_PANTALLA[1] - 110
    
    for i in range(jugador.inventario.tamano):
        nodo = jugador.inventario.get_nodo(i)
        
        if nodo is None or nodo.valor is None:
            continue
        
        item = nodo.valor
        
        # Cuadro del item
        item_rect = pygame.Rect(x_offset, y_offset, 80, 60)
        pygame.draw.rect(pantalla, (40, 40, 40), item_rect)
        pygame.draw.rect(pantalla, COLOR_BORDES, item_rect, 1)
        
        # Guardar rect para clicks
        item.rect_ui = item_rect
        
        # Nombre del item
        nombre_surface = fuente_pequena.render(item.nombre[:8], True, COLOR_TEXTO)
        pantalla.blit(nombre_surface, (x_offset + 2, y_offset + 45))
        
        # Tipo de objeto
        tipo_color = (0, 255, 0) if hasattr(item, 'cantidad_recuperacion') else (255, 255, 0) if hasattr(item, 'danio') else (100, 150, 255)
        tipo_rect = pygame.Rect(x_offset + 2, y_offset + 2, 76, 40)
        pygame.draw.rect(pantalla, tipo_color, tipo_rect, 2)
        
        x_offset += 85
        if x_offset > TAMANIO_PANTALLA[0] - 150:
            break

def usar_objeto_inventario(pos_click):
    """Usa un objeto del inventario cuando se hace click en él"""
    global mensaje_combate, tiempo_mensaje_combate
    
    for i in range(jugador.inventario.tamano):
        nodo = jugador.inventario.get_nodo(i)
        
        if nodo is None or nodo.valor is None:
            continue
            
        item = nodo.valor
        
        if hasattr(item, 'rect_ui') and item.rect_ui.collidepoint(pos_click):
            # Usar poción de salud
            if hasattr(item, 'cantidad_recuperacion'):
                vida_anterior = jugador.vida
                jugador.vida = min(jugador.vida + item.cantidad_recuperacion, 100)  # Máximo 100 de vida
                vida_ganada = jugador.vida - vida_anterior
                mensaje_combate = f"❤️ Usaste {item.nombre}: +{vida_ganada} vida"
                tiempo_mensaje_combate = 120
                
                # Remover del inventario (poción consumida)
                jugador.inventario.eliminar(i)
                return
            
            # Usar poción de maná (si implementas sistema de maná)
            elif "Maná" in item.nombre:
                mensaje_combate = f"💙 Usaste {item.nombre}: Maná restaurado"
                tiempo_mensaje_combate = 120
                jugador.inventario.eliminar(i)
                return
            
            # Equipar arma
            elif hasattr(item, 'danio'):
                mensaje_combate = f"⚔️ Equipaste {item.nombre}: +{item.danio} daño"
                tiempo_mensaje_combate = 120
                # Aquí podrías agregar lógica para equipar el arma
                return
            
            # Usar llave u otros objetos
            else:
                mensaje_combate = f"🔑 Seleccionaste {item.nombre}"
                tiempo_mensaje_combate = 120
                return

def dibujar_habilidades(pantalla):
    """Dibuja el árbol de habilidades visual con imágenes y tooltips"""
    global habilidad_hover, tooltip_timer
    
    if not mostrar_habilidades:
        return
    
    # Fondo
    hab_rect = pygame.Rect(100, 100, TAMANIO_PANTALLA[0] - 200, TAMANIO_PANTALLA[1] - 200)
    pygame.draw.rect(pantalla, (0, 0, 0, 220), hab_rect)
    pygame.draw.rect(pantalla, COLOR_BORDES, hab_rect, 2)
    
    # Título
    titulo = fuente_titulo.render("🌳 ÁRBOL DE HABILIDADES", True, COLOR_TEXTO)
    pantalla.blit(titulo, (120, 110))
    
    # Definir estructura del árbol visual
    # Cada habilidad tiene: nombre, objeto_habilidad, posicion_x, posicion_y, padres
    estructura_arbol = [
        # Nivel 0 - Raíz
        {"nombre": "Ataque Básico", "hab": ataque_basico, "x": 400, "y": 160, "padres": []},
        {"nombre": "Golpe Pesado", "hab": golpe_pesado, "x": 500, "y": 160, "padres": []},
        
        # Nivel 1 - Hijos de Ataque Básico
        {"nombre": "Curación Rápida", "hab": curacion_rapida, "x": 300, "y": 240, "padres": ["Ataque Básico"]},
        {"nombre": "Doble Golpe", "hab": doble_golpe, "x": 400, "y": 240, "padres": ["Ataque Básico"]},
        {"nombre": "Invisibilidad", "hab": invisibilidad, "x": 500, "y": 240, "padres": ["Ataque Básico"]},
        
        # Nivel 2 - Hijos de nivel 1
        {"nombre": "Escudo Energético", "hab": escudo_energetico, "x": 250, "y": 320, "padres": ["Curación Rápida"]},
        {"nombre": "Regeneración", "hab": regeneracion, "x": 400, "y": 320, "padres": ["Doble Golpe"]},
        {"nombre": "Carga Relámpago", "hab": carga_relampago, "x": 550, "y": 320, "padres": ["Invisibilidad"]},
        
        # Nivel 3 - Hijos finales
        {"nombre": "Congelación", "hab": congelacion, "x": 250, "y": 400, "padres": ["Escudo Energético"]},
        {"nombre": "Aumento Velocidad", "hab": aumento_velocidad, "x": 400, "y": 400, "padres": ["Regeneración"]},
        {"nombre": "Maestría Armas", "hab": maestria_armas, "x": 550, "y": 400, "padres": ["Carga Relámpago"]},
    ]
    
    # Dibujar conexiones primero
    for nodo in estructura_arbol:
        for padre_nombre in nodo["padres"]:
            # Encontrar el nodo padre
            padre = next((n for n in estructura_arbol if n["nombre"] == padre_nombre), None)
            if padre:
                # Dibujar línea de conexión
                color_linea = (100, 255, 100) if nodo["hab"].desbloqueada and padre["hab"].desbloqueada else (80, 80, 80)
                pygame.draw.line(pantalla, color_linea, 
                               (padre["x"] + 25, padre["y"] + 50), 
                               (nodo["x"] + 25, nodo["y"]), 3)
    
    # Dibujar nodos
    habilidad_hover = None
    mouse_pos = pygame.mouse.get_pos()
    
    for nodo in estructura_arbol:
        habilidad = nodo["hab"]
        x, y = nodo["x"], nodo["y"]
        
        # Crear rectángulo del nodo
        nodo_rect = pygame.Rect(x, y, 50, 50)
        
        # Determinar color y estado
        if habilidad.desbloqueada:
            color_borde = (0, 255, 0)
            alpha = 255
        else:
            color_borde = (128, 128, 128)
            alpha = 150
            
        # Verificar hover
        is_hover = nodo_rect.collidepoint(mouse_pos)
        if is_hover:
            habilidad_hover = habilidad
            color_borde = (255, 255, 0)  # Amarillo en hover
            
        # Dibujar imagen de habilidad
        imagen = imagenes_habilidades.get(nodo["nombre"])
        if imagen:
            # Aplicar transparencia si no está desbloqueada
            if not habilidad.desbloqueada:
                imagen_alpha = imagen.copy()
                imagen_alpha.set_alpha(alpha)
                pantalla.blit(imagen_alpha, (x, y))
            else:
                pantalla.blit(imagen, (x, y))
        else:
            # Dibujar círculo por defecto
            color_fondo = (100, 150, 200) if habilidad.desbloqueada else (60, 60, 60)
            pygame.draw.circle(pantalla, color_fondo, (x + 25, y + 25), 24)
        
        # Dibujar borde
        pygame.draw.rect(pantalla, color_borde, nodo_rect, 3)
        
        # Nombre debajo del nodo
        nombre_surface = fuente_pequena.render(nodo["nombre"][:8], True, COLOR_TEXTO)
        texto_rect = nombre_surface.get_rect(center=(x + 25, y + 65))
        pantalla.blit(nombre_surface, texto_rect)
        
        # Indicador de estado
        estado = "✓" if habilidad.desbloqueada else "✗"
        estado_color = (0, 255, 0) if habilidad.desbloqueada else (255, 100, 100)
        estado_surface = fuente_pequena.render(estado, True, estado_color)
        pantalla.blit(estado_surface, (x + 40, y + 5))
    
    # Dibujar tooltip si hay hover
    if habilidad_hover:
        dibujar_tooltip_habilidad(pantalla, habilidad_hover, mouse_pos)

def dibujar_tooltip_habilidad(pantalla, habilidad, pos_mouse):
    """Dibuja un tooltip con la descripción de la habilidad"""
    # Crear el texto del tooltip
    lineas = [
        f"🗡️ {habilidad.nombre}",
        f"📝 {habilidad.descripcion}",
        f"🔓 {'Desbloqueada' if habilidad.desbloqueada else 'Bloqueada'}"
    ]
    
    # Calcular tamaño del tooltip
    max_ancho = max(fuente_dialogo.size(linea)[0] for linea in lineas)
    alto_tooltip = len(lineas) * 20 + 10
    ancho_tooltip = max_ancho + 20
    
    # Posicionar tooltip cerca del mouse pero dentro de la pantalla
    tooltip_x = min(pos_mouse[0] + 15, TAMANIO_PANTALLA[0] - ancho_tooltip - 10)
    tooltip_y = max(pos_mouse[1] - alto_tooltip - 15, 10)
    
    # Dibujar fondo del tooltip
    tooltip_rect = pygame.Rect(tooltip_x, tooltip_y, ancho_tooltip, alto_tooltip)
    pygame.draw.rect(pantalla, (0, 0, 0, 200), tooltip_rect)
    pygame.draw.rect(pantalla, (255, 255, 255), tooltip_rect, 2)
    
    # Dibujar texto
    y_offset = tooltip_y + 5
    for linea in lineas:
        color_texto = (255, 255, 255)
        if "Desbloqueada" in linea:
            color_texto = (0, 255, 0) if habilidad.desbloqueada else (255, 100, 100)
        
        texto_surface = fuente_dialogo.render(linea, True, color_texto)
        pantalla.blit(texto_surface, (tooltip_x + 10, y_offset))
        y_offset += 20

def dibujar_misiones(pantalla):
    """Dibuja la lista de misiones"""
    if not mostrar_misiones:
        return
    
    # Fondo
    mis_rect = pygame.Rect(100, 100, TAMANIO_PANTALLA[0] - 200, TAMANIO_PANTALLA[1] - 200)
    pygame.draw.rect(pantalla, (0, 0, 0, 220), mis_rect)
    pygame.draw.rect(pantalla, COLOR_BORDES, mis_rect, 2)
    
    # Título
    titulo = fuente_titulo.render("📋 MISIONES", True, COLOR_TEXTO)
    pantalla.blit(titulo, (120, 110))
    
    # Lista de misiones
    y_pos = 150
    for i in range(jugador.misiones.obtener_tamano()):
        mision = jugador.misiones.obtener_elemento(i)
        color = (0, 255, 0) if mision.completada else (255, 255, 255)
        estado = "✓" if mision.completada else "○"
        texto = f"{estado} {mision.titulo}"
        
        mis_surface = fuente_dialogo.render(texto, True, color)
        pantalla.blit(mis_surface, (120, y_pos))
        
        # Descripción
        desc_surface = fuente_pequena.render(f"   {mision.descripcion}", True, (200, 200, 200))
        pantalla.blit(desc_surface, (120, y_pos + 15))
        
        y_pos += 40
        if y_pos > TAMANIO_PANTALLA[1] - 150:
            break

def dibujar_buffs(pantalla):
    """Dibuja la cola de buffs activos"""
    if jugador.buff_activos.esta_vacia():
        return
    
    # Fondo para buffs
    buff_rect = pygame.Rect(TAMANIO_PANTALLA[0] - 200, 10, 180, 100)
    pygame.draw.rect(pantalla, (0, 0, 0, 150), buff_rect)
    pygame.draw.rect(pantalla, COLOR_BORDES, buff_rect, 1)
    
    # Título
    titulo = fuente_dialogo.render("✨ BUFFS ACTIVOS", True, COLOR_TEXTO)
    pantalla.blit(titulo, (TAMANIO_PANTALLA[0] - 195, 15))
    
    # Acceder a los buffs directamente sin modificar la cola
    # Usar la representación interna de la cola para leer sin modificar
    current_node = jugador.buff_activos.frente
    y_pos = 40
    contador = 0
    
    # Recorrer los nodos de la cola sin desencolar
    while current_node is not None and contador < 3:
        buff = current_node.valor
        buff_text = f"• {buff.nombre}"
        buff_surface = fuente_pequena.render(buff_text, True, (0, 255, 150))
        pantalla.blit(buff_surface, (TAMANIO_PANTALLA[0] - 190, y_pos))
        y_pos += 20
        contador += 1
        current_node = current_node.siguiente

def dibujar_enemigos(pantalla):
    """Dibuja y actualiza los enemigos en la sala actual"""
    global tiempo_movimiento_enemigos
    
    ubicacion_actual = mapa.obtener_ubicacion_actual()
    
    if ubicacion_actual == "Sala":
        # Actualizar movimiento de enemigos
        tiempo_movimiento_enemigos += 1
        if tiempo_movimiento_enemigos >= intervalo_movimiento:
            tiempo_movimiento_enemigos = 0
            mover_enemigos()
        
        # Dibujar enemigos
        for enemigo_data in enemigos_activos:
            if not enemigo_data['vivo']:
                continue
                
            enemigo = enemigo_data['enemigo']
            imagen_enemigo = imagenes_enemigos.get(enemigo.nombre)
            
            # Highlight si está seleccionado
            if enemigo_seleccionado == enemigo_data:
                pygame.draw.rect(pantalla, (255, 255, 0), 
                                (enemigo_data['x'] - 5, enemigo_data['y'] - 5, 70, 70), 3)
            
            if imagen_enemigo:
                pantalla.blit(imagen_enemigo, (enemigo_data['x'], enemigo_data['y']))
            else:
                # Dibujar rectángulo si no hay imagen
                color_enemigo = (255, 0, 0) if enemigo.nombre == "Esqueleto" else (128, 0, 128) if enemigo.nombre == "Bruja" else (139, 69, 19)
                pygame.draw.rect(pantalla, color_enemigo, (enemigo_data['x'], enemigo_data['y'], 60, 60))
            
            # Mostrar información del enemigo
            info_texto = f"{enemigo.nombre} ({enemigo.vida}❤️)"
            info_surface = fuente_pequena.render(info_texto, True, COLOR_TEXTO)
            pantalla.blit(info_surface, (enemigo_data['x'], enemigo_data['y'] + 65))

def mover_enemigos():
    """Mueve los enemigos de forma automática"""
    for enemigo_data in enemigos_activos:
        if not enemigo_data['vivo']:
            continue
            
        # Movimiento aleatorio pero controlado
        import random
        
        # Cambiar dirección ocasionalmente
        if random.randint(1, 10) <= 3:
            enemigo_data['direccion_x'] *= -1
        if random.randint(1, 10) <= 3:
            enemigo_data['direccion_y'] *= -1
        
        # Mover
        nuevo_x = enemigo_data['x'] + enemigo_data['direccion_x'] * 2
        nuevo_y = enemigo_data['y'] + enemigo_data['direccion_y'] * 2
        
        # Mantener dentro de los límites
        if nuevo_x < 50 or nuevo_x > TAMANIO_PANTALLA[0] - 110:
            enemigo_data['direccion_x'] *= -1
        else:
            enemigo_data['x'] = nuevo_x
            
        if nuevo_y < 50 or nuevo_y > TAMANIO_PANTALLA[1] - 110:
            enemigo_data['direccion_y'] *= -1
        else:
            enemigo_data['y'] = nuevo_y
        
        # Actualizar rectángulo de colisión
        enemigo_data['rect'].x = enemigo_data['x']
        enemigo_data['rect'].y = enemigo_data['y']

def manejar_combate(enemigo_data):
    """Maneja el sistema de combate"""
    global en_combate, turno_jugador, mensaje_combate, tiempo_mensaje_combate, experiencia_jugador, nivel_jugador, experiencia_necesaria
    
    if not enemigo_data or not enemigo_data['vivo']:
        return
    
    enemigo = enemigo_data['enemigo']
    
    # Turno del jugador
    if turno_jugador:
        # Usar habilidad más básica disponible
        dano = 10
        habilidad_usada = "Ataque Básico"
        
        if ataque_basico.desbloqueada:
            dano = 15
        if golpe_pesado.desbloqueada:
            dano = 25
            habilidad_usada = "Golpe Pesado"
        if doble_golpe.desbloqueada:
            dano = 20
            habilidad_usada = "Doble Golpe"
            # Atacar dos veces
            enemigo.vida -= dano
            if enemigo.vida > 0:
                enemigo.vida -= dano // 2
        
        enemigo.vida -= dano
        mensaje_combate = f"🗡️ {habilidad_usada}: {dano} daño a {enemigo.nombre}!"
        tiempo_mensaje_combate = 120
        
        # Verificar si el enemigo murió
        if enemigo.vida <= 0:
            enemigo_data['vivo'] = False
            exp_ganada = 25 if enemigo.nombre == "Esqueleto" else 35 if enemigo.nombre == "Bruja" else 50
            experiencia_jugador += exp_ganada
            
            mensaje_combate = f"💀 ¡Derrotaste a {enemigo.nombre}! +{exp_ganada} XP"
            tiempo_mensaje_combate = 180
            
            # Verificar subida de nivel
            if experiencia_jugador >= experiencia_necesaria:
                nivel_jugador += 1
                experiencia_jugador -= experiencia_necesaria
                experiencia_necesaria = int(experiencia_necesaria * 1.5)
                jugador.vida += 20  # Bonus de vida por nivel
                mensaje_combate += f" | ¡NIVEL {nivel_jugador}!"
            
            # Desbloquear habilidades por victorias
            if not golpe_pesado.desbloqueada and experiencia_jugador >= 25:
                golpe_pesado.desbloqueada = True
                mensaje_combate += " | 🗡️ ¡Golpe Pesado desbloqueado!"
            elif not curacion_rapida.desbloqueada and experiencia_jugador >= 50:
                curacion_rapida.desbloqueada = True
                mensaje_combate += " | ❤️ ¡Curación Rápida desbloqueada!"
            elif not doble_golpe.desbloqueada and nivel_jugador >= 2:
                doble_golpe.desbloqueada = True
                mensaje_combate += " | ⚔️ ¡Doble Golpe desbloqueado!"
            elif not invisibilidad.desbloqueada and nivel_jugador >= 3:
                invisibilidad.desbloqueada = True
                mensaje_combate += " | 👻 ¡Invisibilidad desbloqueada!"
            
            en_combate = False
            return
        
        turno_jugador = False
    
    # Turno del enemigo (simplificado)
    else:
        import random
        dano_enemigo = random.randint(5, 12)
        jugador.vida -= dano_enemigo
        mensaje_combate = f"💥 {enemigo.nombre} te ataca: -{dano_enemigo} vida!"
        tiempo_mensaje_combate = 120
        
        if jugador.vida <= 0:
            mensaje_combate = "💀 ¡Has sido derrotado! Juego terminado."
            tiempo_mensaje_combate = 300
        
        turno_jugador = True
        en_combate = False

def manejar_interacciones():
    """Maneja las interacciones del jugador con el entorno"""
    global mostrar_dialogo, jugador_en_combate, mensaje_transicion, tiempo_mensaje
    
    # Verificar colisión con zona de puerta en la Entrada
    if mapa.obtener_ubicacion_actual() == "Entrada" and rect_jugador.colliderect(zona_puerta_sala):
        if mapa.mover_a("Sala"):
            mensaje_transicion = "🚪 Entrando a la Sala Misteriosa..."
            tiempo_mensaje = 60
            # Reposicionar jugador en la nueva sala
            global pos_jugador_x, pos_jugador_y
            pos_jugador_x = 400
            pos_jugador_y = 500
            rect_jugador.x = pos_jugador_x
            rect_jugador.y = pos_jugador_y
            
            # Inicializar enemigos de la sala
            inicializar_enemigos_sala()
            
            # Desbloquear habilidad al entrar por primera vez
            if not ataque_basico.desbloqueada:
                ataque_basico.desbloqueada = True
                print("🗡️ ¡Has desbloqueado: Ataque Básico!")

def manejar_click_mouse(pos_mouse):
    """Maneja los clicks del mouse para seleccionar enemigos y usar objetos"""
    global enemigo_seleccionado, en_combate
    
    # Si el inventario está abierto, verificar clicks en objetos
    if mostrar_inventario:
        usar_objeto_inventario(pos_mouse)
        return
    
    if mapa.obtener_ubicacion_actual() != "Sala":
        return
    
    # Verificar click en enemigos
    for enemigo_data in enemigos_activos:
        if not enemigo_data['vivo']:
            continue
            
        if enemigo_data['rect'].collidepoint(pos_mouse):
            enemigo_seleccionado = enemigo_data
            en_combate = True
            manejar_combate(enemigo_data)
            break

# Desbloquear la primera habilidad
ataque_basico.desbloqueada = True

# Bucle principal del juego
ejecutando = True
while ejecutando:
    clock.tick(FPS)
    dt = clock.get_time()
    
    # Actualizar posición del mouse para tooltips
    pos_mouse = pygame.mouse.get_pos()
    
    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN and mostrar_dialogo:
                dialogo_actual += 1
                if dialogo_actual >= len(dialogos_historia):
                    mostrar_dialogo = False
            elif evento.key == pygame.K_SPACE:
                manejar_interacciones()
            elif evento.key == pygame.K_i:
                mostrar_inventario = not mostrar_inventario
                mostrar_habilidades = False
                mostrar_misiones = False
            elif evento.key == pygame.K_h:
                mostrar_habilidades = not mostrar_habilidades
                mostrar_inventario = False
                mostrar_misiones = False
            elif evento.key == pygame.K_m:
                mostrar_misiones = not mostrar_misiones
                mostrar_inventario = False
                mostrar_habilidades = False
            elif evento.key == pygame.K_ESCAPE:
                # Cerrar paneles
                mostrar_inventario = False
                mostrar_habilidades = False
                mostrar_misiones = False
            elif evento.key == pygame.K_1 and curacion_rapida.desbloqueada:
                # Usar curación rápida
                if jugador.vida < 100:
                    vida_anterior = jugador.vida
                    jugador.vida = min(jugador.vida + 30, 100)
                    vida_ganada = jugador.vida - vida_anterior
                    mensaje_combate = f"❤️ Curación Rápida: +{vida_ganada} vida"
                    tiempo_mensaje_combate = 120
            elif evento.key == pygame.K_2 and invisibilidad.desbloqueada:
                # Activar invisibilidad (efecto temporal)
                mensaje_combate = "👻 Invisibilidad activada (próximo ataque evitado)"
                tiempo_mensaje_combate = 120
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Click izquierdo
                manejar_click_mouse(evento.pos)

    # Obtener teclas presionadas para movimiento
    if not mostrar_dialogo:
        teclas = pygame.key.get_pressed()
        
        # Movimiento del jugador
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            pos_jugador_x -= velocidad
            rect_jugador.x -= velocidad
            mirando_izquierda = True
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            pos_jugador_x += velocidad
            rect_jugador.x += velocidad
            mirando_izquierda = False
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            pos_jugador_y -= velocidad
            rect_jugador.y -= velocidad
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            pos_jugador_y += velocidad
            rect_jugador.y += velocidad
        
        # Mantener al jugador dentro de la pantalla
        pos_jugador_x = max(0, min(pos_jugador_x, TAMANIO_PANTALLA[0] - 40))
        pos_jugador_y = max(0, min(pos_jugador_y, TAMANIO_PANTALLA[1] - 40))
        rect_jugador.x = pos_jugador_x
        rect_jugador.y = pos_jugador_y

    # Actualizar temporizadores
    if tiempo_mensaje > 0:
        tiempo_mensaje -= 1
    if tiempo_mensaje_combate > 0:
        tiempo_mensaje_combate -= 1

    # Dibujar todo
    ubicacion_actual = mapa.obtener_ubicacion_actual()
    
    # Dibujar fondo de la habitación
    if ubicacion_actual in imagenes_habitaciones and imagenes_habitaciones[ubicacion_actual]:
        pantalla.blit(imagenes_habitaciones[ubicacion_actual], (0, 0))
    else:
        pantalla.fill(COLOR_FONDO)
        # Dibujar indicación de puerta en la Entrada
        if ubicacion_actual == "Entrada":
            pygame.draw.rect(pantalla, (139, 69, 19), zona_puerta_sala)
            puerta_texto = fuente_dialogo.render("🚪 SALA", True, COLOR_TEXTO)
            pantalla.blit(puerta_texto, (zona_puerta_sala.x - 10, zona_puerta_sala.y - 25))
    
    # Dibujar enemigos si estás en la Sala
    dibujar_enemigos(pantalla)
    
    # Dibujar jugador con la dirección correcta
    if imagen_jugador_original:
        if mirando_izquierda:
            pantalla.blit(imagen_jugador_izquierda, (pos_jugador_x, pos_jugador_y))
        else:
            pantalla.blit(imagen_jugador_original, (pos_jugador_x, pos_jugador_y))
    else:
        pygame.draw.rect(pantalla, (0, 150, 255), rect_jugador)
    
    # Dibujar HUD
    dibujar_hud(pantalla)
    
    # Dibujar cola de buffs
    dibujar_buffs(pantalla)
    
    # Dibujar paneles (inventario, habilidades, misiones)
    dibujar_inventario(pantalla)
    dibujar_habilidades(pantalla)
    dibujar_misiones(pantalla)
    
    # Dibujar diálogos de historia
    if mostrar_dialogo and dialogo_actual < len(dialogos_historia):
        dibujar_dialogo(pantalla, dialogos_historia[dialogo_actual], TAMANIO_PANTALLA[1] - 120)
    
    # Mostrar mensaje de transición
    if tiempo_mensaje > 0:
        dibujar_dialogo(pantalla, mensaje_transicion, TAMANIO_PANTALLA[1] // 2)
    
    # Mostrar instrucciones si no hay diálogo
    if not mostrar_dialogo and ubicacion_actual == "Entrada":
        instruccion = "🚪 Acércate a la puerta y presiona ESPACIO para entrar"
        instr_surface = fuente_dialogo.render(instruccion, True, COLOR_TEXTO)
        pantalla.blit(instr_surface, (50, TAMANIO_PANTALLA[1] - 80))
    elif not mostrar_dialogo and ubicacion_actual == "Sala" and not any([mostrar_inventario, mostrar_habilidades, mostrar_misiones]):
        instruccion = "🎯 Haz click en los enemigos para atacar"
        instr_surface = fuente_dialogo.render(instruccion, True, COLOR_TEXTO)
        pantalla.blit(instr_surface, (50, TAMANIO_PANTALLA[1] - 80))
    
    # Actualizar pantalla
    pygame.display.flip()

pygame.quit()
