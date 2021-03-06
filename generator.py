import random
from typing import List, Union
from rich import inspect

left = [
    "admiring",
    "adoring",
    "affectionate",
    "agitated",
    "amazing",
    "angry",
    "awesome",
    "beautiful",
    "blissful",
    "bold",
    "boring",
    "brave",
    "busy",
    "charming",
    "clever",
    "cool",
    "compassionate",
    "competent",
    "condescending",
    "confident",
    "cranky",
    "crazy",
    "dazzling",
    "determined",
    "distracted",
    "dreamy",
    "eager",
    "ecstatic",
    "elastic",
    "elated",
    "elegant",
    "eloquent",
    "epic",
    "exciting",
    "fervent",
    "festive",
    "flamboyant",
    "focused",
    "friendly",
    "frosty",
    "funny",
    "gallant",
    "gifted",
    "goofy",
    "gracious",
    "great",
    "happy",
    "hardcore",
    "heuristic",
    "hopeful",
    "hungry",
    "infallible",
    "inspiring",
    "interesting",
    "intelligent",
    "jolly",
    "jovial",
    "keen",
    "kind",
    "laughing",
    "loving",
    "lucid",
    "magical",
    "mystifying",
    "modest",
    "musing",
    "naughty",
    "nervous",
    "nice",
    "nifty",
    "nostalgic",
    "objective",
    "optimistic",
    "peaceful",
    "pedantic",
    "pensive",
    "practical",
    "priceless",
    "quirky",
    "quizzical",
    "recursing",
    "relaxed",
    "reverent",
    "romantic",
    "sad",
    "serene",
    "sharp",
    "silly",
    "sleepy",
    "stoic",
    "strange",
    "stupefied",
    "suspicious",
    "sweet",
    "tender",
    "thirsty",
    "trusting",
    "unruffled",
    "upbeat",
    "vibrant",
    "vigilant",
    "vigorous",
    "wizardly",
    "wonderful",
    "xenodochial",
    "youthful",
    "zealous",
    "zen",
]

