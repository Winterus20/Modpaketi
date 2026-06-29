// JEIEvents.hideItems handles item hiding in Just Enough Items
JEIEvents.hideItems(event => {
    const hiddenItems = [
        // Tide duplicate gear and fish
        'tide:iron_fishing_rod',
        'tide:golden_fishing_rod',
        'tide:diamond_fishing_rod',
        'tide:fishing_line',
        'tide:fishing_bobber',
        'tide:carp',
        'tide:catfish',
        'tide:rainbow_trout',
        'tide:smallmouth_bass',
        'tide:tuna',
        'tide:arapaima',
        'tide:bluegill',
        'tide:coelacanth',
        'tide:mackerel',
        'tide:carp_bucket',
        'tide:catfish_bucket',
        'tide:rainbow_trout_bucket',
        'tide:smallmouth_bass_bucket',
        'tide:tuna_bucket',
        'tide:arapaima_bucket',
        'tide:bluegill_bucket',
        'tide:devils_hole_pupfish_bucket',
        'tide:anglerfish', // Tide version is hidden, Hybrid Aquatic's is kept

        // Hybrid Aquatic duplicate fish
        'hybrid_aquatic:tuna',
        'hybrid_aquatic:carp',
        'hybrid_aquatic:goldfish',
        'hybrid_aquatic:piranha',
        'hybrid_aquatic:blobfish',
        'hybrid_aquatic:flying_fish',

        // Crabber's Delight & Hybrid Aquatic duplicates
        'crabbersdelight:clam',
        'hybrid_aquatic:clam',
        'crabbersdelight:pearl',
        'hybrid_aquatic:pearl',
        'hybrid_aquatic:pearl_block',
        'crabbersdelight:coconut',

        // Hybrid Aquatic duplicates (Alex's Mobs equivalents)
        'hybrid_aquatic:lobster',
        'hybrid_aquatic:cooked_lobster_tail',
        'hybrid_aquatic:shark_tooth',

        // Hybrid Aquatic duplicates (Crabber's Delight equivalents)
        'hybrid_aquatic:crab',
        'hybrid_aquatic:cooked_crab',
        'hybrid_aquatic:shrimp',
        'hybrid_aquatic:cooked_shrimp',

        // Duplicate fish bones
        'aquaculture:fish_bones',
        'crabbersdelight:fish_bones',

        // Duplicate Message in a bottle
        'beachparty:message_in_a_bottle',
        'hybrid_aquatic:message_in_a_bottle',

        // Crabber's Delight Palm Wood Set (Beachparty's is kept)
        'crabbersdelight:palm_log',
        'crabbersdelight:palm_wood',
        'crabbersdelight:palm_planks',
        'crabbersdelight:palm_stairs',
        'crabbersdelight:palm_slab',
        'crabbersdelight:palm_fence',
        'crabbersdelight:palm_fence_gate',
        'crabbersdelight:palm_door',
        'crabbersdelight:palm_button',
        'crabbersdelight:palm_pressure_plate',
        'crabbersdelight:palm_leaves',
        'crabbersdelight:palm_sign',
        'crabbersdelight:palm_hanging_sign',
        'crabbersdelight:palm_boat',
        'crabbersdelight:palm_chest_boat',
        'crabbersdelight:stripped_palm_log',
        'crabbersdelight:stripped_palm_wood',
        'crabbersdelight:palm_cabinet',

        // Crabber's Delight broken recipes item
        'crabbersdelight:lanternfish_barrel',

        // Alex's Mobs duplicate food
        'alexsmobs:shrimp_fried_rice',

        // Seashell duplicates
        'crabbersdelight:seashell_1',
        'crabbersdelight:seashell_2',
        'crabbersdelight:seashell_3',
        'crabbersdelight:seashell_4',
        'crabbersdelight:seashell_5',
        'crabbersdelight:seashell_6',

        // Duplicate Spawn Eggs
        'tide:anglerfish_spawn_egg',
        'tide:bull_shark_spawn_egg',
        'tide:carp_spawn_egg',
        'tide:coelacanth_spawn_egg',
        'tide:great_white_shark_spawn_egg',
        'tide:mackerel_spawn_egg',
        'tide:manta_ray_spawn_egg',
        'tide:sand_tiger_shark_spawn_egg',
        'tide:tuna_spawn_egg',
        'tide:arapaima_spawn_egg',
        'tide:bluegill_spawn_egg',
        'tide:catfish_spawn_egg',
        'tide:rainbow_trout_spawn_egg',
        'tide:smallmouth_bass_spawn_egg',
        'tide:devils_hole_pupfish_spawn_egg',
        'hybrid_aquatic:otter_spawn_egg',
        'hybrid_aquatic:blobfish_spawn_egg',
        'hybrid_aquatic:comb_jelly_spawn_egg',
        'hybrid_aquatic:flying_fish_spawn_egg',
        'hybrid_aquatic:frilled_shark_spawn_egg',
        'hybrid_aquatic:giant_squid_spawn_egg',
        'hybrid_aquatic:hammerhead_shark_spawn_egg',
        'hybrid_aquatic:lobster_spawn_egg',
        'hybrid_aquatic:orca_spawn_egg',

        // Duplicate Seafood Items
        'hybrid_aquatic:raw_crab',
        'hybrid_aquatic:raw_shrimp',
        'hybrid_aquatic:raw_lobster',
        'hybrid_aquatic:raw_lobster_tail',
        'hybrid_aquatic:cooked_lobster',
        'hybrid_aquatic:cooked_clam',
        'hybrid_aquatic:cooked_mussel',
        'hybrid_aquatic:raw_tentacle',
        'hybrid_aquatic:cooked_tentacle',

        // Mükerrer Candlelight Dolapları
        'candlelight:acacia_cabinet',
        'candlelight:bamboo_cabinet',
        'candlelight:birch_cabinet',
        'candlelight:cherry_cabinet',
        'candlelight:crimson_cabinet',
        'candlelight:dark_oak_cabinet',
        'candlelight:jungle_cabinet',
        'candlelight:mangrove_cabinet',
        'candlelight:oak_cabinet',
        'candlelight:spruce_cabinet',
        'candlelight:warped_cabinet',

        // Mükerrer Tarım & Ekin Ögeleri
        'farm_and_charm:onion',
        'croptopia:onion',
        'farm_and_charm:tomato',
        'croptopia:tomato',
        'farm_and_charm:tomato_seeds',
        'croptopia:cabbage',
        'croptopia:rice',
        'croptopia:strawberry',
        'croptopia:barley',
        'croptopia:oat',
        'croptopia:flour',
        'croptopia:hops',
        'farm_and_charm:wild_onions',
        'farm_and_charm:wild_tomatoes',
        'farm_and_charm:wild_carrots',
        'farm_and_charm:wild_potatoes',
        'farm_and_charm:wild_beetroots',

        // Mükerrer Yemekler & Malzemeler
        'candlelight:toast',
        'croptopia:toast',
        'croptopia:strawberry_jam',
        'candlelight:tomato_sauce',
        'farm_and_charm:onion_soup',
        'croptopia:potato_soup',
        'croptopia:pumpkin_soup',
        'croptopia:fruit_salad',
        'croptopia:hamburger',
        'croptopia:sausage',
        'croptopia:fried_chicken',
        'croptopia:mashed_potatoes',

        // Mükerrer Balıklar & Deniz Ürünleri
        'croptopia:tuna',
        'croptopia:shrimp',
        'hybrid_aquatic:goldfish',
        'hybrid_aquatic:piranha',
        'croptopia:sushi',
        'croptopia:fish_and_chips',

        // Diğer Mükerrer Girdiler
        'brewery:rope',
        'farm_and_charm:stove'
    ]

    hiddenItems.forEach(item => {
        event.hide(item)
    })
})
