class transitleastsquaresresults(dict):
    """The results of a transitleastsquares search"""

    def __init__(self, *args):
        super(transitleastsquaresresults, self).__init__(
            zip(
                (
                    "SDE",
                    "SDE_raw",
                    "chi2_min",
                    "chi2red_min",
                    "period",
                    "period_uncertainty",
                    "T0",
                    "duration",
                    "depth",
                    "depth_mean",
                    "depth_mean_even",
                    "depth_mean_odd",
                    "transit_depths",
                    "transit_depths_uncertainties",
                    "rp_rs",
                    "snr",
                    "snr_per_transit",
                    "snr_pink_per_transit",
                    "odd_even_mismatch",
                    "transit_times",
                    "per_transit_count",
                    "transit_count",
                    "distinct_transit_count",
                    "empty_transit_count",
                    "FAP",
                    "in_transit_count",
                    "after_transit_count",
                    "before_transit_count",
                    "periods",
                    "power",
                    "power_raw",
                    "SR",
                    "chi2",
                    "chi2red",
                    "model_lightcurve_time",
                    "model_lightcurve_model",
                    "model_folded_phase",
                    "folded_y",
                    "folded_dy",
                    "folded_phase",
                    "model_folded_model",
                ),
                args,
            )
        )

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class transitleastsquaresresults_limited(transitleastsquaresresults):
    """A subclass of transitleastsquaresresults with subset parameter support"""

    def __init__(self, keys, *args):
        """
        Initialize with a subset of keys and corresponding values.

        Args:
            keys (list of str): The subset of keys to include in the results.
            *args: The values corresponding to the specified keys.
        """
        # Validate keys and values
        if len(keys) != len(args):
            raise ValueError("Number of keys and values must match.")
        
        # Call the parent class constructor with filtered arguments
        super().__init__(*args)  # Initialize with full data structure
        
        # Retain only the specified keys in the dictionary
        for key in list(self.keys()):  # Iterate over all keys
            if key not in keys:
                del self[key]