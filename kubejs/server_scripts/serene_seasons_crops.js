// priority: 1
// Modded crop fertility tags for Serene Seasons (block + item for tooltips)

const cp = name => `croptopia:${name}`
const fd = name => `farmersdelight:${name}`
const fc = name => `farm_and_charm:${name}`
const vn = name => `vinery:${name}`
const ff = name => `fruitfulfun:${name}`
const cd = name => `corn_delight:${name}`
const fr = name => `farmersrespite:${name}`
const wn = name => `wildernature:${name}`

const springBlocks = [
    fd('onions'), fd('cabbages'), fd('tomatoes'), fd('budding_tomatoes'),
    fd('wild_onions'), fd('wild_cabbages'), fd('wild_tomatoes'),
    fc('onion_crop'), fc('lettuce_crop'), fc('strawberry_crop'),
    fc('tomato_crop'), fc('wild_onions'), fc('wild_lettuce'), fc('wild_tomatoes'),
    cp('asparagus_crop'), cp('lettuce_crop'), cp('onion_crop'), cp('greenonion_crop'),
    cp('spinach_crop'), cp('strawberry_crop'), cp('broccoli_crop'), cp('cauliflower_crop'),
    cp('cabbage_crop'), cp('kale_crop'), cp('leek_crop'), cp('radish_crop'),
    cp('turnip_crop'), cp('artichoke_crop'), cp('raspberry_crop'), cp('currant_crop'),
    cp('rhubarb_crop'), cp('cherry_crop'),
    ff('apple_sapling'), ff('cherry_sapling'), vn('apple_tree_sapling'),
    fr('tea_bush'), fr('small_tea_bush'), fr('wild_tea_bush')
]

const summerBlocks = [
    fd('rice'), fd('rice_panicles'), fd('wild_rice'),
    fc('corn_crop'), fc('tomato_crop'), fc('wild_corn'),
    cp('corn_crop'), cp('tomato_crop'), cp('tomatillo_crop'), cp('rice_crop'),
    cp('bellpepper_crop'), cp('chile_pepper_crop'), cp('pepper_crop'),
    cp('cucumber_crop'), cp('eggplant_crop'), cp('soybean_crop'),
    cp('cantaloupe_crop'), cp('honeydew_crop'), cp('squash_crop'), cp('zucchini_crop'),
    cp('blueberry_crop'), cp('blackberry_crop'), cp('grape_crop'), cp('hops_crop'),
    cp('sweetpotato_crop'), cp('peanut_crop'), cp('greenbean_crop'), cp('basil_crop'),
    cp('ginger_crop'), cp('turmeric_crop'), cp('mustard_crop'), cp('pineapple_crop'),
    cp('coffee_crop'), cp('tea_crop'), cp('vanilla_crop'), cp('saguaro_crop'),
    cp('banana_crop'), cp('coconut_crop'), cp('mango_crop'), cp('dragonfruit_crop'),
    cp('kiwi_crop'), cp('starfruit_crop'), cp('avocado_crop'), cp('olive_crop'),
    cp('date_crop'), cp('nutmeg_crop'), cp('orange_crop'), cp('lemon_crop'),
    cp('lime_crop'), cp('grapefruit_crop'), cp('peach_crop'), cp('apricot_crop'),
    cp('nectarine_crop'), cp('plum_crop'), cp('persimmon_crop'), cp('fig_crop'),
    cp('almond_crop'), cp('walnut_crop'), cp('pecan_crop'), cp('cashew_crop'),
    vn('red_grape_bush'), vn('white_grape_bush'),
    vn('jungle_grape_bush_red'), vn('jungle_grape_bush_white'),
    vn('savanna_grape_bush_red'), vn('savanna_grape_bush_white'),
    vn('taiga_grape_bush_red'), vn('taiga_grape_bush_white'),
    vn('grapevine_stem'), vn('grapevine_pot'),
    ff('orange_sapling'), ff('lemon_sapling'), ff('lime_sapling'), ff('grapefruit_sapling'),
    cd('corn_crop'), cd('wild_corn'),
    fr('coffee_bush'), fr('coffee_stem'), fr('coffee_stem_middle'), fr('wild_coffee_bush'),
    wn('hazelnut_bush')
]

const autumnBlocks = [
    fd('wild_beetroots'), fd('wild_carrots'), fd('wild_potatoes'),
    fc('barley_crop'), fc('oat_crop'), fc('wild_barley'), fc('wild_oat'),
    cp('barley_crop'), cp('oat_crop'), cp('cranberry_crop'), cp('garlic_crop'),
    cp('yam_crop'), cp('rutabaga_crop'), cp('celery_crop'), cp('elderberry_crop'),
    cp('apple_crop'), cp('pear_crop'), cp('plum_crop'), cp('peach_crop'),
    cp('apricot_crop'), cp('persimmon_crop'), cp('fig_crop'),
    cp('walnut_crop'), cp('pecan_crop'), cp('almond_crop'), cp('cashew_crop'),
    cp('squash_crop'), cp('sweetpotato_crop'),
    ff('apple_sapling'), ff('cherry_sapling'),
    cd('corn_crop'),
    wn('hazelnut_bush')
]

