AUTHOR= 'CarmBrc'
SITENAME= 'Carmelitas Bariloche'
if 'BRANDNAME' not in locals():
  BRANDNAME= 'Carmelitas Bariloche'
SITEURL= 'https://carmelitasbariloche.github.io/carmelitasbariloche'

if 'SITESUBTITLE' not in locals():
  SITESUBTITLE= "“En el corazón de mi Madre, la Iglesia, yo seré el amor”<p>(Sta. Teresita del Niño de Jesús)</p>"


COPYRIGHT_NOTICE= '© 2025 ' + AUTHOR

if 'WHATSAPPNUM' not in locals():
  WHATSAPPNUM= '542944506063'
if 'EMAIL' not in locals(): 
  EMAIL='trabajosocd@gmail.com'
if 'COSTODEENVIO' not in locals(): 
  COSTODEENVIO=10000


print(EMAIL.split('@'))
def showEMAIL(email):
  return email.replace('@',' @ ')


IMG_DIR='../data/images/'
IMG_DIR='https://carmelitasbariloche.github.io/images/'
IMG_DIR_PRODUCTS=IMG_DIR+""
ImagenMostrador= 'https://www.parroquiasaneduardo.com.ar/images/Carmelitas1_web.jpg'
ImagenMostrador= IMG_DIR+'carmelo-y-sta-teresa.jpg'
IframeMostrador=''



SHORTCEL=WHATSAPPNUM[2:5]+' '+WHATSAPPNUM[5:]

if 'LINKS' not in locals():
  LINKS = (
    ('Mapa: Bustillo km 19,5 ~ Bariloche ~ ARG','https://maps.app.goo.gl/GWnDiSpQmEzwKVXt5'),
    # ('WhatsApp: '+SHORTCEL,'https://wa.me/'+WHATSAPPNUM),
    ('tel: 294 444-8456',"tel:+542944448456"),
    ('e-mail: '+showEMAIL(EMAIL),'mailto: '+EMAIL),
    ('Parroquia San Eduardo', 'https://parroquiasaneduardo.com.ar'),
    )

input_files=['../data/WEB CARMELITAS.csv']
if 'output_file' not in locals():
  print('entro en output')
  output_file='../public/index.html'

#template_subdir:
subdir='productos'
#Categorias
if 'parents' not in locals():
  parents={}
if 'only' not in parents:
  parents['only']=[]

parents['name']='Categorias'
parents['col_title']='categorias'

parents['undesired']=['parador']

parents['first']=['entrega semanal','frescos']
parents['last']=['esenciales']
parents['long_names']={'frescos':'productos frescos','elaborados':'productos elaborados'}
parents['mensajes']={'elaborados':""}
#ARTICULOS

if 'articles' not in locals():
  articles={}

if 'only' not in articles:
  articles['only']=[]
  
#PEDIDOS
pedido=True


#MENSAJES
mensaje={}
mensaje['inicial']="""<p>Monasterio “Nuestra Señora de las Nieves y Sta. Teresita” – Fundado 8 de mayo 1993</p>

Santa Teresa de Jesús, Nuestra Madre, fundó el primer Carmelo reformado en España el 24 de agosto de 1562: Carisma rico y fecundo se extendió rápidamente por todo el mundo hasta llegar a nuestras tierras patagónicas.
Nuestra vida de oración, trabajo, silencio, soledad; junto con una intensa vida de comunidad, fraterna, alegre y sencilla; es nuestra respuesta cotidiana a los grandes desafíos, dolores y esperanzas que vive la humanidad hoy.
Insertas directamente en el Corazón de Cristo, atraídas por su belleza y amor, le entregamos nuestra vida por el bien de todos. El trabajo manual, vivido en soledad y silencio orante, constituye un elemento importante de nuestra vida que nos permite, además de sustentarnos, llegar a las vidas y a los hogares de muchas personas.
Brindamos ahora con mucha sencillez, este espacio online, respondiendo al pedido que muchos nos han hecho llegar; que deseaban también una manera concreta de colaborar con nuestra vida contemplativa.  
Desde ya les estamos muy agradecidas.
<p style='text-align:right'>Hnas. Carmelitas de Bariloche</p>"""
mensaje['pedido']= "<p style='text-align: left;' >Nos comunicamos a la brevedad para confirmar tu pedido y que puedas abonarlo.</p>"
mensaje['pedido2']= " <p>Hacemos envíos a todo el país.</p><p>Podés retirar gratis en el Monasterio de lunes a viernes de 9 a 12hs</p>"


fecha="fecha de hoy"
