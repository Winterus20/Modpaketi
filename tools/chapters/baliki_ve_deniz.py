CHAPTER = {
    'order': 6,
    'filename': 'baliki_ve_deniz',
    'title_en': 'Fishing & Oceans',
    'title_tr': 'Derya Kuzuları ve Denizlerin Sırrı',
    'icon': 'aquaculture:iron_fishing_rod',
    'quests': [
        {
            'key': 'fishing_intro',
            'x': 0.0,
            'y': 0.0,
            'title_en': 'Cast Your First Line',
            'title_tr': 'İlk Oltanı Fırlat',
            'desc_en': ['Perhaps the most peaceful moment of your new life is watching your bobber float on the gentle water. Aquaculture replaces weak old fishing rods with durable, upgradable metal ones. Craft an Iron Fishing Rod to start your journey. Listen to the music of the rivers.'],
            'desc_tr': ['Yeni hayatının belki de en huzurlu anı, bir su kenarında oltanın ucunu izlemektir. Aquaculture, eski zayıf oltaları dayanıklı ve geliştirilebilir metal oltalarla değiştirir. Kendi serüvenine başlamak için bir Demir Olta yap. Nehirlerin ve denizlerin sesine kulak ver.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'aquaculture:iron_fishing_rod',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'aquaculture:worm',
                    'count': 8,
                },
            ],
        },
        {
            'key': 'gold_rod',
            'x': 0.0,
            'y': 1.5,
            'dependency': 'fishing_intro',
            'title_en': 'Shimmering Fortune',
            'title_tr': 'Parıldayan Şans',
            'desc_en': ["The alluring gleam of gold isn't just for show—it also captivates creatures beneath the surface. The Golden Fishing Rod uses its special alloy to lure fish faster and boost your luck. A perfect choice for the lucky angler!"],
            'desc_tr': ['Altının büyleyici ışıltısı sadece göz alıcı değildir, aynı zamanda suyun altındaki canlıları da cezbeder. Altın Olta (Gold Fishing Rod), özel alaşımı sayesinde balıkları kendine daha hızlı çeker ve yakalama şansınızı artırır. Şansına güvenen bir balıkçı için mükemmel bir seçim!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'aquaculture:gold_fishing_rod',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'aquaculture:gold_hook',
                },
            ],
        },
        {
            'key': 'diamond_rod',
            'x': 0.0,
            'y': 3.0,
            'dependency': 'gold_rod',
            'title_en': 'Indomitable Will',
            'title_tr': 'Yıkılmaz İrade',
            'desc_en': ['For the moments when waves crash hardest and ocean giants strain your line, you need something stronger. The Diamond Fishing Rod is forged to withstand the toughest fights and fiercest currents. With near-infinite durability, it is essential for long expeditions.'],
            'desc_tr': ['Dalgaların en sert vurduğu, okyanus devlerinin oltanı zorladığı anlar için daha güçlü bir şeye ihtiyacın var. Elmas Olta (Diamond Fishing Rod), en zorlu çekişlere ve hırçın dalgalara dayanacak şekilde dövülmüştür. Neredeyse sınırsız dayanıklılığıyla uzun soluklu avların vazgeçilmezidir.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'aquaculture:diamond_fishing_rod',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'aquaculture:diamond_hook',
                },
            ],
        },
        {
            'key': 'neptunium_rod',
            'x': 0.0,
            'y': 10.5,
            'dependencies': ['diamond_rod', 'neptunium_ingot'],
            'title_en': 'Scepter of the Sea God',
            'title_tr': 'Deniz Tanrısının Asası',
            'desc_en': ['The legendary Neptunium Fishing Rod, spoken of in sailor myths... This rod can conquer not only the deepest oceans but also the boiling lava seas of the Nether. Prepare to catch the magmatic mysteries below!'],
            'desc_tr': ["Efsanelere konu olan Neptünyum Olta (Neptunium Fishing Rod)... Bu olta sadece okyanusların derinliklerini değil, aynı zamanda Nether'ın kor lav denizlerini de fethedebilir. Lavların altında yüzen gizemli yaratıkları avlamaya hazır ol!"],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'aquaculture:neptunium_fishing_rod',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'aquaculture:nether_star_hook',
                },
            ],
        },
        {
            'key': 'neptunium_gear',
            'x': 0.0,
            'y': 12.0,
            'dependencies': ['neptunium_rod', 'neptunium_ingot'],
            'title_en': 'Blessing of the Deep',
            'title_tr': 'Derinliklerin Lütfu',
            'desc_en': ['Neptunium metal holds magical subaquatic properties. Crafting a full set of Neptunium gear allows you to breathe underwater, swim with incredible speed, and move unrestricted on the sea floor. Forge a piece of Neptunium armor or tools to claim this power!'],
            'desc_tr': ['Neptünyum metali, su altındaki yaşamı kolaylaştıran büyülü özelliklere sahiptir. Neptünyum zırh parçaları veya aletleri yapmak su altında nefes almanıza, inanılmaz hızlarda yüzmenize ve deniz tabanında sınırsızca hareket etmenize olanak tanır. Bu gücü elde etmek için bir parça Neptünyum zırh veya alet dövün!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'aquaculture:neptunium_chestplate',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'aquaculture:neptunium_ingot',
                    'count': 1,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:diamond',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'lava_fishing',
            'x': 0.0,
            'y': 13.5,
            'dependency': 'neptunium_rod',
            'title_en': 'In the Embers of the Nether',
            'title_tr': "Nether'ın Korlarında",
            'desc_en': ['Once your Neptunium rod is ready, leave the cool streams of the Overworld behind and brave the bubbling lava oceans of the Nether. Catch magmatic fish like the Magma Mackerel, but beware—you might burn just as easily as your catch!'],
            'desc_tr': ["Neptünyum oltanı hazırladıktan sonra, Overworld'ün tatlı sularını geride bırakıp Nether'ın kızgın lav denizlerine açılabilirsin. Lavların altında yaşayan Magma Uskumrusu (Magma Mackerel) gibi magmatik canlıları yakala. Dikkat et, burada oltan kadar sen de yanabilirsin!"],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'tide:magma_mackerel',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'tide:incandescent_bait',
                },
            ],
        },
        {
            'key': 'celestial_fish',
            'x': 0.0,
            'y': 15.0,
            'dependencies': ['neptunium_rod', 'lava_fishing'],
            'title_en': 'Astral Alignment',
            'title_tr': 'Göksel Hizalanma',
            'desc_en': ['When celestial bodies align and waters glow with mystic starlight, cosmic fish like the Neptune Koi ascend. Catching this legendary fish requires patience, perfect timing, and your best rod. Its cosmic scales hold great energy.'],
            'desc_tr': ['Gök cisimleri hizalandığında ve sular mistik bir ışıkla parıldadığında, Neptune Koi gibi kozmik balıklar yüzeye yaklaşır. Bu efsanevi balığı yakalamak sabır, doğru zamanlama ve en iyi oltanı gerektirir. Onun pulundaki kozmik enerji sana büyük kapılar açacak.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'tide:neptune_koi',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'aquaculture:neptunes_bounty',
                },
            ],
        },
        {
            'key': 'message_in_a_bottle',
            'x': -1.8,
            'y': 0.0,
            'dependency': 'fishing_intro',
            'title_en': 'Whispers of the Sea',
            'title_tr': 'Denizin Fısıltıları',
            'desc_en': ['While fishing, the waves will occasionally wash a glass bottle onto your line. This Message in a Bottle could contain the diary of a lost sailor, a mysterious poem, or a forgotten treasure map. Break it open and listen to the whispers of the sea.'],
            'desc_tr': ['Balık tutarken dalgalar bazen oltana ahşap veya cam bir şişe takar. Bu Şişedeki Mektup (Message in a Bottle) geçmişte kaybolmuş bir denizcinin günlüğü, gizemli bir şiir ya da unutulmuş bir hazine haritası olabilir. Şişeyi aç ve denizin fısıltılarını dinle.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'aquaculture:message_in_a_bottle',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:emerald',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'tackle_box',
            'x': -1.8,
            'y': 1.5,
            'dependency': 'fishing_intro',
            'title_en': 'The Organized Angler',
            'title_tr': 'Düzenli Balıkçının Çantası',
            'desc_en': ['A true fisherman never leaves their gear in disarray. The Tackle Box is your best companion to store rods, hooks, lines, and baits in one convenient place. Stay organized and focus on the catch!'],
            'desc_tr': ['Gerçek bir balıkçı asla malzemelerini dağınık bırakmaz. Malzeme Kutusu (Tackle Box), oltalarını, yedek kancalarını, misinalarını ve yemlerini tek bir yerde saklamak için en kullanışlı yardımcındır. Düzenli ol, avına odaklan!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'aquaculture:tackle_box',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'aquaculture:double_hook',
                },
            ],
        },
        {
            'key': 'lines_bobbers',
            'x': -1.8,
            'y': 3.0,
            'dependency': 'tackle_box',
            'title_en': 'Personalized Touch',
            'title_tr': 'Kişisel Dokunuşlar',
            'desc_en': ['Your rod should reflect your style. Craft Fishing Lines and Bobbers dyed in different colors to fully customize its appearance. Choose your color and let it float.'],
            'desc_tr': ['Oltan senin tarzını yansıtmalı. Farklı renklerde boyanabilen Misinalar (Fishing Line) ve Mantarlar (Bobber) hazırlayarak oltanı tamamen kendine göre kişiselleştir. Rengini seç ve suya bırak.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'aquaculture:fishing_line',
                },
                {
                    'type': 'item',
                    'item': 'aquaculture:bobber',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:string',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:red_dye',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'hooks',
            'x': -1.8,
            'y': 4.5,
            'dependency': 'tackle_box',
            'title_en': 'Choosing the Right Hook',
            'title_tr': 'Doğru Kanca Tercihi',
            'desc_en': ['The hook at the end of your line shapes your fortune. Iron hooks preserve durability, gold hooks bring luck, and double hooks offer a chance to catch two fish at once. Choose your hook wisely.'],
            'desc_tr': ['Oltanın ucundaki kanca, avının kaderini belirler. Demir kanca dayanıklılığı korur, altın kanca şans getirir, çift kanca ise tek seferde iki balık yakalama olasılığı sunar. Avına göre kancanı seç.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'aquaculture:iron_hook',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'aquaculture:light_hook',
                },
            ],
        },
        {
            'key': 'advanced_hooks',
            'x': -1.8,
            'y': 6.0,
            'dependency': 'hooks',
            'title_en': 'Engineered Angling',
            'title_tr': 'Mühendislik Harikası Kancalar',
            'desc_en': ['Advanced hooks like Redstone or Slime hooks modify your fishing speed or catch behavior. Redstone hooks lure fish rapidly, while slime hooks make it harder for them to slip away. Power up your rod with technology!'],
            'desc_tr': ['Gelişmiş kancalar veya Slime kancaları gibi özel kancalar balık tutma hızını veya şansını etkiler. Kızıltaş kancası balıkları hızla çekerken, slime kancası balıkların kaçmasını zorlaştırır. Oltanı teknolojiyle güçlendir!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'aquaculture:redstone_hook',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'aquaculture:diamond_hook',
                },
            ],
        },
        {
            'key': 'neptunes_bounty',
            'x': -1.8,
            'y': 7.5,
            'dependency': 'diamond_rod',
            'title_en': "Neptune's Grace",
            'title_tr': "Neptün'ün Lütfu",
            'desc_en': ["Only the most patient anglers, attuned to the rhythm of the rivers, can pull a Neptune's Bounty box from the deep. This ancient chest holds the secrets and treasures of the sea gods themselves."],
            'desc_tr': ["Sadece en sabırlı ve nehirlerle dost olan balıkçılar Neptün'ün Bounty sandığını (Neptune's Bounty) suyun derinliklerinden çekebilir. Bu antik kutu, içinde deniz tanrılarının hediyelerini saklar."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'aquaculture:neptunes_bounty',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'aquaculture:neptunium_ingot',
                },
            ],
        },
        {
            'key': 'neptunium_ingot',
            'x': -1.8,
            'y': 9.0,
            'dependency': 'neptunes_bounty',
            'title_en': 'Neptunium Metallurgy',
            'title_tr': 'Neptünyum Metalürjisi',
            'desc_en': ["Neptunium Ingots harvested from Neptune's Bounty are made of a legendary metal that never rusts and carries the power of the ocean. Forge them into ultimate tools and armor."],
            'desc_tr': ["Neptün'ün Bounty sandığından elde ettiğin Neptünyum Külçeleri (Neptunium Ingot), su altında paslanmayan ve denizlerin gücünü taşıyan efsanevi bir metaldir. Onu eriterek en güçlü su altı ekipmanlarını yapabilirsin."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'aquaculture:neptunium_ingot',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:emerald',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'natural_baits',
            'x': -3.5,
            'y': 1.0,
            'dependency': 'tackle_box',
            'title_en': 'Bounty of the Soil',
            'title_tr': 'Toprağın Bereketi',
            'desc_en': ["Worms and leeches are natural delicacies that fish cannot resist. Equipping bait on your rod significantly reduces bite times. Don't forget to dig up some worms from moist soil!"],
            'desc_tr': ['Solucanlar ve sülükler balıkların en sevdiği doğal lezzetlerdir. Oltana takacağın bir yem, balıkların yemi kapma süresini önemli ölçüde azaltır. Nemli topraklardan solucan toplamayı unutma!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'aquaculture:worm',
                },
                {
                    'type': 'item',
                    'item': 'aquaculture:leech',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'tide:bait',
                },
            ],
        },
        {
            'key': 'magnetic_bait',
            'x': -3.5,
            'y': 2.5,
            'dependency': 'natural_baits',
            'title_en': 'Magnetic Attraction',
            'title_tr': 'Manyetik Çekim',
            'desc_en': ["Fish aren't the only things at the bottom of the water—sunken wrecks, lost armor, and iron relics lie there too. Equipping a Magnetic Bait boosts your chance to pull up treasures instead of fish."],
            'desc_tr': ['Suyun dibinde sadece balıklar yoktur; batık gemiler, kayıp zırhlar ve demir eşyalar da bulunur. Oltana takacağın Manyetik Yem (Magnetic Bait), metal eşyaları kendine çekerek hazine bulma şansını büyük ölçüde artırır.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'tide:magnetic_bait',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'tide:lucky_bait',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'tide_baits',
            'x': -3.5,
            'y': 4.0,
            'dependency': 'magnetic_bait',
            'title_en': 'Gifts of the Tide',
            'title_tr': 'Gelgitin Getirdikleri',
            'desc_en': ["Tide's Lucky Bait is designed to coax hidden underwater secrets to the surface. With these artificial lures, multiply your luck and reel in catches that would normally remain out of reach."],
            'desc_tr': ['Tide modunun Şanslı Yemi (Lucky Bait), su altındaki gizemleri yüzeye çıkarmak için üretilmiştir. Bu yapay yemler sayesinde şansını katlayabilir ve normalde ulaşamayacağın avları çekebilirsin.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'tide:lucky_bait',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'tide:bait',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'abyssal_baits',
            'x': -3.5,
            'y': 5.5,
            'dependency': 'tide_baits',
            'title_en': 'Call of the Abyss',
            'title_tr': 'Karanlık Suların Çağrısı',
            'desc_en': ["Deep-sea creatures like anglerfish that dwell in the pitch-black trenches don't care for ordinary bait. Abyss Bait and Incandescent Bait glow in the dark, drawing these strange creatures to your line."],
            'desc_tr': ['Okyanusun en karanlık çukurlarında yaşayan fener balıkları veya derin deniz yaratıkları, normal yemlere ilgi duymaz. Abyss Bait and Incandescent Bait, derinliklerin zifiri karanlığında parıldayarak bu yaratıkları oltana çeker.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'tide:abyss_bait',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'tide:lucky_bait',
                },
            ],
            'custom_id': '71CA152F68BB4D01',
        },
        {
            'key': 'marine_salvage',
            'x': -3.5,
            'y': 7.0,
            'dependency': 'tide_baits',
            'title_en': 'Marine Salvage & Sunken Treasures',
            'title_tr': 'Deniz Kurtarma ve Batık Hazineler',
            'desc_en': ['Oceans are not just filled with marine life, but also with historical debris and sunken treasures. Using magnetic bait and lucky hooks, try to salvage some historical junk or metal items from the sea floor. Retrieve some Driftwood or a Gold Ring from the water!'],
            'desc_tr': ['Okyanuslar sadece deniz yaşamıyla dolu değildir; aynı zamanda tarihi kalıntılar ve batık hazineler barındırır. Manyetik yemler ve şanslı kancalar kullanarak, deniz tabanından bazı tarihi çöpleri veya metal eşyaları kurtarmaya çalışın. Sudan bir Sürüklenen Odun (Driftwood) veya Altın Yüzük (Gold Ring) çekip çıkarın!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'aquaculture:driftwood',
                },
                {
                    'type': 'item',
                    'item': 'candlelight:gold_ring',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'aquaculture:box',
                    'count': 2,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:gold_ingot',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'crab_trap',
            'x': -5.0,
            'y': 2.0,
            'dependency': 'tackle_box',
            'title_en': 'Shellfish Trapping',
            'title_tr': 'Kabuklu Avcısı',
            'desc_en': ["Set up a passive income by the shore with Crabber's Delight. Place a Crab Trap baited with fish into the water. Over time, crabs, clams, and shrimp will find their way inside while you rest."],
            'desc_tr': ["Crabber's Delight ile deniz kıyısında pasif bir gelir kaynağı yarat. Yengeç Kapanı'nı (Crab Trap) içine bir yem koyarak suya yerleştir. Zamanla yengeçler, midyeler ve karidesler kapana kısılacaktır. Sen dinlenirken kapanın çalışsın."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'crabbersdelight:crab_trap',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'crittersandcompanions:clam',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'fish_trap',
            'x': -5.0,
            'y': 3.5,
            'dependency': 'crab_trap',
            'title_en': 'Cast the Nets',
            'title_tr': 'Ağları Suya Bırak',
            'desc_en': ["The Fisherman's Trap catches fish in the background while you tend to your crops or explore caves. Place it in water, bait it, and return periodically to collect your bounty. Practical and efficient!"],
            'desc_tr': ["Fisherman's Trap, sen çiftliğinle veya madeninle ilgilenirken arka planda senin için balık tutar. Suya yerleştir, içine yem koy ve ara sıra gelip biriken avları topla. Pratik ve verimli!"],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'fishermens_trap:fishtrap',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:cod',
                    'count': 8,
                },
            ],
        },
        {
            'key': 'automatic_fish_processing',
            'x': -5.0,
            'y': 5.0,
            'dependencies': ['fish_trap', 'seafood'],
            'title_en': 'Industrial Fish Processing',
            'title_tr': 'Endüstriyel Balık İşleme',
            'desc_en': ['Manually cutting fish slices becomes exhausting when you have nets and traps full of them. Use Kinetically powered slicing machines to automate your seafood production! Craft a Slicer from Slice & Dice to process your catch effortlessly.'],
            'desc_tr': ['Kapanlarınız ve ağlarınız balık dolduğunda, onları elinizle tek tek dilimlemek yorucu hale gelir. Kinetik enerjiyle çalışan kesme makinelerini kullanarak deniz ürünleri üretiminizi otomatikleştirin! Avınızı zahmetsizce işlemek için Slice & Dice modundan bir Dilimleyici (Slicer) yapın.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'sliceanddice:slicer',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:iron_knife',
                },
                {
                    'type': 'item',
                    'item': 'farmersdelight:cod_slice',
                    'count': 8,
                },
            ],
        },
        {
            'key': 'tide_fish',
            'x': 1.8,
            'y': 1.0,
            'dependency': 'fishing_intro',
            'title_en': 'Timing is Everything',
            'title_tr': 'Zamanlama Her Şeydir',
            'desc_en': ["With the Tide system, fish now move according to seasons, time of day, and weather conditions. Being in the right place at the right time is the angler's greatest virtue. Catch a Largemouth Bass to prove your skill."],
            'desc_tr': ['Tide sistemiyle birlikte balıklar artık mevsimlere, günün saatlerine ve hatta hava durumuna göre hareket eder. Doğru zamanda doğru yerde olmak bir balıkçının en büyük erdemidir. Yeteneğini kanıtlamak için bir Largemouth Bass yakala.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'tide:largemouth_bass',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:cooked_cod',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'deep_dive',
            'x': 1.8,
            'y': 2.5,
            'dependency': 'tide_fish',
            'title_en': 'First Step into the Depths',
            'title_tr': 'Derinlere İlk Adım',
            'desc_en': ['Time to leave the surface and explore the true kingdom beneath the waves. The Diving Helmet lets you breathe underwater and clears your vision in murky depths. The abyss awaits.'],
            'desc_tr': ['Denizlerin altındaki gerçek krallığı keşfetmek için su yüzeyinden ayrılma zamanı. Dalgıç Kaskı (Diving Helmet) su altında nefes almanı sağlarken görüşünü de netleştirir. Derinlikler seni bekliyor.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'hybrid_aquatic:diving_helmet',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'hybrid_aquatic:diving_boots',
                },
            ],
        },
        {
            'key': 'diving_suit',
            'x': 1.8,
            'y': 4.0,
            'dependency': 'deep_dive',
            'title_en': 'Under Pressure',
            'title_tr': 'Basınç Altında',
            'desc_en': ['Complete the ensemble with the Diving Suit and Leggings. This heavy gear increases pressure resistance in deep waters and allows you to swim as swiftly as a fish.'],
            'desc_tr': ['Dalgıç Elbisesi ve Dalgıç Pantolonu (Diving Suit & Leggings) ile tam takımı tamamla. Bu özel giysi, derin sulardaki basınç direncini artırır ve su altında adeta bir balık gibi hızlı yüzmeni sağlar.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'hybrid_aquatic:diving_suit',
                },
                {
                    'type': 'item',
                    'item': 'hybrid_aquatic:diving_leggings',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:copper_ingot',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'pearl_hunter',
            'x': 1.8,
            'y': 5.5,
            'dependency': 'deep_dive',
            'title_en': 'Pearls and Oysters',
            'title_tr': 'İnci Avcısı',
            'desc_en': ['Harvest shimmering Pearls from clams and oysters on the ocean floor. Use them for elegant decorations or combine them into valuable Pearl Blocks.'],
            'desc_tr': ['Okyanus tabanındaki midyelerden ve istiridyelerden parıldayan İnciler (Pearl) toplayın. Bu incileri hem şık dekorasyonlarda kullanabilir hem de birleştirerek değerli İnci Blokları üretebilirsin.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'crittersandcompanions:pearl',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'crabbersdelight:pearl_block',
                },
            ],
        },
        {
            'key': 'deep_sea_wildlife',
            'x': 1.8,
            'y': 7.0,
            'dependency_or': ['diving_suit', 'abyssal_baits'],
            'title_en': 'Abyssal Denizens',
            'title_tr': 'Abisal Bölgenin Sakinleri',
            'desc_en': ['In the dark waters where sunlight never reaches, strange bioluminescent creatures live. Dive to the deepest sea floor with your diving suit and use abyssal bait to catch rare species like the Anglerfish.'],
            'desc_tr': ['Güneş ışığının asla ulaşmadığı o karanlık yerlerde yaşayan, kendi ışığını üreten tuhaf canlılar vardır. Fener Balığı (Anglerfish) gibi derin deniz yaratıklarını yakalamak için en dip sulara dalış yap ve özel yemini kullan.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'hybrid_aquatic:anglerfish',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'tide:abyss_bait',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'abyssal_chasm_expedition',
            'x': 1.8,
            'y': 8.5,
            'dependency': 'deep_sea_wildlife',
            'title_en': 'Voyage to the Abyssal Chasm',
            'title_tr': 'Abisal Çukura Yolculuk',
            'desc_en': ["The Abyssal Chasm is the deepest, darkest ocean biome in the world, where the pressure is immense and giant sea monsters roam. Normal diving gear won't protect you here. You need to build a heavy Submarine to explore this luminescent biome safely. Find some Sea Glass Shards to prove your success!"],
            'desc_tr': ['Abisal Çukur (Abyssal Chasm), devasa su basıncının hüküm sürdüğü ve dev deniz canavarlarının gezindiği dünyanın en derin, en karanlık okyanus biyomudur. Normal dalış ekipmanı sizi burada korumaz. Bu biyomu güvenle keşfetmek için ağır bir Denizaltı (Submarine) inşa etmeniz gerekir. Başarınızı kanıtlamak için Deniz Camı Parçaları (Sea Glass Shards) bulun!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'alexscaves:submarine',
                },
                {
                    'type': 'item',
                    'item': 'alexscaves:sea_glass_shards',
                    'count': 4,
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'alexscaves:deep_sea_sushi_roll',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:emerald',
                    'count': 8,
                },
            ],
        },
        {
            'key': 'abyssal_gear',
            'x': 1.8,
            'y': 10.0,
            'dependency': 'abyssal_chasm_expedition',
            'title_en': 'Heavy Diving Suit of the Abyss',
            'title_tr': 'Abisin Ağır Dalgıç Elbisesi',
            'desc_en': ['To explore the Abyssal Chasm on foot without a submarine, you need to forge the ultimate heavy diving armor using materials found in the deep. This armor protects you from the crushing deep-sea pressure and lets you walk freely in the dark. Craft the Diving Helmet of the Abyss!'],
            'desc_tr': ["Denizaltı olmadan Abisal Çukur'u yürüyerek keşfetmek için, derinliklerde bulunan malzemeleri kullanarak nihai ağır dalgıç zırhını dövmelisiniz. Bu zırh sizi ezici derin deniz basıncından korur ve karanlıkta özgürce yürümenizi sağlar. Abisin Dalgıç Kaskı'nı (Diving Helmet) üretin!"],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'alexscaves:diving_helmet',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'alexscaves:depth_charge',
                    'count': 2,
                },
                {
                    'type': 'item',
                    'item': 'alexscaves:sea_glass_shards',
                    'count': 8,
                },
            ],
        },
        {
            'key': 'seasonal_mastery',
            'x': 3.5,
            'y': 2.0,
            'dependency': 'tide_fish',
            'title_en': 'Seasonal Fishing Mastery',
            'title_tr': 'Mevsimsel Balıkçılık Uzmanlığı',
            'desc_en': ['A true master angler knows that seasons shift the currents and temperature, bringing different species. Catching a tropical Angelfish in warm summer waters and a chorus-infused Chorus Cod in the coldest conditions will prove your mastery over the seasons!'],
            'desc_tr': ['Gerçek bir usta balıkçı, mevsimlerin akıntıları ve sıcaklıkları değiştirdiğini, farklı balık türlerini beraberinde getirdiğini bilir. Sıcak yaz sularında tropikal bir Melek Balığı (Angelfish) ve en soğuk koşullarda koro enerjili bir Koro Morinası (Chorus Cod) yakalamak, mevsimler üzerindeki hakimiyetinizi kanıtlayacaktır!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'tide:angelfish',
                },
                {
                    'type': 'item',
                    'item': 'tide:chorus_cod',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'tide:lucky_bait',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:emerald',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'seafood',
            'x': 5.0,
            'y': 1.0,
            'dependency': 'tide_fish',
            'title_en': 'Scent of Fish in the Kitchen',
            'title_tr': 'Mutfakta Balık Kokusu',
            'desc_en': ["Don't let your fresh catch go to waste. Use a chef's knife on a Farmer's Delight cutting board to slice your fish. These fresh slices will be the foundation of your gourmet dishes."],
            'desc_tr': ["Yakaladığınız taze balıkları boşa harcama. Farmer's Delight kesme tahtasında bir şef bıçağı yardımıyla balıkları dilimle. Bu taze balık dilimleri, yapacağın gurme yemeklerin temel taşı olacak."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:cod_slice',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:bowl',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'shellfish_feast',
            'x': 5.0,
            'y': 2.5,
            'dependency': 'seafood',
            'title_en': 'Seafood Banquet',
            'title_tr': 'Kabuklu Deniz Ürünleri Şöleni',
            'desc_en': ['Cook crabs and shrimp harvested from your traps to prepare delicious seafood plates. They offer high saturation and keep you energized all day long.'],
            'desc_tr': ['Kapanlarından topladığın yengeç ve karidesleri pişirerek harika deniz ürünleri tabakları hazırla. Bu yemekler yüksek besleyicilik sunar ve sana gün boyu zindelik verir.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'crabbersdelight:cooked_crab',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:cooked_cod',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'ocean_delight',
            'x': 5.0,
            'y': 4.0,
            'dependency': 'shellfish_feast',
            'title_en': 'From Ocean to Table',
            'title_tr': 'Okyanustan Masanıza',
            'desc_en': ['Turn guardians and squid into delicious meals. Cook up a bowl of hot Guardian Soup or roll some fresh Fugu Roll from pufferfish to offer your guests an unforgettable feast.'],
            'desc_tr': ['Guardianları ve deniz yaratıklarını lezzetli çorbalara dönüştür. Oceans Delight modundan Guardian Çorbası veya balon balığından Fugu Roll hazırlayarak misafirlerine unutulmaz lezzetler sun.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'oceansdelight:guardian_soup',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'oceansdelight:fugu_roll',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'gourmet_fish',
            'x': 5.0,
            'y': 5.5,
            'dependency': 'ocean_delight',
            'title_en': "The Chef's Masterpiece",
            'title_tr': 'Şefin Başyapıtı',
            'desc_en': ["Combine the elegance of Let's Do Candlelight with your fresh catch. Prepare Salmon on White Wine to turn your dining table into a fine restaurant. Where a master angler meets a master chef!"],
            'desc_tr': ["Let's Do Candlelight'ın zarafetini deniz ürünleriyle birleştir. Somon balığını beyaz şarap eşliğinde pişirerek (Salmon on White Wine) masanı bir restoran sofrasına dönüştür. Gerçek bir usta balıkçı ve usta şefin buluşması!"],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'candlelight:salmon_on_white_wine',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:onion',
                    'count': 2,
                },
                {
                    'type': 'item',
                    'item': 'farmersdelight:tomato',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'tropical_fish_supreme_quest',
            'x': 5.0,
            'y': 7.0,
            'dependencies': ['gourmet_fish', 'deep_sea_wildlife'],
            'title_en': 'Gourmet Ocean Dining',
            'title_tr': 'Gurme Okyanus Ziyafeti',
            'desc_en': ["Combine the delicacies of Let's Do Candlelight with the exotic fish of the deep. Cook a Tropical Fish Supreme using cod slices, onion, mushrooms, and milk, and roll some Deep Sea Sushi from the Abyssal Chasm. A feast fit for a king!"],
            'desc_tr': ["Let's Do Candlelight'ın lezzetlerini derinliklerin egzotik balıklarıyla birleştirin. Morina dilimleri, soğan, mantar ve süt kullanarak bir Tropikal Balık Ziyafeti (Tropical Fish Supreme) pişirin ve Abisal Çukur'dan çıkardığınız malzemelerle Derin Deniz Suşisi (Deep Sea Sushi Roll) hazırlayın. Krallara layık bir şölen!"],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'candlelight:tropical_fish_supreme',
                },
                {
                    'type': 'item',
                    'item': 'alexscaves:deep_sea_sushi_roll',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'farmersdelight:onion',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:sugar',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'beach_party_quest',
            'x': 5.0,
            'y': 8.5,
            'dependency': 'tropical_fish_supreme_quest',
            'title_en': 'Tropical Leisure & Beach Party',
            'title_tr': 'Tropikal Keyif ve Plaj Partisi',
            'desc_en': ["After all the dangerous deep-sea dives and freezing winter catches, it's time to enjoy the warm sunshine. Craft a beach chair, open some coconuts, mix a Coconut Cocktail and a Honey Cocktail, and throw a relaxing beach party! You've earned it, Captain!"],
            'desc_tr': ['Tüm tehlikeli derin deniz dalışlarından ve dondurucu kış avlarından sonra, sıcak güneşin tadını çıkarma vakti geldi. Bir plaj sandalyesi yapın, hindistan cevizlerini açın, Hindistan Cevizi Kokteyli (Coconut Cocktail) ve Bal Kokteyli (Honey Cocktail) hazırlayın ve rahatlatıcı bir plaj partisi düzenleyin! Bunu hak ettiniz, Kaptan!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'beachparty:beach_chair',
                },
                {
                    'type': 'item',
                    'item': 'beachparty:coconut_cocktail',
                },
                {
                    'type': 'item',
                    'item': 'beachparty:honey_cocktail',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'beachparty:sunglasses',
                    'count': 1,
                },
                {
                    'type': 'item',
                    'item': 'beachparty:radio',
                    'count': 1,
                },
            ],
        },
    ],
}
