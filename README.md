# 🏰 Data Dungeon - La Leyenda del Héroe Perdido

> **Versión 0.1** | Desarrollado por **Angel Suescun** | Proyecto de Estructuras de Datos

## 📋 Descripción

**Data Dungeon** es un RPG completo desarrollado en Python que demuestra la implementación práctica de estructuras de datos fundamentales. El juego combina mecánicas de RPG clásico con una arquitectura de código que utiliza listas, pilas, colas, árboles, grafos y arreglos de manera funcional y educativa.

### 🎯 Objetivo del Proyecto

Este proyecto fue creado como parte del curso de Estructuras de Datos, demostrando la aplicación real de conceptos teóricos en un entorno de desarrollo de videojuegos interactivo.

## ✨ Características Principales

### 🎮 Gameplay
- **Sistema de Combate por Turnos**: Enfréntate a 3 tipos de enemigos únicos
- **Árbol de Habilidades Visual**: 11 habilidades interconectadas con tooltips informativos
- **Sistema de Inventario**: Gestión de objetos con interfaz clickeable
- **Sistema de Misiones**: Seguimiento de progreso con objetivos dinámicos
- **Sistema de Experiencia**: Progresión de niveles con recompensas
- **Buffs y Efectos**: Cola de efectos temporales visualizada
- **Exploración**: Navegación entre diferentes ubicaciones del castillo

### 🔧 Estructuras de Datos Implementadas

| Estructura | Uso en el Juego | Archivo |
|------------|-----------------|---------|
| **Lista** | Gestión de enemigos y misiones | `estructuras/lista.py` |
| **Arreglo** | Sistema de inventario del jugador | `estructuras/arreglo.py` |
| **Pila** | Historial de acciones del jugador | `estructuras/pila.py` |
| **Cola** | Buffs activos y efectos temporales | `estructuras/cola.py` |
| **Árbol** | Árbol de habilidades del jugador | `estructuras/arbol.py` |
| **Grafo** | Mapa del mundo y conexiones | `estructuras/grafo.py` |

## 🎨 Capturas del Juego

### 🏠 Pantalla Principal
- Interfaz HUD con información del jugador
- Sistema de diálogos narrativos
- Controles intuitivos

### ⚔️ Sistema de Combate
- Selección de enemigos por click
- Feedback visual en tiempo real
- Mecánicas de turnos estratégicas

### 🌳 Árbol de Habilidades
- Nodos visuales con imágenes
- Tooltips informativos
- Sistema de desbloqueo progresivo

### 🎒 Inventario Interactivo
- Interfaz visual de objetos
- Uso de items por click
- Categorización por colores

## 🛠️ Tecnologías Utilizadas

- **Python 3.13+**
- **Pygame 2.6.1** - Motor gráfico y manejo de eventos
- **POO Avanzada** - Herencia, polimorfismo, abstracción
- **Arquitectura MVC** - Separación clara de responsabilidades

## 📁 Estructura del Proyecto

```
Data_Dungeon/
├── 📂 Estructuras/           # Implementaciones de estructuras de datos
│   ├── __init__.py
│   ├── arbol.py             # Árbol n-ario para habilidades
│   ├── arreglo.py           # Arreglo dinámico para inventario
│   ├── cola.py              # Cola FIFO para buffs
│   ├── grafo.py             # Grafo para mapas
│   ├── lista.py             # Lista enlazada para enemigos
│   ├── nodo.py              # Nodo base para estructuras
│   ├── pila.py              # Pila LIFO para historial
│   ├── tabla_hash.py        # Tabla hash para optimizaciones
│   └── vertice.py           # Vértices para el grafo de mapas
├── 📂 game/                 # Lógica del juego
│   ├── jugador.py           # Clase principal del jugador
│   ├── mapa.py              # Sistema de navegación
│   ├── variacionesEnemigos.py # Tipos de enemigos
│   └── 📂 objetos/          # Objetos del juego
│       ├── buff.py          # Efectos temporales
│       ├── habilidad.py     # Sistema de habilidades
│       ├── mision.py        # Sistema de misiones
│       ├── objeto.py        # Objetos base
│       └── variaciones*/    # Implementaciones específicas
├── 📂 assets/               # Recursos gráficos
│   └── 📂 images/           # Sprites e imágenes
├── config.py                # Configuración global
├── main.py                  # Archivo principal del juego
└── README.md               # Documentación del proyecto
```

## 🚀 Instalación y Ejecución

### Prerequisitos
```bash
Python 3.13 o superior
pip (gestor de paquetes de Python)
```

