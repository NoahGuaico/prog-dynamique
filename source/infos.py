class DocumentInfos:

    title = u'Les failles zéro day'
    first_name = 'Noah'
    last_name = 'Guaico'
    author = f'{first_name} {last_name}'
    year = u'2022'
    month = u'Décemenbre'
    seminary_title = u'Travail personnel OCI'
    tutor = u"Cédric Donner"
    release = "(Version première)"
    repository_url = "https://github.com/donnerc/prog-dynamique"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()