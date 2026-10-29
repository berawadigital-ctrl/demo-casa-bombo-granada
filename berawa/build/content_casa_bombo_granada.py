# Contenido de la demo Casa Bombo (Granada) (es/ca/en/fr). Hechos de casabombo.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Superior con terraza privada','Doble deluxe y 2 camas','Cuádruple'],'ca':['Superior amb terrassa privada','Doble deluxe i 2 llits','Quàdruple'],'en':['Superior with private terrace','Deluxe double and twin','Quadruple'],'fr':['Supérieure avec terrasse privée','Double deluxe et deux lits','Quadruple']}
RD={
'es':['50 m² con cama doble, baño con bañera y una terraza privada con mesa, sillas y sofá frente a la Alhambra.','La deluxe (15 m²) tiene cama doble, sofá cama y ventana a la Alhambra; la de 2 camas (12 m²) abre a la terraza y la piscina compartidas.','16 m² con cama doble y dos individuales, baño con ducha y puerta acristalada a la terraza panorámica y la piscina.'],
'ca':['50 m² amb llit doble, bany amb banyera i una terrassa privada amb taula, cadires i sofà davant de l\'Alhambra.','La deluxe (15 m²) té llit doble, sofà llit i finestra a l\'Alhambra; la de 2 llits (12 m²) dona a la terrassa i la piscina compartides.','16 m² amb llit doble i dos individuals, bany amb dutxa i porta vidriera a la terrassa panoràmica i la piscina.'],
'en':['50 m² with a double bed, bathroom with bathtub and a private terrace with table, chairs and sofa facing the Alhambra.','The deluxe (15 m²) has a double bed, sofa bed and a window onto the Alhambra; the twin (12 m²) opens onto the shared terrace and pool.','16 m² with a double bed and two singles, shower room and a glass door onto the panoramic terrace and pool.'],
'fr':['50 m² avec lit double, salle de bain avec baignoire et une terrasse privée avec table, chaises et canapé face à l\'Alhambra.','La deluxe (15 m²) a un lit double, un canapé-lit et une fenêtre sur l\'Alhambra ; la chambre à deux lits (12 m²) donne sur la terrasse et la piscine partagées.','16 m² avec un lit double et deux lits simples, salle d\'eau et porte vitrée sur la terrasse panoramique et la piscine.']}
ART={
'hero':('arches',9801,['#f3e6d4','#e8b27e','#a24a2c','#5f2a2a','#3a1818']),
'intro':('skyline',9802,['#5f2a2a','#e7a568','#f5d5a3','#2c4a3e','#233e33','#162a22']),
'r1':('hills',9811,['#e6ece5','#f1e9d3','#edbb79','#a7bd9d','#7b9a81','#52735c']),
'r2':('arches',9812,['#f0e3cf','#dfad78','#9b4428','#5f2a2a','#3a1818']),
'r3':('waves',9813,['#2c4a3e','#edbd83','#f6deb5','#3c6657','#2c4a3e','#1a3028']),
'g1':('skyline',9821,['#5f2a2a','#e3a266','#f4d29f','#2a483c','#213b31','#152820']),
'g2':('arches',9822,['#eee2ce','#dfae7a','#a14526','#5f2a2a','#3a1818']),
'g3':('waves',9823,['#2a483c','#ebb57c','#f5dcb2','#3a6455','#2a483c','#182e26']),
'g4':('hills',9824,['#e3eae2','#eee6ce','#eab875','#a4ba9a','#78977e','#4f7059']),
'g5':('columns',9825,['#edeae2','#f7f4ee','#ab4e2f','#5f2a2a','#3a1818']),
'g6':('skyline',9826,['#5f2a2a','#e0a064','#f2cf9c','#29473b','#203a30','#14271f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Casa Bombo · Bed and Breakfast en el Albaicín, Granada',see_rooms='Ver habitaciones',hero_k='Granada · Albaicín',hero_t='Desayunar mirando a la Alhambra',hero_s='Bed and Breakfast boutique en pleno Albaicín, con terraza panorámica y piscina frente a la Alhambra.',
 intro_t='Una casa tradicional granadina',intro_p1='Casa Bombo combina el encanto de una casa tradicional granadina con las comodidades para una estancia tranquila, a pocos minutos caminando del centro.',
 intro_p2='Desayuno buffet mediterráneo en la terraza, bar y terraza todo el día, piscina con vistas a la Alhambra y wifi gratis en habitaciones y zonas comunes.',
 stats=['Vistas a la Alhambra','Desayuno incluido','Piscina exterior','Wifi gratis'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Superior con terraza privada, doble deluxe, habitación de 2 camas y cuádruple, con vistas a la Alhambra.',
 svcs=['Desayuno incluido','Wifi gratis','Terraza compartida','Piscina con vistas','Bar y terraza todo el día','Consigna de equipaje','Cuna y parking privado bajo demanda','Traslados bajo demanda'],
 loc_p='Calle Aljibe de Trillo, 22 · 18010 Granada, en el Albaicín. Si vienes en coche, no pongas la dirección en el GPS: escríbeles antes y te indican la ruta y dónde aparcar.',
 chips=['¿Qué habitaciones tiene?','¿El desayuno está incluido?','¿Cómo llego en coche?','¿Cómo se reserva?']),
'ca':dict(title='Casa Bombo · Bed and Breakfast a l\'Albaicín, Granada',see_rooms='Veure habitacions',hero_k='Granada · Albaicín',hero_t='Esmorzar mirant l\'Alhambra',hero_s='Bed and Breakfast boutique al bell mig de l\'Albaicín, amb terrassa panoràmica i piscina davant de l\'Alhambra.',
 intro_t='Una casa tradicional granadina',intro_p1='Casa Bombo combina l\'encant d\'una casa tradicional granadina amb les comoditats per a una estada tranquil·la, a pocs minuts a peu del centre.',
 intro_p2='Esmorzar bufet mediterrani a la terrassa, bar i terrassa tot el dia, piscina amb vistes a l\'Alhambra i wifi gratuït a habitacions i zones comunes.',
 stats=['Vistes a l\'Alhambra','Esmorzar inclòs','Piscina exterior','Wifi gratuït'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Superior amb terrassa privada, doble deluxe, habitació de 2 llits i quàdruple, amb vistes a l\'Alhambra.',
 svcs=['Esmorzar inclòs','Wifi gratuït','Terrassa compartida','Piscina amb vistes','Bar i terrassa tot el dia','Consigna d\'equipatge','Bressol i pàrquing privat sota demanda','Trasllats sota demanda'],
 loc_p='Calle Aljibe de Trillo, 22 · 18010 Granada, a l\'Albaicín. Si hi vas en cotxe, no posis l\'adreça al GPS: escriu-los abans i t\'indiquen la ruta i on aparcar.',
 chips=['Quines habitacions té?','L\'esmorzar està inclòs?','Com hi arribo en cotxe?','Com es reserva?']),
'en':dict(title='Casa Bombo · Bed and Breakfast in the Albaicín, Granada',see_rooms='See the rooms',hero_k='Granada · Albaicín',hero_t='Breakfast facing the Alhambra',hero_s='Boutique Bed and Breakfast in the heart of the Albaicín, with a panoramic terrace and pool facing the Alhambra.',
 intro_t='A traditional Granada house',intro_p1='Casa Bombo combines the charm of a traditional Granada house with the comforts for a quiet stay, a few minutes\' walk from the centre.',
 intro_p2='Mediterranean buffet breakfast on the terrace, bar and terrace all day, a pool with Alhambra views and free wifi in rooms and common areas.',
 stats=['Alhambra views','Breakfast included','Outdoor pool','Free wifi'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Superior with private terrace, deluxe double, twin room and quadruple, with Alhambra views.',
 svcs=['Breakfast included','Free wifi','Shared terrace','Pool with views','Bar and terrace all day','Luggage storage','Cot and private parking on request','Transfers on request'],
 loc_p='Calle Aljibe de Trillo, 22 · 18010 Granada, in the Albaicín. If you come by car, do not put the address in your GPS: write to them first and they will tell you the route and where to park.',
 chips=['What rooms does it have?','Is breakfast included?','How do I arrive by car?','How do I book?']),
'fr':dict(title='Casa Bombo · Bed and Breakfast dans l\'Albaicín, Grenade',see_rooms='Voir les chambres',hero_k='Grenade · Albaicín',hero_t='Petit-déjeuner face à l\'Alhambra',hero_s='Bed and Breakfast de charme au cœur de l\'Albaicín, avec terrasse panoramique et piscine face à l\'Alhambra.',
 intro_t='Une maison traditionnelle de Grenade',intro_p1='Casa Bombo allie le charme d\'une maison traditionnelle de Grenade au confort d\'un séjour au calme, à quelques minutes à pied du centre.',
 intro_p2='Petit-déjeuner buffet méditerranéen en terrasse, bar et terrasse toute la journée, piscine avec vue sur l\'Alhambra et wifi gratuit dans les chambres et les parties communes.',
 stats=['Vue sur l\'Alhambra','Petit-déjeuner inclus','Piscine extérieure','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Supérieure avec terrasse privée, double deluxe, chambre à deux lits et quadruple, avec vue sur l\'Alhambra.',
 svcs=['Petit-déjeuner inclus','Wifi gratuit','Terrasse partagée','Piscine avec vue','Bar et terrasse toute la journée','Consigne à bagages','Lit bébé et parking privé sur demande','Transferts sur demande'],
 loc_p='Calle Aljibe de Trillo, 22 · 18010 Grenade, dans l\'Albaicín. En voiture, ne mettez pas l\'adresse dans le GPS : écrivez-leur avant et ils vous indiqueront l\'itinéraire et où vous garer.',
 chips=['Quelles chambres a-t-il ?','Le petit-déjeuner est-il inclus ?','Comment venir en voiture ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://hotels.cloudbeds.com/reservation/24a5mw'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':RES,'fr':RES})
D=dict(name='Casa Bombo',ac='#5f2a2a',ac2='#2f6b5a',ac2_a11y='#235246',book=BOOK,around=[],foot=FOOT,
 address='Calle Aljibe de Trillo, 22 · 18010 Granada',phones=['+34 958 29 06 35'],emails=['info@casabombo.com'],maps='Casa Bombo, Calle Aljibe de Trillo 22, Granada',t=T)
META=dict(repo='demo-casa-bombo-granada',name='Casa Bombo',legal_name='ITALCARMENES SOCIEDAD LIMITADA',registry_ids=['CIF B18994822'],
 url='https://www.casabombo.com/',domain='casabombo.com',municipality='Granada',province='Granada',sector='bed and breakfast boutique en el Albaicin (Granada)',
 read_at='2026-10-29T17:06:00+01:00',created_at='2026-10-29T17:06:00+01:00',built_at='2026-10-29T17:15:00+01:00',audit_date='2026-10-29T12:52:00+01:00',
 rating=dict(value=4.7,coincide=['telefono','web'],date='2026-10-29T12:50:21+01:00',url='https://www.google.com/maps/place/Casa+Bombo/@37.180081,-3.5935096,17z/data=!4m9!3m8!1s0xd71fcc7a202b989:0xdcb0517801c89a3!5m2!4m1!1i2!8m2!3d37.180081!4d-3.5935096!16s%2Fg%2F11r8ck52r'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas del propio negocio (Cloudbeds, hotels.cloudbeds.com/reservation/24a5mw, enlazado desde casabombo.com); la demo no construye ningun motor.'),
 first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Hay habitación con terraza privada?','K02'),('¿Tienen habitación para cuatro?','K03'),('¿Dónde está?','K04'),('¿Cómo llego en coche?','K05'),('¿Hay parking?','K06'),('¿El desayuno está incluido?','K07'),('¿Hay piscina?','K08'),('¿Hay wifi?','K09'),('¿Tienen bar?','K10'),('¿Cómo compro entradas para la Alhambra?','K11'),('¿Cómo reservo?','K12'),('¿Quién es el titular?','K13'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K12'),('¿Tienen spa?',None)],
'ca':[('Quines habitacions té?','K01'),('Hi ha habitació amb terrassa privada?','K02'),('Teniu habitació per a quatre?','K03'),('On és?','K04'),('Com hi arribo en cotxe?','K05'),('Hi ha pàrquing?','K06'),('L\'esmorzar està inclòs?','K07'),('Hi ha piscina?','K08'),('Hi ha wifi?','K09'),('Teniu bar?','K10'),('Com compro entrades per a l\'Alhambra?','K11'),('Com reservo?','K12'),('Qui és el titular?','K13'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K12'),('Teniu spa?',None)],
'en':[('What rooms does it have?','K01'),('Is there a room with a private terrace?','K02'),('Do you have a room for four?','K03'),('Where is it?','K04'),('How do I arrive by car?','K05'),('Is there parking?','K06'),('Is breakfast included?','K07'),('Is there a pool?','K08'),('Is there wifi?','K09'),('Do you have a bar?','K10'),('How do I buy Alhambra tickets?','K11'),('How do I book?','K12'),('Who is the owner?','K13'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K12'),('Is there a spa?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Y a-t-il une chambre avec terrasse privée ?','K02'),('Avez-vous une chambre pour quatre ?','K03'),('Où est-il ?','K04'),('Comment venir en voiture ?','K05'),('Y a-t-il un parking ?','K06'),('Le petit-déjeuner est-il inclus ?','K07'),('Y a-t-il une piscine ?','K08'),('Y a-t-il le wifi ?','K09'),('Avez-vous un bar ?','K10'),('Comment acheter les billets de l\'Alhambra ?','K11'),('Comment réserver ?','K12'),('Qui est le titulaire ?','K13'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K12'),('Y a-t-il un spa ?',None)]}
