#!/bin/env python

import plottery_wrapper as p


# Common options
fnames=[ "outputs/higgs.root", "outputs/othernoh.root", "outputs/ttz.root", "outputs/twz.root", "outputs/wz.root", "outputs/zz.root", ]
sig_fnames=[ "outputs/wwz.root", "outputs/wzz.root", "outputs/zzz.root", ]
data_fname="outputs/data.root"
legend_labels=[ "Higgs", "Others", "t#bar{t}Z", "tWZ", "WZ", "ZZ", ]
signal_labels=["WWZ", "WZZ", "ZZZ"]
usercolors=[2011,920,2005,2007,2003,2001]
dirname="plots/",

p.dump_plot(
        filter_pattern="ChannelOnZ__,ChannelBTagEMu__",
        dogrep=True, # Set it to True to match the pattern provided above (i.e. if filter_pattern="fatjetMass_lead" and dogrep=True, then any histogram object with name "*fatjetMass_lead*" will be plotted)
        extraoptions= {
            "signal_scale":1,
            "print_yield": True,
            "nbins":30,
            "legend_ncolumns":3,
            "legend_scalex":1.8,
            "legend_scaley":1.2,
            "yield_prec":4, # yield precision
            "ratio_range":[0.,2.],
            }, # look at rooutil/plottery/plottery.py for more available option. Also there are some special options in rooutil/plottery_wrapper.py but .. it might be a bit harder to decipher
        # _plotter=p.plot_cut_scan  # <--- uncomment this line if you want to perform a cut scan optimization
        fnames=fnames,
        sig_fnames=sig_fnames,
        data_fname=data_fname,
        legend_labels=legend_labels,
        signal_labels=signal_labels,
        usercolors=usercolors,
        dirname=dirname,
        )

p.dump_plot(
        filter_pattern="ChannelEMu__,ChannelOffZ__",
        dogrep=True, # Set it to True to match the pattern provided above (i.e. if filter_pattern="fatjetMass_lead" and dogrep=True, then any histogram object with name "*fatjetMass_lead*" will be plotted)
        extraoptions= {
            "signal_scale":1,
            "print_yield": True,
            "nbins":30,
            "legend_ncolumns":3,
            "legend_scalex":1.8,
            "legend_scaley":1.2,
            "yield_prec":4, # yield precision
            "ratio_range":[0.,2.],
            "blind":True,
            }, # look at rooutil/plottery/plottery.py for more available option. Also there are some special options in rooutil/plottery_wrapper.py but .. it might be a bit harder to decipher
        # _plotter=p.plot_cut_scan  # <--- uncomment this line if you want to perform a cut scan optimization
        fnames=fnames,
        sig_fnames=sig_fnames,
        data_fname=data_fname,
        legend_labels=legend_labels,
        signal_labels=signal_labels,
        usercolors=usercolors,
        dirname=dirname,
        )
