// flask = framework web de python
// express = framework web de nodejs (que se escribe en javascript)

// el interprete del codigo escrito en el lenguaje python, se llama python
// el interprete del codigo escrito en el lenguaje javascript, se llama nodejs
// nodejs traspila a javascript a c++, python hace algo similar

// python lenguaje, interprete python
// javascript lenguaje, interprete nodejs

=======================================================

// instalar python

// instalar python3-virtualenv
sudo apt install python3-virtualenv

// crear una carpeta de trabajo

// crear el environment (bin, lib)
virtualenv venv (o virtualenv_espacio_nombrecarpeta)
// otra forma
python3 -m venv venv (lenguaje_espacio_modulo_venv_espacio_nombrecarpeta)

// activar el environment
source venv/bin/activate

// instalar el pquete (o modulo flask)
pip install Flask

// ejecutar aplicacion
flask --app (nombrearchivo) run
// ejecutar aplicacion modo debug (recarga en guardado)
flask --app (nombrearchivo) --debug run