const winterBlocks = [
    fd('cabbages'), fd('onions'),
    fc('lettuce_crop'), fc('barley_crop'), fc('oat_crop'),
    cp('cabbage_crop'), cp('kale_crop'), cp('onion_crop'), cp('leek_crop'),
    cp('garlic_crop'), cp('turnip_crop'), cp('rutabaga_crop'), cp('celery_crop'),
    cp('cranberry_crop'), cp('elderberry_crop'), cp('spinach_crop')
]

const springItems = [
    fd('cabbage_seeds'), fd('tomato_seeds'), fd('onion'),
    fc('strawberry_seeds'), fc('lettuce_seeds'), fc('tomato_seeds'),
    cp('asparagus_seed'), cp('lettuce_seed'), cp('onion_seed'), cp('greenonion_seed'),
    cp('spinach_seed'), cp('strawberry_seed'), cp('broccoli_seed'), cp('cauliflower_seed'),
    cp('cabbage_seed'), cp('kale_seed'), cp('leek_seed'), cp('radish_seed'),
    cp('turnip_seed'), cp('artichoke_seed'), cp('raspberry_seed'), cp('currant_seed'),
    cp('rhubarb_seed'), cp('cherry_sapling')
]

const summerItems = [
    fd('rice'), fd('tomato_seeds'),
    fc('kernels'), fc('tomato_seeds'),
    cp('corn_seed'), cp('tomato_seed'), cp('tomatillo_seed'), cp('rice_seed'),
    cp('bellpepper_seed'), cp('chile_pepper_seed'), cp('pepper_seed'),
    cp('cucumber_seed'), cp('eggplant_seed'), cp('soybean_seed'),
    cp('cantaloupe_seed'), cp('honeydew_seed'), cp('squash_seed'), cp('zucchini_seed'),
    cp('blueberry_seed'), cp('blackberry_seed'), cp('grape_seed'), cp('hops_seed'),
    cp('sweetpotato_seed'), cp('peanut_seed'), cp('greenbean_seed'),
    cp('pineapple_seed'), cp('coffee_seed'), cp('tea_seed'),
    cp('banana_sapling'), cp('orange_sapling'), cp('lemon_sapling'), cp('lime_sapling'),
    cp('grapefruit_sapling'), cp('peach_sapling'), cp('mango_sapling'),
    wn('hazelnut')
]

const autumnItems = [
    fc('barley_seeds'), fc('oat_seeds'),
    cp('barley_seed'), cp('oat_seed'), cp('cranberry_seed'), cp('garlic_seed'),
    cp('yam_seed'), cp('rutabaga_seed'), cp('celery_seed'), cp('elderberry_seed'),
    cp('apple_sapling'), cp('pear_sapling'), cp('plum_sapling'), cp('peach_sapling'),
    cp('apricot_sapling'), cp('persimmon_sapling'), cp('fig_sapling'),
    cp('walnut_sapling'), cp('pecan_sapling'), cp('almond_sapling'), cp('cashew_sapling'),
    wn('hazelnut')
]

const winterItems = [
    fd('cabbage_seeds'), fd('onion'),
    fc('lettuce_seeds'), fc('barley_seeds'), fc('oat_seeds'),
    cp('cabbage_seed'), cp('kale_seed'), cp('onion_seed'), cp('leek_seed'),
    cp('garlic_seed'), cp('turnip_seed'), cp('rutabaga_seed'), cp('celery_seed'),
    cp('cranberry_seed'), cp('elderberry_seed'), cp('spinach_seed')
]

const addTags = (event, tag, entries) => {
    entries.forEach(entry => event.add(tag, entry))
}

ServerEvents.tags('block', event => {
    addTags(event, 'sereneseasons:spring_crops', springBlocks)
    addTags(event, 'sereneseasons:summer_crops', summerBlocks)
    addTags(event, 'sereneseasons:autumn_crops', autumnBlocks)
    addTags(event, 'sereneseasons:winter_crops', winterBlocks)
})

ServerEvents.tags('item', event => {
    addTags(event, 'sereneseasons:spring_crops', springItems)
    addTags(event, 'sereneseasons:summer_crops', summerItems)
    addTags(event, 'sereneseasons:autumn_crops', autumnItems)
    addTags(event, 'sereneseasons:winter_crops', winterItems)
})
