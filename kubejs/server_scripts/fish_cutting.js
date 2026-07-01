// priority: 1
// Farmer's Delight cutting board compatibility for Tide, Aquaculture 2, Hybrid Aquatic & Critters and Companions fish.
// Also includes custom cooking pot recipes for Let's Do Candlelight gourmet meals.

ServerEvents.recipes(event => {
    // 1. Salmon Slice (Pink/Red Meat Fish)
    const salmonFish = [
        'aquaculture:rainbow_trout',
        'aquaculture:tuna',
        'aquaculture:red_shrooma',
        'aquaculture:red_grouper',
        'aquaculture:pink_salmon',
        'aquaculture:brown_trout'
    ];

    // 2. Cod Slice (White/Other Meat Fish)
    const codFish = [
        'aquaculture:carp',
        'aquaculture:catfish',
        'aquaculture:smallmouth_bass',
        'aquaculture:bluegill',
        'aquaculture:arapaima',
        'aquaculture:piranha',
        'aquaculture:goldfish',
        'aquaculture:minnow',
        'aquaculture:perch',
        'aquaculture:pollock',
        'aquaculture:atlantic_cod',
        'aquaculture:blackfish',
        'aquaculture:atlantic_herring',
        'aquaculture:pacific_halibut',
        'aquaculture:atlantic_halibut',
        'aquaculture:bayad',
        'aquaculture:boulti',
        'aquaculture:capitaine',
        'aquaculture:gar',
        'aquaculture:muskellunge',
        'aquaculture:synodontis',
        'aquaculture:tambaqui',
        'hybrid_aquatic:coelacanth',
        'hybrid_aquatic:mackerel',
        'hybrid_aquatic:anglerfish',
        'hybrid_aquatic:betta',
        'hybrid_aquatic:cichlid',
        'hybrid_aquatic:danio',
        'hybrid_aquatic:discus',
        'hybrid_aquatic:gourami',
        'hybrid_aquatic:pleco',
        'hybrid_aquatic:sunfish',
        'hybrid_aquatic:tetra',
        'hybrid_aquatic:tiger_barb',
        'alexsmobs:blobfish',
        'alexsmobs:flying_fish',
        'crittersandcompanions:koi_fish'
    ];

    // Giant fish list (gives 3 slices)
    const giantFish = [
        'aquaculture:arapaima',
        'aquaculture:atlantic_halibut',
        'aquaculture:pacific_halibut',
        'aquaculture:capitaine',
        'aquaculture:muskellunge',
        'aquaculture:tuna'
    ];

    // Small fish list (gives 1 slice)
    const smallFish = [
        'aquaculture:minnow',
        'aquaculture:goldfish',
        'hybrid_aquatic:betta',
        'hybrid_aquatic:cichlid',
        'hybrid_aquatic:danio',
        'hybrid_aquatic:discus',
        'hybrid_aquatic:gourami',
        'hybrid_aquatic:pleco',
        'hybrid_aquatic:sunfish',
        'hybrid_aquatic:tetra',
        'hybrid_aquatic:tiger_barb'
    ];

    // Register cutting board recipes
    const registerFishCutting = (fishList, sliceItem) => {
        fishList.forEach(fish => {
            // Skip aquaculture:catfish since it's already configured in mod_compat_fixes.js
            if (fish === 'aquaculture:catfish') return;

            let count = 2;
            if (giantFish.includes(fish)) {
                count = 3;
            } else if (smallFish.includes(fish)) {
                count = 1;
            }

            event.custom({
                type: 'farmersdelight:cutting',
                ingredients: [{ item: fish }],
                tool: { tag: 'forge:tools/knives' },
                result: [
                    { count: count, item: sliceItem },
                    { item: 'minecraft:bone_meal' }
                ]
            }).id(`harborhaven:cutting/${fish.replace(':', '_')}`);
        });
    };

    registerFishCutting(salmonFish, 'farmersdelight:salmon_slice');
    registerFishCutting(codFish, 'farmersdelight:cod_slice');

    // 3. Custom Gourmet Cooking Pot Recipes for Let's Do Candlelight meals
    // Salmon on White Wine (using salmon slices, tomato sauce, onion in a bowl)
    event.custom({
        type: 'farmersdelight:cooking',
        ingredients: [
            { item: 'farmersdelight:salmon_slice' },
            { item: 'farmersdelight:tomato_sauce' },
            { tag: 'forge:crops/onion' }
        ],
        result: { item: 'candlelight:salmon_on_white_wine' },
        container: { item: 'minecraft:bowl' },
        experience: 0.35,
        cookingTime: 200
    }).id('harborhaven:cooking/salmon_on_white_wine_from_slice');

    // Tropical Fish Supreme (using cod slices, milk, mushroom, onion in a bowl)
    event.custom({
        type: 'farmersdelight:cooking',
        ingredients: [
            { item: 'farmersdelight:cod_slice' },
            { tag: 'forge:milk' },
            { tag: 'forge:mushrooms' },
            { tag: 'forge:crops/onion' }
        ],
        result: { item: 'candlelight:tropical_fish_supreme' },
        container: { item: 'minecraft:bowl' },
        experience: 0.35,
        cookingTime: 200
    }).id('harborhaven:cooking/tropical_fish_supreme_from_slice');

    // Beetroot Salad (using beetroot, lettuce, tomato in a bowl)
    event.custom({
        type: 'farmersdelight:cooking',
        ingredients: [
            { item: 'minecraft:beetroot' },
            { item: 'farm_and_charm:lettuce' },
            { tag: 'forge:crops/tomato' }
        ],
        result: { item: 'candlelight:beetroot_salad' },
        container: { item: 'minecraft:bowl' },
        experience: 0.2,
        cookingTime: 100
    }).id('harborhaven:cooking/beetroot_salad');
});
