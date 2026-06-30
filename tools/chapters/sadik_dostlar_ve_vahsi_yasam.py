CHAPTER = {
    'order': 4,
    'filename': 'sadik_dostlar_ve_vahsi_yasam',
    'title_en': 'Companions & Wildlife',
    'title_tr': 'Sadık Dostlar ve Vahşi Yaşam',
    'icon': 'doggytalents:training_treat',
    'quests': [
        {
            'key': 'doggy_talents',
            'custom_id': '6C804FD7CB2806CF',
            'x': 2.5,
            'y': 0.0,
            'title_tr': 'İnsanın En İyi Dostu',
            'title_en': "Man's Best Friend",
            'desc_tr': ['Doggy Talents Next, kurtları tam anlamıyla yeniden tanımlıyor. Eğitim Mamaları ile yetenek slotlarını aç, sonra puanları köpeğine avlanma, koruma, sürü gütme veya eşya getirme gibi görevlere yönlendir. İyi eğitilmiş bir köpek, mod paketinin en güçlü konfor araçlarından biridir.'],
            'desc_en': ['Doggy Talents Next rebuilds wolves into proper companions. Use Training Treats to unlock talent slots, then spend points to teach a dog to hunt, guard, herd, or even fetch items for you. A well-trained dog is one of the strongest quality-of-life tools in the modpack.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'doggytalents:training_treat',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:clay_ball',
                    'count': 4,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:bone',
                    'count': 2,
                },
            ],
        },
        {
            'key': 'dog_bed',
            'custom_id': '1D6526BFDCF0173C',
            'x': 2.5,
            'y': 2.0,
            'title_tr': 'Sıcak Bir Yuva',
            'title_en': 'A Cozy Home',
            'desc_tr': ['Köpek Yatağı, sadık dostunun doğma noktasını belirler ve dinleneceği bir alan sunar. Boş elle sağ tıkla (ya da kemer ile eğilip sağ tıkla) yatağı belirli bir köpeğe bağlamak için. Uzakta ölürlerse yatağa sağ tıklayarak onları diriltebilirsin — riskli her yolculukta kendini amorti eden küçük bir lüks.'],
            'desc_en': ["A Dog Bed marks your companion's respawn point and gives them a place to rest. Right-click with empty hands (or sneak-right-click with a bone) to claim the bed for a specific dog. If they die far from home, you can revive them by right-clicking the bed — a small luxury that pays for itself on every risky trip."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'doggytalents:dog_bed',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:red_dye',
                },
                {
                    'type': 'item',
                    'item': 'minecraft:leather',
                },
            ],
            'dependency': ['doggy_talents'],
        },
        {
            'key': 'super_treat',
            'custom_id': '7E1CA10026000001',
            'x': 3.5,
            'y': 3.0,
            'title_tr': 'Süper Ödül',
            'title_en': 'Super Treat',
            'desc_tr': ["Doggy Talents'ın Süper Ödülü (Super Treat), temel eğitim mamasının güçlendirilmiş versiyonudur. Kurt arkadaşını erken yetenek sınırının ötesine, geç oyun seviyesine taşımak için kullan — ekstra seviye, ekstra yetenek, ekstra sadakat."],
            'desc_en': ["Doggy Talents' Super Treat is the upgraded version of the basic training treat. Use it to push a wolf companion past the early talent cap and into the late-game tier — extra levels, extra abilities, extra loyalty."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'doggytalents:super_treat',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'doggytalents:whistle',
                    'count': 2,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:bone',
                    'count': 6,
                },
            ],
            'dependency': ['dog_bed'],
        },
        {
            'key': 'whistle',
            'custom_id': '7E1CA1002E000001',
            'x': 6.5,
            'y': 1.0,
            'title_tr': 'Düdük Komutları',
            'title_en': 'Whistle Commands',
            'desc_tr': ['Düdük tüm takip eden köpeklerine aynı anda komut yayar — otur, yanıma gel, kalk, yatağına git, ulu, hatta seni Wolf Mount üzerinde taşı. Modlar arasında geçmek için eğilip sağ tıkla. Sıcak çubuğunda bir tane bulundur, tüm sürüyü komutla yönet.'],
            'desc_en': ['The Whistle broadcasts commands to all your following dogs at once — sit, heel, stand, go to bed, howl, even carry you on a Wolf Mount. Sneak-right-click to cycle between modes. With one in your hotbar, you direct your entire pack without typing anything.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'doggytalents:whistle',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'doggytalents:training_treat',
                    'count': 2,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:bone',
                    'count': 8,
                },
            ],
            'dependency': ['super_treat'],
        },
        {
            'key': 'treat_bag',
            'custom_id': '7E1CA1002E000004',
            'x': 7.5,
            'y': 1.0,
            'title_tr': 'Ödül Çantası',
            'title_en': 'Treat Bag',
            'desc_tr': ['Ödül Çantası (Treat Bag) bir yığın köpek maması saklar ve uzaktan fırlatmanı sağlar. Çantayı açmak ve doldurmak için eğilip sağ tıkla. Köpeklerini madende, keşifte veya savaşta beslemenin en temiz yolu — düşen eşya yığınına elveda.'],
            'desc_en': ["The Treat Bag stores up to a stack of dog treats and lets you throw them at distance. Sneak-right-click to open the bag and refill it. It's the cleanest way to keep your dogs fed while mining, exploring, or fighting — no more dropped items littering the floor."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'doggytalents:treat_bag',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'doggytalents:canine_tracker',
                },
            ],
            'dependency': ['whistle'],
        },
        {
            'key': 'canine_tracker',
            'custom_id': '7E1CA1002E000002',
            'x': 8.5,
            'y': 1.0,
            'title_tr': 'Köpek İzci',
            'title_en': 'Canine Tracker',
            'desc_tr': ['Köpek İzci (Canine Tracker), pusula tarzı bir eşyadır; daha önce kaydettiğin belirli bir köpeğe doğru yön gösterir. Bir köpeğe sağ tıklayarak izciyi bağla, sonra dostunu haritada göremediğinde yönü kontrol et.'],
            'desc_en': ["The Canine Tracker is a compass-style item that points toward a specific dog you've previously registered with it. Right-click a dog to bind the tracker to it, then check the direction whenever you can't see your companion on the map."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'doggytalents:canine_tracker',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'doggytalents:training_treat',
                    'count': 4,
                },
            ],
            'dependency': ['treat_bag'],
        },
        {
            'key': 'locator_orb',
            'custom_id': '7E1CA1002E000003',
            'x': 9.5,
            'y': 1.0,
            'title_tr': 'Bulucu Küresi',
            'title_en': 'Locator Orb',
            'desc_tr': ["Bulucu Küreleri Doggy Talents'ın toplanabilir ödülleridir — on iki temalı küre, köpeğine özel görsel efektler kazandırır. Temel Boyanabilir (Dyable) varyantı, mod paketinde kullandığın her tasma veya yapı paletine uyacak şekilde renklendirilebilir."],
            'desc_en': ['Locator Orbs are collectable trophies from Doggy Talents — twelve themed orbs that unlock unique cosmetic effects for your dog. The basic Dyable variant lets you recolour it to match any collar or build palette you use across the modpack.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'doggytalents:locator_orb_dyable',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:compass',
                },
            ],
            'dependency': ['canine_tracker'],
        },
        {
            'key': 'throw_stick',
            'custom_id': '7E1CA1002E000005',
            'x': 2.5,
            'y': -1.5,
            'title_tr': 'Fırlatma Çubuğu',
            'title_en': 'Throw Stick',
            'desc_tr': ['Fırlatma Çubukları köpeklerinin kovalayıp geri getireceği oyuncaklardır. Her getirilen çubuk küçük bir XP eğitir ve Getir yeteneğini pekiştirir. Merkezkaç döngüsünün bitmesini beklerken yan elde bir tane bulundur, sonsuz eğlence.'],
            'desc_en': ['Throw Sticks are toys your dogs will chase and bring back. Each retrieved stick trains a small amount of XP and reinforces the Fetch talent. Keep one in your off-hand for endless entertainment while waiting for a Centrifuge to finish its cycle.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'doggytalents:throw_stick',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'doggytalents:frisbee',
                },
            ],
            'dependency': ['doggy_talents'],
        },
        {
            'key': 'frisbee',
            'custom_id': '7E1CA1002E000006',
            'x': 4.0,
            'y': -1.5,
            'title_tr': 'Frizbi',
            'title_en': 'Frisbee',
            'desc_tr': ['Frizbiler fırlatma çubuğu gibi çalışır ama daha uzağa gider ve farklı bir yeteneği eğitir. Getir yeteneğiyle birleştir, birleşik eğitim elde et. Salya Frizbi varyantı daha hızlı eğitir ama envanterine salya sıçratır — yanına bez al.'],
            'desc_en': ['Frisbees behave like throw sticks but travel farther and reward a different talent. Pair them with the Fetch talent for compound training. The Drool Frisbee variant trains faster but slobbers all over your inventory — bring wipes.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'doggytalents:frisbee',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'doggytalents:throw_stick',
                },
            ],
            'dependency': ['throw_stick'],
        },
        {
            'key': 'rice_grains',
            'custom_id': '7E1CA1002E000007',
            'x': 3.5,
            'y': 7.5,
            'title_tr': 'Pirinç Tarımı',
            'title_en': 'Rice Farming',
            'desc_tr': ["Pirinç Taneleri (Rice Grains), Doggy Talents'ın suya yakın yetişen köpek yemi bitkisidir. Sulu bir tarla ek ve et düşüşlerinden bağımsız, yenilenebilir köpek yemi kaynağına sahip ol. Pirinç Kasesi, çiğ pirinçten daha hızlı iyileştiren bir konfor yemeğidir."],
            'desc_en': ["Rice Grains are a Doggy Talents food crop that grows near water. Plant a flooded field and you'll have a renewable source of dog food independent of meat drops. The Rice Bowl is a comfort food that heals dogs faster than raw rice."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'doggytalents:rice_grains',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'doggytalents:rice_grains',
                    'count': 16,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:bowl',
                    'count': 4,
                },
            ],
            'dependency': ['super_treat'],
        },
        {
            'key': 'rice_mill',
            'custom_id': '7E1CA1002E000008',
            'x': 4.5,
            'y': 7.5,
            'title_tr': 'Pirinç Değirmeni',
            'title_en': 'Rice Mill',
            'desc_tr': ['Pirinç Değirmeni hasat edilen pirinci pişirmeye hazır kabuksuz tanelere dönüştürür. Kaselerle birleştirip tam Pirinç Kasesi yapabilir ya da taneleri doğrudan köpek yemi olarak verebilirsin. Tek bir değirmen bir tarlanın tüm hasadını saniyeler içinde işler.'],
            'desc_en': ["The Rice Mill converts harvested rice into dehusked grains ready for cooking. Combine it with bowls for full Rice Bowls, or feed the grains directly as dog food. A single mill can process a full field's harvest in seconds."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'doggytalents:rice_mill',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'doggytalents:rice_bowl',
                    'count': 2,
                },
            ],
            'dependency': ['rice_grains'],
        },
        {
            'key': 'pet_care',
            'custom_id': '6716F7B7563D507B',
            'x': 6.5,
            'y': 2.0,
            'title_tr': 'Evcil Hayvan Bakımı',
            'title_en': 'Pet Care',
            'desc_tr': ['Domestication Innovation, Doggy Talents sistemini Evcil Hayvan Yatakları, tasma yükseltmeleri ve aksesuar modelleriyle genişletir. Bir Evcil Hayvan Yatağı kur, sonra dostlarını tasmalar, kalkanlar ve mıknatıs modelleriyle donatarak uzun keşif gezilerinde işe yarar hale getir.'],
            'desc_en': ['Domestication Innovation extends the Doggy Talents system with Pet Beds, collar upgrades, and accessory models. Set a Pet Bed as a true respawn anchor, then equip your companions with collars, shields, and magnet models to make them useful on long supply runs.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'domesticationinnovation:pet_bed_red',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'domesticationinnovation:collar_tag',
                    'count': 2,
                },
            ],
            'dependency': ['dog_bed'],
        },
        {
            'key': 'wayward_lantern',
            'custom_id': '7E1CA1002F000003',
            'x': 7.5,
            'y': 2.0,
            'title_tr': 'Sapkın Fener',
            'title_en': 'Wayward Lantern',
            'desc_tr': ["Sapkın Fener (Wayward Lantern), Domestication Innovation'ın soul-lantern tarzı ışık kaynağıdır. Evcil hayvanının doğma yatağının yanına koy, gece yatağı kolay bul; ya da evinde glowstone bütçesi harcamadan sıcak ve yumuşak bir ışık kaynağı olarak kullan."],
            'desc_en': ["The Wayward Lantern is a soul-lantern style light source from Domestication Innovation. Place it at your pet's respawn bed so the bed is easy to find at night, or use it as a soft warm light source in your house without a glowstone budget."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'domesticationinnovation:wayward_lantern',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:soul_lantern',
                    'count': 4,
                },
            ],
            'dependency': ['pet_care'],
        },
        {
            'key': 'feather_on_a_stick',
            'custom_id': '7E1CA1002F000002',
            'x': 8.5,
            'y': 2.0,
            'title_tr': 'Çubukta Tüy',
            'title_en': 'Feather on a Stick',
            'desc_tr': ['Çubukta Tüy eğlenceli bir evcil hayvan oyuncağıdır — kedini ya da köpeğini kovalayarak oyun animasyonlarını ve küçük bir XP kazancını tetiklersin. Yük taşıyan bir eşya değil ama dostunun sadece bir savaş hayvanı değil, gerçek bir canlı hissetmesini sağlar.'],
            'desc_en': ["The Feather on a Stick is a fun pet toy — chase your cat or dog around with it to trigger play animations and a small amount of XP. It's not load-bearing, but it makes your companion feel like a real animal instead of just a combat pet."],
            'tasks': [
                {
                    'type': 'item',
                    'item': {
                        'id': 'domesticationinnovation:feather_on_a_stick',
                        'Count': 1,
                        'tag': {
                            'Damage': 0,
                        },
                    },
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'domesticationinnovation:deflection_shield',
                },
            ],
            'dependency': ['wayward_lantern'],
        },
        {
            'key': 'magnet',
            'custom_id': '7E1CA10027000001',
            'x': 9.5,
            'y': 2.0,
            'title_tr': 'Mıknatıs Modeli',
            'title_en': 'Magnet Model',
            'desc_tr': ['Mıknatıs modeli evcil hayvanlara yerdeki düşmüş eşyaları toplama etkisi kazandırır. Uzun maden seferleri, tedarik turları veya geniş biyomlerdeki savaşlar sırasında kendini amorti eden küçük ama etkili bir konfor yükseltmesidir.'],
            'desc_en': ["The Magnet model gives pets a handy pickup effect for loose items on the ground. It's a small quality-of-life upgrade that pays off during long mining trips, supply runs, or battles in wide open biomes."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'domesticationinnovation:magnet',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'domesticationinnovation:deflection_shield',
                    'count': 2,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:emerald',
                    'count': 4,
                },
            ],
            'dependency': ['feather_on_a_stick'],
        },
        {
            'key': 'deflection_shield',
            'custom_id': '7E1CA1002F000001',
            'x': 9.5,
            'y': 3.0,
            'title_tr': 'Sapma Kalkanı',
            'title_en': 'Deflection Shield',
            'desc_tr': ['Sapma Kalkanı (Deflection Shield), tasma aksesuarı olarak evcil hayvanına gelen hasarın bir kısmını periyodik olarak saptıran bir eşyadır. Tek bir üretimle uzun süre dayanır ve diğer tasma modelleriyle yığılarak çalışır. En çok tehlikede olan dostuna tak.'],
            'desc_en': ["The Deflection Shield is a collar accessory that periodically deflects a portion of incoming damage away from your pet. It's a single crafted item but lasts a long time and stacks with other collar models. Equip it on your most exposed companion."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'domesticationinnovation:deflection_shield',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:diamond',
                },
            ],
            'dependency': ['magnet'],
        },
        {
            'key': 'pet_beds',
            'custom_id': '7E1CA1002F000004',
            'x': 8.5,
            'y': 3.0,
            'title_tr': 'Evcil Hayvan Yatağı Koleksiyonu',
            'title_en': 'Pet Bed Collection',
            'desc_tr': ['Domestication Innovation her yün rengi için Evcil Hayvan Yatağı sunar. Her renkten en az bir tane yap — koyun çiftliğinden yünün olduktan sonra neredeyse hiçbir maliyeti yoktur ve bir sıra dolusu yatak bir yan odayı tüm dostların için gerçek bir sığınağa dönüştürür.'],
            'desc_en': ['Domestication Innovation ships Pet Beds in every wool colour. Build at least one of each — it costs almost nothing once you have wool from your sheep farm, and a full row of beds turns a side room into a real sanctuary for your entire companion pack.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'domesticationinnovation:pet_bed_red',
                },
                {
                    'type': 'item',
                    'item': 'domesticationinnovation:pet_bed_blue',
                },
                {
                    'type': 'item',
                    'item': 'domesticationinnovation:pet_bed_green',
                },
                {
                    'type': 'item',
                    'item': 'domesticationinnovation:pet_bed_yellow',
                },
                {
                    'type': 'item',
                    'item': 'domesticationinnovation:pet_bed_purple',
                },
                {
                    'type': 'item',
                    'item': 'domesticationinnovation:pet_bed_cyan',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'domesticationinnovation:deed_of_ownership',
                },
            ],
            'dependency': ['deflection_shield'],
        },
    ],
}