right = [
    "agnesi",
    "albattani",
    "allen",
    "almeida",
    "antonelli",
    "archimedes",
    "ardinghelli",
    "aryabhata",
    "austin",
    "babbage",
    "banach",
    "banzai",
    "bardeen",
    "bartik",
    "bassi",
    "beaver",
    "bell",
    "benz",
    "bhabha",
    "bhaskara",
    "black",
    "blackburn",
    "blackwell",
    "bohr",
    "booth",
    "borg",
    "bose",
    "bouman",
    "boyd",
    "brahmagupta",
    "brattain",
    "brown",
    "buck",
    "burnell",
    "cannon",
    "carson",
    "cartwright",
    "carver",
    "cerf",
    "chandrasekhar",
    "chaplygin",
    "chatelet",
    "chatterjee",
    "chaum",
    "chebyshev",
    "clarke",
    "cohen",
    "colden",
    "cori",
    "cray",
    "curran",
    "curie",
    "darwin",
    "davinci",
    "dewdney",
    "dhawan",
    "diffie",
    "dijkstra",
    "dirac",
    "driscoll",
    "dubinsky",
    "easley",
    "edison",
    "einstein",
    "elbakyan",
    "elgamal",
    "elion",
    "ellis",
    "engelbart",
    "euclid",
    "euler",
    "faraday",
    "feistel",
    "fermat",
    "fermi",
    "feynman",
    "franklin",
    "gagarin",
    "galileo",
    "galois",
    "ganguly",
    "gates",
    "gauss",
    "germain",
    "goldberg",
    "goldstine",
    "goldwasser",
    "golick",
    "goodall",
    "gould",
    "greider",
    "grothendieck",
    "haibt",
    "hamilton",
    "haslett",
    "hawking",
    "hellman",
    "heisenberg",
    "hermann",
    "herschel",
    "hertz",
    "heyrovsky",
    "hodgkin",
    "hofstadter",
    "hoover",
    "hopper",
    "hugle",
    "hypatia",
    "ishizaka",
    "jackson",
    "jang",
    "jemison",
    "jennings",
    "jepsen",
    "johnson",
    "joliot",
    "jones",
    "kalam",
    "kapitsa",
    "kare",
    "keldysh",
    "keller",
    "kepler",
    "khayyam",
    "khorana",
    "kilby",
    "kirch",
    "knuth",
    "kowalevski",
    "lalande",
    "lamarr",
    "lamport",
    "leakey",
    "leavitt",
    "lederberg",
    "lehmann",
    "lewin",
    "lichterman",
    "liskov",
    "lovelace",
    "lumiere",
    "mahavira",
    "margulis",
    "matsumoto",
    "maxwell",
    "mayer",
    "mccarthy",
    "mcclintock",
    "mclaren",
    "mclean",
    "mcnulty",
    "mendel",
    "mendeleev",
    "meitner",
    "meninsky",
    "merkle",
    "mestorf",
    "mirzakhani",
    "montalcini",
    "moore",
    "morse",
    "murdock",
    "moser",
    "napier",
    "nash",
    "neumann",
    "newton",
    "nightingale",
    "nobel",
    "noether",
    "northcutt",
    "noyce",
    "panini",
    "pare",
    "pascal",
    "pasteur",
    "payne",
    "perlman",
    "pike",
    "poincare",
    "poitras",
    "proskuriakova",
    "ptolemy",
    "raman",
    "ramanujan",
    "ride",
    "ritchie",
    "rhodes",
    "robinson",
    "roentgen",
    "rosalind",
    "rubin",
    "saha",
    "sammet",
    "sanderson",
    "satoshi",
    "shamir",
    "shannon",
    "shaw",
    "shirley",
    "shockley",
    "shtern",
    "sinoussi",
    "snyder",
    "solomon",
    "spence",
    "stonebraker",
    "sutherland",
    "swanson",
    "swartz",
    "swirles",
    "taussig",
    "tereshkova",
    "tesla",
    "tharp",
    "thompson",
    "torvalds",
    "tu",
    "turing",
    "varahamihira",
    "vaughan",
    "villani",
    "visvesvaraya",
    "volhard",
    "wescoff",
    "wilbur",
    "wiles",
    "williams",
    "williamson",
    "wilson",
    "wing",
    "wozniak",
    "wright",
    "wu",
    "yalow",
    "yonath",
    "zhukovsky",
]


def get_mock_dirs() -> List[Union[str, List[Union[str, List[str]]]]]:
    already_used_names = set()
    layout: List[Union[str, List]] = []

    def get_rand_name() -> str:
        while True:
            left_idx, right_idx = random.randint(0, len(left) - 1), random.randint(
                0, len(right) - 1
            )
            name = f"{left[left_idx]}_{right[right_idx]}"
            if name not in already_used_names:
                already_used_names.add(name)
                return name

    def get_random_bool() -> bool:
        return bool(random.getrandbits(1))

    def get_files() -> List[str]:
        def get_file_name() -> str:
            return get_rand_name() + random.choice([".py", ".txt", ".csv"])

        return [get_file_name() for _ in range(random.randint(2, 6))]

    def add_dir_entry(ip: List) -> List:
        ip.extend([get_rand_name(), []])
        return ip[-1]

    number_of_dirs = random.randint(5, 9)
    for _ in range(number_of_dirs):
        top_level = add_dir_entry(layout)

        # Generate some files
        if get_random_bool():
            top_level.extend(get_files())

        # Generate some sub dirs
        if get_random_bool():
            number_of_sub_dirs = random.randint(2, 5)
            for _ in range(0, number_of_sub_dirs):
                sub_dir_level = add_dir_entry(top_level)

                # Generate some files
                if get_random_bool():
                    sub_dir_level.extend(get_files())

    return layout


if __name__ == "__main__":
    from rich import print

    print(get_mock_dirs())
