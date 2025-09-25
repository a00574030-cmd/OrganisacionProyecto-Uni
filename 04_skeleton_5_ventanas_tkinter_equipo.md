# Documentación del Proyecto Integrador - MVP (tkinter)

Este proyecto es una **Aplicación Demo (MVP - Producto Mínimo Viable)** desarrollada en **Python** usando la librería **tkinter** para la interfaz gráfica de usuario (GUI). Su propósito es mostrar la implementación de varias ventanas y componentes comunes de una aplicación de escritorio, como formularios, listas (CRUD básico), tablas (Treeview) y un canvas para dibujo.

La estructura del proyecto implica un archivo `main.py` en la raíz (simulada) que actúa como punto de entrada, y módulos separados para cada ventana de la aplicación.

## 1. Estructura de Archivos

| Archivo | Propósito | Contenido Principal |
| :--- | :--- | :--- |
| `main.py` | Punto de entrada y Ventana Principal. | Configura la ventana principal y los botones para abrir otras ventanas. |
| `win_home.py` | Ventana de Bienvenida. | Muestra un mensaje simple y un `messagebox`. |
| `win_form.py` | Ventana de Formulario. | Demuestra la captura de datos, validación básica y guardado en archivo (`.txt`). |
| `win_list.py` | Ventana de Lista (CRUD Básico). | Implementa una lista (`Listbox`) con funciones básicas de Crear (Agregar), Eliminar y Limpiar. |
| `win_table.py` | Ventana de Tabla. | Utiliza `ttk.Treeview` para mostrar datos leídos de un archivo CSV de ejemplo. |
| `win_canvas.py` | Ventana de Canvas. | Demuestra el uso de `tk.Canvas` para dibujar figuras. |
| `launch.json` | Configuración de lanzamiento de VS Code. | Define cómo ejecutar el programa con `PYTHONPATH`. |

---

## 2. Análisis Detallado del Código

### `main.py` (Módulo Principal)

Es el **controlador principal**. Inicializa la ventana raíz (`tk.Tk`) y define la interfaz principal con **cinco botones** para abrir las ventanas secundarias (`Toplevel`) mediante la función `lambda` que llama a la función de apertura respectiva (e.g., `open_win_form(root)`).

### `win_home.py` (Ventana 1 - Home)

Implementa una ventana simple. Muestra un mensaje de bienvenida y un botón para abrir un `messagebox.showinfo` ("¡Equipo listo!").

### `win_form.py` (Ventana 2 - Formulario)

Demuestra captura de datos y **validación**.

* **Validación:**
    1.  Verifica que el campo **Nombre** no esté vacío.
    2.  Verifica que el campo **Edad** sea un número entero (`isdigit()`).
* **Guardado:** Si la validación es exitosa, usa `filedialog.asksaveasfilename` para solicitar una ruta y guarda los datos en un archivo de texto (`.txt`).

### `win_list.py` (Ventana 3 - Lista/CRUD)

Implementa un **CRUD básico** usando `tk.Listbox`.

* **`agregar()` (Crear):** Inserta el texto de la entrada al final de la lista.
* **`eliminar()` (Borrar):** Elimina el ítem seleccionado (`lb.curselection()`).
* **`limpiar()`:** Borra todos los ítems.
* **Diseño:** Utiliza `grid` para posicionar los elementos, con el `Listbox` configurado para expandirse (`weight=1`).

### `win_table.py` (Ventana 4 - Tabla/Treeview)

Muestra datos tabulares.

* Utiliza el widget **`ttk.Treeview`** con tres columnas definidas: "nombre", "valor1", y "valor2".
* La carga de datos se realiza leyendo un archivo CSV (`sample.csv`) con el módulo estándar `csv.DictReader`.
* Incluye lógica para verificar la existencia del archivo CSV usando `pathlib.Path` y muestra una advertencia si no se encuentra.

### `win_canvas.py` (Ventana 5 - Canvas)

Demuestra las capacidades de dibujo del widget **`tk.Canvas`**. Se crean ejemplos de figuras geométricas (rectángulo, óvalo, línea) y texto.

---

## 3. Configuración de Desarrollo (`launch.json`)

Este archivo es esencial para configurar el entorno de ejecución en **Visual Studio Code**, permitiendo que el proyecto se ejecute correctamente.

```json
// ...
      "program": "${workspaceFolder}/src/app/main.py",
      "env": { "PYTHONPATH": "${workspaceFolder}/src" }, // <--- CLAVE
// ...