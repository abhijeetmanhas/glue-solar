from pkg_resources import get_distribution, DistributionNotFound
from sunpy.cm import cmlist

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    pass


def setup():
    from glue.viewers.image.qt import ImageViewer
    from glue_solar.pixel_extraction import PixelExtractionTool  # noqa
    ImageViewer.tools.append('solar:pixel_extraction')
    from glue.config import Colormaps
#    for i in range(len(cmlist)):
    Colormaps.add(['hmimag',cmlist['hmimag']])
