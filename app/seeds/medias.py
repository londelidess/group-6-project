from app.models import db, Media, Post, environment, SCHEMA
from sqlalchemy.sql import text


def seed_medias():
    media1 = Media(post_id=1, media_type='image', media_url='https://a0.muscache.com/im/pictures/prohost-api/Hosting-909399031194511254/original/5a311792-559c-45de-8352-f14b4fff9f78.jpeg?im_w=1200')
    media2 = Media(post_id=2, media_type='image', media_url='https://images-ext-2.discordapp.net/external/x1fwKg75qUWD3gq8-hForasipeJ2Un8byqkyLYO-Htc/https/www.thinkrightme.com/wp-content/uploads/2022/02/shutterstock_1064525450.jpg?width=720&height=429')
    media3 = Media(post_id=3, media_type='image', media_url='https://1.bp.blogspot.com/-RuyIFjxvzug/XpyWTDH1-LI/AAAAAAABgYY/1IuSnJ_Y-lcPLSav2SGo-86mDWEw-yKBACPcBGAsYHg/s1200-rw/photos_of_machu_picchu_peru_4.jpg')
    media4 = Media(post_id=4, media_type='image', media_url='https://images-ext-1.discordapp.net/external/Uun0K68F2pAJD41fP9UgeY_ItHSVdP8u-_Z6qAQ1IbY/https/nerdnomads.com/wp-content/uploads/2021/02/Street-food-Yaowarat-Street-Chinatown-Bangkok.jpg?width=720&height=480')
    media5 = Media(post_id=5, media_type='image', media_url='https://cdn.pixabay.com/photo/2023/05/30/22/20/ai-generated-8030115_1280.png')
    media6 = Media(post_id=1, media_type='image', media_url='https://a0.muscache.com/im/pictures/prohost-api/Hosting-909399031194511254/original/3752f812-e337-4474-80e7-3641ddffe9ad.jpeg?im_w=1440')
    media7 = Media(post_id=6, media_type='image', media_url='https://scx2.b-cdn.net/gfx/news/2016/stellarghost.jpg')
    media8 = Media(post_id=7, media_type='image', media_url='https://images.adsttc.com/media/images/6290/ac61/3e4b/31f4/d600/0001/medium_jpg/155108.jpg?1653648474')
    media9 = Media(post_id=8, media_type='image', media_url='https://i.pinimg.com/564x/00/bc/fa/00bcfa572b8245a8791dd3fc350fa89a.jpg')
    media10 = Media(post_id=9, media_type='image', media_url='https://publish.purewow.net/wp-content/uploads/sites/2/2021/04/national-parks-in-california-yosemite.jpg?fit=728%2C921')
    media11 = Media(post_id=10, media_type='image', media_url='https://www.udiscovermusic.com/wp-content/uploads/2020/12/Jazz-New-Thing-Featured-Art.jpg')
    media12 = Media(post_id=11, media_type='image', media_url='https://assets.st-note.com/img/1654584322718-eCGyAs8Q9o.jpg?width=2000height=2000fit=boundsquality=85')
    media13 = Media(post_id=12, media_type='image', media_url='https://i.etsystatic.com/6630676/r/il/8f86db/2219511397/il_fullxfull.2219511397_c2a7.jpg')
    media14 = Media(post_id=13, media_type='image', media_url='https://luxurycolumnist.com/wp-content/uploads/2022/02/Oscar-Niemeyer-International-Cultural-Centre-Asturias-Most-Famous-Architects.jpg')
    media15 = Media(post_id=14, media_type='image', media_url='https://i.pinimg.com/564x/9e/90/e7/9e90e750e9225d652c259f06b63ecb01.jpg')
    media16 = Media(post_id=15, media_type='image', media_url='https://image.cnbcfm.com/api/v1/image/106964911-1635070875003-Xpeng_Flying_Car_.png?v=1635071509&w=1600&h=900')
    media17 = Media(post_id=16, media_type='image', media_url='https://media.makeameme.org/created/why-did-the-gap3ab.jpg')
    media18 = Media(post_id=17, media_type='image', media_url='https://www.cnet.com/a/img/resize/d03e72c27eb86305dbee285390446b89dd47b330/hub/2021/10/07/5a02a361-77d9-49db-9b40-d0e504d6af55/mysterysquid.jpg?auto=webp&fit=crop&height=675&width=1200')
    media19 = Media(post_id=18, media_type='image', media_url='https://i.imgflip.com/525h5r.jpg')
    media20 = Media(post_id=19, media_type='image', media_url='https://swayshow.files.wordpress.com/2015/03/jumpin-jive-cab_calloway-fayard_harold_nicholas030.jpg')
    media21 = Media(post_id=20, media_type='image', media_url='https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/1-how-do-you-organize-a-space-party-you-planet-noirty-designs.jpg')
    media22 = Media(post_id=21, media_type='image', media_url='https://i.pinimg.com/736x/39/5e/04/395e046e2dc2077f9c9b5387db45d9fd--vintage-auto-vintage-cars.jpg')
    media23 = Media(post_id=22, media_type='image', media_url='https://i.imgflip.com/21rw8o.jpg')
    media24 = Media(post_id=23, media_type='image', media_url='https://cdn8.openculture.com/wp-content/uploads/2016/03/Miyazaki-Running-4.jpg')
    media25 = Media(post_id=24, media_type='image', media_url='https://images-us.bookshop.org/ingram/9781501144325.jpg?height=500&v=v2')
    media26 = Media(post_id=25, media_type='image', media_url='https://images.squarespace-cdn.com/content/v1/5f024ccc9fa198769d8942bf/1596468691657-WDVBPJ4Z9O4C2C9Y8QG8/Salad+dressing.png?format=750w')
    media27 = Media(post_id=26, media_type='image', media_url='https://th-thumbnailer.cdn-si-edu.com/8yMAOfbFD4mREBGWs7AdqByEM3U=/fit-in/1600x0/https%3A%2F%2Ftf-cmsv2-smithsonianmag-media.s3.amazonaws.com%2Ffiler%2Fac%2F26%2Fac26fc2a-9fe6-4d47-87c3-1749bcc2ceba%2Ftikal-pyramid.jpg')
    media28 = Media(post_id=27, media_type='image', media_url='https://i.imgflip.com/s5fct.jpg')
    media29 = Media(post_id=28, media_type='image', media_url='https://miro.medium.com/v2/resize:fit:828/format:webp/1*eirCSYtSgHLp3AoaBubDXw.png')
    media30 = Media(post_id=29, media_type='image', media_url='https://i.imgflip.com/5f0rtg.jpg')
    media31 = Media(post_id=30, media_type='image', media_url='https://cdn3.volusion.com/euhfr.xvuyx/v/vspfiles/photos/1500-4002-A254-2.jpg?v-cache=1662121011')
    media32 = Media(post_id=31, media_type='gif', media_url='https://media.tenor.com/PeIy6o0R9kAAAAAC/mark-zuckerberg-zuckerberg.gif')


    db.session.add(media1)
    db.session.add(media2)
    db.session.add(media3)
    db.session.add(media4)
    db.session.add(media5)
    db.session.add(media6)
    db.session.add(media7)
    db.session.add(media8)
    db.session.add(media9)
    db.session.add(media10)
    db.session.add(media11)
    db.session.add(media12)
    db.session.add(media13)
    db.session.add(media14)
    db.session.add(media15)
    db.session.add(media16)
    db.session.add(media17)
    db.session.add(media18)
    db.session.add(media19)
    db.session.add(media20)
    db.session.add(media21)
    db.session.add(media22)
    db.session.add(media23)
    db.session.add(media24)
    db.session.add(media25)
    db.session.add(media26)
    db.session.add(media27)
    db.session.add(media28)
    db.session.add(media29)
    db.session.add(media30)
    db.session.add(media31)
    db.session.add(media32)

    db.session.commit()

def undo_medias():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.medias RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM medias"))
        db.session.execute(text("DELETE FROM posts"))

    db.session.commit()
