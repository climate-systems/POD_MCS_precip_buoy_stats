# POD_MCS_precip_buoy_stats
This POD provides diagnostics of tropical mesoscale convective systems (MCSs) and their thermodynamic environments,informed by an empirical buoyancy measure (B<sub>L</sub>). Specifically, these diagnostics are designed to evaluate model performance in representing basic spatial-temporal characteristics of tropical MCSs and associated precipitation responses to the buoyancy measure under MCS and non-MCS conditions. The diagnostics include:

- Tropical-mean precipitation
- MCS frequency and its contribution to total precipitation
- Sensitivity of precipitation to individual buoyancy components, evaluated separately for MCS and non-MCS conditions
[!NOTE]
- A minimum of one year of data at 3-hourly temporal resolution is recommended to ensure a sufficient sample size of tropical MCSs.
- This POD is designed for models with relatively high horizontal resolution (≤ 0.5°). Conservative regridding is applied by default to ensure consistent comparisons between model outputs and the observational reference (GPM-IMERG + ERA5).
- Detailed descriptions of the POD are documeneted in "diagnostics/MCS_precip_buoy_stats/doc/MCS_precip_buoy_stats.rst"
