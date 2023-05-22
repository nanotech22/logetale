

class Collaborator():
    def __init__(self,
                 first_name,
                 last_name,
                 website_link = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.website_link = None if website_link is None else website_link
        


class Paper():
    def __init__(self, 
                 title,
                 other_authors = [],
                 arXiv_year = None, 
                 arXiv_link = None,
                 journal_name = None,
                 journal_link = None, 
                 journal_year = None,
                 abstract = None,
                 notes = None,
                 picture_link = None) -> None:
        self.title = title
        self.other_authors = None if other_authors is None else other_authors
        self.arXiv_year = None if arXiv_year is None else arXiv_year
        self.arXiv_link = None if arXiv_link is None else arXiv_link
        self.journal_name = None if journal_name is None else journal_name
        self.journal_link = None if journal_link is None else journal_link
        self.journal_year = None if journal_year is None else journal_year
        self.abstract = None if abstract is None else abstract
        self.notes = None if notes is None else notes
        self.picture_link = None if picture_link is None else picture_link
















# Collaborators

youcheng = Collaborator(
    first_name="You-Cheng",
    last_name="Chou",
    website_link="https://www.math.sinica.edu.tw/www/people/post-doc20_e.jsp"
)

yplee = Collaborator(
    first_name="Y.P.",
    last_name="Lee",
    website_link="https://www.math.utah.edu/~yplee/"
)

saraharpin = Collaborator(
    first_name="Sarah",
    last_name="Arpin",
    website_link="https://sites.google.com/view/saraharpin"
)

sebastian = Collaborator(
    first_name="Sebastian",
    last_name="Bozlee",
    website_link="https://www.sebastianbozlee.net/"
)

patrickmcfaddin = Collaborator(
    first_name="Patrick",
    last_name="McFaddin",
    website_link="https://mcfaddin.github.io/"
)


hansonsmith = Collaborator(
    first_name="Hanson",
    last_name="Smith",
    website_link="https://www.hansonsmath.info/"
)

rahul = Collaborator(
    first_name="Rahul",
    last_name="Pandharipande",
    website_link="https://people.math.ethz.ch/~rahul/"
)


sammolcho = Collaborator(
    first_name="Sam",
    last_name="Molcho",
    website_link="http://math.huji.ac.il/~samouilmolcho/"
)


davidholmes = Collaborator(
    first_name="David",
    last_name="Holmes",
    website_link="http://www.davidholmes.nl/"
)



jonathan = Collaborator(
    first_name="Jonathan",
    last_name="Wise",
    website_link="https://math.colorado.edu/~jonathan.wise/"
)










# Papers




<i>The log tangent space of the log jet space.</i> <a href="https://arxiv.org/abs/2210.08505">arXiv (2022)</a>.

logjetspace = Paper(
    title="The log tangent space of the log jet space",
    arXiv_year=2022,
    arXiv_link="https://arxiv.org/abs/2210.08505",
    abstract='''
    We introduce new notions of log jet spaces. Mildly singular spaces are ``smooth'' in log geometry, so their log jet spaces behave like the jet spaces of smooth varieties. Myriad examples contrast log jet spaces with the usual jet spaces of schemes. We then compute the log Kähler differentials of the log jet and arc spaces after de Fernex and Docampo. We obtain some of their applications to the structure of the log jet space. We conclude with comparison remarks with other log jet spaces. 
    ''',
)











