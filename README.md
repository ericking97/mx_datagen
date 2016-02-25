# MX_DATAGENERATOR

MX_DATAGENERATOR es una paquetería desarrollada en Python para la generación de datos aleatorios principalmente orientada al área de testeo, sin embargo los métodos son muy flexibles y se puede ocupar de la forma que tu desees.

Esta libreria se ira robusteciendo poco a poco aún así puedes disfrutar de todas las funcionalidades que se vayan desarrollando.

## Instalación
MX_DATAGENERATOR esta disponible en https://pypi.python.org/pypi/mx_datagenerator.
El único paquete adicional que esta librería instala es python-dateutil.
```sh
$ pip install mx_datagenerator
```

## Uso
Una vez instalado puedes realizar su importación de la siguente manera:
```sh
from mx_datagen import *
```
Actualmente la librería cuenta con los siguientes métodos
* Name
* Email
* Phone
* Date
* PostalCode

#### Name

El módulo Name tiene métodos para generar nombres aleatorios, tiene opciones para crear nombres de cierto genero o apellidos de ciertas culturas comúnes de México (mayas, nahuatl). A continuación se explicará como usar dichas funciones junto con ejemplos ilustrativos.

##### Name.first_name(gender)
El método first_name generá un primer nombre.
Puede o no aceptar un parametro, si no recibe ninguno genera un nombre masculino o femenino.
Si recibe una 'M', 'male', 'Male', 'Hombre' generá un nombre siempre masculino.
Si recibe una 'F', 'female', 'Female', 'Mujer' generá un nombre siempre femenino.
Si recibe algo más que no sea los parametros previamente estípulados regresa error y la lista de parametros aceptados.
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import Name
>>> Name.first_name()
u'Eduardo'
>>> Name.first_name('M')
u'Axel'
>>> Name.first_name('F')
u'Karen'
>>> Name.first_name('S')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "mx_datagen/names.py", line 22, in first_name
    raise ValueError('Please enter one of the following gender options:'
ValueError: Please enter one of the following gender options:
* Male    * male      * M     * Hombre
* Female  * female    * F     * Mujer
```

##### Name.surname(culture)
El método surname generá un apellido.
* Si no recibe un parametro generá un apellido aleatorio.
* Si recibe alguna cultura como parametro crea un apellido común de esa cultura.
* Si recibe alguna cultura que no esta dentro del generador, devuelve la lista de culturas validas.
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import Name
>>> Name.surname()
u'Mendoza'
>>> Name.surname('mayan')
u'Dzal'
>>> Name.surname('otaku')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "mx_datagen/names.py", line 42, in surname
    raise ValueError('Please enter one of the following culture options'
ValueError: Please enter one of the following culture options
* common
* mayan
* nahuatl
* yaqui
```

##### Name.fullname(gender, culture)
Generá un nombre completo.
* Si no se especifica ni el genero ni la cultura crea un nombre completo aleatorio.
* Si se especifica el genero se crea el nombre con el genero especificado.
* Si se especifica la cultura se crean los apellidos en base a la cultura seleccionada.
* Si se especifica cultura y genero se crea el nombre en base a los parametros
* Si hay algun parametro no soportado devuelve la lista de parametros aceptados

``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import Name
>>> Name.fullname()
u'Cesidio Berzal Sesma'
>>> Name.fullname('M')
u'Erick Florit Riveiro'
>>> Name.fullname('F')
u'Nicte Coulibaly Olivar'
>>> Name.fullname(None, 'mayan')
u'Belinda Puch Peech'
>>> Name.fullname('M', 'nahuatl')
u'Imma Chamilpa Atzin'
>>> Name.fullname('X', 'otaku')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "mx_datagen/names.py", line 111, in fullname
    raise ValueError('Please enter one of the following gender options\n'
ValueError: Please enter one of the following gender options
* Male        *M      *Hombre
* Female      *F      *Mujer
```

#### Email
El módulo de Email tiene varias opciones para crear un email aleatorio, un mail con cierto username o un email con alias. Se recomienda usar el email con alias la mayoría de las veces si es que tu página realiza algun proceso ya que algunos servicios web (Ej: Amazon) detecta el envio de correos a email no existentes y los marca como spam.

##### Email.random()
Regresa un email aleatorio.
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import Email
>>> Email.random()
u'Aventina@likely.net'
```

##### Email.name_email(name)
Regresa un email comenzando el encabezado por el nombre que le haya mandado.
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import Email
>>> Email.name_email('ale')
u'ale@limp.gov'
```
##### Email.alias_email(email)
Regresa un alias del email enviado.
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import Email
>>> Email.alias_email('erick97@gmail.com')
u'erick97+70089123@gmail.com'
```
#### Phone
El módulo de Phone crea números telefónicos aleatorios, todos dentro de la republica mexicana, se puede especificar si deseas que un número tenga una lada especifíca.

##### Phone.random()
Regresa un número telefónico aleatorio.
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import Phone
>>> Phone.random()
'9217064515'
```
##### Phone.lada_phone(lada)
Regresa un número telefónico aleatorio con la lada enviada.
Si se manda una lada invalida regresa la lista de ladas.
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import Phone
>>> Phone.lada_phone('55')
'5560592002'
```
#### Date
El módulo Date sirve para crear fechas aleatorias, fechas entre cierto lapso, fechas de nacimiento en base a la edad que quieras y próximas o anteriores fechas de pago (Quincenalidades o catorcenalidades).

##### Date.create_date(after, before)
Crea una fecha aleatoria.
* Si no parametros crea una fecha completamente aleatoria.
* Si hay after, se crea una fecha despues de la dada.
* Si hay before, se crea una fecha antes de la dada.
* Si se dan los 2 parametros, crea una fecha entre las fechas dadas.
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import Date
>>> Date.create_date()
'2014-06-03'
>>> Date.create_date('2016-02-24')
'2016-03-11'
>>> Date.create_date(None, '1997-02-10')
'1997-01-28'
>>> Date.create_date('2015-01-01', '2016-01-01')
'2015-01-22'
```
##### Date.create_date_old(year)
Crea una fecha segun los años dados.
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import Date
>>> Date.create_date_old(18)
'1997-07-20'
>>> Date.create_date_old(0)
'2015-11-22'
>>> Date.create_date_old(-1)
'2016-03-02'
```

##### Date.create_age_between(min, max)
Crea una fecha entre dos años dados.
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import Date
>>> Date.create_age_between(0, 1)
'2014-06-18'
>>> Date.create_age_between(5, 10)
'2009-08-05'
```

##### Date.next_payment_day(pivot)
Calcula la próxima fecha de pago.
* Si quieres calcular quincenalidad no mandes parametros.
* Si quieres calcular catorcenalidad manda tu fecha de pivote.

Como referencia la fecha en la que se corrió este código fue el 24-02-2016.
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import Date
>>> Date.next_payment_day()
'2016-02-29'
>>> Date.next_payment_day('2016-02-02')
'2016-03-01'
```

##### Date.last_payment_day(pivot)
Calcula la última fecha de pago.
* Si quieres calcular quincenalidad no mandes parametros.
* Si quieres calcular catorcenalidad manda tu fecha de pivote.

Como referencia la fecha en la que se corrió este código fue el 24-02-2016.
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import Date
>>> Date.last_payment_day()
'2016-02-15'
>>> Date.last_payment_day('2016-02-02')
'2016-02-16'
```
#### PostalCode
Este módulo contiene funciones para crear un código postal aleatorio, buscar información relacionada a un código postal o bien crear un código postal de cierto estado.

##### PostalCode.random(info)
Regresa un código postal aleatorio.
* Si no se manda parametros solo envía el código postal.
* Si se le manda "Basic" regresa información básica del código postal. (Colonia, Municipio, Ciudad y Estado)
* Si se le manda "All" regresa toda la información del código postal. (Tipo de colonia, Colonia, Municipio, Ciudad, Estado, Número de Colonia)
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import PostalCode
>>> PostalCode.random()
u'92783'
>>> PostalCode.random('Basic')
(u'59531', u'Cerro de San Francisco', u'Jiquilpan', u'59511', u'Michoac\xe1n de Ocampo')
>>> PostalCode.random('All')
(u'56244', u'Pueblo', u'San Jer\xf3nimo Amanalco', u'Texcoco', u'56101', u'M\xe9xico', u'56101')
>>> PostalCode.random('asd')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "mx_datagen/postalcode.py", line 41, in random
    raise ValueError('Please enter one of the following param\n'
ValueError: Please enter one of the following param
* Basic       * All
```
##### PostalCode.get_info(postal_code, info)
Regresa la información de una código postal.
* Si se le manda solo el código postal regresa toda la información
* Si se le manda el código postal y en info 'Basic' regresa la información básica (Colonia, Municipio y Estado)
* Si se le manda el código postal y en info ('Colony', 'Municipality', 'State', 'Type of Colony', 'Colony number') regresa lo que le hayas pedido
* Puedes buscar más de un dato como parametro

NOTA: Si el código postal que mandaste tiene varias colonias, todas estas se imprimiran, al igual que el tipo de colonia y el número de colonia.
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import PostalCode
>>> PostalCode.get_info('57170')
(u'Colonia', u'Bosques de Arag\xf3n', u'Nezahualc\xf3yotl', u'Ciudad Nezahualcoyotl', u'M\xe9xico', u'15')
>>> PostalCode.get_info('57170', 'Basic')
(u'Bosques de Arag\xf3n', u'Nezahualc\xf3yotl', u'M\xe9xico')
>>> PostalCode.get_info('57170', 'Colony', 'State')
[u'Bosques de Arag\xf3n', u'M\xe9xico']
>>> PostalCode.get_info('24030', 'Colony')
[u'Prado', u'Villas Universidad', u'Miramar', u'Lomas del Castillo', u'Bosques de Campeche', u'H\xe9roes de Chapultepec (FOVI)']
```
##### PostalCode.state_postal_code(state)
Regresa un código postal del estado que mandes como parametro.
``` sh
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from mx_datagen import PostalCode
>>> PostalCode.state_postal_code('Distrito Federal')
u'09429'
>>> PostalCode.state_postal_code('México')
u'50903'
>>> PostalCode.state_postal_code('asdf')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "mx_datagen/postalcode.py", line 178, in state_postal_code
    raise ValueError("The state you send doesn't exist, here's the list\n"
ValueError: The state you send doesn't exist, here's the list
* Coahuila de Zaragoza        * Querétaro
* Guerrero                    * Veracruz de Ignacio de la Llave
* Guanajuato                  * Michoacán de Ocampo
* Sinaloa                     * Tamaulipas
* Chihuahua                   * Aguascalientes
* Nuevo León                  * Tlaxcala
* Nayarit                     * Chiapas
* Zacatecas                   * Baja California
* San Luis Potosí             * Quintana Roo
* Colima                      * Sonora
* Tabasco                     * Baja California Sur
* Puebla                      * México
* Jalisco                     * Distrito Federal
* Campeche                    * Durango
* Oaxaca                      * Yucatán
* Morelos                     * Hidalgo
```