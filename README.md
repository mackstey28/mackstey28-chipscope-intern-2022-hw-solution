# Problem statement
Implement a python program to
- view the hierarchy of the files and sub-directories as a tree
- use customizable regular expressions as filters to filter based on the file/directory name

**You may not use** any 3rd party python package apart from [rich](https://github.com/Textualize/rich). More on why you will need `rich` is given in the "Sample Output" section.

To get you started, a `main.py` file is included that does the bare minimum needed to get you started. You may add your logic to this
file.

# Version constraints
- Python `3.8` or higher
- Rich `12.0.0` or higher

# Input

The files and directory structure will be provided to you as a nested `list` by the `get_mock_dirs()` in `generator.py`.

The name of the files and directories are stored as strings in the list.

For the purposes of this assignment, you can assume 
- an entry with one of these extensions - `.py`, `.txt`, `.csv` - is a file
- an entry without any extension is a directory
- names of the files and directories will be unique
- the `list` after each directory entry, provides the contents of that directory.

  For example, the `list` following the directory entry `funny_chaum` is meant to describe it's contents.

### Sample Input

```
[
    'strange_chatelet',
    [],
    'funny_chaum',
    [
        'silly_boyd.py',
        'zealous_driscoll.txt',
        'lucid_ganguly.py',
        'vibrant_bohr.txt',
        'hardcore_ishizaka.py'
    ],
    'wizardly_rubin',
    [
        'intelligent_hamilton.csv',
        'eloquent_tereshkova.txt',
        'optimistic_varahamihira.py',
        'nifty_kare.py',
        'charming_satoshi.py'
    ],
    'eloquent_mayer',
    [
        'frosty_dubinsky.txt',
        'stoic_northcutt.csv',
        'nervous_nash.txt',
        'flamboyant_ritchie.py'
    ],
    'dreamy_chaum',
    [],
    'confident_mclaren',
    [
        'confident_golick.py',
        'vigilant_banzai.py',
        'musing_brattain.csv',
        'relaxed_chatelet.txt',
        'sad_wilson.csv'
    ],
    'wizardly_solomon',
    [
        'keen_rosalind.txt',
        'fervent_gould.txt',
        'gifted_williams.py',
        'epic_wilbur.txt',
        'thirsty_noyce.txt',
        'pensive_grothendieck',
        ['hardcore_gauss.txt', 'jovial_brown.txt'],
        'wonderful_noyce',
        [],
        'relaxed_chandrasekhar',
        [],
        'loving_boyd',
        [
            'elated_knuth.csv',
            'pensive_darwin.csv',
            'nostalgic_kepler.py',
            'flamboyant_lumiere.txt',
            'trusting_cartwright.csv',
            'competent_sutherland.txt'
        ],
        'funny_allen',
        []
    ],
    'romantic_kare',
    [
        'relaxed_nightingale.py',
        'recursing_dirac.py',
        'musing_yalow',
        [],
        'quirky_snyder',
        [],
        'wizardly_saha',
        [],
        'frosty_ganguly',
        [
            'adoring_jepsen.py',
            'zen_mirzakhani.py',
            'reverent_wilson.py',
            'angry_pasteur.csv',
            'cool_visvesvaraya.txt'
        ]
    ]
]
```

# Output

You should display a hierarchial tree visualization of the directory and files(see sample output below).
For creating the tree, you should use trees from the python package [rich](https://github.com/Textualize/rich).
Feel free to use any other functionality from [rich](https://github.com/Textualize/rich) as you deem necessary.


## Sample Output
```
Regular tree
├── strange_chatelet
│   └── <Empty>
├── funny_chaum
│   ├── silly_boyd.py
│   ├── zealous_driscoll.txt
│   ├── lucid_ganguly.py
│   ├── vibrant_bohr.txt
│   └── hardcore_ishizaka.py
├── wizardly_rubin
│   ├── intelligent_hamilton.csv
│   ├── eloquent_tereshkova.txt
│   ├── optimistic_varahamihira.py
│   ├── nifty_kare.py
│   └── charming_satoshi.py
├── eloquent_mayer
│   ├── frosty_dubinsky.txt
│   ├── stoic_northcutt.csv
│   ├── nervous_nash.txt
│   └── flamboyant_ritchie.py
├── dreamy_chaum
│   └── <Empty>
├── confident_mclaren
│   ├── confident_golick.py
│   ├── vigilant_banzai.py
│   ├── musing_brattain.csv
│   ├── relaxed_chatelet.txt
│   └── sad_wilson.csv
├── wizardly_solomon
│   ├── keen_rosalind.txt
│   ├── fervent_gould.txt
│   ├── gifted_williams.py
│   ├── epic_wilbur.txt
│   ├── thirsty_noyce.txt
│   ├── pensive_grothendieck
│   │   ├── hardcore_gauss.txt
│   │   └── jovial_brown.txt
│   ├── wonderful_noyce
│   │   └── <Empty>
│   ├── relaxed_chandrasekhar
│   │   └── <Empty>
│   ├── loving_boyd
│   │   ├── elated_knuth.csv
│   │   ├── pensive_darwin.csv
│   │   ├── nostalgic_kepler.py
│   │   ├── flamboyant_lumiere.txt
│   │   ├── trusting_cartwright.csv
│   │   └── competent_sutherland.txt
│   └── funny_allen
│       └── <Empty>
└── romantic_kare
    ├── relaxed_nightingale.py
    ├── recursing_dirac.py
    ├── musing_yalow
    │   └── <Empty>
    ├── quirky_snyder
    │   └── <Empty>
    ├── wizardly_saha
    │   └── <Empty>
    └── frosty_ganguly
        ├── adoring_jepsen.py
        ├── zen_mirzakhani.py
        ├── reverent_wilson.py
        ├── angry_pasteur.csv
        └── cool_visvesvaraya.txt
```



# Bonus task - Filtering based on file extension

For the bonus task, you should filter the contents of the "regular" tree built in the main task. 
Filtering should be done based on one or more file extension(s).


## Sample output

If we filter on the extension `.py`, output should be
```
Filtered tree
├── strange_chatelet
│   └── <Empty>
├── funny_chaum
│   ├── silly_boyd.py
│   ├── lucid_ganguly.py
│   └── hardcore_ishizaka.py
├── wizardly_rubin
│   ├── optimistic_varahamihira.py
│   ├── nifty_kare.py
│   └── charming_satoshi.py
├── eloquent_mayer
│   └── flamboyant_ritchie.py
├── dreamy_chaum
│   └── <Empty>
├── confident_mclaren
│   ├── confident_golick.py
│   └── vigilant_banzai.py
├── wizardly_solomon
│   ├── gifted_williams.py
│   ├── pensive_grothendieck
│   ├── wonderful_noyce
│   │   └── <Empty>
│   ├── relaxed_chandrasekhar
│   │   └── <Empty>
│   ├── loving_boyd
│   │   └── nostalgic_kepler.py
│   └── funny_allen
│       └── <Empty>
└── romantic_kare
    ├── relaxed_nightingale.py
    ├── recursing_dirac.py
    ├── musing_yalow
    │   └── <Empty>
    ├── quirky_snyder
    │   └── <Empty>
    ├── wizardly_saha
    │   └── <Empty>
    └── frosty_ganguly
        ├── adoring_jepsen.py
        ├── zen_mirzakhani.py
        └── reverent_wilson.py
```

If we filter based on the extension `.py` and `.txt`, the output should be
```
Filtered tree
├── funny_chaum
│   ├── silly_boyd.py
│   ├── zealous_driscoll.txt
│   ├── lucid_ganguly.py
│   ├── vibrant_bohr.txt
│   └── hardcore_ishizaka.py
├── wizardly_rubin
│   ├── eloquent_tereshkova.txt
│   ├── optimistic_varahamihira.py
│   ├── nifty_kare.py
│   └── charming_satoshi.py
├── eloquent_mayer
│   ├── frosty_dubinsky.txt
│   ├── nervous_nash.txt
│   └── flamboyant_ritchie.py
├── confident_mclaren
│   ├── confident_golick.py
│   ├── vigilant_banzai.py
│   └── relaxed_chatelet.txt
├── wizardly_solomon
│   ├── keen_rosalind.txt
│   ├── fervent_gould.txt
│   ├── gifted_williams.py
│   ├── epic_wilbur.txt
│   ├── thirsty_noyce.txt
│   ├── pensive_grothendieck
│   │   ├── hardcore_gauss.txt
│   │   └── jovial_brown.txt
│   └── loving_boyd
│       ├── nostalgic_kepler.py
│       ├── flamboyant_lumiere.txt
│       └── competent_sutherland.txt
└── romantic_kare
    ├── relaxed_nightingale.py
    ├── recursing_dirac.py
    └── frosty_ganguly
        ├── adoring_jepsen.py
        ├── zen_mirzakhani.py
        ├── reverent_wilson.py
        └── cool_visvesvaraya.txt
```