CHAPTER = {
    'order': 8,
    'filename': 'kendi_kasabani_kur',
    'title_en': 'Build Your Own Town',
    'title_tr': 'Kendi Kasabanı Kur',
    'icon': 'minecolonies:blockhuttownhall',
    'quests': [
        {
            'key': 'minecolonies_intro',
            'x': 0.0,
            'y': 0.0,
            'title_en': 'Supply Camp',
            'title_tr': 'Tedarik Kampı',
            'desc_en': ["MineColonies lets you build a thriving city of citizens. Start by crafting a Supply Camp Deployer and right-clicking it on a flat, clear 16x17 area (no flowers, grass, or holes). Inside the deployed camp's rack you'll find the precious Build Tool and a Town Hall block — the two items every colony is founded on."],
            'desc_tr': ['MineColonies, vatandaşlardan oluşan gelişen bir şehir kurmanızı sağlar. Bir Tedarik Kampı Dağıtıcısı (Supply Camp Deployer) yapın ve düz, temiz bir 16x17 alana (çiçek, çimen veya çukur olmayan) sağ tıklayarak yerleştirin. Yerleştirilen kampın rafında değerli İnşaat Aletini (Build Tool) ve bir Belediye Binası bloğu bulacaksınız — her koloninin temelini oluşturan iki eşya.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'minecolonies:supplycampdeployer',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:oak_log',
                    'count': 32,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:chest',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'town_hall',
            'x': 0.0,
            'y': 1.5,
            'dependency': 'minecolonies_intro',
            'title_en': 'Establishing a Colony',
            'title_tr': 'Koloni Kurmak',
            'desc_en': ['Hold the Build Tool, right-click the ground, and select the Town Hall to preview and place it. Then right-click the placed Town Hall block and choose Create Colony. Sign the Settlement Covenant and your first citizens will arrive shortly!'],
            'desc_tr': ["İnşaat Aletini elinize alın, yere sağ tıklayın ve Belediye Binası'nı (Town Hall) seçerek önizleyip yerleştirin. Ardından yerleştirilen Belediye Binası bloğuna sağ tıklayıp Koloni Oluştur'u seçin. Yerleşim Sözleşmesi'ni imzalayın; ilk vatandaşlarınız kısa süre sonra gelecek!"],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'minecolonies:blockhuttownhall',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecolonies:clipboard',
                },
                {
                    'type': 'item',
                    'item': 'minecraft:bread',
                    'count': 8,
                },
            ],
        },
        {
            'key': 'builder',
            'x': 0.0,
            'y': 3.0,
            'dependency': 'town_hall',
            'title_en': 'The Colony Builder',
            'title_tr': 'Koloni İnşaatçısı',
            'desc_en': ["Citizens cannot construct buildings on their own. Build a Builder's Hut, place it with the Build Tool, assign a Builder, then open its GUI and pick Build Options to start construction. Keep the builder's chest supplied to grow your town."],
            'desc_tr': ["Vatandaşlar binaları kendi başlarına kuramazlar. İnşaatçı Kulübesi (Builder's Hut) yapın, İnşaat Aleti ile yerleştirin, inşaatçı atayın, ardından GUI'sini açıp İnşaat Seçenekleri'ni seçerek inşaata başlayın. İstediği malzemeleri sandığına koyarak şehri genişletin."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'minecolonies:blockhutbuilder',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:stone_bricks',
                    'count': 32,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:oak_planks',
                    'count': 32,
                },
            ],
        },
        {
            'key': 'food_supply',
            'x': 1.5,
            'y': 3.0,
            'dependency': 'builder',
            'title_en': 'Feeding the Citizens',
            'title_tr': 'Vatandaşları Besleme',
            'desc_en': ['Citizens get hungry and stop working if not fed. Establish a Farm Hut or Fishery Hut so your colonists can gather and produce food automatically. A Farmer also needs a Field block assigned nearby.'],
            'desc_tr': ['Vatandaşlar acıkır ve beslenmezlerse çalışmayı bırakırlar. Kolonistlerinizin otomatik olarak yiyecek toplayıp üretebilmesi için Çiftçi Kulübesi (Farm Hut) veya Balıkçı Kulübesi (Fishery Hut) kurun. Çiftçinin yakınına bir Tarla (Field) bloğu atamanız da gerekir.'],
            'tasks': [
                {
                    'type': 'checkmark',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:wheat_seeds',
                    'count': 8,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:cooked_beef',
                    'count': 8,
                },
            ],
        },
        {
            'key': 'guard_tower',
            'x': 0.0,
            'y': 4.5,
            'dependency': 'builder',
            'title_en': 'Raids \\& Security',
            'title_tr': 'Baskınlar ve Güvenlik',
            'desc_en': ['As your colony grows, barbarians and raiders will attack during the night. Build Guard Towers and recruit guards to defend your citizens!'],
            'desc_tr': ['Koloniniz büyüdükçe, barbarlar ve akıncılar geceleri saldıracaktır. Vatandaşlarınızı savunmak için Nöbetçi Kuleleri (Guard Towers) inşa edin ve muhafızlar kiralayın!'],
            'tasks': [
                {
                    'type': 'checkmark',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:iron_sword',
                },
                {
                    'type': 'item',
                    'item': 'minecraft:iron_shield',
                },
            ],
        },
    ],
}
