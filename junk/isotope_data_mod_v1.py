import numpy as np

# Placeholder isotopes dictionary; cross-sections will be filled later dynamically
isotopes = {
    'U234': {
        'prod': [],
        'loss': [('U234','absorption')]
    },
    'U235': {
        'prod': [('U234', 'n_gamma')],
        'loss': [('U235','absorption')]
    },
    'U236': {
        'prod': [('U235', 'n_gamma'),('Np236','decay')],
        'loss': [('U235','absorption')]
    },
    'U237': {
        'prod': [('U236', 'n_gamma'),('U238','n2n')],
        'loss': [('U237','decay')]
    },
    'U238': {
        'prod': [],
        'loss': [('U238','absorption')]
    },
    'U239': {
        'prod': [('U238', 'n_gamma')],
        'loss': [('U237','decay'),('U239','absorption')]
    },
    'Np236': {
        'prod': [('Np237','n2n')],
        'loss': [('Np236','decay'),('Np236','absorption')]
    },
    'Np237': {
        'prod': [('U237', 'decay')],
        'loss': [('Np237','absorption')]
    },
    'Np238': {
        'prod': [('Np237', 'n_gamma')],
        'loss': [('Np238','decay'),('Np238','absorption')]
    },
    'Np239': {
        'prod': [('U239', 'decay')],
        'loss': [('Np239','decay'),('Np239','absorption')]
    },
    'Pu238': {
        'prod': [('Np238', 'decay')],
        'loss': [('Pu238','absorption')]
    },
    'Pu239': {
        'prod': [('Np239', 'decay'),('Pu238', 'n_gamma')],
        'loss': [('Pu239', 'absorption')]
    },
    'Pu240': {
        'prod' : [('U239','n_gamma'), ('Np239','n_gamma'), ('Pu239', 'n_gamma')],
        'loss': [('Pu240', 'absorption')]
    },
    'Pu241': {
        'prod': [('Pu240', 'n_gamma')],
        'loss': [('Pu241','decay'),('Pu241','absorption')]
    },
    'Pu242': {
        'prod': [('Pu241', 'n_gamma')],
        'loss': [('Pu242','absorption')]
    },
    'Pu243': {
        'prod': [('Pu242', 'n_gamma')],
        'loss': [('Pu243','decay'),('Pu243','absorption')]
    },
    'Am241': {
        'prod': [('Pu241', 'decay')],
        'loss': [('Am241','decay'),('Am241','absorption')]
    },
    'Am242': {
        'prod': [('Am241', 'n_gamma')],
        'loss': [('Am242','absorption')]
    },
    'Am243': {
        'prod': [('Pu243', 'decay'),('Am242', 'n_gamma')],
        'loss': [('Am243','absorption')]
    }
}

# Cross-section data will be added to each isotope entry later via your integration script.
