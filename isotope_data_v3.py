import numpy as np

isotopes = {
    'U234': {
        'decay': np.log(2) / (2.455e5 * 365.25 * 24 * 3600),
        'n_gamma': 0.0,
        'n_2n': 0.0,
        'n_fission': 0.0,
        'prod': [('U235', 'n_gamma')]
    },
    'U235': {
        'decay': np.log(2) / (7.04e8 * 365.25 * 24 * 3600),  # 704Myr
        'n_gamma': 100.0e-24,
        'n_2n': 0.0,
        'n_fission': 583.0e-24,
        'prod': [('U234', 'n_gamma')]
    },
    'U236': {
        'decay': 0.0,
        'n_gamma': 5.0e-24,
        'n_2n': 0.0,
        'n_fission': 0.0,
        'prod': [('U235', 'n_gamma')]
    },
    'U237': {
        'decay': np.log(2) / (6.75 * 60),
        'n_gamma': 0.0,
        'n_2n': 0.0,
        'n_fission': 0.0,
        'prod': [('U236', 'n_gamma')]
    },
    'U238': {
        'decay': 0.0,
        'n_gamma': 2.7e-24,
        'n_2n': 0.3e-24,
        'n_fission': 0.00002e-24,
        'prod': []
    },
    'U239': {
        'decay': np.log(2) / (23.5 * 60),
        'n_gamma': 0.0,
        'n_2n': 0.0,
        'n_fission': 0.0,
        'prod': [('U238', 'n_gamma')]
    },
    'Np236': {
        'decay': 0.0,
        'n_gamma': 0.0,
        'n_2n': 0.0,
        'n_fission': 0.0,
        'prod': []
    },
    'Np237': {
        'decay': np.log(2) / (2.14e6 * 365.25 * 24 * 3600),
        'n_gamma': 1.0e-24,
        'n_2n': 0.0,
        'n_fission': 0.0,
        'prod': [('U237', 'decay')]
    },
    'Np238': {
        'decay': 0.0,
        'n_gamma': 0.0,
        'n_2n': 0.0,
        'n_fission': 0.0,
        'prod': []
    },
    'Np239': {
        'decay': np.log(2) / (2.3565 * 24 * 3600),
        'n_gamma': 0.0,
        'n_2n': 0.0,
        'n_fission': 0.0,
        'prod': [('U239', 'decay')]
    },
    'Pu238': {
        'decay': np.log(2) / (87.7 * 365.25 * 24 * 3600),
        'n_gamma': 8.0e-24,
        'n_2n': 0.0,
        'n_fission': 0.0,
        'prod': [('Cm242', 'decay'), ('U237', 'alpha')]
    },
    'Pu239': {
        'decay': np.log(2) / (2.41e4 * 365.25 * 24 * 3600),
        'n_gamma': 270.0e-24,
        'n_2n': 0.0,
        'n_fission': 747.0e-24,
        'prod': [('Np239', 'decay')]
    },
    'Pu240': {
        'decay': np.log(2) / (6560 * 365.25 * 24 * 3600),
        'n_gamma': 288.0e-24,
        'n_2n': 0.0,
        'n_fission': 0.064e-24,
        'prod': [('Pu239', 'n_gamma')]
    },
    'Pu241': {
        'decay': np.log(2) / (14.35 * 365.25 * 24 * 3600),
        'n_gamma': 363.0e-24,
        'n_2n': 0.0,
        'n_fission': 1012.0e-24,
        'prod': [('Pu240', 'n_gamma')]
    },
    'Pu242': {
        'decay': np.log(2) / (3.75e5 * 365.25 * 24 * 3600),
        'n_gamma': 19.0e-24,
        'n_2n': 0.0,
        'n_fission': 0.001e-24,
        'prod': [('Pu241', 'n_gamma')]
    },
    'Pu243': {
        'decay': 0.0,
        'n_gamma': 0.0,
        'n_2n': 0.0,
        'n_fission': 0.0,
        'prod': [('Pu242', 'n_gamma')]
    },
    'Am241': {
        'decay': np.log(2) / (432.2 * 365.25 * 24 * 3600),
        'n_gamma': 600.0e-24,
        'n_2n': 0.0,
        'n_fission': 0.0,
        'prod': [('Pu241', 'decay')]
    },
    'Am242': {
        'decay': np.log(2) / (0.664 * 3600),
        'n_gamma': 0.0,
        'n_2n': 0.0,
        'n_fission': 0.0,
        'prod': [('Am241', 'n_gamma')]
    },
    'Am243': {
        'decay': np.log(2) / (7400 * 365.25 * 24 * 3600),
        'n_gamma': 0.0,
        'n_2n': 0.0,
        'n_fission': 0.0,
        'prod': [('Am242', 'decay')]
    },
    'Cm242': {
        'decay': np.log(2) / (162.8 * 24 * 3600),
        'n_gamma': 0.0,
        'n_2n': 0.0,
        'n_fission': 0.0,
        'prod': [('Am242', 'decay')]
    }
}
