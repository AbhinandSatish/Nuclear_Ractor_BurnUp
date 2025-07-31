import numpy as np

isotopes = {
    'U234': {
        'decay': np.log(2) / (2.455e5 * 365.25 * 24 * 3600),
        'prod': [('U235', 'n_gamma')],
        'loss': [("U234", "absorption")],
    },
    'U235': {
        'decay': np.log(2) / (7.04e8 * 365.25 * 24 * 3600),
        'prod': [('U234', 'n_gamma')],
        'loss': [("U235", "absorption")],
    },
    'U236': {
        'decay': 0.0,
        'prod': [('U235', 'n_gamma')],
        'loss': [("U236", "absorption")],
    },
    'U237': {
        'decay': np.log(2) / (6.75 * 60),
        'prod': [('U236', 'n_gamma')],
        'loss': [("U237", "decay")],
    },
    'U238': {
        'decay': 0.0,
        'prod': [],
        'loss': [("U238", "absorption")],
    },
    'U239': {
        'decay': np.log(2) / (23.5 * 60),
        'prod': [('U238', 'n_gamma')],
        'loss': [("U239", "decay")],
    },
    'Np236': {
        'decay': 0.0,
        'prod': [],
        'loss': [("Np236", "absorption")],
    },
    'Np237': {
        'decay': np.log(2) / (2.14e6 * 365.25 * 24 * 3600),
        'prod': [('U237', 'decay')],
        'loss': [("Np237", "absorption")],
    },
    'Np238': {
        'decay': 0.0,
        'prod': [],
        'loss': [("Np238", "absorption"), ("Np238", "decay")],
    },
    'Np239': {
        'decay': np.log(2) / (2.3565 * 24 * 3600),
        'prod': [('U239', 'decay')],
        'loss': [("Np239", "absorption"), ("Np239", "decay")],
    },
    'Pu238': {
        'decay': np.log(2) / (87.7 * 365.25 * 24 * 3600),
        'prod': [('Cm242', 'decay'), ('U237', 'alpha')],
        'loss': [("Pu238", "absorption"), ("Pu238", "decay")],
    },
    'Pu239': {
        'decay': np.log(2) / (2.41e4 * 365.25 * 24 * 3600),
        'prod': [('Np239', 'decay')],
        'loss': [("Pu239", "absorption"), ("Pu239", "decay")],
    },
    'Pu240': {
        'decay': np.log(2) / (6560 * 365.25 * 24 * 3600),
        'prod': [('Pu239', 'n_gamma'), ('Np239', 'n_gamma'),('U239', 'n_gamma')],
        'loss': [("Pu240", "absorption")],
    },
    'Pu241': {
        'decay': np.log(2) / (14.35 * 365.25 * 24 * 3600),
        'prod': [('Pu240', 'n_gamma')],
        'loss': [("Pu241", "absorption"), ("Pu241", "decay")],
    },
    'Pu242': {
        'decay': np.log(2) / (3.75e5 * 365.25 * 24 * 3600),
        'prod': [('Pu241', 'n_gamma')],
        'loss': [("Pu242", "absorption")],
    },
    'Pu243': {
        'decay': 0.0,
        'prod': [('Pu242', 'n_gamma')],
        'loss': [("Pu243", "absorption"), ("Pu243", "decay")],
    },
    'Am241': {
        'decay': np.log(2) / (432.2 * 365.25 * 24 * 3600),
        'prod': [('Pu241', 'decay')],
        'loss': [("Am241", "absorption"), ("Am241", "decay")],
    },
    'Am242': {
        'decay': np.log(2) / (0.664 * 3600),
        'prod': [('Am241', 'n_gamma')],
        'loss': [("Am242", "absorption")],
    },
    'Am243': {
        'decay': np.log(2) / (7400 * 365.25 * 24 * 3600),
        'prod': [('Am242', 'decay')],
        'loss': [("Am243", "absorption")],
    },
    'Cm242': {
        'decay': np.log(2) / (162.8 * 24 * 3600),
        'prod': [('Am242', 'decay')],
        'loss': [("Cm242", "absorption")],
    },
}

# Cross-section data will be added to each isotope entry later via your integration script.
