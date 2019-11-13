import numpy as np

def zscore(test_signal, ref_signal, **kwargs):
    options = {
        'axis': 0
    }
    options.update(kwargs)
    mean_reference = np.mean(ref_signal, axis=kwargs['axis'])
    std_baseline = np.std(ref_signal, axis=kwargs['axis'])
    z_score = (test_signal - mean_reference)/std_baseline
    
    return z_score
   
