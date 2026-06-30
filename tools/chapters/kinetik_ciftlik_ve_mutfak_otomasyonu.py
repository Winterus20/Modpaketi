CHAPTER = {
    'order': 7,
    'filename': 'kinetik_ciftlik_ve_mutfak_otomasyonu',
    'title_en': 'Kinetic Farming & Kitchen Automation',
    'title_tr': 'Kinetik Çiftlik ve Mutfak Otomasyonu',
    'icon': 'create:water_wheel',
    'quests': [
        {
            'key': 'create_intro',
            'x': 0.0,
            'y': 0.0,
            'title_en': 'Kinetic Power',
            'title_tr': 'Kinetik Güç',
            'desc_en': ['Create introduces mechanical engineering and kinetic stress. To generate rotational force, craft a Water Wheel, some Shafts, and Cogwheels to transmit rotational energy.'],
            'desc_tr': ['Create, mekanik mühendisliği ve kinetik stresi sunar. Dönme gücü üretmek için bir Su Çarkı (Water Wheel), miller (Shafts) ve dönme enerjisini iletmek için dişliler (Cogwheels) yapın.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'create:water_wheel',
                },
                {
                    'type': 'item',
                    'item': 'create:shaft',
                },
                {
                    'type': 'item',
                    'item': 'create:cogwheel',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:andesite',
                    'count': 16,
                },
            ],
        },
        {
            'key': 'press',
            'x': -1.5,
            'y': 1.5,
            'dependency': 'create_intro',
            'title_en': 'Iron Sheets',
            'title_tr': 'Demir Plakalar',
            'desc_en': ['The Mechanical Press squeezes ingots into metal sheets. Place items under it on a depot or belt to press them automatically. Crucial for advanced crafting recipes.'],
            'desc_tr': ['Mekanik Pres (Mechanical Press), külçeleri ezerek metal plakalara dönüştürür. Otomatik olarak preslemek için eşyaları altına yerleştirin. Gelişmiş tarifler için çok önemlidir.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'create:mechanical_press',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:iron_ingot',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'mixer',
            'x': 1.5,
            'y': 1.5,
            'dependency': 'create_intro',
            'title_en': 'Alloys and Mixing',
            'title_tr': 'Alaşım ve Karıştırma',
            'desc_en': ['The Mechanical Mixer and Basin mix materials under rotational force. Some recipes require heat, which can be supplied by placing a Blaze Burner beneath the Basin.'],
            'desc_tr': ['Mekanik Mikser ve Hazne (Basin), malzemeleri dönme kuvveti altında karıştırır. Bazı tarifler, Haznenin altına bir Blaze Burner yerleştirilerek sağlanabilecek ısı gerektirir.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'create:mechanical_mixer',
                },
                {
                    'type': 'item',
                    'item': 'create:basin',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:coal',
                    'count': 8,
                },
            ],
        },
        {
            'key': 'automated_kitchen',
            'x': 0.0,
            'y': 3.0,
            'dependency_or': ['press', 'mixer'],
            'title_en': 'Automated Cooking',
            'title_tr': 'Otomatik Mutfak',
            'desc_en': ["Integrate Create machinery with Farmer's Delight using Slice & Dice or Create Central Kitchen. Automate food slicing or soup cooking to supply your colony or spice of life goals effortlessly!"],
            'desc_tr': ["Slice & Dice veya Create Central Kitchen kullanarak Create makinelerini Farmer's Delight ile birleştirin. Koloninizi veya Spice of Life hedeflerinizi zahmetsizce beslemek için yiyecek dilimlemeyi veya çorba pişirmeyi otomatikleştirin!"],
            'tasks': [
                {
                    'type': 'checkmark',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:golden_carrot',
                    'count': 8,
                },
            ],
        },
        {
            'key': 'slicer',
            'x': -3.0,
            'y': 3.0,
            'dependency': 'automated_kitchen',
            'title_en': 'Slice & Dice',
            'title_tr': 'Dilimle & Doğra',
            'desc_en': ["Slice & Dice adds a Slicer that automates Farmer's Delight cutting-board recipes, and a Sprinkler driven by Create's rotation. Hook a Slicer to a belt and a depot to mass-produce sliced ingredients without lifting a finger."],
            'desc_tr': ["Slice & Dice, Farmer's Delight kesme tahtası tariflerini otomatikleştiren bir Dilimleyici (Slicer) ve Create'in dönüşüyle çalışan bir Serpme ekler. Bir Dilimleyiciyi bant ve depoya bağlayın ve parmağınızı kıpırdatarak dilimlenmiş malzeme üretin."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'sliceanddice:slicer',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'sliceanddice:sprinkler',
                },
            ],
        },
        {
            'key': 'central_kitchen',
            'x': 3.0,
            'y': 3.0,
            'dependency': 'automated_kitchen',
            'title_en': 'Central Kitchen',
            'title_tr': 'Merkez Mutfak',
            'desc_en': ["Create Central Kitchen integrates Farmer's Delight cooking with Create: a Blaze Stove heats multiple pots at once and automated recipes pour out syrup, tomato sauce, and more. Grab the Cooking Guide to learn the recipes and start your factory kitchen."],
            'desc_tr': ["Create Central Kitchen, Farmer's Delight pişirmeyi Create ile bütünleştirir: bir Blaze Stove aynı anda birden fazla tencereyi ısıtır ve otomatik tarifler şurup, domates sosu ve daha fazlasını döker. Tarifleri öğrenmek ve fabrika mutfağınızı kurmak için Pişirme Rehberini (Cooking Guide) alın."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'create_central_kitchen:cooking_guide',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'create_central_kitchen:syrup_bucket',
                },
            ],
        },
    ],
}
