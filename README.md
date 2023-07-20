# Programación web de harvard CS50 con Python y JavaScript

## Challenge wiki-Markdown

[Grabación de pantalla desde 2023-07-19 22-21-21.webm](https://github.com/Menrry/Wiki-Markdown/assets/83178947/af7844b0-ba01-4b29-b07a-c51d02fe3286)


En el código de distribución hay un proyecto **Django Llamado wiki** que contiene una sola aplicación llamada **encyclopedia.**

Al abrir **encyclopedia/urls.py,** dónde se define la configuración de URL para esta aplicación. Se puede observar una ruta predeterminada que está 
asociada con la **función views.index.**

Al observar **encyclopedia/util.py.** se apreciará que hay tres funciones que pueden resultar util.py para interactuar con las entradas de la 
enciclopedia: 

- **list_entries** devuelve una lista de los nombres de todas las entradas de la enciclopedia guardadas actualmente. 
* **save_entry** guardará una nueva entrada de enciclopedia, dado su título y algún contenido de Markdown. 
+ **get_entry** recuperará una entrada de enciclopedia por su título, devolviendo su contenido de Markdown si la entrada existe o None si no existe. 

**Cualquiera de las vistas que escriba puede usar estas funciones para interactuar con las entradas de la enciclopedia.**

Cada entrada de la enciclopedia se guardará como un archivo **Markdown** dentro del **entries/directorio.** Entrando allí ahora, verá que hay  
previamente algunas entradas de muestra. **¡Al ejecutar el programa podrás agregar más!** Lea [la guía Markdown de GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) para comprender cómo funciona la sintaxis de Markdown. Preste especial atención a cómo se ve la sintaxis de Markdown para encabezados, texto en negrita, enlaces y listas.



**Ahora, echemos un vistazo a :**
- **encyclopedia/views.py.** Sólo hay una vista aquí inicialmene.
* **index vista**. Esta vista devuelve una plantilla 
+ **encyclopedia/index.html,** proporcionando a la plantilla una lista de todas las entradas de la enciclopedia 
(obtenida llamando a **util.list_entries,** que vimos definida en **util.py**).

Puede encontrar la plantilla explorando **encyclopedia/templates/encyclopedia/index.html.** Esta plantilla hereda de un 
**layout.html** archivo base y especifica cuál debe ser el título de la página y qué debe contener el cuerpo de la página: 
en este caso, una lista desordenada de todas las entradas de la enciclopedia. **layout.html,** mientras tanto, 
define la estructura más amplia de la página: cada página tiene una barra lateral con un campo de búsqueda, un enlace para ir a **home** y enlaces para **crear** una nueva página o visitar una **página al azar.**

[Especificación](https://cs50.harvard.edu/web/2020/projects/1/wiki/#specification)
----------------------------------------------------------------------------------

la implementación de la enciclopedia Wiki. Cumple con los siguientes requisitos:

-   Página de entrada : Visiting `/wiki/TITLE`, donde `TITLE`está el título de una entrada de enciclopedia, genera una página que muestra el contenido de esa entrada de enciclopedia.
    -   La vista obtiene el contenido de la entrada de la enciclopedia llamando a la función adecuada que se encuentra en **util.py.**
    *   Si se solicita una entrada que no existe, se presenta al usuario una página de error que indica que no se encontró la página solicitada.
    +   Si la entrada existe, al usuario se le presenta una página que muestra el contenido de la entrada. El título de la página incluye el nombre de la entrada.
-   Página de índice : Se actualiza `index.html`de tal manera que, en lugar de simplemente enumerar los nombres de todas las páginas de la enciclopedia, el usuario puede hacer clic en cualquier nombre de entrada para ir directamente a esa página de entrada.
-   Buscar : permite al usuario escribir una consulta en el cuadro de búsqueda de la barra lateral para buscar una entrada de la enciclopedia.
    -   Si la consulta coincide con el nombre de una entrada de la enciclopedia, se redirige al usuario a la página de esa entrada.
    *   Si la consulta no coincide con el nombre de una entrada de la enciclopedia, se lleva al usuario a una página de resultados de búsqueda que muestra una lista de todas las entradas de la enciclopedia que tienen la consulta como una subcadena. Por ejemplo, si la consulta de búsqueda fuera `ytho`, `Python`debería aparecer en los resultados de búsqueda.
    -   Al hacer clic en cualquiera de los nombres de las entradas en la página de resultados de búsqueda, el usuario irá a la página de esa entrada.
-   Nueva página : al hacer clic en "Crear nueva página" en la barra lateral, el usuario irá a una página donde puede crear una nueva entrada de enciclopedia.
    -   Los usuarios podrán ingresar un título para la página y, en un [`textarea`](https://www.w3schools.com/tags/tag_textarea.asp), podrán ingresar el contenido de Markdown para la página.
    -   Los usuarios pueden hacer clic en un botón para guardar su nueva página.
    *   Cuando se guarda la página, si ya existe una entrada de enciclopedia con el título proporcionado, se le presenta al usuario un mensaje de error.
    -   De lo contrario, la entrada de la enciclopedia guardará en el disco y se llevará al usuario a la página de la nueva entrada.
-   Editar página : en cada página de entrada, el usuario puede hacer clic en un enlace para ir a una página donde el usuario puede editar el contenido de Markdown de esa entrada en un archivo `textarea`.
    -   El `textarea`se rellenará previamente con el contenido Markdown existente de la página. (es decir, el contenido existente será la inicial `value`de `textarea`).
    -   El usuario puede hacer clic en un botón para guardar los cambios realizados en la entrada.
    *   Una vez que se guarda la entrada, se redirigir al usuario a la página de esa entrada.
-   Página aleatoria : Hacer clic en "Página aleatoria" en la barra lateral se lleva al usuario a una entrada aleatoria de la enciclopedia.
-   Conversión de Markdown a HTML : en la página de cada entrada, cualquier contenido de Markdown en el archivo de entrada se convertirá a HTML antes de mostrarse al usuario. Se implementa el uso del paquete [`python-markdown2`](https://github.com/trentm/python-markdown2) para realizar esta conversión, instalable a través de `pip3 install markdown2`. Además adjunto al proyecto está un doc.odt que detalla otros comandos para instalar markdow que fué la que me funcionó.
   

