// ServerEvents.recipes handles recipe modifications
ServerEvents.recipes(event => {
    // 1. Remove recipes for Tide's duplicate equipment
    event.remove({ output: 'tide:iron_fishing_rod' })
    event.remove({ output: 'tide:golden_fishing_rod' })
    event.remove({ output: 'tide:diamond_fishing_rod' })
    event.remove({ output: 'tide:fishing_line' })
    event.remove({ output: 'tide:fishing_bobber' })

    // Remove recipes for Crabber's Delight palm stuff and broken lanternfish barrel
    const recipesToRemove = [
        'crabbersdelight:lanternfish_barrel',
        'crabbersdelight:lanternfish_from_barrel',
        'crabbersdelight:palm_planks',
        'crabbersdelight:palm_stairs',
        'crabbersdelight:palm_slab',
        'crabbersdelight:palm_fence',
        'crabbersdelight:palm_fence_gate',
        'crabbersdelight:palm_door',
        'crabbersdelight:palm_button',
        'crabbersdelight:palm_pressure_plate',
        'crabbersdelight:palm_sign',
        'crabbersdelight:palm_hanging_sign',
        'crabbersdelight:palm_boat',
        'crabbersdelight:palm_chest_boat',
        'crabbersdelight:palm_wood',
        'crabbersdelight:stripped_palm_wood',
        'crabbersdelight:palm_cabinet'
    ]
    recipesToRemove.forEach(rId => {
        event.remove({ id: rId })
        event.remove({ output: rId })
    })

    // 2. Globally replace duplicate items with their chosen equivalents
    const duplicates = [
        // Tide -> Aquaculture
        ['tide:carp', 'aquaculture:carp'],
        ['tide:catfish', 'aquaculture:catfish'],
        ['tide:rainbow_trout', 'aquaculture:rainbow_trout'],
        ['tide:smallmouth_bass', 'aquaculture:smallmouth_bass'],
        ['tide:tuna', 'aquaculture:tuna'],
        ['tide:arapaima', 'aquaculture:arapaima'],
        ['tide:bluegill', 'aquaculture:bluegill'],
        ['tide:carp_bucket', 'aquaculture:carp_bucket'],
        ['tide:catfish_bucket', 'aquaculture:catfish_bucket'],
        ['tide:rainbow_trout_bucket', 'aquaculture:rainbow_trout_bucket'],
        ['tide:smallmouth_bass_bucket', 'aquaculture:smallmouth_bass_bucket'],
        ['tide:tuna_bucket', 'aquaculture:tuna_bucket'],
        ['tide:arapaima_bucket', 'aquaculture:arapaima_bucket'],
        ['tide:bluegill_bucket', 'aquaculture:bluegill_bucket'],
        ['tide:devils_hole_pupfish_bucket', 'alexsmobs:devils_hole_pupfish_bucket'],
        ['tide:iron_fishing_rod', 'aquaculture:iron_fishing_rod'],
        ['tide:golden_fishing_rod', 'aquaculture:gold_fishing_rod'],
        ['tide:diamond_fishing_rod', 'aquaculture:diamond_fishing_rod'],
        ['tide:fishing_line', 'aquaculture:fishing_line'],

        // Hybrid Aquatic -> Aquaculture (Fish)
        ['hybrid_aquatic:tuna', 'aquaculture:tuna'],
        ['hybrid_aquatic:carp', 'aquaculture:carp'],
        ['hybrid_aquatic:goldfish', 'aquaculture:goldfish'],
        ['hybrid_aquatic:piranha', 'aquaculture:piranha'],

        // Tide -> Hybrid Aquatic (Fish)
        ['tide:coelacanth', 'hybrid_aquatic:coelacanth'],
        ['tide:mackerel', 'hybrid_aquatic:mackerel'],

        // Hybrid Aquatic & Tide -> Hybrid Aquatic (Anglerfish)
        ['tide:anglerfish', 'hybrid_aquatic:anglerfish'],

        // Crabber's Delight & Hybrid Aquatic -> Critters and Companions (Clam, Pearl)
        ['crabbersdelight:clam', 'crittersandcompanions:clam'],
        ['hybrid_aquatic:clam', 'crittersandcompanions:clam'],
        ['crabbersdelight:pearl', 'crittersandcompanions:pearl'],
        ['hybrid_aquatic:pearl', 'crittersandcompanions:pearl'],
        ['hybrid_aquatic:pearl_block', 'crabbersdelight:pearl_block'],

        // Crabber's Delight -> Let's Do Beachparty (Coconut)
        ['crabbersdelight:coconut', 'beachparty:coconut'],

        // Hybrid Aquatic -> Alex's Mobs (Lobster)
        ['hybrid_aquatic:cooked_lobster_tail', 'alexsmobs:cooked_lobster_tail'],

        // Hybrid Aquatic -> Crabber's Delight (Crab, Shrimp)
        ['hybrid_aquatic:cooked_crab', 'crabbersdelight:cooked_crab'],
        ['hybrid_aquatic:cooked_shrimp', 'crabbersdelight:cooked_shrimp'],

        // Hybrid Aquatic -> Alex's Mobs (Shark Tooth)
        ['hybrid_aquatic:shark_tooth', 'alexsmobs:shark_tooth'],

        // Aquaculture & Crabber's Delight -> Alex's Mobs (Fish Bones)
        ['aquaculture:fish_bones', 'alexsmobs:fish_bones'],
        ['crabbersdelight:fish_bones', 'alexsmobs:fish_bones'],

        // Beachparty & Hybrid Aquatic -> Aquaculture (Message in a Bottle)
        ['beachparty:message_in_a_bottle', 'aquaculture:message_in_a_bottle'],
        ['hybrid_aquatic:message_in_a_bottle', 'aquaculture:message_in_a_bottle'],

        // Crabber's Delight -> Let's Do Beachparty (Palm Wood Set)
        ['crabbersdelight:palm_log', 'beachparty:palm_log'],
        ['crabbersdelight:palm_wood', 'beachparty:palm_wood'],
        ['crabbersdelight:palm_planks', 'beachparty:palm_planks'],
        ['crabbersdelight:palm_stairs', 'beachparty:palm_stairs'],
        ['crabbersdelight:palm_slab', 'beachparty:palm_slab'],
        ['crabbersdelight:palm_fence', 'beachparty:palm_fence'],
        ['crabbersdelight:palm_fence_gate', 'beachparty:palm_fence_gate'],
        ['crabbersdelight:palm_door', 'beachparty:palm_door'],
        ['crabbersdelight:palm_button', 'beachparty:palm_button'],
        ['crabbersdelight:palm_pressure_plate', 'beachparty:palm_pressure_plate'],
        ['crabbersdelight:palm_leaves', 'beachparty:palm_leaves'],
        ['crabbersdelight:palm_sign', 'beachparty:palm_sign'],
        ['crabbersdelight:palm_hanging_sign', 'beachparty:palm_hanging_sign'],
        ['crabbersdelight:palm_boat', 'beachparty:palm_boat'],
        ['crabbersdelight:palm_chest_boat', 'beachparty:palm_chest_boat'],
        ['crabbersdelight:stripped_palm_log', 'beachparty:stripped_palm_log'],
        ['crabbersdelight:stripped_palm_wood', 'beachparty:stripped_palm_wood'],
        ['crabbersdelight:palm_cabinet', 'beachparty:palm_cabinet'],

        // Alex's Mobs <-> Crabber's Delight
        ['alexsmobs:shrimp_fried_rice', 'crabbersdelight:shrimp_fried_rice'],

        // Alex's Mobs <-> Hybrid Aquatic
        ['hybrid_aquatic:blobfish', 'alexsmobs:blobfish'],
        ['hybrid_aquatic:flying_fish', 'alexsmobs:flying_fish'],

        // Newly Unified Raw & Cooked Seafood Duplicates
        ['hybrid_aquatic:raw_crab', 'crabbersdelight:crab'],
        ['hybrid_aquatic:raw_shrimp', 'crabbersdelight:shrimp'],
        ['hybrid_aquatic:raw_lobster', 'alexsmobs:lobster_tail'],
        ['hybrid_aquatic:raw_lobster_tail', 'alexsmobs:lobster_tail'],
        ['hybrid_aquatic:cooked_lobster', 'alexsmobs:cooked_lobster_tail'],
        ['hybrid_aquatic:cooked_clam', 'crabbersdelight:cooked_clam_meat'],
        ['hybrid_aquatic:cooked_mussel', 'beachparty:cooked_mussel_meat'],
        ['hybrid_aquatic:raw_tentacle', 'crabbersdelight:raw_squid_tentacles'],
        ['hybrid_aquatic:cooked_tentacle', 'crabbersdelight:cooked_squid_tentacles'],

        // Let's Do Candlelight -> Farmer's Delight (Cabinets)
        ['candlelight:acacia_cabinet', 'farmersdelight:acacia_cabinet'],
        ['candlelight:bamboo_cabinet', 'farmersdelight:bamboo_cabinet'],
        ['candlelight:birch_cabinet', 'farmersdelight:birch_cabinet'],
        ['candlelight:cherry_cabinet', 'farmersdelight:cherry_cabinet'],
        ['candlelight:crimson_cabinet', 'farmersdelight:crimson_cabinet'],
        ['candlelight:dark_oak_cabinet', 'farmersdelight:dark_oak_cabinet'],
        ['candlelight:jungle_cabinet', 'farmersdelight:jungle_cabinet'],
        ['candlelight:mangrove_cabinet', 'farmersdelight:mangrove_cabinet'],
        ['candlelight:oak_cabinet', 'farmersdelight:oak_cabinet'],
        ['candlelight:spruce_cabinet', 'farmersdelight:spruce_cabinet'],
        ['candlelight:warped_cabinet', 'farmersdelight:warped_cabinet'],

        // Farm & Charm / Croptopia -> Farmer's Delight (Onion & Tomato)
        ['farm_and_charm:onion', 'farmersdelight:onion'],
        ['croptopia:onion', 'farmersdelight:onion'],
        ['farm_and_charm:tomato', 'farmersdelight:tomato'],
        ['croptopia:tomato', 'farmersdelight:tomato'],
        ['farm_and_charm:tomato_seeds', 'farmersdelight:tomato_seeds'],
        ['croptopia:cabbage', 'farmersdelight:cabbage'],
        ['croptopia:rice', 'farmersdelight:rice'],

        // Croptopia -> Farm & Charm (Strawberry, Barley, Oat, Flour)
        ['croptopia:strawberry', 'farm_and_charm:strawberry'],
        ['croptopia:barley', 'farm_and_charm:barley'],
        ['croptopia:oat', 'farm_and_charm:oat'],
        ['croptopia:flour', 'farm_and_charm:flour'],

        // Croptopia -> Brewery (Hops)
        ['croptopia:hops', 'brewery:hops'],

        // Candlelight / Croptopia -> Bakery (Toast)
        ['croptopia:toast', 'bakery:toast'],

        // Croptopia -> Bakery (Strawberry Jam)
        ['croptopia:strawberry_jam', 'bakery:strawberry_jam'],

        // Farm & Charm -> Farmer's Delight (Onion Soup)
        ['farm_and_charm:onion_soup', 'farmersdelight:onion_soup'],

        // Croptopia -> Farm & Charm (Potato Soup)
        ['croptopia:potato_soup', 'farm_and_charm:potato_soup'],

        // Croptopia -> Farmer's Delight (Pumpkin Soup & Fruit Salad & Hamburger)
        ['croptopia:pumpkin_soup', 'farmersdelight:pumpkin_soup'],
        ['croptopia:fruit_salad', 'farmersdelight:fruit_salad'],
        ['croptopia:hamburger', 'farmersdelight:hamburger'],

        // Croptopia -> Brewery (Sausage, Fried Chicken, Mashed Potatoes)
        ['croptopia:sausage', 'brewery:sausage'],
        ['croptopia:fried_chicken', 'brewery:fried_chicken'],
        ['croptopia:mashed_potatoes', 'brewery:mashed_potatoes'],

        // Croptopia / Hybrid Aquatic -> Aquaculture (Tuna, Goldfish, Piranha, Sushi, Fish & Chips)
        ['croptopia:tuna', 'aquaculture:tuna'],
        ['croptopia:shrimp', 'crabbersdelight:shrimp'],
        ['croptopia:sushi', 'aquaculture:sushi'],
        ['croptopia:fish_and_chips', 'aquaculturedelight:fish_and_chips'],

        // Brewery -> Farmer's Delight (Rope)
        ['brewery:rope', 'farmersdelight:rope'],

        // Farm & Charm -> Farmer's Delight (Stove)
        ['farm_and_charm:stove', 'farmersdelight:stove'],

        // Farm & Charm -> Farmer's Delight (Wild Crops)
        ['farm_and_charm:wild_onions', 'farmersdelight:wild_onions'],
        ['farm_and_charm:wild_tomatoes', 'farmersdelight:wild_tomatoes'],
        ['farm_and_charm:wild_carrots', 'farmersdelight:wild_carrots'],
        ['farm_and_charm:wild_potatoes', 'farmersdelight:wild_potatoes'],
        ['farm_and_charm:wild_beetroots', 'farmersdelight:wild_beetroots']
    ]

    duplicates.forEach(([dupItem, mainItem]) => {
        event.replaceInput({}, dupItem, mainItem)
        event.replaceOutput({}, dupItem, mainItem)
    })
})

