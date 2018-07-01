from distutils.version import LooseVersion

from . import patch, _hv

import param

try:
    import intake.plotting # noqa
    patch('intake', extension='bokeh')
except:
    import intake
    version = LooseVersion(intake.__version__)
    raise Exception(intake.__version__)
    if LooseVersion(intake.__version__) <= '0.1.5':
        patch('intake', extension='bokeh')
        patch('intake', 'plot')
    else:
        if not _hv.extension._loaded:
            _hv.extension('bokeh', logo=False)
