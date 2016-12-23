The Matplotlib Aesthetic
==========

Or, I Have Spent More Time Making Plots Look Cool Than I Ever Will On Actual Science
----------

I got tired of having to manually TeXify everything and change the default plot colors every time, so here's my solution to that.

Basic usage:

```python
from aesthetics import aestheticize
aestheticize()
```

Currently offers three color schemes: ``brewer`` (default, Brewer colors), ``vaporwave`` (you can guess), and ``bw`` (black-and-white). To set the style:
```python
aestheticize(colorscheme = 'vaporwave')
```

To see what specific color combinations and other settings are used, pass ``verbose=True``.

Makes use of [palettable](https://jiffyclub.github.io/palettable/colorbrewer/) color palettes. Inspired by [prettyplotlib](https://github.com/olgabot/prettyplotlib/).
