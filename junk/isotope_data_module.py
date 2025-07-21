
import numpy as np

isotopes = {
    'U230': {
        'decay': np.log(2) / (20.8 * 3600),  # 20.8 hours
        'n_gamma': 1.0e-24,
        'prod': [('Th230', 'decay')]
    },
    'U231': {
        'decay': np.log(2) / (4.2 * 3600),  # 4.2 hours
        'n_gamma': 1.0e-24,
        'prod': [('U230', 'n_gamma')]
    },
    'Pa231': {
        'decay': np.log(2) / (32760 * 365.25 * 24 * 3600),  # 32,760 years
        'n_gamma': 1.0e-24,
        'prod': [('U231', 'decay')]
    },
    'U232': {
        'decay': np.log(2) / (68.9 * 365.25 * 24 * 3600),  # 68.9 years
        'n_gamma': 1.0e-24,
        'prod': [('Pa231', 'n_gamma')]
    },
    'U233': {
        'decay': 0.0,
        'n_gamma': 1.0e-24,
        'prod': [('U232', 'n_gamma')]
    },
    'Np233': {
        'decay': np.log(2) / (36.2 * 60),  # 36.2 minutes
        'n_gamma': 0.0,
        'prod': [('U233', 'decay')]
    },
    'Pu233': {
        'decay': 0.0,
        'n_gamma': 1.0e-24,
        'prod': [('Np233', 'decay')]
    },
    'Pu234': {
        'decay': 0.0,
        'n_gamma': 1.0e-24,
        'prod': [('Pu233', 'n_gamma')]
    },
    'U234': {
        'decay': np.log(2) / (2.455e5 * 365.25 * 24 * 3600),  # 245,500 years
        'n_gamma': 1.0e-24,
        'prod': [('Pu234', 'decay')]
    },
    'U235': {
        'decay': 0.0,
        'n_gamma': 1.0e-24,
        'prod': [('U234', 'n_gamma')]
    },
    'U236': {
        'decay': 0.0,
        'n_gamma': 1.0e-24,
        'prod': [('U235', 'n_gamma')]
    },
    'U237': {
        'decay': np.log(2) / (6.75 * 60),  # 6.75 minutes
        'n_gamma': 0.0,
        'prod': [('U236', 'n_gamma')]
    },
    'Np237': {
        'decay': np.log(2) / (2.14e6 * 365.25 * 24 * 3600),  # 2.14 million years
        'n_gamma': 1.0e-24,
        'prod': [('U237', 'decay')]
    },
    'U238': {
        'decay': 0.0,
        'n_gamma': 2.68e-24,
        'prod': []
    },
    'U239': {
        'decay': np.log(2) / (23.5 * 60),  # 23.5 minutes
        'n_gamma': 0.0,
        'prod': [('U238', 'n_gamma')]
    },
    'Np239': {
        'decay': np.log(2) / (2.3565 * 24 * 3600),  # 2.3565 days
        'n_gamma': 0.0,
        'prod': [('U239', 'decay')]
    },
    'Pu239': {
        'decay': 0.0,
        'n_gamma': 2.7e-25,
        'prod': [('Np239', 'decay')]
    },
    'Pu240': {
        'decay': 0.0,
        'n_gamma': 1.0e-25,
        'prod': [('Pu239', 'n_gamma')]
    },
    'Pu241': {
        'decay': np.log(2) / (14.35 * 365.25 * 24 * 3600),  # 14.35 years
        'n_gamma': 1.2e-25,
        'prod': [('Pu240', 'n_gamma')]
    },
    'Am241': {
        'decay': np.log(2) / (432.2 * 365.25 * 24 * 3600),  # 432.2 years
        'n_gamma': 2e-25,
        'prod': [('Pu241', 'decay')]
    },
    'Am242': {
        'decay': np.log(2) / (16 * 3600),  # 16 hours
        'n_gamma': 0.0,
        'prod': [('Am241', 'n_gamma')]
    },
    'Cm242': {
        'decay': np.log(2) / (162.8 * 24 * 3600),  # 162.8 days
        'n_gamma': 0.0,
        'prod': [('Am242', 'decay')]
    },
    'Pu238': {
        'decay': np.log(2) / (87.7 * 365.25 * 24 * 3600),  # 87.7 years
        'n_gamma': 0.0,
        'prod': [('Cm242', 'decay')]
    },
    'Th230': {
        'decay': np.log(2) / (7.54e4 * 365.25 * 24 * 3600),  # 75,400 years
        'n_gamma': 1.0e-24,
        'prod': []
    }
}


