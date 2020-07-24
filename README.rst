=========
DBTraits
=========

Este proyecto busca crear los elementos compartidos entre todos los microservicios de
inmobilio.co.

Cuenta con los siguientes elementos:

* Timestamp: contiene los campos con las fechas de creacion y de actualizacion de los objetos.
* Softdelete: contiene el campo que indica si el elemento fue eliminado y cuando.
* Address: contiene la informacion basica para ubicar a una persona u objeto.


Quick start
-----------

1. Instalar usando pipenv y llamando el paquete directo desde el repositorio:
    https://gitlab.com/inmobilio/backend/dependencies/dbtraits/-/archive/master/dbtraits-master.tar.gz

2. Aniadir la application a las INSTALLED_APPS de django de la siguiente manera:
    'dbtraits'
