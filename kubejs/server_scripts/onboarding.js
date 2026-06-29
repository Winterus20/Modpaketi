// priority: 0

PlayerEvents.loggedIn(event => {
    const player = event.player
    if (player.level.isClientSide()) return

    const data = player.persistentData
    if (data.balik_journal_v2) return

    data.balik_journal_v2 = true
    player.give(Item.of('patchouli:guide_book', '{"patchouli:book":"balik:field_journal"}'))
    player.tell('§aKöy Günlüğü envanterine eklendi.')
})
