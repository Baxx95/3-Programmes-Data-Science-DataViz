# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 08:53:33 2021

@author: Zakaria
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs


fig = plt.figure(figsize=(25,15))
axe = fig.add_subplot(1,1,1, projection=ccrs.PlateCarree())
#----------------------------------------------------------------
#Liste de projection CARTOGRAPHIQUES :
# - AzimuthalEquidistant : projection azumitale équidistante
# - LambertCylindrical
# - Mollweide
# - Robinson
# - InterruptedGoodeHomolosine
#----------------------------------------------------------------

axe.set_extent((251, 21, 75, -35))
axe.stock_img()
axe.coastelines()
axe.tissot(facecolor='purple', alpha=0.8)


