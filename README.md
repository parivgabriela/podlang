# podlang
Este proyecto se basa en una red de ayuda para quienes quieren aprender un nuevo lenguaje.
Se generará una comunidad la cual quiere aprender un nuevo idioma escuchando un libro, articulo, noticia, etc. Lo hará y también podra ayudar leyendo un articulo en su lengua nativa. Y dentro de esta página lo podrá hacer, requisito inicar sesión para agregar contenido nuevo. Para asegurar la calidad de la página se agregaran puntajes/validaciones en la página. 

##endpoints
[get]
    users:
        -prerequisite logged with admin role
        -response: list of all users
    podcasts:
        -response list of all podcast in order of (variable)
[post] user:
    -prerequisite: logged with role admin
[update]

[delete]
