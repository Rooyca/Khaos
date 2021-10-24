# Khaos
![Khaos-logo](LogoChaosFinal.png)

Una API que generar aleatoriedad para (casi) cualquier cosa

# ¿Qué es Khaos?
Khaos (/ˈkeɪ.ɑs/) es la forma romanizada del vocablo griego "χάος" y se define como:

>  el mitológico vacio precedente a la creación del universo (el cosmos).[_Wikipedia_](https://en.wikipedia.org/wiki/Chaos_(cosmogony))

Para mí y muchos otros el cao es es una de las principales características de la aleatoriedad porque no hay forma de predecirlo.
Siempre he estado facinado con el concepto de aleatoriedad, me parece que es algo extraordinariamente hermoso.
El hecho de que podamos generar cosas geniales sin entender qué hay detrás (qué proceso) o, puesto de otra forma, "sabiendo" que lo que hay detras
no es algo necesariamente *humano*, que lo que se creó es simplemente producto de la aleatoriedad, del Khaos. Eso amigos míos, eso es asombroso.

Aquí vamos a divertirnos intentando generar resultados aleatorios (o semi-aleatorios) para (casi) cualquier cosa... Comencemos!

# ¿Qué tiene Khaos para ofrecer?

Primero que nada, puedes probar Khaos aquí:

1. [RapidAPI](https://rapidapi.com/rooyca@gmail.com/api/random14/)
2. [Pura API](https://api.rooyca.xyz)

O tambien puedes correr tu propia API clonando este repositorio y ejecutando el siguiente comando:

```bash
uvicorn main:app
```
Bueno, una vez hayas escojido la opcion que más se acomode a tus necesidades vamos a ver qué podemos hacer con esto.

## Endpoints
Hay diez endpoints y voy a dividirlos por secciones:

- Seguridad y privacidad
- Información
- Palabras, juegos y demás
 
### Seguridad y privacidad

![S&P](https://res.cloudinary.com/rooyca/image/upload/v1635035284/Images/S_P_yx1i6o.png)

Todos estamos concientes de la importancia de tener una contraseña segura, de que debería ser muy dificil (o casi imposible) de descifrar,
y más en estos tiempos en los que nuestro mundo entero depende de una cadena de numeros, letras y simbolos. Una cosa si es seguro, no debemos dejar el
proceso de escojer una contraseña al azar... ¿o si? Como ya dijimos anteriormente, la aleatoriedad es la ausencia de prediccion así que qué mejor que 
generar contraseñas sin ningun tipo de patron, haciendolas imposibles para los humanos de descifrarlas. Con las maquinas es un poco diferentes pues ellas
no son como nosotros... o no completamente.
Así que tecnicamente ellas *podrían* adivinarlas, pero no es muy probable (al menos no por ahora). Aunque también hay que tener en cuenta que esto solo aplica
si escojemos contraseñas de al menos trece caracteres de largo y con más que solo numeros o solo letras.

#### :small_red_triangle_down:Contraseñas

Parametros Query:
|Parametro|Tipo|Por defecto|Obligatorio|Descripcion|
|---|---|---|---|---|
|leng|int|12|NO|Longitud de las contraseñas|
|numb|int|1|NO|Número de contraseñas|
|include|str|"ULNS"|NO|Carácteres en las contraseñas: (U)ppercases(mayusculas), (L)owercases(minusculas), (N)umbers(numeros) and (S)imbols(simbolos)

Para nadie es un secreto que la tecnología a avanzado mucho en los últimos años y seguirá haciendolo aún más. Es por eso que las contraseñas no son 
(en algunos casos) la mejor opcion para mantener nuestra dineron y/o informacion personal a salvo... Déjame presentarte a:

#### :small_red_triangle_down:Passphrases
¿Qué son? En pocas palabras podemos decir que las passphrases son más (o igual de) seguras que las contraseñas pero muchísimo más fáciles de recordar.
Si quieres saber más al respecto te invito a leer [esto](https://es.wikipedia.org/wiki/Frase_de_contrase%C3%B1a). 

Parametros Query:
|Parametro|Tipo|Por defecto|Obligatorio|Descripcion|
|---|---|---|---|---|
|n_words|int|7|NO|Número de palabras de tu passphrase|
|esp|bool|False|NO|Passphrase en español|

##### :small_red_triangle_down:UUID

Aquí encontrarás un Único identificador universal... nada más. Si no sabes lo que es te invito a leer [este](https://es.wikipedia.org/wiki/Identificador_%C3%BAnico_universal)
articulo de Wikipedia.

### Información
![I&D](https://res.cloudinary.com/rooyca/image/upload/v1635035285/Images/I_D_pcljto.png)

En algunas ocaciones queremos registrarnos en un sitio pero nos pide un montón de informacion personal la cual no estamos dispuestos a compartir, pues estos
endpoints pueden ayudarnos en esos momentos.

#### :small_red_triangle_down:Información personal

Aquí optendrás:
- Nombre
- Apellido
- Direccion de correo
- Número de teléfono
- País (Solo USA por el momento)
- Estado
- Fecha de nacimiento
- Genero

Toda esta información es generada de manera aleatoria aunque el número de telefono está basado en el estado, para que haya un poquito de presicion. (Dejame
saber si en realidad funciona así :laughing:)

#### :small_red_triangle_down:Tarjetas de Credito
Aquí podrás generar tarjetas de credito al azár que son validas pero NO reales... es decir no vas a encontrar dinero en ninguna de ellas (o quizás sí, pero 
lo más probable es que no)

Parametros Query:
|Parametro|Tipo|Por defecto|Obligatorio|Descripcion|
|---|---|---|---|---|
|numb|int|1|NO|Número de tarjetas de credito|

### Palabras, juegos y demás
![GT](https://res.cloudinary.com/rooyca/image/upload/v1635035285/Images/G_efg3ph.png)

Por último, pero no por ello menos importante, aquí encontrarás un monton de enpoints sin relación entre sí.
#### :small_red_triangle_down:Frases
Alguna vez te ha tocado escribir algo pero tu cabeza simplemente dice: "No, no, no!"? Bueno, esto quizás pueda ayudarte. En este endpoint vas a generar
pequeñas frases de manera aleatoria (con solo dos palabras, por el momento)... estas frases son gramaticamente correctas y puede (o no) ayudarte
con tu problema... Y si no funciona al menos te vas a diestraer pensando en un montón de cosas bizarras.

Parametros Query:
|Parametro|Tipo|Por defecto|Obligatorio|Descripcion|
|---|---|---|---|---|
|numb|int|1|NO|Número de frases|
|ussing|str|"AN"|NO|Estructura de las frases: Adjetive+Noun(AN), Noun+Noun(NN) or Verb+Noun(VN)|
#### :small_red_triangle_down:LoR Deck
Legends of Runeterra es un fantástico juego de cartas (el mejor del momento, en mi opinion) pero como muchos otros juegos de cartas hay momentos en los
que no hya mucha variedad, todo el mundo juega los mismos decks una y otra vez. Bueno, tu no tienes que ser como los demás, de hecho puedes ser el rey
de los "únicos y d~~etergentes~~iferentes" al jugar decks generados de manera completamente aleatoria. ¿Vás a ganar con estos mazos? Probablemente no.
¿Te vas a divertir? Si lo único que te preocupa es ganar entonces no, de lo contrario claro que te divertirás!

Solo una cosa, a veces se generan decks que no son validos. Cuando eso pase solo envía otra preticion y ya. (Actualemten estoy trabajando en arreglar este bug)
#### :small_red_triangle_down:Colores
Ahora vamos a imaginar un escenario en el que estas trabajando en algo relacionado con colores y tienes que escoger algunos colores. ¿Qué harías?
Si es algo realmente importante te pones a ello y los escojes de manera conciensuda, pero si es algo que no necesita tener una relación entre sí o, incluso,
si dicho proyecto se veneficia de la aleatoriedad entonces este endpoint es para ti. Aquí podras generar colores de forma aleatoria.

Parametros Query:
|Parametro|Tipo|Por defecto|Obligatorio|Descripcion|
|numb|int|1|NO|Numero de colores|
|using|str|hex|NO|La forma en la que mostrar los colores: hex, rgb or all (Todo en minusculas)|
#### :small_red_triangle_down:Desciciones
No hay mucho que decir sobre este... aquí puedes tomar una desicion sin tomar una desicion :smile:.
Esto no funciona en RappidAPI, pero si realmente quieres ensayarlo puedes ir [aquí](https://api.rooyca.xyz/v1/random/choice)

Parametros Query:
|Parametro|Tipo|Por defecto|Obligatorio|Descripcion|
|option|str|None|YES|Las diferentes opciones|
#### :small_red_triangle_down:Palabras
¿Quieres aumentar tu vocabulario? O simplemente necesitas una palabra del inglés (Por ahora, si quieres que se añada tu idioma por favor hasmelo saber).
Entonces este endpoint es para ti.

Tengo un reto para ti... Haz tres peticiones a este endpoint y obten palabras las cuales ya conocias su significado. Bastante complicado!

Parametros Query:
|Parametro|Tipo|Por defecto|Obligatorio|Descripcion|
|---|---|---|---|---|
|numb|int|1|NO|Número de palabras|

## TODO
- [ ] Generar informacion al azar con el ruido ambiente
- [ ] Generar "arte" de forma aleatoria
- [x] Traducir esto al español (Falta corregir algunos errores)
- [ ] Tu idea va aquí...

## Colaboración

Si deseas colaborar con ideas o cualquier otra cosa porfavor contactame. (Información en mi perfil)
