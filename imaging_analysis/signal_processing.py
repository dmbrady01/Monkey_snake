import scipy.signal as ssp

def FilterSignal(signal, **kwargs):

    """Given some signal data, uses ButterFilterDesign to
    construct a filter and applies it to signal.
    signal: data signal
    lowcut: lower bound for filter
    highcut: upper bound for filter
    fs: sampling frequency
    order: filter order
    axis: axis of matrix to apply filter
    """

    options = {
        'lowcut': 5,
        'highcut': 30,
        'fs': 1018,
        'order': 5,
        #'btype': 'lowpass',
        'axis': 0,
    }
    options.update(kwargs)

    lowcut = options['lowcut']
    highcut = options['highcut']
    fs = options['fs']
    order = options['order']
    #btype = options['btype']
    axis = options['axis']

    """Constructs the numerator and denominator for the low/high/bandpass/bandstop
    filter. low and high are the cutoff frequencies, fs is the sampling frequency,
    order is the desired filter order, and btype designates what type of filter will
    ultimately be constructed (lowpass, highpass, bandpass, bandstop)."""
    # calculate nyquist frequency (half the sampling frequency)
    nyquist = fs * 0.5
    # try constructing normalized lowcut
    try:
        norm_low = lowcut / nyquist
    except TypeError:
        pass
    # try constructing normalized highcut
    try:
        norm_high = highcut / nyquist
        # Makes sure highcut is lower than nyquist frequency
        if norm_high > 1:
            raise ValueError('%s is larger than the nyquist frequency. Choose a smaller highcut (at most half the sampling rate).' % highcut)
    except TypeError:
        pass
    # Construct param to be bassed into butter

    if (lowcut != None) and (highcut == None):
        btype = 'lowpass'
    elif (lowcut == None) and (highcut != None):
        btype = 'highpass'
    elif (lowcut != None) and (highcut != None):
        btype = 'bandpass'
    else:
        raise ValueError("Both lowcut and highcut are equal to None. You must pass a value for lowcut, highcut, or both variables")

    if btype == 'lowpass':
        params = norm_high
    elif btype == 'highpass':
        params = norm_low
    elif (btype == 'bandpass') or (btype == 'bandstop'):
        params = [norm_low, norm_high]
    else:
        raise ValueError("%s must be 'lowpass', 'highpass', 'bandpass', or 'bandstop'"
            % btype)
    # Return butter
    b, a = ssp.butter(order, params, btype=btype, analog=False)

    return ssp.filtfilt(b, a, signal, axis=options['axis'])
