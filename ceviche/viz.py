import numpy as np
import matplotlib.pylab as plt

def real(val, outline=None, ax=None, cbar=False, cmap='RdBu', outline_alpha=0.5):
    """Plots the real part of 'val', optionally overlaying an outline of 'outline'
    """

    if ax is None:
        fig, ax = plt.subplots(1, 1, constrained_layout=True)
    
    vmax = np.abs(val).max()
    h = ax.imshow(np.real(val.T), cmap=cmap, origin='lower left', vmin=-vmax, vmax=vmax)
    
    if outline is not None:
        ax.contour(outline.T, 1, colors='k', alpha=outline_alpha)
    
    ax.set_ylabel('y')
    ax.set_xlabel('x')
    if cbar:
        plt.colorbar(h, ax=ax)
    
    return ax

def abs(val, outline=None, ax=None, cbar=False, cmap='magma', outline_alpha=0.5):
    """Plots the absolute value of 'val', optionally overlaying an outline of 'outline'
    """
    
    if ax is None:
        fig, ax = plt.subplots(1, 1, constrained_layout=True)      
    
    vmax = np.abs(val).max()
    h = ax.imshow(np.abs(val.T), cmap=cmap, origin='lower left', vmin=0, vmax=vmax)
    
    if outline is not None:
        ax.contour(outline.T, 1, colors='w', alpha=outline_alpha)
    
    ax.set_ylabel('y')
    ax.set_xlabel('x')
    if cbar:
        plt.colorbar(h, ax=ax)
    
    return ax
