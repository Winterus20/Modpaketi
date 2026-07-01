// priority: 1
// Fixes for mod integration issues (LO, Naturalist Delight, TFC leftovers)

ServerEvents.recipes(event => {
    // Naturalist catfish is banned by Alex's Mobs compat; redirect FD cutting to Aquaculture
    event.remove({ id: 'farmerd_naturalist_compat:cutting/catfish' })
    event.remove({ id: 'farmerd_naturalist_compat:cutting/catfish_cooked' })

    event.custom({
        type: 'farmersdelight:cutting',
        ingredients: [{ item: 'aquaculture:catfish' }],
        result: [
            { count: 2, item: 'farmersdelight:cod_slice' },
            { item: 'minecraft:bone_meal' }
        ],
        tool: { tag: 'forge:tools/knives' }
    }).id('harborhaven:cutting/aquaculture_catfish')

    // Aquaculture 2.5.x has no cooked_catfish item; smelt to fish_fillet_cooked instead
    event.shapeless('alexsmobs:banana', ['croptopia:banana']).id('harborhaven:compat/croptopia_banana_to_alexsmobs')

    // Broken TFC compat recipes shipped inside Livestock Overhaul without TFC present
    event.remove({ id: 'tfc:tfc_bucket' })
    event.remove({ id: 'tfc:wool_yarn_lo' })
    event.remove({ id: 'tfc:leather_knapping/light_saddle' })
    event.remove({ id: 'tfc:leather_knapping/heavy_saddle' })
    event.remove({ id: 'tfc:leather_knapping/wagon_harness' })
})