### Instalación
1. **Clona o descarga el proyecto**
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd Data_Dungeon
   ```

2. **Instala las dependencias**
   ```bash
   pip install pygame
   ```

3. **Ejecuta el juego**
   ```bash
   python main.py
   ```

## 🎮 Controles del Juego

| Tecla | Acción |
|-------|--------|
| **WASD** / **Flechas** | Movimiento del jugador |
| **ESPACIO** | Interactuar con objetos/puertas |
| **I** | Abrir/cerrar inventario |
| **H** | Abrir/cerrar árbol de habilidades |
| **M** | Abrir/cerrar misiones |
| **1** | Usar curación rápida (si está desbloqueada) |
| **2** | Activar invisibilidad (si está desbloqueada) |
| **ESC** | Cerrar paneles abiertos |
| **ENTER** | Avanzar diálogos |
| **Click Izquierdo** | Atacar enemigos / Usar objetos |

## 🏗️ Arquitectura del Código

### 🎯 Patrón de Diseño
El proyecto implementa varios patrones de diseño:
- **Strategy Pattern**: Para diferentes tipos de habilidades y buffs
- **Factory Pattern**: Para la creación de enemigos y objetos
- **Observer Pattern**: Para el sistema de eventos del juego

### 🔗 Estructuras de Datos en Acción

#### 📋 Lista Enlazada - Gestión de Enemigos
```python
enemigos = Lista()
enemigos.agregar(Esqueleto(...))
enemigos.agregar(Bruja(...))
enemigos.agregar(Golem(...))
```

#### 🎒 Arreglo Dinámico - Inventario
```python
inventario = Arreglo(12)  # Capacidad fija de 12 slots
inventario.set_nodo(index, Nodo(objeto))
```

#### 🔄 Cola FIFO - Sistema de Buffs
```python
buff_activos = Cola()
buff_activos.encolar(BuffVelocidad())
buff_actual = buff_activos.desencolar()
```

#### 🌳 Árbol N-ario - Habilidades
```python
arbol_habilidades = Arbol("Raíz")
arbol_habilidades.agregar_nodo("Raíz", AtaqueBasico())
arbol_habilidades.agregar_nodo(AtaqueBasico(), CuracionRapida())
```

#### 🗺️ Grafo - Sistema de Mapas
```python
mapa = Mapa()
mapa.agregar_ubicacion("Entrada", "ruta/imagen.png")
mapa.conectar_ubicaciones("Entrada", "Sala")
```

## 🎯 Mecánicas de Juego Detalladas

### ⚔️ Sistema de Combate
- **Turnos alternados** entre jugador y enemigos
- **Cálculo de daño** basado en habilidades desbloqueadas
- **Sistema de experiencia** con recompensas por victoria
- **Progresión de dificultad** escalonada

### 🌟 Sistema de Progresión
- **11 habilidades únicas** organizadas en árbol
- **Desbloqueo por experiencia y nivel**
- **Vida máxima escalable** con el nivel
- **Recompensas por logros** automáticas

### 🎒 Gestión de Inventario
- **12 slots de capacidad** fija
- **Objetos consumibles** (pociones)
- **Equipamiento** (armas y llaves)
- **Interfaz visual** con feedback inmediato

## 🧪 Casos de Prueba

El proyecto incluye ejemplos de uso de cada estructura:

### ✅ Lista - Pruebas de Enemigos
- Agregar múltiples tipos de enemigos
- Iteración y acceso por índice
- Eliminación de enemigos derrotados

### ✅ Arreglo - Pruebas de Inventario
- Inserción en posiciones específicas
- Gestión de capacidad máxima
- Eliminación y reorganización

### ✅ Cola - Pruebas de Buffs
- Orden FIFO para efectos temporales
- Visualización sin modificación
- Gestión de estados activos

### ✅ Árbol - Pruebas de Habilidades
- Construcción de jerarquías complejas
- Recorrido y búsqueda de nodos
- Validación de dependencias

## 🤝 Contribuciones

Este proyecto es educativo y forma parte del portafolio académico de Angel Suescun. Las sugerencias y mejoras son bienvenidas a través de:

- Issues en el repositorio
- Pull requests con mejoras
- Documentación adicional

## 📄 Licencia

Proyecto académico desarrollado para fines educativos en el curso de Estructuras de Datos.

## 👨‍💻 Autor

**Angel Suescun**
- Estudiante de Ingeniería de Sistemas
- Proyecto de Estructuras de Datos
- Versión 0.1 - 2025

---

### 🙏 Agradecimientos

- Al profesor del curso por la guía en estructuras de datos
- A la comunidad de Pygame por la documentación
- A los recursos educativos que hicieron posible este proyecto

---

**¡Sumérgete en Data Dungeon y explora el mundo de las estructuras de datos de manera interactiva! 🎮✨**
