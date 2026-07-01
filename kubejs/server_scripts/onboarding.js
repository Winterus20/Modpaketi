// priority: 0

PlayerEvents.loggedIn(event => {
    const player = event.player
    if (player.level.isClientSide()) return

    const data = player.persistentData
    if (data.harborhaven_onboarding_v1) return
    if (data.balik_journal_v3) {
        data.harborhaven_onboarding_v1 = true
        return
    }

    data.harborhaven_onboarding_v1 = true
    player.give(Item.of('ftbquests:book'))
    player.tell('§aGörev Kitabı envanterine eklendi.')
})
