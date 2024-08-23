#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pycbc.waveform
from pycbc.types import TimeSeries
from pycbc.waveform.ringdown import get_td_from_final_mass_spin as wf0
from pycbc import conversions as cn


#--------------------------------MODIFIED WAVEFORM--------------------------------#
def TdQNMfromFinalMassSpin_Lensing(**args):
    hpu, hcu = wf0(**args)
    
    ratio_m_key = args['ratio_m'];
    n_key = args['n'];
   
    hpl = hpu * np.cos(n_key * np.pi) - hcu * np.sin(n_key * np.pi)
    hcl = hcu * np.cos(n_key * np.pi) + hpu * np.sin(n_key * np.pi)
    
    hpl /= ratio_m_key
    hcl /= ratio_m_key
    
    return hpl, hcl
    #hpl, hcl = hpu.copy(), hcu.copy()
    

#    for i in range(1, n_images + 1):
#        ratio_m_key = args[f'ratio_m{i}']
#        n_key = args[f'n{i}']

#        if f'ratio_m{i}' in args and f'n{i}' in args:
#            hpl = hpu * np.cos(n_key * np.pi) - hcu * np.sin(n_key * np.pi)
#            hcl = hcu * np.cos(n_key * np.pi) + hpu * np.sin(n_key * np.pi)

#            hpl *= ratio_m_key
#            hcl *= ratio_m_key
#        else:
#            raise ValueError(f'Missing parameters for image {i}: {ratio_m_key} or {n_key}')