CHAPTER = {
    'order': 5,
    'filename': 'kumes_ve_agil_gunlukleri',
    'title_en': 'Coop & Barn Chronicles',
    'title_tr': 'Kümes ve Ağıl Günlükleri',
    'icon': 'dragnlivestock:gender_test_strip',
    'quests': [
        {
            'key': 'gender_strip',
            'x': 0.0,
            'y': 0.0,
            'title_en': 'Animal Genders',
            'title_tr': 'Hayvan Cinsiyetleri',
            'desc_en': ["DragN's Livestock Overhaul introduces genders to animals! Animals now require both a male and female to mate. Milk and wool are also gender-restricted. Craft a Gender Test Strip to easily identify an animal's gender if you are unsure."],
            'desc_tr': ["DragN's Livestock Overhaul, hayvanlara cinsiyet getiriyor! Hayvanlar artık çiftleşmek için hem bir erkek hem de dişiye ihtiyaç duyuyor. Süt ve yün üretimi de cinsiyete göre sınırlandırılmıştır. Emin değilseniz bir hayvanın cinsiyetini kolayca belirlemek için Cinsiyet Test Şeridi hazırlayın."],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'dragnlivestock:gender_test_strip',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'dragnlivestock:gender_test_strip',
                    'count': 4,
                },
            ],
        },
        {
            'key': 'scissors',
            'x': -1.5,
            'y': 1.5,
            'dependency': 'gender_strip',
            'title_en': 'Mount Grooming',
            'title_tr': 'Binek Tımarı',
            'desc_en': ["Horses' manes and tails grow over time. Use Mane Scissors and Tail Scissors to groom them, change their hairstyles, and maintain their speed and performance."],
            'desc_tr': ['Atların yeleleri ve kuyrukları zamanla büyür. Onları tımar etmek, saç stillerini değiştirmek ve hız/performanslarını korumak için Yele Makası ve Kuyruk Makası kullanın.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'dragnlivestock:mane_scissors',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'dragnlivestock:tail_scissors',
                },
            ],
        },
        {
            'key': 'brand_tags',
            'x': 1.5,
            'y': 1.5,
            'dependency': 'gender_strip',
            'title_en': 'Animal Identification',
            'title_tr': 'Hayvan Kimliklendirme',
            'desc_en': ['Use color-coded Brand Tags to identify your animals. This helps manage breeding programs, dairy cattle, or sheep lineages in your farm.'],
            'desc_tr': ['Hayvanlarınızı ayırt etmek için renk kodlu İşaret Etiketleri (Brand Tags) kullanın. Bu, çiftliğinizdeki damızlık programlarını, süt sığırlarını veya koyun soylarını yönetmenize yardımcı olur.'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'dragnlivestock:yellow_brand_tag',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'minecraft:leather',
                    'count': 2,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:yellow_dye',
                },
            ],
        },
        {
            'key': 'cured_meat',
            'x': 0.0,
            'y': 2.0,
            'dependency': 'gender_strip',
            'title_en': 'Et Kurutma ve Salatalar',
            'title_tr': 'Et Kurutma ve Salatalar',
            'desc_en': ['Process your livestock meat into thin strips and dry them into Pork Jerky or Beef Strips. You can also boil eggs to make delicious egg salads. High nutrition and long shelf life!'],
            'desc_tr': ['Hayvan etlerinizi ince şeritler halinde işleyin ve onları Domuz Eti Jerky veya Dana Şeritleri olarak kurutun. Ayrıca lezzetli yumurta salataları yapmak için yumurta kaynatabilirsiniz. Yüksek besin değeri ve uzun raf ömrü!'],
            'tasks': [
                {
                    'type': 'item',
                    'item': 'dragnlivestock:pork_jerky',
                },
            ],
            'rewards': [
                {
                    'type': 'item',
                    'item': 'dragnlivestock:pork_strips',
                    'count': 2,
                },
                {
                    'type': 'item',
                    'item': 'minecraft:bowl',
                    'count': 2,
                },
            ],
        },
    ],
}
