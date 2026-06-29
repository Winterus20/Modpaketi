// priority: 0

LootJS.modifiers(event => {
    global.DEDUP_MAPPINGS.forEach(([dupItem, mainItem]) => {
        event.addLootTableModifier(/.*/)
            .replaceLoot(dupItem, mainItem)
    })
})
