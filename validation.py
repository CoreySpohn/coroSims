from pathlib import Path

import astropy.units as u
import numpy as np
from astropy.time import Time
from exoverses.base.planet import Planet
from exoverses.base.star import Star
from exoverses.base.system import System

from coroSims import coronagraph, observations

# Input files
# scene = Path("input/scenes/999-HIP_-TYC_SUN-mv_4.83-L_1.00-d_10.00-Teff_5778.00.fits")
coronagraph_dir = Path("input/coronagraphs/LUVOIR-B-VC6_timeseries/")
# coronagraph_dir = Path(
#     "input/coronagraphs/LUVOIR-A_APLC_18bw_medFPM_2021-05-07_Dyn10pm-nostaticabb/"
# )

# Parameters
observing_scenario = {
    "diameter": 1 * u.m,
    "wavelengths": 1.0 * u.um,
    "times": Time(2000, format="decimalyear"),
    "include_star": False,
    "include_planets": True,
    "include_disk": False,
}

# Initialize coronagraph object.
coro = coronagraph.Coronagraph(coronagraph_dir)

# Load ExoVista scene
star_dict = {
    "name": "Sun",
    "spectral_type": "G2V",
    "dist": 10 * u.pc,
    "mass": 1 * u.M_sun,
}
star = Star(star_dict)
planet_dict = {
    "t0": Time(2000, format="decimalyear"),
    "a": 1 * u.au,
    "e": 0,
    "inc": 90 * u.deg,
    "W": 0 * u.deg,
    "w": 0 * u.deg,
    "M0": 0 * u.deg,
    "radius": 1 * u.R_earth,
    "mass": 1 * u.M_earth,
    "p": 0.3,
}
planet = Planet(planet_dict, star)
system = System(star=star, planets=[planet], disk=None)

# system = ExovistaSystem(scene)
breakpoint()

# Simulate observations
observations = observations.Observations(coro, system, observing_scenario)