// ServerEvents.tags handles item tagging
ServerEvents.tags('item', event => {
    // 1. Add Aquaculture and Hybrid Aquatic fish to Tide's fish tags so Tide's mechanics/journal can recognize them
    const aqFish = [
        'aquaculture:carp',
        'aquaculture:catfish',
        'aquaculture:rainbow_trout',
        'aquaculture:smallmouth_bass',
        'aquaculture:tuna',
        'aquaculture:bluegill',
        'aquaculture:arapaima',
        'aquaculture:piranha',
        'aquaculture:goldfish',
        'hybrid_aquatic:coelacanth',
        'hybrid_aquatic:mackerel',
        'hybrid_aquatic:anglerfish'
    ]
    aqFish.forEach(fish => {
        event.add('tide:fish', fish)
        event.add('tide:cookable_fish', fish)
    })

    // 2. Fix Fisherman's Trap bait limitation: add Aquaculture and Tide baits
    const baits = [
        'aquaculture:worm',
        'aquaculture:leech',
        'tide:bait',
        'tide:abyss_bait',
        'tide:incandescent_bait',
        'tide:lucky_bait',
        'tide:magnetic_bait'
    ]
    event.add('fishermens_trap:fish_baits', baits)

    // 3. Add Aquaculture rods to Tide's fishing rod tags so Tide's minigame and hook logic applies to them
    const aqRods = [
        'aquaculture:iron_fishing_rod',
        'aquaculture:gold_fishing_rod',
        'aquaculture:diamond_fishing_rod',
        'aquaculture:neptunium_fishing_rod'
    ]
    aqRods.forEach(rod => {
        event.add('tide:fishing_rods', rod)
    })
    // Neptunium fishing rod is lava-resistant, so it goes to lava_fishing_rods as well
    event.add('tide:lava_fishing_rods', 'aquaculture:neptunium_fishing_rod')

    // 4. Unify pearl tags (item → crittersandcompanions; block → crabbersdelight — tek block modu)
    event.add('forge:pearls', 'crittersandcompanions:pearl')
    event.add('forge:storage_blocks/pearl', 'crabbersdelight:pearl_block')
})
