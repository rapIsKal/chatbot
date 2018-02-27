def get_song_alias(text_input):
    inp = text_input.lower()
    if inp in ['тыж', 'тыж программист', 'тыжпрограммист']:
        return 'тыжпрограммист'
    elif inp in ['тт', 'твердое тело']:
        return 'твердое_тело'
    elif inp in ['хуяк', 'хуяк хуяк', 'хуяк хуяк и в продакшн',
                                'хх', 'xх и в продакшн']:
        return 'х_х_и_в_продакшн'
    elif inp in ['полиморфизм']:
        return 'полиморфизм'
    elif inp in ['папа может в си']:
        return 'си'
    elif inp in ['теорема лагранжа']:
        return 'лагранж'
    elif inp in ['теорема ролля']:
        return 'ролль'
    elif inp in ['тестерс', 'тестерс гонна тест', 'ария тестировщика', 'ария тестировщика по']:
        return 'testers'
    elif inp in ['hello world', 'хелло ворлд', 'хелловорлд']:
        return 'hello_world'
    elif inp in ['правило лопиталя']:
        return 'лопиталь'
    elif inp in ['научно-техническое r&b', 'научно-техническое rnb', 'научно-техническое арнби',
                'арнби']:
        return 'R_n_b'
    elif inp in ['бэкап', 'делай бэкап']:
        return 'backup'
    elif inp in ['джава', 'это джава', 'это java', 'ява']:
        return 'java'
    elif inp in ['deadline']:
        return 'дедлайн'
    elif inp in ['определенный интеграл']:
        return 'интеграл'
    elif inp in ['костыль и велосипед']:
        return 'костыль'
    elif inp in ['b.s.o.d.']:
        return 'bsod'
    elif inp in ['мнимая единица']:
        return 'мнимая_единица'
    elif inp in ['ферма', 'лемма ферма']:
        return 'лемма_ферма'
    else:
        return inp