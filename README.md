# Programación web de CS50 con Python y JavaScript

##

### Challenge wiki-Markdown

En el código de distribución hay un proyecto llamado **Django wiki** que contiene una sola aplicación llamada encyclopedia.

Al abrir encyclopedia/urls.py, dónde se define la configuración de URL para esta aplicación. Se puede observar una ruta predeterminada que está 
asociada con la función **views.index.**

Al observar **encyclopedia/util.py.** se apreciará que hay tres funciones que pueden resultar útiles para interactuar con las entradas de la 
enciclopedia: 

- **list_entries** devuelve una lista de los nombres de todas las entradas de la enciclopedia guardadas actualmente. 
* **save_entry** guardará una nueva entrada de enciclopedia, dado su título y algún contenido de Markdown. 
+ **get_entry** recuperará una entrada de enciclopedia por su título, devolviendo su contenido de Markdown si la entrada existe o None si no existe. 

**Cualquiera de las vistas que escriba puede usar estas funciones para interactuar con las entradas de la enciclopedia.**

Cada entrada de la enciclopedia se guardará como un archivo **Markdown** dentro del **entries/directorio.** Entrando allí ahora, verá que hay  
previamente algunas entradas de muestra. **¡Al ejecutar el programa podrás agregar más!**

Ahora, echemos un vistazo a **encyclopedia/views.py.** Sólo hay una vista aquí ahora, la **index vista**. Esta vista devuelve una plantilla 
**encyclopedia/index.html,** proporcionando a la plantilla una lista de todas las entradas de la enciclopedia 
(obtenida llamando a **util.list_entries,** que vimos definida en **util.py**).

Puede encontrar la plantilla explorando **encyclopedia/templates/encyclopedia/index.html.** Esta plantilla hereda de un 
**layout.html** archivo base y especifica cuál debe ser el título de la página y qué debe contener el cuerpo de la página: 
en este caso, una lista desordenada de todas las entradas de la enciclopedia. **layout.html,** mientras tanto, 
define la estructura más amplia de la página: cada página tiene una barra lateral con un campo de búsqueda (que inicialmente no estará configurarda), 
un enlace para ir a **home** y enlaces **(que deben implementarse)** para crear una nueva página o visita una página al azar.

