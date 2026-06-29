// priority: 0

JEIEvents.hideItems(event => {
    global.HIDDEN_ITEMS.forEach(item => {
        event.hide(item)
    })
})
