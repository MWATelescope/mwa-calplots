This module provides a single script `aocal_plot.py` and the supporting library `aocal.py` together they are able to read calibration files created by `calibrate` and produce amplitude and phase plots.



```
Usage: aocal_plot.py binfile
    Plot calibration solutions
    

Options:
  -h, --help            show this help message and exit
  --refant=REFANT       divide solutions through by reference antenna.
                        Negative means divide through by mean antenna
  -m METAFITS, --metafits=METAFITS
                        metafits file (for ordering by receiver)
  -v, --verbose         -v info, -vv debug
  --outdir=OUTDIR       output directory [default: same as binfile]
  --title=PLOT_TITLE    plot title
  --format=FORMAT       plot format [default: png]
  --suffix=SUFFIX       suffix to add to plot names
  --amp_max=AMP_MAX     Maximum of y axis of amplitude plots
  --marker=MARKER       matplotlib marker [default: ,]
  --markersize=MARKERSIZE
                        matplotlib markersize [default: 2]
```
