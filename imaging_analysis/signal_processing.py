import scipy.signal as ssp
def savGolFilter(signal,**kwargs):
    
    options = {
        'window_length': 3001,
        'polyorder': 1,
        'deriv': 0,
        'delta': 1,
        'axis': -1,
        'mode': 'interp',
        'cval': 0,
    }
    
    # Update based on kwargs
    options.update(kwargs)
    
    return ssp.savgol_filter(signal, options['window_length'], options['polyorder'],
                         options['deriv'], options['delta'], options['axis'],
                         options['mode'], options['cval'])
