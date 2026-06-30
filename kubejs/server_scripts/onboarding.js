// priority: 0

PlayerEvents.loggedIn(event => {
    const player = event.player
    if (player.level.isClientSide()) return

    const data = player.persistentData
    if (data.balik_journal_v3) return

    data.balik_journal_v3 = true
    player.give(Item.of('ftbquests:book'))
    player.tell('§aGörev Kitabı envanterine eklendi.')
})
