from django.db import models
from models import Artist, Work

# run script in shell_plus to populate database with artists and works
# just once.  running again will create duplicates!!!

# attribute artist to work in admin 


artist_data = (
    ("Vernon Pratt", "https://www.thevernonprattproject.com/about"),
    ("Brenda Miller Holmes", "http://www.brendamillerholmes.com/about.html"),
    ("Cornelio Campos", "https://corneliocampos.web.unc.edu/"),
    ("Cecilia Lueza", "https://lueza.com"),
    ("Scott Nurkin", "http://themuralshop.com/"),
    ("Andria Linn", "https://www.andrialinn.com"),
    ("Olalekan “LEk” Jeyifous", "http://vigilism.com"),
    ("Mary Carter Taub", "https://marycartertaub.com/home.html"),
    ("Matthew Willey", "https://www.thegoodofthehive.com"),
    ("Michael Brown", "https://muralsbymichaelbrown.com"),
    ("Karen Stern Perkins", None),
    ("Frank Kreacic", "https://frankkreacic.com/"),
    ("Victor Knight", "https://www.instagram.com/dartsky/?hl=en"),
    ("Robert Winkler", "https://www.robertwinklersculpture.com/"),
    ("Michael Waller and Lee Foushee", "https://www.wallerfoushee.com/"),
    ("Al Frega", "https://fregacreative.com/"),
    ("Charlie Brouwer", "http://charliebrouwer.com/index.html"),
    ("Odili Donald Odita", "https://www.odilidonaldodita.com/"),
    ("Brett Cook", "https://www.brett-cook.com/"),
    ("Darius Quarles", "http://virginiahenrys.com/"),
    ("Josh McBride", None), 
    ("Duke students and visiting artists", None),
    ("Multiple artists", "https://uhillwalls.com/artists/"),
    ("Unknown", None),
    ("Candy Carver", "https://candycarver.com/"),
    ("David Wilson", None),
    ("Norman Lee and Shane Albritton", "https://www.resite-studio.com/about"),
    ("Sampada Kodagali Agarwal", "https://ansimit.wordpress.com/"),
    ("Ramya S. Kapadia", None),
    ("Bethany Bash", "https://www.bethanybash.com/"),
    ("Andrew Preiss", "https://www.arpdesignstudio.com/about"),
    ("Wade Williams", "https://wadehwilliamsartist.com/"),
    ("JP Trostle", "https://japeart.com/"),
    ("YouthWorks Interns", None),
    ("Muriel Epling", "http://murielepling.squarespace.com/"),
    ("Thomas Sayre", "https://www.thomassayre.com/"),
    ("Julienne Alexander", "http://www.yssrs.com/"),
    ("Julia Gartrell", "http://juliagartrell.com/"),
    ("Volkan Alkanoglu", "https://www.alkanoglu.com"),
)

# works :
# (0, 1, 2, 3, 4, 5)
# ("string", integer, float, float, "string", Boolean)
# (title, year, lat, long, category, wheelchair accessibility)

work_data = (
    ("All the Possibilities", 1988, 35.9978484, -78.9036197, "sculpture", True),
    ("We Must Remember and Continue to Tell", 2015, 35.9978485, -78.9036197, "mural", True),
    ("Juchari Ziranhua / Nuestros Raices / Our Roots", 2019, 35.9971181, -78.9031230, "mural", True), 
    ("I Am My Own Muse", 2019, 35.9970920, -78.9028380, "mural", True),
    ("Ninth Street Bakery Mural", None, 35.9967071, -78.9031598, "mural", True),
    ("Wall of Hope", 2008, 35.9963675, -78.9027649, "mural", True),
    ("Durham in Continuum", 2018, 35.9958228, -78.9035749, "mural", True),
    ("Along the way: Snapping!, Crackling!, and Popping!", 2019, 36.0009749, -78.9014761, "crosswalk", True),
    # ("Cracking")
    # ("Popping")
    ("Swarm", None, 35.9951356, -78.9063472, "mural", True),
    ("Celebrate", None, 35.9946107, -78.9026999, "mural", True),
    ("Here Comes The Sun", 1975, 35.9947170, -78.8996630, "mural", True), 
    ("Charging Durham", 2017, 35.9960850, -78.9014468, "mural", True),
    ("Grab Life by the Horns", 2017, 35.9964094, -78.9028958, "mural", True),
    ("Winding Out", 2014, 35.9959346, -78.9002386, "sculpture", True),
    ("Major the Bull", None, 35.9963274, -78.9014462, "sculpture", True),
    ("Chalice", 2014, 35.9965452, -78.9020611, "sculpture", True),
    ("Pursuit of Happiness", 2014, 35.9974708, -78.9037234, "sculpture", True),
    ("Time Bridge", 2015, 35.9984626, -78.9032525, "mural", True),
    ("Pauli Murray from the Face Up", 2008, 35.9993035, -78.9017161, "mural", True),
    ("Liberty Warehouse Mural", None, 36.0019981, -78.9021754,"mural", True),
    ("Untitled", None, 36.0038010, -78.9000240, "mural", True),
    ("Two Way Bridges", None, 35.9996805, -78.9104586, "mural", True),
    ("Angel of Spring", 2015, 36.0077861, -78.9221369, "mural", True),
    ("UHill Walls", 2020, 35.9671719, -78.9545263, "mural", True),
    ("Pepsi", None, 35.9820036, -78.8803929, "mural", True),
    ("Cecy's Gallery Mural", None, 35.9998487, -78.9016427, "mural", True),
    ("El Futuro Mural", None, 36.0837620, -78.9175081, "mural", True),
    ("Visionary Leadership in the New South", 2009, 35.9962457, -78.9016548, "sculpture", True),
    ("A Black Capital for the World to See", 2009, 35.9960558, -78.9009963, "sculpture", True),
    ("Financial and Professional Impact in Durham", 2009, 35.9956194, -78.9003559, "sculpture", True),
    ("A Legacy of Community and Institutional Connections", 2009, 35.9960314, -78.9003204, "sculpture", True),
    ("Empowering and Diverse Opportunities", 2009, 35.9949640, -78.8989558, "sculpture", True), 
    ("Tobacco and E.J. Parish", 2009, 35.9952052, -78.8993920, "sculpture", True), 
    ("The Drain on Main", 2017, 35.9966561, -78.903862, "mural", True), 
    ("The Art of the Warli in Durham", None, 35.9987581, -78.9018720, "mural", True),
    ("Mr. Pickles", 2005, 36.0006088, -78.9009637, "sculpture", True),
    ("Phat Ryan", 2009, 36.0004300, -78.9010900, "sculpture", True),
    # ("Earthsplitter", 2007, None, None, None, "sculpture", True),
    ("Purple Steam", 2020, 35.9948067, -78.8972575, "sculpture", True),
)


def seedDatabaseArtist():
    for artist in artist_data:
        Artist(name=artist[0], website=artist[1]).save()
        
def seedDatabaseWork():
    for work in work_data:
        Work(title=work[0], year=work[1], latitude=work[2], longitude=work[3], category=work[4], wheelchairAccessible=work[5]).save()

seedDatabaseArtist()
seedDatabaseWork()