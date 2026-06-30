CHAPTER = {
    'order': 9,
    'filename': 'gizemli_magaralar_ve_kesif',
    'title_en': 'Mysterious Caves \\& Exploration',
    'title_tr': 'Gizemli Mağaralar ve Keşif',
    'icon': 'alexscaves:cave_tablet',
    'quests': [
        {
            'key': 'explore_intro',
            'x': 0.0,
            'y': 0.0,
            'title_en': 'Wildlife Encyclopedia',
            'title_tr': 'Yaban Hayatı Ansiklopedisi',
            'desc_en': ["This world is full of wild beasts and birds. Craft the Animal Dictionary from Alex's Mobs to learn taming methods, drops, and ecosystem interactions for all creatures."],
            'desc_tr': ["Bu dünya vahşi hayvanlar ve kuşlarla doludur. Tüm canlıların evcilleştirme yöntemlerini, düşürdükleri eşyaları ve ekosistem etkileşimlerini öğrenmek için Alex's Mobs'tan Hayvan Sözlüğü'nü (Animal Dictionary) yapın."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'alexsmobs:animal_dictionary',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:melon_seeds',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'caves_tablet',
            'x': -1.5,
            'y': 1.5,
            'dependency': 'explore_intro',
            'title_en': 'Deep Cave Biomes',
            'title_tr': 'Derin Mağara Biyomları',
            'desc_en': ["Alex's Caves introduces 5 subterranean biomes filled with magnetic forces, toxic waste, prehistoric dinosaurs, bioluminescent oceans, and dark hollows. Locate one using a Cave Tablet."],
            'desc_tr': ["Alex's Caves; manyetik kuvvetler, toksik atıklar, tarih öncesi dinozorlar, biyolüminesans okyanuslar ve karanlık boşluklarla dolu 5 yeraltı biyomu sunar. Bir Mağara Tableti (Cave Tablet) kullanarak birini bulun."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'alexscaves:cave_tablet',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:iron_pickaxe',
                },
            ],
        },
        {
            'key': 'wildernature_bounty',
            'x': 1.5,
            'y': 1.5,
            'dependency': 'explore_intro',
            'title_en': "Hunter's Bounties",
            'title_tr': 'Avcı İlanları',
            'desc_en': ['Wildernature adds a Bounty Board where you can accept hunting contracts to track down wild animals for rewards. Craft a Bounty Board, take a Common Contract, and start earning loot bags and trophies from the wilderness.'],
            'desc_tr': ['Wildernature, ödüller karşılığı vahşi hayvanları izlemeniz için avcılık sözleşmeleri kabul edebileceğiniz bir İlan Tahtası (Bounty Board) ekler. Bir İlan Tahtası yapın, bir Sözleşme alın ve doğadan ganimet çantaları ve trofe kazanmaya başlayın.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'wildernature:bounty_board',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'wildernature:common_contract',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'goblin_trader',
            'x': 0.0,
            'y': 3.0,
            'dependency': 'explore_intro',
            'title_en': 'Underground Merchants',
            'title_tr': 'Yeraltı Tüccarları',
            'desc_en': ['Goblin Traders spawn deep in the caves and offer rare trades for emeralds. Some goblins even sell vein-mining tools. Explore the caves below, find a Goblin Trader, and trade for something shiny!'],
            'desc_tr': ['Goblin Tüccarlar mağaraların derinliklerinde belirir ve zümrüt karşılığında nadir takaslar sunar. Bazı goblinler damar-madenciliği aletleri bile satar. Aşağıdaki mağaraları keşfedin, bir Goblin Tüccar bulun ve parlayan bir şeyler alın!'],
            'tasks': [
                {
                    'type': 'checkmark',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:emerald',
                    'count': 4,
                },
            ],
        },
    ],
}
