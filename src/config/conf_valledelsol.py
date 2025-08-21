BRANDNAME= 'Valle del Sol'
SITEURL= '.' #'https://januspri.github.io/almacen'
SITESUBTITLE= "ofrece productos de JANUS Proyecto Rural Integrador"


WHATSAPPNUM= '542996069138'

EMAIL='comunicacioncolegiovalledelsol@gmail.com'

COSTODEENVIO=0

output_file='../output/valledelsol/index.html'

articles={}
productos_valledelsol=[
'Jugo de MANZANA',
'Dulce de CIRUELA',
'Dulce de MANZANA',
'Dulce de TOMATE',
'Vinagre de sidra de Manzana (chico)',
'Pepinillos en vinagre',
'Puré de MANZANA',
'Chutney de TOMATE intenso',
'Crema untable de ESPINACA',
'Crema untable de GALLINA',
'Morrón en aceite 200cc',
'Ají dulce en vinagre',
'LICOR de Ciruela',
'Vinagre de sidra de Manzana (chico)'
]
articles['only']=[x.lower() for x in productos_valledelsol]

parents={}
parents['only']=['elaborados','productos elaborados','Productos Elaborados','Esenciales']

mensaje['pedido']=''

LINKS = (
  ('Janus Proyecto Rural Integrador', 'http://janus.bio/'),
  ('WhatsApp: '+SHORTCEL,'https://wa.me/'+WHATSAPPNUM),
  ('e-mail: '+showEMAIL(EMAIL),'mailto: '+EMAIL)
  )