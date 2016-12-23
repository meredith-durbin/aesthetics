"""Configure matplotlib ~aesthetics~

This script provides a way to restyle matplotlib plots in two lines.
Works best with matplotlib 2.0 but compatible with 1.5 and up.

Credit for inspiration goes to the now-defunct prettyplotlib
(https://github.com/olgabot/prettyplotlib).

Requirements:

    * matplotlib >= 1.5 (prop_cycle vs color_cycle)
    * cycler
    * palettable (https://jiffyclub.github.io/palettable/)
    * working TeX installation

**NB: For El Capitan and above, "/Library/TeX/texbin" must be added to your path
rather than "/usr/local/texbin". I spent three sad hours figuring this out.**

Usage::

    from aesthetics import aestheticize
    aestheticize()

Todo:

    * Make backwards compatible (color_cycle rather than prop_cycle)
    * Add more color schemes (esp. inverted)
    * Check colorblind friendliness + other accessibility metrics
    * Configure sans-serif + monospace font options--usetex does not like this!

"""

from __future__ import print_function
from matplotlib import rc
from cycler import cycler
import matplotlib
import palettable

def aestheticize(colorscheme='brewer', lw=0.75, universal_color='#262626',
    verbose=False, return_colormaps=False):
    '''Set matplotlibrc params without editing local matplotlibrc

    Parameters:

        colorscheme ({'brewer' | 'vaporwave' | 'bw'}): Sets color cycle for
            axes objects. In matplotlib 2.0 this applies to patches as well as
            lines; in earlier versions patch colors must be set manually.

        lw (float): Linewidth for axis spines, tick marks, and plot lines.
            Default is 0.75.

        universal_color (color tuple or HTML hex color): Color for axis spines
            and text. Default is off-black, #262626.

        verbose (boolean): Whether to print settings for linewidth, color, and 
            colormaps. Default is false.

    '''
    defined_colorschemes = ['brewer', 'vaporwave', 'bw']
    if colorscheme not in defined_colorschemes:
        raise ValueError('Colorscheme arg must be one of: {}'.\
            format(defined_colorschemes))

    # universal settings
    rc('font', family='serif', serif='Computer Modern Roman')
    rc('text', usetex=True, color=universal_color)
    rc('lines', linewidth=lw, markeredgewidth=lw*0.5)
    rc('patch', linewidth=lw, edgecolor='#FAFAFA')
    rc('axes', linewidth=lw, edgecolor=universal_color, labelcolor=universal_color, 
        axisbelow=True)
    rc('image', origin='lower') # fits images
    rc('xtick.major', width=lw*0.75)
    rc('xtick.minor', width=lw*0.5)
    rc('xtick', color=universal_color)
    rc('ytick.major', width=lw*0.75)
    rc('ytick.minor', width=lw*0.5)
    rc('ytick', color=universal_color)
    rc('grid', linewidth=lw)
    rc('legend', loc='best', numpoints=1, scatterpoints=1, handlelength=1.5,
        fontsize='medium', columnspacing=1, handletextpad=0.75)
    
    width_cycle = cycler(linewidth=[1*lw, 2*lw, 3*lw])

    if colorscheme == 'brewer':
        cmap_discrete = palettable.colorbrewer.qualitative.Dark2_8
        cmap_continuous = 'viridis'
        color_cycle = cycler(color = cmap_discrete.mpl_colors)
        cycle = width_cycle * color_cycle

    elif colorscheme == 'vaporwave':
        cmap_discrete = palettable.cubehelix.perceptual_rainbow_16
        cmap_continuous = 'BuPu_r'
        color_cycle = cycler(color = cmap_discrete.mpl_colors[3:12:2])
        cycle = width_cycle * color_cycle

    elif colorscheme == 'bw':
        cmap_discrete = palettable.colorbrewer.sequential.Greys_5_r
        cmap_continuous = 'Greys_r'
        color_cycle = cycler(color=cmap_discrete.mpl_colors[1:4])
        linestyle_cycle = cycler(linestyle=['-', '--', ':', '-.'])
        cycle = width_cycle * linestyle_cycle * color_cycle

    rc('axes', prop_cycle=cycle)
    rc('image', cmap=cmap_continuous)

    mpl_ver = matplotlib.__version__
    if mpl_ver.startswith('1.'):
        # sets patch default color to first color in axes cycle
        rc('patch',facecolor=color_cycle.by_key()['color'][0])

    if verbose:
        print('Matplotlib version: {}'.format(mpl_ver))
        print('Universal linewidth: {}'.format(lw))
        print('Universal color: {}'.format(universal_color))
        print('Color cycle palette: {}'.format(cmap_discrete.name))
        print('Image colormap: {}'.format(cmap_continuous))
