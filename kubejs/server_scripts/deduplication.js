// priority: 0

ServerEvents.recipes(event => {
    global.DEDUP_REMOVED_OUTPUTS.forEach(item => {
        event.remove({ output: item })
    })

    global.DEDUP_REMOVED_RECIPES.forEach(recipeId => {
        event.remove({ id: recipeId })
        event.remove({ output: recipeId })
    })

    global.DEDUP_MAPPINGS.forEach(([dupItem, mainItem]) => {
        event.replaceInput({}, dupItem, mainItem)
        event.replaceOutput({}, dupItem, mainItem)
    })
})

ServerEvents.tags('item', event => {
    global.TIDE_FISH_ITEMS.forEach(fish => {
        event.add('tide:fish', fish)
        event.add('tide:cookable_fish', fish)
        event.add('forge:raw_fishes', fish)
    })

    global.FISH_BAITS.forEach(bait => {
        event.add('fishermens_trap:fish_baits', bait)
    })

    global.TIDE_ROD_ITEMS.forEach(rod => {
        event.add('tide:fishing_rods', rod)
    })
    event.add('tide:lava_fishing_rods', 'aquaculture:neptunium_fishing_rod')

    event.add('forge:pearls', 'crittersandcompanions:pearl')
    event.add('forge:storage_blocks/pearl', 'crabbersdelight:pearl_block')

    // Alex's Caves / Productive Bees / Create tag integrations
    event.add('forge:gems/amber', 'alexscaves:amber')
    event.add('forge:amber', 'alexscaves:amber')
    event.add('forge:sulfur', 'alexscaves:sulfur')
    event.add('forge:dusts/sulfur', 'alexscaves:sulfur')
    event.add('forge:limestone', 'alexscaves:limestone')
    event.add('forge:limestone', 'create:limestone')
})

