CHAPTER = {
    'order': 10,
    'filename': 'mahzen_gunlukleri_ve_bag_bozumu',
    'title_en': 'Cellar Diaries & Wine Harvest',
    'title_tr': 'Mahzen Günlükleri ve Bağ Bozumu',
    'icon': 'brewinandchewin:keg',
    'quests': [
        {
            'key': 'keg',
            'x': 0.0,
            'y': 0.0,
            'title_en': 'Fermentation Station',
            'title_tr': 'Fermentasyon İstasyonu',
            'desc_en': ["Brewin' & Chewin' introduces the Keg, which ferments drinks and ages cheese. Place a Keg, fill it, and let time work its magic to brew Beer, Mead, Rice Wine, or Kombucha — each with unique effects."],
            'desc_tr': ["Brewin' & Chewin', içecekleri fermente eden ve peyniri aged yapan Fıçıyı (Keg) sunar. Bir Fıçı yerleştirin, doldurun ve zamanın sihrini Beer, Mead, Pirinç Şarabı veya Kombucha üretmesine izin verin — her biri benzersiz etkilere sahiptir."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'brewinandchewin:keg',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'brewinandchewin:beer',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'brewery',
            'x': -1.5,
            'y': 1.5,
            'dependency': 'keg',
            'title_en': 'The Brewery',
            'title_tr': 'Bira Fabrikası',
            'desc_en': ["Let's Do: Brewery adds a full brewing line. Build a Wooden Brewing Station, grow Hops, and craft mugs of Beer, Pretzels, and Sausage to host a proper brewfest. Don't drink too much, or the Breathalyzer will give you away!"],
            'desc_tr': ["Let's Do: Brewery, tam bir bira yapım hattı ekler. bir Ahşap Mayalama İstasyonu (Wooden Brewing Station) kurun, Şerbetçi Otunu (Hops) büyütün ve gerçek bir brewfest düzenlemek için biralar, Pretzel ve Sosis yapın. Çok içmeyin, yoksa Alkolmetre (Breathalyzer) sizi ele verir!"],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'brewery:wooden_brewingstation',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'brewery:beer_mug',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'cheese',
            'x': 1.5,
            'y': 1.5,
            'dependency': 'keg',
            'title_en': 'Aged Cheese',
            'title_tr': 'Yıllandırılmış Peynir',
            'desc_en': ['Age a Flaxen Cheese Wheel in the Keg to turn it into a sharp, sliceable delicacy. Combine it with bread, pasta, or use it in Cheesy Pasta and Fondue for a rich, comforting meal.'],
            'desc_tr': ["Bir Külçe Peyniri (Flaxen Cheese Wheel) Fıçıda aged ederek keskin, dilimlenebilir bir lezzete dönüştürün. Ekmek, makarna ile birleştirin veya Peynirli Makarna (Cheesy Pasta) ve Fondü'de kullanarak zengin, doyurucu bir öğün hazırlayın."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'brewinandchewin:flaxen_cheese_wheel',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'brewinandchewin:cheesy_pasta',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'beach_party',
            'x': 0.0,
            'y': 3.5,
            'dependency': 'keg',
            'title_en': 'Beach Party!',
            'title_tr': 'Plaj Partisi!',
            'desc_en': ["Let's Do: Beachparty brings tropical fun. Set down a Beach Chair and a Mini Fridge, then mix a Coconut Cocktail or Honey Cocktail. Hunt for buried message-in-a-bottle loot and relax by the waves."],
            'desc_tr': ["Let's Do: Beachparty, tropik eğlence getirir. bir Plaj Sandalyesi (Beach Chair) ve bir Mini Buzdolabı yerleştirin, ardından bir Hindistan Cevizi Kokteyli veya Bal Kokteyli karıştırın. Kumda gömülü şişedeki-mektup ganimetini arayın ve dalgaların yanında dinlenin."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'beachparty:beach_chair',
                },
                {
                    'type': 'item',
                    'item': 'beachparty:coconut_cocktail',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'beachparty:mini_fridge',
                },
            ],
        },
    ],
}
