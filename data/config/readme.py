import os
import json

dataset_readme = {
    "atm_atomic": """Navigation and Meteorological Measurements

Ship Position (Latitude and Longitude):
In the one minute files the position is treated somewhat differently from all the other data. The position given is the ship's position at the start of the one minute 'averaging' period. All other data are a true average. The PMEL GPS was the primary source. The Ship's GPS was used when there were missing data in the PMEL record.

Ship Speed, Course and Gyro:
The ship's GPS speed in knots (Speed Over Ground) and GPS Course in compass degrees (Course Over Ground) are the one minute averages from the GPS (the PMEL GPS as the primary source, the Ship's GPS was the secondary source). To make the one minute averages the 1-second recorded motion vector was separated into east and north components that were averaged into one minute bins. The one minute components were then combined into the ship Velocity Vector. The GyroCompass in compass degrees is the one minute average heading. The primary source was the PMEL GPS compass (Si-TEX Vector Pro), the ship gyro compass data were used when the primary data were missing. The 1-second data were separated into an east and north component before averaging and then recombined. NOTE: The GPS-Course is the direction the ship is moving. The GyroCompass is the direction the ship's bow is pointing. When the ship is moving at 6 or more knots they generally are the same. Due to water currents, at slow speeds there can be quite a difference between the two. When the ship is stationary, the two are totally unrelated.

Relative Wind:
The primary source for the relative wind data was the PMEL Vaisala WX520 sonic anemometer, located on the aerosol sampling mast. For periods of missing data, the PSD Sonic anemometer on the ship’s foremast was used. The one second relative wind speed and direction data were separated into orthogonal components of "keel" and "beam". These components were averaged into 1 minute averages, and then recombined to relative wind vectors. Wind speed is reported in meters per second and wind direction is in degrees with -90 being wind approaching the ship on the port beam, 0 degrees being wind approaching the ship directly on the bow, and +90 degrees being wind approaching the ship on the starboard beam.

Wind Components/ True Wind Speed/ True Wind Direction:
The primary source for the true wind data was the average of the PMEL Vaisala WX520 and WX536 sonic anemometers, both located on the aerosol sampling mast, 17 m above sea level.   For periods of missing data the average of the ship’s two WXT sensors, located above the ship’s navigation bridge,  were used.  True wind speed and direction were calculated from the relative wind taking into account the ship's motion from the GPS and the ship heading from the GPS compass. The true wind vector is given as wind speed in m/s and wind direction in compass degrees (0 degrees meaning wind arriving from the north). The WindU and WindV are the east and north components of the wind vector in m/s.  WindU and WindV are positive for wind going in the east and north directions.

Atmospheric Temperature:
One minute averages in degrees C. The following data sources were used. The PMEL Vaisala WXT536 and the PMEL Vaisala WXT520 sensor (both on the sampling aerosol mast at 17 m above sea level) and the NOAA PSD sensor on the bow foremast also at 17 meters above the sea surface.  These 3 sensors generally agreed to better than 0.5 deg C. For this project the average of the two PMEL WXT sensors was used. During periods of missing data in the PMEL record the PSD sensor was used.

Relative humidity:
One minute averages in %. The following data sources were used. The PMEL Vaisala WXT536 and the PMEL Vaisala WXT520 sensor (both on the sampling aerosol mast at 17 m above sea level) and the  NOAA PSD sensor on the bow foremast also at 17 meters above the sea surface.  These 3 sensors generally agreed within 5% in rh.   For this project the average of the two PMEL WXT sensors was used. During periods of missing data in the PMEL record the PSD sensor was used.

Barometric Pressure:
One minute averages in units of mb. There were two sources of raw data, the PMEL WXT sensors (corrected to sea level) and the NOAA PSD sensor (corrected to sea level).  For this project the average of the sea level corrected PMEL WXT sensors was used.  Missing data were filled in with the PSD sea level corrected pressure.

Insolation:
One minute averages in units of watts per square meter. Total solar radiation was measured with an Epply black and white pyranometer (horizontal surface receiver -180, model 8-48, serial number 12946) and an Epply precision pyranometer (horizontal surface receiver -180, twin hemispheres, model PSP, serial number 133035F3) that were mounted on the top of Areophys van. Both instruments were calibrated by the Epply Laboratory on October 11, 1994. There were times when the sampling mast shaded one or both sensors. There were also times when the ship's mast/bridge shaded the sensors. The shaded data have not been edited out of the 1 minute data record. The data reported here are from the model 8-48, serial number 12946 radiometer and are in watts per square meter and are the average value over the 1 minute sampling period.

Rain Rate (Precipitation):
The rain rate, in mm/hr, was measured by the PMEL-Vaisala WX520 and WX536 Met sensors located near the top of the aerosol sampling mast.  The average of the two sensors was used.  During periods of high wind speed (above about 15 m/s), sea spray causes drops that will impact the rain sensor and register as rain, thus there are periods where rain is recorded when there is no rain falling. We have no way of editing this out of the data record so the measured rain rate at these higher wind speeds is unreliable.

Aerosol inlet:
Ambient aerosol particles were sampled at 18 m above sea level through a heated mast. The mast extended 5 m above and forward of the aerosol measurement container. The inlet was a rotating cone-shaped nozzle that was automatically positioned into the relative wind to maintain nominally isokinetic flow and minimize the loss of supermicrometer particles. Air entered the inlet through a 5 cm diameter hole, passed through a 7 degree expansion cone, and then into the 20 cm inner diameter sampling mast. The flow through the mast was 1 m3 min-1. The transmission efficiency of the inlet for particles with aerodynamic diameters less than 6.5 um (the largest size tested) is greater than 95% [Bates et al., 2002].

The bottom 1.5 m of the mast were heated to establish a stable reference relative humidity (RH) for the sample air controlled to the indicated target sample RH. Twenty one 1.6 cm inner diameter stainless steel tubes extending into the heated portion of the mast were connected to downstream aerosol instrumentation with either conductive silicon tubing or stainless steel tubing for analysis of organic aerosol.

CN and UFCN:
One of the twenty one 1.6 cm diameter tubes was used to supply ambient air to TSI 3010 (CN_Direct), a Brechtel aMCPC (CN_Stack) and TSI 3025A (UFCN_Direct) particle counters. Another one of the tubes was used to supply ambient air to TSI3785 (UFCN_Chem)  and Aerosol Devices MAGIC210 (CN_MART) particle counters. The 3010, aMCPC, 3025, 3785 and MAGIC210 measure all particles larger than roughly 12, 5, 3, 5 and 5 nm respectively. The total particle counts from each instrument were recorded each second. The data were filtered to eliminate periods of calibration and instrument malfunction and zero air periods, and periods of obvious ship contamination from the R/V Brown (based on relative wind and high CN counts). The "best" filtered values were chosen to represent CN>12 (CN) and ultra-fine (UFCN) particle concentrations. The best CN values are primarily from CN_Direct with data from CN_Stack used to fill in periods where the CN_Direct data were not available. Similarly, the UFCN values are primarily from UFCN_Direct with the UFCN_Chem and CN_MART data used to fill in periods where UFCN_Direct data were not available. These "best" data were averaged into one minute periods. One second data are available upon request.
  """,
    "atm": """Navigation and Meteorological Measurements

Ship Position (Latitude and Longitude):
In the one minute files the position is treated somewhat differently from all the other data. The position given is the ship's position at the start of the one minute 'averaging' period. All other data are a true average. The PMEL GPS was the primary source. The Ship's GPS was used when there were missing data in the PMEL record.

Ship Speed, Course and Gyro:
The ship's GPS speed in knots (Speed Over Ground) and GPS Course in compass degrees (Course Over Ground) are the one minute averages from the GPS (the PMEL GPS as the primary source, the Ship's GPS was the secondary source). To make the one minute averages the 1-second recorded motion vector was separated into east and north components that were averaged into one minute bins. The one minute components were then combined into the ship Velocity Vector. The GyroCompass in compass degrees is the one minute average heading. The primary source was the PMEL GPS compass (Si-TEX Vector Pro), the ship gyro compass data were used when the primary data were missing. The 1-second data were separated into an east and north component before averaging and then recombined. NOTE: The GPS-Course is the direction the ship is moving. The GyroCompass is the direction the ship's bow is pointing. When the ship is moving at 6 or more knots they generally are the same. Due to water currents, at slow speeds there can be quite a difference between the two. When the ship is stationary, the two are totally unrelated.

Relative Wind:
The primary source for the relative wind data was the PMEL Vaisala WX520 sonic anemometer, located on the aerosol sampling mast. For periods of missing data, the PSD Sonic anemometer on the ship’s foremast was used. The one second relative wind speed and direction data were separated into orthogonal components of "keel" and "beam". These components were averaged into 1 minute averages, and then recombined to relative wind vectors. Wind speed is reported in meters per second and wind direction is in degrees with -90 being wind approaching the ship on the port beam, 0 degrees being wind approaching the ship directly on the bow, and +90 degrees being wind approaching the ship on the starboard beam.

Wind Components/ True Wind Speed/ True Wind Direction:
The primary source for the true wind data was the average of the PMEL Vaisala WX520 and WX536 sonic anemometers, both located on the aerosol sampling mast, 17 m above sea level.   For periods of missing data the average of the ship’s two WXT sensors, located above the ship’s navigation bridge,  were used.  True wind speed and direction were calculated from the relative wind taking into account the ship's motion from the GPS and the ship heading from the GPS compass. The true wind vector is given as wind speed in m/s and wind direction in compass degrees (0 degrees meaning wind arriving from the north). The WindU and WindV are the east and north components of the wind vector in m/s.  WindU and WindV are positive for wind going in the east and north directions.

Atmospheric Temperature:
One minute averages in degrees C. The following data sources were used. The PMEL Vaisala WXT536 and the PMEL Vaisala WXT520 sensor (both on the sampling aerosol mast at 17 m above sea level) and the NOAA PSD sensor on the bow foremast also at 17 meters above the sea surface.  These 3 sensors generally agreed to better than 0.5 deg C. For this project the average of the two PMEL WXT sensors was used. During periods of missing data in the PMEL record the PSD sensor was used.

Relative humidity:
One minute averages in %. The following data sources were used. The PMEL Vaisala WXT536 and the PMEL Vaisala WXT520 sensor (both on the sampling aerosol mast at 17 m above sea level) and the  NOAA PSD sensor on the bow foremast also at 17 meters above the sea surface.  These 3 sensors generally agreed within 5% in rh.   For this project the average of the two PMEL WXT sensors was used. During periods of missing data in the PMEL record the PSD sensor was used.

Barometric Pressure:
One minute averages in units of mb. There were two sources of raw data, the PMEL WXT sensors (corrected to sea level) and the NOAA PSD sensor (corrected to sea level).  For this project the average of the sea level corrected PMEL WXT sensors was used.  Missing data were filled in with the PSD sea level corrected pressure.

Insolation:
One minute averages in units of watts per square meter. Total solar radiation was measured with an Epply black and white pyranometer (horizontal surface receiver -180, model 8-48, serial number 12946) and an Epply precision pyranometer (horizontal surface receiver -180, twin hemispheres, model PSP, serial number 133035F3) that were mounted on the top of Areophys van. Both instruments were calibrated by the Epply Laboratory on October 11, 1994. There were times when the sampling mast shaded one or both sensors. There were also times when the ship's mast/bridge shaded the sensors. The shaded data have not been edited out of the 1 minute data record. The data reported here are from the model 8-48, serial number 12946 radiometer and are in watts per square meter and are the average value over the 1 minute sampling period.

Rain Rate (Precipitation):
The rain rate, in mm/hr, was measured by the PMEL-Vaisala WX520 and WX536 Met sensors located near the top of the aerosol sampling mast.  The average of the two sensors was used.  During periods of high wind speed (above about 15 m/s), sea spray causes drops that will impact the rain sensor and register as rain, thus there are periods where rain is recorded when there is no rain falling. We have no way of editing this out of the data record so the measured rain rate at these higher wind speeds is unreliable.

Aerosol inlet:
Ambient aerosol particles were sampled at 18 m above sea level through a heated mast. The mast extended 5 m above and forward of the aerosol measurement container. The inlet was a rotating cone-shaped nozzle that was automatically positioned into the relative wind to maintain nominally isokinetic flow and minimize the loss of supermicrometer particles. Air entered the inlet through a 5 cm diameter hole, passed through a 7 degree expansion cone, and then into the 20 cm inner diameter sampling mast. The flow through the mast was 1 m3 min-1. The transmission efficiency of the inlet for particles with aerodynamic diameters less than 6.5 um (the largest size tested) is greater than 95% [Bates et al., 2002].

The bottom 1.5 m of the mast were heated to establish a stable reference relative humidity (RH) for the sample air controlled to the indicated target sample RH. Twenty one 1.6 cm inner diameter stainless steel tubes extending into the heated portion of the mast were connected to downstream aerosol instrumentation with either conductive silicon tubing or stainless steel tubing for analysis of organic aerosol.

CN and UFCN:
One of the twenty one 1.6 cm diameter tubes was used to supply ambient air to TSI 3010 (CN_Direct) and TSI 3025A (UFCN_Direct) particle counters. Another one of tubes was used to supply ambient air to a TSI3785 (UFCN_Chem) particle counter. A separate 1/4" line was used to supply air from the top of the mast directly to a TSI 3760 particle counter. The 3760, 3010, 3025 and 3785 measure all particles larger than roughly 12, 12, 3 and 5 nm respectively. The total particle counts from each instrument were recorded each second. The data were filtered to eliminate periods of calibration and instrument malfunction and zero air periods, and periods of obvious ship contamination (based on relative wind and high CN counts). The "best" filtered values were chosen to represent CN>12 (CN) and ultra-fine (UFCN) particle concentrations. The best CN values are primarily from CN_Direct with data from CN_Stack used to fill in periods where the CN_Direct data were not available. Similarly, the UFCN values are primarily from UFCN_Direct with the UFCN_Chem data used to fill in periods where UFCN_Direct data were not available.
  """,
# #     "atm_naames_lo_rh": """Navigation and Meteorological Measurements

# # Ship Position (Latitude and Longitude):
# # In the one minute files the position is treated somewhat differently from all the other data. The position given is the ship's position at the start of the one minute 'averaging' period. All other data are a true average. The PMEL GPS was the primary source. The Ship's GPS was used when there were missing data in the PMEL record.

# # Ship Speed, Course and Gyro:
# # The ship's GPS speed in knots (Speed Over Ground) and GPS Course in compass degrees (Course Over Ground) are the one minute averages from the GPS (the PMEL GPS as the primary source, the Ship's GPS was the secondary source). To make the one minute averages the 1-second recorded motion vector was separated into east and north components that were averaged into one minute bins. The one minute components were then combined into the ship Velocity Vector. The GyroCompass in compass degrees is the one minute average heading. The primary source was the PMEL GPS compass (Si-TEX Vector Pro), the ship gyro compass data were used when the primary data were missing. The 1-second data were separated into an east and north component before averaging and then recombined. NOTE: The GPS-Course is the direction the ship is moving. The GyroCompass is the direction the ship's bow is pointing. When the ship is moving at 6 or more knots they generally are the same. Due to water currents, at slow speeds there can be quite a difference between the two. When the ship is stationary, the two are totally unrelated.

# # Relative Wind:
# # The primary source for the relative wind data was the PMEL Vaisala WX520 sonic anemometer, located on the aerosol sampling mast. For periods of missing data, the PSD Sonic anemometer on the ship’s foremast was used. The one second relative wind speed and direction data were separated into orthogonal components of "keel" and "beam". These components were averaged into 1 minute averages, and then recombined to relative wind vectors. Wind speed is reported in meters per second and wind direction is in degrees with -90 being wind approaching the ship on the port beam, 0 degrees being wind approaching the ship directly on the bow, and +90 degrees being wind approaching the ship on the starboard beam.

# # Wind Components/ True Wind Speed/ True Wind Direction:
# # The primary source for the true wind data was the average of the PMEL Vaisala WX520 and WX536 sonic anemometers, both located on the aerosol sampling mast, 17 m above sea level.   For periods of missing data the average of the ship’s two WXT sensors, located above the ship’s navigation bridge,  were used.  True wind speed and direction were calculated from the relative wind taking into account the ship's motion from the GPS and the ship heading from the GPS compass. The true wind vector is given as wind speed in m/s and wind direction in compass degrees (0 degrees meaning wind arriving from the north). The WindU and WindV are the east and north components of the wind vector in m/s.  WindU and WindV are positive for wind going in the east and north directions.

# # Atmospheric Temperature:
# # One minute averages in degrees C. The following data sources were used. The PMEL Vaisala WXT536 and the PMEL Vaisala WXT520 sensor (both on the sampling aerosol mast at 17 m above sea level) and the NOAA PSD sensor on the bow foremast also at 17 meters above the sea surface.  These 3 sensors generally agreed to better than 0.5 deg C. For this project the average of the two PMEL WXT sensors was used. During periods of missing data in the PMEL record the PSD sensor was used.

# # Relative humidity:
# # One minute averages in %. The following data sources were used. The PMEL Vaisala WXT536 and the PMEL Vaisala WXT520 sensor (both on the sampling aerosol mast at 17 m above sea level) and the  NOAA PSD sensor on the bow foremast also at 17 meters above the sea surface.  These 3 sensors generally agreed within 5% in rh.   For this project the average of the two PMEL WXT sensors was used. During periods of missing data in the PMEL record the PSD sensor was used.

# # Barometric Pressure:
# # One minute averages in units of mb. There were two sources of raw data, the PMEL WXT sensors (corrected to sea level) and the NOAA PSD sensor (corrected to sea level).  For this project the average of the sea level corrected PMEL WXT sensors was used.  Missing data were filled in with the PSD sea level corrected pressure.

# # Insolation:
# # One minute averages in units of watts per square meter. Total solar radiation was measured with an Epply black and white pyranometer (horizontal surface receiver -180, model 8-48, serial number 12946) and an Epply precision pyranometer (horizontal surface receiver -180, twin hemispheres, model PSP, serial number 133035F3) that were mounted on the top of Areophys van. Both instruments were calibrated by the Epply Laboratory on October 11, 1994. There were times when the sampling mast shaded one or both sensors. There were also times when the ship's mast/bridge shaded the sensors. The shaded data have not been edited out of the 1 minute data record. The data reported here are from the model 8-48, serial number 12946 radiometer and are in watts per square meter and are the average value over the 1 minute sampling period.

# # Rain Rate (Precipitation):
# # The rain rate, in mm/hr, was measured by the PMEL-Vaisala WX520 and WX536 Met sensors located near the top of the aerosol sampling mast.  The average of the two sensors was used.  During periods of high wind speed (above about 15 m/s), sea spray causes drops that will impact the rain sensor and register as rain, thus there are periods where rain is recorded when there is no rain falling. We have no way of editing this out of the data record so the measured rain rate at these higher wind speeds is unreliable.

# # Aerosol inlet:
# # Ambient aerosol particles were sampled at 18 m above sea level through a heated mast. The mast extended 5 m above and forward of the aerosol measurement container. The inlet was a rotating cone-shaped nozzle that was automatically positioned into the relative wind to maintain nominally isokinetic flow and minimize the loss of supermicrometer particles. Air entered the inlet through a 5 cm diameter hole, passed through a 7 degree expansion cone, and then into the 20 cm inner diameter sampling mast. The flow through the mast was 1 m3 min-1. The transmission efficiency of the inlet for particles with aerodynamic diameters less than 6.5 um (the largest size tested) is greater than 95% [Bates et al., 2002].

# # The bottom 1.5 m of the mast were heated to establish a stable reference relative humidity (RH) for the sample air of in the controlled range of 25 to 35 %RH. Twenty one 1.6 cm inner diameter stainless steel tubes extending into the heated portion of the mast were connected to downstream aerosol instrumentation with either conductive silicon tubing or stainless steel tubing for analysis of organic aerosol.

# # CN and UFCN:
# # One of the twenty one 1.6 cm diameter tubes was used to supply ambient air to TSI 3010 (CN_Direct), a Brechtel aMCPC (CN_Stack) and TSI 3025A (UFCN_Direct) particle counters. Another one of the tubes was used to supply ambient air to TSI3785 (UFCN_Chem)  and Aerosol Devices MAGIC210 (CN_MART) particle counters. The 3010, aMCPC, 3025, 3785 and MAGIC210 measure all particles larger than roughly 12, 5, 3, 5 and 5 nm respectively. The total particle counts from each instrument were recorded each second. The data were filtered to eliminate periods of calibration and instrument malfunction and zero air periods, and periods of obvious ship contamination from the R/V Brown (based on relative wind and high CN counts). The "best" filtered values were chosen to represent CN>12 (CN) and ultra-fine (UFCN) particle concentrations. The best CN values are primarily from CN_Direct with data from CN_Stack used to fill in periods where the CN_Direct data were not available. Similarly, the UFCN values are primarily from UFCN_Direct with the UFCN_Chem and CN_MART data used to fill in periods where UFCN_Direct data were not available. These "best" data were averaged into one minute periods. One second data are available upon request.
# #   """,
# #     "atm_naames2": """Navigation and Meteorological Measurements

# # Ship Position (Latitude and Longitude):
# # In the one minute files the position is treated somewhat differently from all the other data. The position given is the ship's position at the start of the one minute 'averaging' period. All other data are a true average. The PMEL GPS was the primary source. The Ship's GPS was used when there were missing data in the PMEL record.

# # Ship Speed, Course and Gyro:
# # The ship's GPS speed in knots (Speed Over Ground) and GPS Course in compass degrees (Course Over Ground) are the one minute averages from the GPS (the PMEL GPS as the primary source, the Ship's GPS was the secondary source). To make the one minute averages the 1-second recorded motion vector was separated into east and north components that were averaged into one minute bins. The one minute components were then combined into the ship Velocity Vector. The GyroCompass in compass degrees is the one minute average heading. The primary source was the PMEL GPS compass (Si-TEX Vector Pro), the ship gyro compass data were used when the primary data were missing. The 1-second data were separated into an east and north component before averaging and then recombined. NOTE: The GPS-Course is the direction the ship is moving. The GyroCompass is the direction the ship's bow is pointing. When the ship is moving at 6 or more knots they generally are the same. Due to water currents, at slow speeds there can be quite a difference between the two. When the ship is stationary, the two are totally unrelated.

# # Relative Wind:
# # The primary source for the relative wind data was the PMEL Vaisala WX520 sonic anemometer, located on the aerosol sampling mast. For periods of missing data, the PSD Sonic anemometer on the ship’s foremast was used. The one second relative wind speed and direction data were separated into orthogonal components of "keel" and "beam". These components were averaged into 1 minute averages, and then recombined to relative wind vectors. Wind speed is reported in meters per second and wind direction is in degrees with -90 being wind approaching the ship on the port beam, 0 degrees being wind approaching the ship directly on the bow, and +90 degrees being wind approaching the ship on the starboard beam.

# # Wind Components/ True Wind Speed/ True Wind Direction:
# # The primary source for the true wind data was the average of the PMEL Vaisala WX520 and WX536 sonic anemometers, both located on the aerosol sampling mast, 17 m above sea level.   For periods of missing data the average of the ship’s two WXT sensors, located above the ship’s navigation bridge,  were used.  True wind speed and direction were calculated from the relative wind taking into account the ship's motion from the GPS and the ship heading from the GPS compass. The true wind vector is given as wind speed in m/s and wind direction in compass degrees (0 degrees meaning wind arriving from the north). The WindU and WindV are the east and north components of the wind vector in m/s.  WindU and WindV are positive for wind going in the east and north directions.

# # Atmospheric Temperature:
# # One minute averages in degrees C. The following data sources were used. The PMEL Vaisala WXT536 and the PMEL Vaisala WXT520 sensor (both on the sampling aerosol mast at 17 m above sea level) and the NOAA PSD sensor on the bow foremast also at 17 meters above the sea surface.  These 3 sensors generally agreed to better than 0.5 deg C. For this project the average of the two PMEL WXT sensors was used. During periods of missing data in the PMEL record the PSD sensor was used.

# # Relative humidity:
# # One minute averages in %. The following data sources were used. The PMEL Vaisala WXT536 and the PMEL Vaisala WXT520 sensor (both on the sampling aerosol mast at 17 m above sea level) and the  NOAA PSD sensor on the bow foremast also at 17 meters above the sea surface.  These 3 sensors generally agreed within 5% in rh.   For this project the average of the two PMEL WXT sensors was used. During periods of missing data in the PMEL record the PSD sensor was used.

# # Barometric Pressure:
# # One minute averages in units of mb. There were two sources of raw data, the PMEL WXT sensors (corrected to sea level) and the NOAA PSD sensor (corrected to sea level).  For this project the average of the sea level corrected PMEL WXT sensors was used.  Missing data were filled in with the PSD sea level corrected pressure.

# # Insolation:
# # One minute averages in units of watts per square meter. Total solar radiation was measured with an Epply black and white pyranometer (horizontal surface receiver -180, model 8-48, serial number 12946) and an Epply precision pyranometer (horizontal surface receiver -180, twin hemispheres, model PSP, serial number 133035F3) that were mounted on the top of Areophys van. Both instruments were calibrated by the Epply Laboratory on October 11, 1994. There were times when the sampling mast shaded one or both sensors. There were also times when the ship's mast/bridge shaded the sensors. The shaded data have not been edited out of the 1 minute data record. The data reported here are from the model 8-48, serial number 12946 radiometer and are in watts per square meter and are the average value over the 1 minute sampling period.

# # Rain Rate (Precipitation):
# # The rain rate, in mm/hr, was measured by the PMEL-Vaisala WX520 and WX536 Met sensors located near the top of the aerosol sampling mast.  The average of the two sensors was used.  During periods of high wind speed (above about 15 m/s), sea spray causes drops that will impact the rain sensor and register as rain, thus there are periods where rain is recorded when there is no rain falling. We have no way of editing this out of the data record so the measured rain rate at these higher wind speeds is unreliable.

# # Aerosol inlet:
# # Ambient aerosol particles were sampled at 18 m above sea level through a heated mast. The mast extended 5 m above and forward of the aerosol measurement container. The inlet was a rotating cone-shaped nozzle that was automatically positioned into the relative wind to maintain nominally isokinetic flow and minimize the loss of supermicrometer particles. Air entered the inlet through a 5 cm diameter hole, passed through a 7 degree expansion cone, and then into the 20 cm inner diameter sampling mast. The flow through the mast was 1 m3 min-1. The transmission efficiency of the inlet for particles with aerodynamic diameters less than 6.5 um (the largest size tested) is greater than 95% [Bates et al., 2002].

# # The bottom 1.5 m of the mast were heated to establish a stable reference relative humidity (RH) for the sample air of in the controlled range of 45 to 55 %RH. Twenty one 1.6 cm inner diameter stainless steel tubes extending into the heated portion of the mast were connected to downstream aerosol instrumentation with either conductive silicon tubing or stainless steel tubing for analysis of organic aerosol.

# # CN and UFCN:
# # One of the twenty one 1.6 cm diameter tubes was used to supply ambient air to TSI 3010 (CN_Direct), a Brechtel aMCPC (CN_Stack) and TSI 3025A (UFCN_Direct) particle counters. Another one of the tubes was used to supply ambient air to TSI3785 (UFCN_Chem)  and Aerosol Devices MAGIC210 (CN_MART) particle counters. The 3010, aMCPC, 3025, 3785 and MAGIC210 measure all particles larger than roughly 12, 5, 3, 5 and 5 nm respectively. The total particle counts from each instrument were recorded each second. The data were filtered to eliminate periods of calibration and instrument malfunction and zero air periods, and periods of obvious ship contamination from the R/V Brown (based on relative wind and high CN counts). The "best" filtered values were chosen to represent CN>12 (CN) and ultra-fine (UFCN) particle concentrations. The best CN values are primarily from CN_Direct with data from CN_Stack used to fill in periods where the CN_Direct data were not available. Similarly, the UFCN values are primarily from UFCN_Direct with the UFCN_Chem and CN_MART data used to fill in periods where UFCN_Direct data were not available. These "best" data were averaged into one minute periods. One second data are available upon request.
# #   """,
# #     "atm_naames1": """Navigation and Meteorological Measurements

# # Ship Position (Latitude and Longitude):
# # In the one minute files the position is treated somewhat differently from all the other data. The position given is the ship's position at the start of the one minute 'averaging' period. All other data are a true average. The PMEL GPS was the primary source. The Ship's GPS was used when there were missing data in the PMEL record.

# # Ship Speed, Course and Gyro:
# # The ship's GPS speed in knots (Speed Over Ground) and GPS Course in compass degrees (Course Over Ground) are the one minute averages from the GPS (the PMEL GPS as the primary source, the Ship's GPS was the secondary source). To make the one minute averages the 1-second recorded motion vector was separated into east and north components that were averaged into one minute bins. The one minute components were then combined into the ship Velocity Vector. The GyroCompass in compass degrees is the one minute average heading. The primary source was the PMEL GPS compass (Si-TEX Vector Pro), the ship gyro compass data were used when the primary data were missing. The 1-second data were separated into an east and north component before averaging and then recombined. NOTE: The GPS-Course is the direction the ship is moving. The GyroCompass is the direction the ship's bow is pointing. When the ship is moving at 6 or more knots they generally are the same. Due to water currents, at slow speeds there can be quite a difference between the two. When the ship is stationary, the two are totally unrelated.

# # Relative Wind:
# # The primary source for the relative wind data was the PMEL Vaisala WX520 sonic anemometer, located on the aerosol sampling mast. For periods of missing data, the PSD Sonic anemometer on the ship’s foremast was used. The one second relative wind speed and direction data were separated into orthogonal components of "keel" and "beam". These components were averaged into 1 minute averages, and then recombined to relative wind vectors. Wind speed is reported in meters per second and wind direction is in degrees with -90 being wind approaching the ship on the port beam, 0 degrees being wind approaching the ship directly on the bow, and +90 degrees being wind approaching the ship on the starboard beam.

# # Wind Components/ True Wind Speed/ True Wind Direction:
# # The primary source for the true wind data was the average of the PMEL Vaisala WX520 and WX536 sonic anemometers, both located on the aerosol sampling mast, 17 m above sea level.   For periods of missing data the average of the ship’s two WXT sensors, located above the ship’s navigation bridge,  were used.  True wind speed and direction were calculated from the relative wind taking into account the ship's motion from the GPS and the ship heading from the GPS compass. The true wind vector is given as wind speed in m/s and wind direction in compass degrees (0 degrees meaning wind arriving from the north). The WindU and WindV are the east and north components of the wind vector in m/s.  WindU and WindV are positive for wind going in the east and north directions.

# # Atmospheric Temperature:
# # One minute averages in degrees C. The following data sources were used. The PMEL Vaisala WXT536 and the PMEL Vaisala WXT520 sensor (both on the sampling aerosol mast at 17 m above sea level) and the NOAA PSD sensor on the bow foremast also at 17 meters above the sea surface.  These 3 sensors generally agreed to better than 0.5 deg C. For this project the average of the two PMEL WXT sensors was used. During periods of missing data in the PMEL record the PSD sensor was used.

# # Relative humidity:
# # One minute averages in %. The following data sources were used. The PMEL Vaisala WXT536 and the PMEL Vaisala WXT520 sensor (both on the sampling aerosol mast at 17 m above sea level) and the  NOAA PSD sensor on the bow foremast also at 17 meters above the sea surface.  These 3 sensors generally agreed within 5% in rh.   For this project the average of the two PMEL WXT sensors was used. During periods of missing data in the PMEL record the PSD sensor was used.

# # Barometric Pressure:
# # One minute averages in units of mb. There were two sources of raw data, the PMEL WXT sensors (corrected to sea level) and the NOAA PSD sensor (corrected to sea level).  For this project the average of the sea level corrected PMEL WXT sensors was used.  Missing data were filled in with the PSD sea level corrected pressure.

# # Insolation:
# # One minute averages in units of watts per square meter. Total solar radiation was measured with an Epply black and white pyranometer (horizontal surface receiver -180, model 8-48, serial number 12946) and an Epply precision pyranometer (horizontal surface receiver -180, twin hemispheres, model PSP, serial number 133035F3) that were mounted on the top of Areophys van. Both instruments were calibrated by the Epply Laboratory on October 11, 1994. There were times when the sampling mast shaded one or both sensors. There were also times when the ship's mast/bridge shaded the sensors. The shaded data have not been edited out of the 1 minute data record. The data reported here are from the model 8-48, serial number 12946 radiometer and are in watts per square meter and are the average value over the 1 minute sampling period.

# # Rain Rate (Precipitation):
# # The rain rate, in mm/hr, was measured by the PMEL-Vaisala WX520 and WX536 Met sensors located near the top of the aerosol sampling mast.  The average of the two sensors was used.  During periods of high wind speed (above about 15 m/s), sea spray causes drops that will impact the rain sensor and register as rain, thus there are periods where rain is recorded when there is no rain falling. We have no way of editing this out of the data record so the measured rain rate at these higher wind speeds is unreliable.

# # Aerosol inlet:
# # Ambient aerosol particles were sampled at 18 m above sea level through a heated mast. The mast extended 5 m above and forward of the aerosol measurement container. The inlet was a rotating cone-shaped nozzle that was automatically positioned into the relative wind to maintain nominally isokinetic flow and minimize the loss of supermicrometer particles. Air entered the inlet through a 5 cm diameter hole, passed through a 7 degree expansion cone, and then into the 20 cm inner diameter sampling mast. The flow through the mast was 1 m3 min-1. The transmission efficiency of the inlet for particles with aerodynamic diameters less than 6.5 um (the largest size tested) is greater than 95% [Bates et al., 2002].

# # The bottom 1.5 m of the mast were heated to establish a stable reference relative humidity (RH) for the sample air.  In the northern section of the cruise the temperature constraints of the control system were such that up until 18-Nov. the mesurements were made at 20 to 50 %RH.  After 18-Nov. the mesurements were made in the controlled range of 55 to 65 %RH. Twenty one 1.6 cm inner diameter stainless steel tubes extending into the heated portion of the mast were connected to downstream aerosol instrumentation with either conductive silicon tubing or stainless steel tubing for analysis of organic aerosol.

# # CN and UFCN:
# # One of the twenty one 1.6 cm diameter tubes was used to supply ambient air to TSI 3010 (CN_Direct), a Brechtel aMCPC (CN_Stack) and TSI 3025A (UFCN_Direct) particle counters. Another one of the tubes was used to supply ambient air to TSI3785 (UFCN_Chem)  and Aerosol Devices MAGIC210 (CN_MART) particle counters. The 3010, aMCPC, 3025, 3785 and MAGIC210 measure all particles larger than roughly 12, 5, 3, 5 and 5 nm respectively. The total particle counts from each instrument were recorded each second. The data were filtered to eliminate periods of calibration and instrument malfunction and zero air periods, and periods of obvious ship contamination from the R/V Brown (based on relative wind and high CN counts). The "best" filtered values were chosen to represent CN>12 (CN) and ultra-fine (UFCN) particle concentrations. The best CN values are primarily from CN_Direct with data from CN_Stack used to fill in periods where the CN_Direct data were not available. Similarly, the UFCN values are primarily from UFCN_Direct with the UFCN_Chem and CN_MART data used to fill in periods where UFCN_Direct data were not available. These "best" data were averaged into one minute periods. One second data are available upon request.
# #   """,
#     "atm_wacs2014": """Navigation and Meteorological Measurements

# Ship Position (Latitude and Longitude):
# In the one minute files the position is treated somewhat differently from all the other data. The position given is the ship's position at the start of the one minute 'averaging' period. All other data are a true average. The PMEL GPS was the primary source. The Ship's GPS was used when there were missing data in the PMEL record.

# Ship Speed, Course and Gyro:
# The ship's GPS speed in knots (Speed Over Ground) and GPS Course in compass degrees (Course Over Ground) are the one minute averages from the GPS (the PMEL GPS as the primary source, the Ship's GPS was the secondary source). To make the one minute averages the 1-second recorded motion vector was separated into east and north components that were averaged into one minute bins. The one minute components were then combined into the ship Velocity Vector. The GyroCompass in compass degrees is the one minute average heading. The primary source was the PMEL GPS compass (Si-TEX Vector Pro), the ship gyro compass data were used when the primary data were missing. The 1-second data were separated into an east and north component before averaging and then recombined. NOTE: The GPS-Course is the direction the ship is moving. The GyroCompass is the direction the ship's bow is pointing. When the ship is moving at 6 or more knots they generally are the same. Due to water currents, at slow speeds there can be quite a difference between the two. When the ship is stationary, the two are totally unrelated.

# Relative Wind:
# The primary source for the relative wind data was the PMEL Vaisala WX520 sonic anemometer, located on the aerosol sampling mast. For periods of missing data, the PSD Sonic anemometer on the ship’s foremast was used. The one second relative wind speed and direction data were separated into orthogonal components of "keel" and "beam". These components were averaged into 1 minute averages, and then recombined to relative wind vectors. Wind speed is reported in meters per second and wind direction is in degrees with -90 being wind approaching the ship on the port beam, 0 degrees being wind approaching the ship directly on the bow, and +90 degrees being wind approaching the ship on the starboard beam.

# Wind Components/ True Wind Speed/ True Wind Direction:
# The primary source for the true wind data was the average of the PMEL Vaisala WX520 and WX536 sonic anemometers, both located on the aerosol sampling mast, 17 m above sea level.   For periods of missing data the average of the ship’s two WXT sensors, located above the ship’s navigation bridge,  were used.  True wind speed and direction were calculated from the relative wind taking into account the ship's motion from the GPS and the ship heading from the GPS compass. The true wind vector is given as wind speed in m/s and wind direction in compass degrees (0 degrees meaning wind arriving from the north). The WindU and WindV are the east and north components of the wind vector in m/s.  WindU and WindV are positive for wind going in the east and north directions.

# Atmospheric Temperature:
# One minute averages in degrees C. The following data sources were used. The PMEL Vaisala WXT536 and the PMEL Vaisala WXT520 sensor (both on the sampling aerosol mast at 17 m above sea level) and the NOAA PSD sensor on the bow foremast also at 17 meters above the sea surface.  These 3 sensors generally agreed to better than 0.5 deg C. For this project the average of the two PMEL WXT sensors was used. During periods of missing data in the PMEL record the PSD sensor was used.

# Relative humidity:
# One minute averages in %. The following data sources were used. The PMEL Vaisala WXT536 and the PMEL Vaisala WXT520 sensor (both on the sampling aerosol mast at 17 m above sea level) and the  NOAA PSD sensor on the bow foremast also at 17 meters above the sea surface.  These 3 sensors generally agreed within 5% in rh.   For this project the average of the two PMEL WXT sensors was used. During periods of missing data in the PMEL record the PSD sensor was used.

# Barometric Pressure:
# One minute averages in units of mb. There were two sources of raw data, the PMEL WXT sensors (corrected to sea level) and the NOAA PSD sensor (corrected to sea level).  For this project the average of the sea level corrected PMEL WXT sensors was used.  Missing data were filled in with the PSD sea level corrected pressure.

# Insolation:
# One minute averages in units of watts per square meter. Total solar radiation was measured with an Epply black and white pyranometer (horizontal surface receiver -180, model 8-48, serial number 12946) and an Epply precision pyranometer (horizontal surface receiver -180, twin hemispheres, model PSP, serial number 133035F3) that were mounted on the top of Areophys van. Both instruments were calibrated by the Epply Laboratory on October 11, 1994. There were times when the sampling mast shaded one or both sensors. There were also times when the ship's mast/bridge shaded the sensors. The shaded data have not been edited out of the 1 minute data record. The data reported here are from the model 8-48, serial number 12946 radiometer and are in watts per square meter and are the average value over the 1 minute sampling period.

# Rain Rate (Precipitation):
# The rain rate, in mm/hr, was measured by the PMEL-Vaisala WX520 and WX536 Met sensors located near the top of the aerosol sampling mast.  The average of the two sensors was used.  During periods of high wind speed (above about 15 m/s), sea spray causes drops that will impact the rain sensor and register as rain, thus there are periods where rain is recorded when there is no rain falling. We have no way of editing this out of the data record so the measured rain rate at these higher wind speeds is unreliable.

# Aerosol inlet:
# Ambient aerosol particles were sampled at 18 m above sea level through a heated mast. The mast extended 5 m above and forward of the aerosol measurement container. The inlet was a rotating cone-shaped nozzle that was automatically positioned into the relative wind to maintain nominally isokinetic flow and minimize the loss of supermicrometer particles. Air entered the inlet through a 5 cm diameter hole, passed through a 7 degree expansion cone, and then into the 20 cm inner diameter sampling mast. The flow through the mast was 1 m3 min-1. The transmission efficiency of the inlet for particles with aerodynamic diameters less than 6.5 um (the largest size tested) is greater than 95% [Bates et al., 2002].

# The bottom 1.5 m of the mast were heated to establish a stable reference relative humidity (RH) for the sample air of 51 ± 4%. Twenty one 1.6 cm inner diameter stainless steel tubes extending into the heated portion of the mast were connected to downstream aerosol instrumentation with either conductive silicon tubing or stainless steel tubing for analysis of organic aerosol.

# CN and UFCN:
# One of the twenty one 1.6 cm diameter tubes was used to supply ambient air to TSI 3010 (CN_Direct), a Brechtel aMCPC (CN_Stack) and TSI 3025A (UFCN_Direct) particle counters. Another one of the tubes was used to supply ambient air to TSI3785 (UFCN_Chem)  and Aerosol Devices MAGIC210 (CN_MART) particle counters. The 3010, aMCPC, 3025, 3785 and MAGIC210 measure all particles larger than roughly 12, 5, 3, 5 and 5 nm respectively. The total particle counts from each instrument were recorded each second. The data were filtered to eliminate periods of calibration and instrument malfunction and zero air periods, and periods of obvious ship contamination from the R/V Brown (based on relative wind and high CN counts). The "best" filtered values were chosen to represent CN>12 (CN) and ultra-fine (UFCN) particle concentrations. The best CN values are primarily from CN_Direct with data from CN_Stack used to fill in periods where the CN_Direct data were not available. Similarly, the UFCN values are primarily from UFCN_Direct with the UFCN_Chem and CN_MART data used to fill in periods where UFCN_Direct data were not available. These "best" data were averaged into one minute periods. One second data are available upon request.
#   """,
    "atm_pre_calnex": """Navigation and Meteorological Measurements

Ship Position (Latitude and Longitude):
In the one minute files the position is treated somewhat differently from all the other data. The position given is the ship's position at the start of the one minute 'averaging' period. All other data are a true average. The PMEL GPS was the primary source. The Ship's GPS was used when there were missing data in the PMEL record.

Ship Speed, Course and Gyro:
The ship's GPS speed in knots (Speed Over Ground) and GPS Course in compass degrees (Course Over Ground) are the one minute averages from the GPS (the PMEL GPS as the primary source, the Ship's GPS was the secondary source). To make the one minute averages the 1-second recorded motion vector was separated into east and north components that were averaged into one minute bins. The one minute components were then combined into the ship Velocity Vector. The GyroCompass in compass degrees is the one minute average heading. The primary source was the PMEL GPS compass (Si-TEX Vector Pro), the ship gyro compass data were used when the primary data were missing. The 1-second data were separated into an east and north component before averaging and then recombined. NOTE: The GPS-Course is the direction the ship is moving. The GyroCompass is the direction the ship's bow is pointing. When the ship is moving at 6 or more knots they generally are the same. Due to water currents, at slow speeds there can be quite a difference between the two. When the ship is stationary, the two are totally unrelated.

Relative Wind:
The primary source for the relative wind data was the PMEL Vaisala WX520 sonic anemometer, located on the aerosol sampling mast. For periods of missing data, the PSD Sonic anemometer on the ship’s foremast was used. The one second relative wind speed and direction data were separated into orthogonal components of "keel" and "beam". These components were averaged into 1 minute averages, and then recombined to relative wind vectors. Wind speed is reported in meters per second and wind direction is in degrees with -90 being wind approaching the ship on the port beam, 0 degrees being wind approaching the ship directly on the bow, and +90 degrees being wind approaching the ship on the starboard beam.

Wind Components/ True Wind Speed/ True Wind Direction:
The primary source for the true wind data was the average of the PMEL Vaisala WX520 and WX536 sonic anemometers, both located on the aerosol sampling mast, 17 m above sea level.   For periods of missing data the average of the ship’s two WXT sensors, located above the ship’s navigation bridge,  were used.  True wind speed and direction were calculated from the relative wind taking into account the ship's motion from the GPS and the ship heading from the GPS compass. The true wind vector is given as wind speed in m/s and wind direction in compass degrees (0 degrees meaning wind arriving from the north). The WindU and WindV are the east and north components of the wind vector in m/s.  WindU and WindV are positive for wind going in the east and north directions.

Atmospheric Temperature
One minute averages in degrees C. There were three possible sources, the 2 PMEL rotronics sensors (T1 and T2) and the ship's SCS IMET sensor.  The ship's IMET sensor was located on the IMET mast at the bow of the ship, the PMEL sensors were located at the top of the Aero-phys van.  The IMET sensor being located at the bow had less warming from the daytime heating of the ship deck, (and the data record did show that IMET was cooler than T1 and T2 during the afternoon, when deck heating was a max).    Therefore, the SCS IMET sensor was used as the primary source and for the few times that data were missing from SCS, the PMEL-T1 sensor was used.

Relative humidity:
There were two PMEL rotronics sensors (RH1, and RH2) and one Ship IMET sensor (on the IMET Bow mast).   Due to the daytime deck heating (see air temperatue above) the PMEL sensors showed a "dip" in RH during the afternoon, while the Ship IMET sensor did not.  Thus, the Ship IMET sensor was used as the primary sensor and the PMEL RH1 sensor was used as the secondary sensor

Barometric Pressure:
One minute averages in units of mb.  There were two sources of raw data, the PMEL Vaisala sensor and the SCS digital sensor.  They both agreed within 0.5 mb.  There were less data gaps in the ship SCS sensor it was used as the primary sensor with a few periods filled in with the PMEL sensor.

Insolation:
One minute averages in units of watts per square meter. Total solar radiation was measured with an Epply black and white pyranometer (horizontal surface receiver -180, model 8-48, serial number 12946) and an Epply precision pyranometer (horizontal surface receiver -180, twin hemispheres, model PSP, serial number 133035F3) that were mounted on the top of Areophys van. Both instruments were calibrated by the Epply Laboratory on October 11, 1994. There were times when the sampling mast shaded one or both sensors. There were also times when the ship's mast/bridge shaded the sensors. The shaded data have not been edited out of the 1 minute data record. The data reported here are from the model 8-48, serial number 12946 radiometer and are in watts per square meter and are the average value over the 1 minute sampling period.

Rain Rate (Precipitation):
The rain rate, in mm/hr, was measured by the PMEL-Vaisala WX520 and WX536 Met sensors located near the top of the aerosol sampling mast.  The average of the two sensors was used.  During periods of high wind speed (above about 15 m/s), sea spray causes drops that will impact the rain sensor and register as rain, thus there are periods where rain is recorded when there is no rain falling. We have no way of editing this out of the data record so the measured rain rate at these higher wind speeds is unreliable.

Aerosol inlet:
Ambient aerosol particles were sampled at 18 m above sea level through a heated mast. The mast extended 5 m above and forward of the aerosol measurement container. The inlet was a rotating cone-shaped nozzle that was automatically positioned into the relative wind to maintain nominally isokinetic flow and minimize the loss of supermicrometer particles. Air entered the inlet through a 5 cm diameter hole, passed through a 7 degree expansion cone, and then into the 20 cm inner diameter sampling mast. The flow through the mast was 1 m3 min-1. The transmission efficiency of the inlet for particles with aerodynamic diameters less than 6.5 um (the largest size tested) is greater than 95% [Bates et al., 2002].

The bottom 1.5 m of the mast were heated to establish a stable reference relative humidity (RH) for the sample air controlled to the indicated target sample RH. Twenty one 1.6 cm inner diameter stainless steel tubes extending into the heated portion of the mast were connected to downstream aerosol instrumentation with either conductive silicon tubing or stainless steel tubing for analysis of organic aerosol.

CN and UFCN:
One of the twenty one 1.6 cm diameter tubes was used to supply ambient air to TSI 3010 (CN_Direct) and TSI 3025A (UFCN_Direct) particle counters. Another one of tubes was used to supply ambient air to a TSI3785 (UFCN_Chem) particle counter. A separate 1/4" line was used to supply air from the top of the mast directly to a TSI 3760 particle counter. The 3760, 3010, 3025 and 3785 measure all particles larger than roughly 12, 12, 3 and 5 nm respectively. The total particle counts from each instrument were recorded each second. The data were filtered to eliminate periods of calibration and instrument malfunction and zero air periods, and periods of obvious ship contamination (based on relative wind and high CN counts). The "best" filtered values were chosen to represent CN>12 (CN) and ultra-fine (UFCN) particle concentrations. The best CN values are primarily from CN_Direct with data from CN_Stack used to fill in periods where the CN_Direct data were not available. Similarly, the UFCN values are primarily from UFCN_Direct with the UFCN_Chem data used to fill in periods where UFCN_Direct data were not available.
  """,
#     "atm_icealot": """Navigation and Meteorological Measurements

# Ship Position (Latitude and Longitude):
# In the one minute files the position is treated somewhat differently from all the other data. The position given is the ship's position at the start of the one minute 'averaging' period. All other data are a true average. The PMEL GPS was the primary source. The Ship's GPS was used when there were missing data in the PMEL record.

# Ship Speed, Course and Gyro:
# The ship's GPS speed in knots (Speed Over Ground) and GPS Course in compass degrees (Course Over Ground) are the one minute averages from the GPS (the PMEL GPS as the primary source, the Ship's GPS was the secondary source). To make the one minute averages the 1-second recorded motion vector was separated into east and north components that were averaged into one minute bins. The one minute components were then combined into the ship Velocity Vector. The GyroCompass in compass degrees is the one minute average heading. The primary source was the PMEL GPS compass (Si-TEX Vector Pro), the ship gyro compass data were used when the primary data were missing. The 1-second data were separated into an east and north component before averaging and then recombined. NOTE: The GPS-Course is the direction the ship is moving. The GyroCompass is the direction the ship's bow is pointing. When the ship is moving at 6 or more knots they generally are the same. Due to water currents, at slow speeds there can be quite a difference between the two. When the ship is stationary, the two are totally unrelated.

# Relative Wind:
# The primary source for the relative wind data was the PMEL Vaisala WX520 sonic anemometer, located on the aerosol sampling mast. For periods of missing data, the PSD Sonic anemometer on the ship’s foremast was used. The one second relative wind speed and direction data were separated into orthogonal components of "keel" and "beam". These components were averaged into 1 minute averages, and then recombined to relative wind vectors. Wind speed is reported in meters per second and wind direction is in degrees with -90 being wind approaching the ship on the port beam, 0 degrees being wind approaching the ship directly on the bow, and +90 degrees being wind approaching the ship on the starboard beam.

# Wind Components/ True Wind Speed/ True Wind Direction:
# The primary source for the true wind data was the average of the PMEL Vaisala WX520 and WX536 sonic anemometers, both located on the aerosol sampling mast, 17 m above sea level.   For periods of missing data the average of the ship’s two WXT sensors, located above the ship’s navigation bridge,  were used.  True wind speed and direction were calculated from the relative wind taking into account the ship's motion from the GPS and the ship heading from the GPS compass. The true wind vector is given as wind speed in m/s and wind direction in compass degrees (0 degrees meaning wind arriving from the north). The WindU and WindV are the east and north components of the wind vector in m/s.  WindU and WindV are positive for wind going in the east and north directions.

# Atmospheric Temperature
# One minute averages in degrees C. There were three possible sources, the 2 PMEL rotronics sensors (T1 and T2) and the ship's SCS IMET sensor.  The ship's IMET sensor was located on the IMET mast at the bow of the ship, the PMEL sensors were located at the top of the Aero-phys van.  The IMET sensor being located at the bow had less warming from the daytime heating of the ship deck, (and the data record did show that IMET was cooler than T1 and T2 during the afternoon, when deck heating was a max).    Therefore, the SCS IMET sensor was used as the primary source and for the few times that data were missing from SCS, the PMEL-T1 sensor was used.

# Relative humidity:
# There were two PMEL rotronics sensors (RH1, and RH2) and one Ship IMET sensor (on the IMET Bow mast).   Due to the daytime deck heating (see air temperatue above) the PMEL sensors showed a "dip" in RH during the afternoon, while the Ship IMET sensor did not.  Thus, the Ship IMET sensor was used as the primary sensor and the PMEL RH1 sensor was used as the secondary sensor

# Barometric Pressure:
# One minute averages in units of mb.  There were two sources of raw data, the PMEL Vaisala sensor and the SCS digital sensor.  They both agreed within 0.5 mb.  There were less data gaps in the ship SCS sensor it was used as the primary sensor with a few periods filled in with the PMEL sensor.

# Insolation:
# One minute averages in units of watts per square meter. Total solar radiation was measured with an Epply black and white pyranometer (horizontal surface receiver -180, model 8-48, serial number 12946) and an Epply precision pyranometer (horizontal surface receiver -180, twin hemispheres, model PSP, serial number 133035F3) that were mounted on the top of Areophys van. Both instruments were calibrated by the Epply Laboratory on October 11, 1994. There were times when the sampling mast shaded one or both sensors. There were also times when the ship's mast/bridge shaded the sensors. The shaded data have not been edited out of the 1 minute data record. The data reported here are from the model 8-48, serial number 12946 radiometer and are in watts per square meter and are the average value over the 1 minute sampling period.

# Rain Rate (Precipitation):
# The rain rate, in mm/hr, was measured by the PMEL-Vaisala WX520 and WX536 Met sensors located near the top of the aerosol sampling mast.  The average of the two sensors was used.  During periods of high wind speed (above about 15 m/s), sea spray causes drops that will impact the rain sensor and register as rain, thus there are periods where rain is recorded when there is no rain falling. We have no way of editing this out of the data record so the measured rain rate at these higher wind speeds is unreliable.

# PMEL/UW CN and UFCN:
# Aerosol particles were sampled at 18 m above sea level through a heated mast. The mast extended 5 m above and forward of the aerosol measurement container. The inlet was a rotating cone-shaped nozzle that was automatically positioned into the relative wind. Air was pulled through this 5 cm diameter inlet nozzle at 1 m3 min-1 and down the 20 cm inner diameter mast. The lowest 1.5 m of the mast was heated to dry the aerosol to a relative humidity (RH) of 25% or less. Twenty one 1.6 cm inner diameter conductive tubes extending into this heated zone were used to subsample the main air flow for the various aerosol instruments at flows of 30 l min-1.

# One of the twenty one 1.6 cm diameter tubes was used to supply ambient air to TSI 3010 and TSI 3025A particle counters. Another one of tubes was used to supply ambient air to a TSI3785 particle counter. A separate 1/4” line was used to supply air from the top of the mast directly to a TSI 3760 particle counter. The 3760, 3010, 3025 and 3785 measure all particles larger than roughly 13, 12, 3 and 5 nm respectively. The counts from the three detectors are referred to here as CN>13 (TSI3760), CN>12 (TSI3010), CN>3 (TSI3025) and CN>5 (TSI3785). The total particle counts from each instrument were recorded each second. The data were filtered to eliminate periods of calibration and instrument malfunction and periods of ship contamination (based on relative wind and high CN counts). The “best” filtered values were chosen to represent CN>13 and ultra-fine (UFCN) particle concentrations. The best CN>13 values primarily include data from CN>12 and the data from CN>13 were used to fill in periods where the CN>12 were not available. Similarly, the UFCN values primarily include data from CN>5 and the CN>3 data were used to fill in periods where CN>5 were not available. These "best" data were averaged into one minute periods. One second data are available upon request. 
#   """,
    "gas_chemistry_ozone": """Ozone
Air was pulled from 16 m above sea level through a 1/4 inch teflon line at approximately 1 liter min-1 into a Thermo Environmental Instruments Model 49c ozone analyzer. The air inlet was approximately 2 meters below the aerosol inlet. During periods when the relative wind was behind the beam, there were obvious periods when ship exhaust was reacting with ozone, resulting in sudden spikes of low ozone.  These spikes of low ozone have been edited out.   The data are reported as one minute averages in units of ppb.
  """,
    "gas_chemistry_ozone_so2": """Ozone
Air was pulled from 16 m above sea level through a 1/4 inch teflon line at approximately 1 liter min-1 into a Thermo Environmental Instruments Model 49c ozone analyzer. The air inlet was approximately 2 meters below the aerosol inlet. During periods when the relative wind was behind the beam, there were obvious periods when ship exhaust was reacting with ozone, resulting in sudden spikes of low ozone.  These spikes of low ozone have been edited out.   The data are reported as one minute averages in units of ppb.

PMEL SO2
Inlet and Instrument
Air was pulled from 18 m above sea level down the 20 cm ID powder-coated aluminum aerosol sampling mast (6 m) at approximately 1 m3min-1. At the base of the sampling mast a 2.8 Lmin-1 flow was pulled through a 0.32 cm ID, 1m long Teflon tube, a Millipore Fluoropore filter (1.0-um pore size) housed in a Teflon filter holder, a Perma Pure Inc. Nafion Drier (MD-070, stainless steel, 61 cm long) and then through 2 m of Telfon tubing to the Thermo Environmental Instruments Model 43C Trace Level Pulsed Fluorescence Analyzer. The initial 1 m of tubing, filter and drier we located in the humidity controlled (60%) chamber at the base of the mast. Dry zero air (scrubbed with a charcoal trap) was run through the outside of the Nafion Drier at 2 Lmin-1. Data were recorded in 10 second averages. The data have not been filtered for periods when ship exhaust entered the mast.

Standardization:
Zero air was introduced into the sample line upstream of the Fluoropore filter periodically throughout the cruise to establish a zero baseline. An SO2 standard was generated with a permeation tube held at 40ºC. The flow over the permeation tube, diluted to 4.6 ppb, was introduced into the sample line upstream of the Fluoropore filter periodically throughout the cruise. The limit of detection for 1 min averaged data, defined as 2 times the standard deviation of the signal during the zero periods, was 150 ppt. Data below detection limit are listed as 0and missing data are listed as NaN.  Uncertainties in the concentrations based on the permeation tube weight and dilution flows are <5%.
  """,
    "gas_chemistry_ozone_so2_co": """Ozone
Air was pulled from 16 m above sea level through a 1/4 inch teflon line at approximately 1 liter min-1 into a Thermo Environmental Instruments Model 49c ozone analyzer. The air inlet was approximately 2 meters below the aerosol inlet. During periods when the relative wind was behind the beam, there were obvious periods when ship exhaust was reacting with ozone, resulting in sudden spikes of low ozone.  These spikes of low ozone have been edited out.   The data are reported as one minute averages in units of ppb.

PMEL SO2
Inlet and Instrument
Air was pulled from 18 m above sea level down the 20 cm ID powder-coated aluminum aerosol sampling mast (6 m) at approximately 1 m3min-1. At the base of the sampling mast a 2.8 Lmin-1 flow was pulled through a 0.32 cm ID, 1m long Teflon tube, a Millipore Fluoropore filter (1.0-um pore size) housed in a Teflon filter holder, a Perma Pure Inc. Nafion Drier (MD-070, stainless steel, 61 cm long) and then through 2 m of Telfon tubing to the Thermo Environmental Instruments Model 43C Trace Level Pulsed Fluorescence Analyzer. The initial 1 m of tubing, filter and drier we located in the humidity controlled (60%) chamber at the base of the mast. Dry zero air (scrubbed with a charcoal trap) was run through the outside of the Nafion Drier at 2 Lmin-1. Data were recorded in 10 second averages. The data have not been filtered for periods when ship exhaust entered the mast.

Standardization:
Zero air was introduced into the sample line upstream of the Fluoropore filter periodically throughout the cruise to establish a zero baseline. An SO2 standard was generated with a permeation tube held at 40ºC. The flow over the permeation tube, diluted to 4.6 ppb, was introduced into the sample line upstream of the Fluoropore filter periodically throughout the cruise. The limit of detection for 1 min averaged data, defined as 2 times the standard deviation of the signal during the zero periods, was 150 ppt. Data below detection limit are listed as 0and missing data are listed as NaN.  Uncertainties in the concentrations based on the permeation tube weight and dilution flows are <5%.

Carbon monoxide:
Air was continuously pumped at 5 to 10 L/min through a plastic coated aluminum tubing (Dekoron) sample line that ran from the an inlet at the top of the aerosol sampling mast (18 m above sea level, forward of the ship’s bridge) to the analytical system at the forward end of the ship's main oceanographic laboratory. The analytical system was a PMEL built, automated GC system consisting of a mole sieve 5A chromatographic column and a Trace Analytical reduction gas detector. Every seven minutes a 5 ml sample of air from the sample line, air standard from a gas cylinder, or CO free air from a zero air generator was injected into the system. The air standards were dried, whole-air mixtures contained in aluminum cylinders and were calibrated by NOAA/CMDL. The sampling schedule was such that generally 3 air sample were analyzed per hour. The data presented on this server consist of one hour averages of the all CO measurements during that hour. There were several occasions when the ship was running downwind when it was obvious that ship exhaust was entering the air sample line; these data points were removed before averaging. There was a 2 day data gap during day-of-year 101-102 when the uv lamp in the detector was failing. The detector was fixed by the start of DOY 103.
  """,
    "seawater": """Seawater Measurements
Sea Surface Temperature and Salinity:
Sea Surface Temperature (SST) in degrees C is from the ship’s Hull Probe (SBT38, calibrated on Sep. 17, 2019), Salinity in PSU is from the ship's SeaBird  thermosalinograph (SBE 45, calibrated on Sep. 25, 2019). The temperature probe and water inlet for the thermosalinograph were located 5.3 meters below the water line. The underway chlorophyll data are from the ship’s Seapoint fluorometer, which was calibrated by the factory on Nov. 21, 2019.
    """,
    "seawater_naames1_2": """Seawater Measurements
Sea Surface Temperature and Salinity:
Sea Surface Temperature (SST) in degrees C is from the ship’s Hull Probe (SBT38, calibrated on Sep. 17, 2019), Salinity in PSU is from the ship's SeaBird  thermosalinograph (SBE 45, calibrated on Sep. 25, 2019). The temperature probe and water inlet for the thermosalinograph were located 5.3 meters below the water line. The underway chlorophyll data are from the ship’s Seapoint fluorometer, which was calibrated by the factory on Nov. 21, 2019.
Chlorophyll:
Chlorophyll concentrations were measured from the continuous flow seawater system (inlet 5.3 meters below the water line at the bow of the ship) by Emmanuel Boss of the University of Maine and their data are presented here. Data are given in mg/m-3.
    """,
    "seawater_wacs2014": """Seawater Measurements
Sea Surface Temperature and Salinity:
Sea Surface Temperature (SST) in degrees C is from the ship’s Hull Probe (SBT38, calibrated on Sep. 17, 2019), Salinity in PSU is from the ship's SeaBird  thermosalinograph (SBE 45, calibrated on Sep. 25, 2019). The temperature probe and water inlet for the thermosalinograph were located 5.3 meters below the water line. The underway chlorophyll data are from the ship’s Seapoint fluorometer, which was calibrated by the factory on Nov. 21, 2019.
Chlorophyll:
Chlorophyll concentrations were measured with a continuous flow Turner model 10-AU fluorometer located in the main lab. The inlet for this system was located 5.3 meters below the water line at the bow of the ship.    Discreet filter samples from the ship's seawater system were taken approximately 6 times per day during the cruise. The filters were extracted and analyzed for chlorophyll “a” aboard ship using a second Turner model 10-AU fluorometer operated by Millersville University. The discrete samples were used to calibrate the continuous flow signal. Data are given in mg/m-3.
    """,
    "inorganic_ion_chemistry": """Ion Chemistry Data (Ion Chromatograph):
Two and seven-stage multi-jet cascade impactors (Berner et al., 1979) sampling air at 55-60% RH were used to determine the mass size distribution of Cl-, NO3-, SO4=, Na+, NH4+, K+, Mg+2, and Ca+2. Sampling periods ranged from 12 to 24 hours. The RH of the sampled air stream was measured a few inches upstream from the impactors. The 2-stage impactors cut the samples into submicrometer (Daero < 1.1 um at 60% RH), and supermicrometer (1.1 um < Daero < 10 um) samples. Aerosol mass size distributions from the 7-stage impactors (size cuts at: 0.18, 0.31, 0.55, 1.1, 2.0, 4.1 and 10 um) are available for download at: http://saga.pmel.noaa.gov/data/chemdist.php?cruise=ATOMIC.

The impaction stage at the inlet of the impactor was coated with silicone grease to prevent the bounce of larger particles onto the downstream stages. Tedlar films were used as the collection substrate in the impaction stage and a Millipore Fluoropore filter (1.0-um pore size) was used for the backup filter. Films were cleaned in an ultrasonic bath in 10% H2O2 for 30 min, rinsed in distilled, deionized water, and dried in an NH3- and SO2-free glove box. Filters and films were wetted with 1 ml of spectral grade methanol and additional 5 ml of distilled deionized water were added to the solution and the substrates were extracted by sonicated for 30 min. For the 7 stage impactor (sizes 0.18, 0.31, 0.55 and 1.1), the extraction volume was reduced to 0.5mL:2.5mL methanol:water in later samples (12 and 15 through 27) to increase detection. The extracts were analyzed by ion chromatography [Quinn et al., 2000]. All handling of the substrates was done in the glove box. Blank levels were determined by loading an impactor with substrates but not drawing any air through it.

Concentrations are reported as ug/m3 at STP (25C and 1 atm). Values below the detection limit are denoted with a zero and missing data are denoted with a NaN.

Berner et al., Sci. Total Environ., 13, 245 - 261, 1979.
Quinn et al., J. Geophys. Res., 105, 6785 - 6805, 2000.
    """,
    "inorganic_ion_chemistry_icealot": """Aerosol Ion Chemistry Data
Two-stage multi-jet cascade impactors (Berner et al., 1979) sampling air at <25% RH were used to determine the sub- and supermicrometer concentrations of Cl-, Br-, NO3-, SO4=, methanesulfonate (MSA-), oxalate (Ox-), Na+, NH4+, K+, Mg+2, and Ca+2. Sampling periods ranged from 2 to 23 hours. The RH of the sampled air stream was measured a few inches upstream from the impactor. The 50% aerodynamic cutoff diameters, D50,aero, were 1.1 and 10 um. Submicrometer refers to particles with Daero < 1.1 um at <25% RH and supermicrometer refers to particles with 1.1 um < Daero < 10 um at <25% RH.

The impaction stage at the inlet of the impactor was coated with silicone grease to prevent the bounce of larger particles onto the downstream stages. Tedlar films were used as the collection substrate in the impaction stage and a Millipore Fluoropore filter (1.0-um pore size) was used for the backup filter. Films were cleaned in an ultrasonic bath in 10% H2O2 for 30 min, rinsed in distilled, deionized water, and dried in an NH3- and SO2-free glove box. Filters and films were wetted with 1 mL of spectral grade methanol. An additional 5 mLs of distilled deionized water were added to the solution and the substrates were extracted by sonicating for 30 min. The extracts were analyzed by ion chromatography [Quinn et al., 1998]. All handling of the substrates was done in the glove box. Blank levels were determined by loading an impactor with substrates but not drawing any air through it.

Non-sea salt sulfate concentrations were calculated from Na+ concentrations and the ratio of sulfate to sodium in seawater. Concentrations are reported as ug/m3 at STP (25C and 1 atm).  Values below the detection limit are denoted with a 0, missing data are denoted with a NaN.

Berner et al., Sci. Total Environ., 13, 245 - 261, 1979.
Quinn et al., J. Geophys. Res., 105, 6785 - 6805, 2000.
    """,
    "total_mass": """NOAA PMEL Gravimetrically-determined Aerosol Mass - collected with 2 stage impactors
Two-stage multi-jet cascade impactors (Berner et al., 1979) sampling air at the indicated target sample RH were used to determine sub- and supermicron aerosol mass concentrations. The RH of the sampled air stream was measured a few inches upstream from the impactor. The 50% aerodynamic cutoff diameters, D50,aero, were 1.1 and 10 um. Submicron refers to particles with Daero < 1.1 um at 55% RH and supermicron refers to particles with 1.1 um < Daero < 10 um at 55% RH.

The impaction stage at the inlet of the impactor was coated with silicone grease to prevent the bounce of larger particles onto the downstream stages. Millipore Fluoropore films were used as the collection substrate in the impaction stage and a Millipore Fluoropore filter (1.0-um pore size) was used for the backup filter. Films were cleaned in an ultrasonic bath in 10% H2O2 for 30 min, rinsed in distilled, deionized water, and dried in an NH3- and SO2-free glove box.

Films and filters were weighed at PMEL with a Cahn Model 29 and Mettler UMT2 microbalance, respectively. The balances are housed in a glove box kept at a humidity of 65 ± 4%. The resulting mass concentrations from the gravimetric analysis include the water mass that is associated with the aerosol at 65% RH.

The glove box was continually purged with room air that had passed through a scrubber of activated charcoal, potassium carbonate, and citric acid to remove gas phase organics, acids, and ammonia. Static charging, which can result in balance instabilities, was minimized by coating the walls of the glove box with a static dissipative polymer (Tech Spray, Inc.), placing an anti-static mat on the glove box floor, using anti-static gloves while handling the substrates, and exposing the substrates to a 210Po source to dissipate any charge that had built up on the substrates. Before and after sample collection, substrates were stored double-bagged with the outer bag containing citric acid to prevent absorption of gas phase ammonia. More details of the weighing procedure can be found in Quinn and Coffman [1998].

Concentrations are reported as ug/m3 at STP (25C and 1 atm).

Berner et al., Sci. Total Environ., 13, 245 - 261, 1979.
Quinn et al., J. Geophys. Res., 105, 6785 - 6805, 2000.
    """,
#     "total_mass_55": """NOAA PMEL Gravimetrically-determined Aerosol Mass - collected with 2 stage impactors
# Two-stage multi-jet cascade impactors (Berner et al., 1979) sampling air at 55 ± 5% RH were used to determine sub- and supermicron aerosol mass concentrations. The RH of the sampled air stream was measured a few inches upstream from the impactor. The 50% aerodynamic cutoff diameters, D50,aero, were 1.1 and 10 um. Submicron refers to particles with Daero < 1.1 um at 55% RH and supermicron refers to particles with 1.1 um < Daero < 10 um at 55% RH.

# The impaction stage at the inlet of the impactor was coated with silicone grease to prevent the bounce of larger particles onto the downstream stages. Millipore Fluoropore films were used as the collection substrate in the impaction stage and a Millipore Fluoropore filter (1.0-um pore size) was used for the backup filter. Films were cleaned in an ultrasonic bath in 10% H2O2 for 30 min, rinsed in distilled, deionized water, and dried in an NH3- and SO2-free glove box.

# Films and filters were weighed at PMEL with a Cahn Model 29 and Mettler UMT2 microbalance, respectively. The balances are housed in a glove box kept at a humidity of 65 ± 4%. The resulting mass concentrations from the gravimetric analysis include the water mass that is associated with the aerosol at 65% RH.

# The glove box was continually purged with room air that had passed through a scrubber of activated charcoal, potassium carbonate, and citric acid to remove gas phase organics, acids, and ammonia. Static charging, which can result in balance instabilities, was minimized by coating the walls of the glove box with a static dissipative polymer (Tech Spray, Inc.), placing an anti-static mat on the glove box floor, using anti-static gloves while handling the substrates, and exposing the substrates to a 210Po source to dissipate any charge that had built up on the substrates. Before and after sample collection, substrates were stored double-bagged with the outer bag containing citric acid to prevent absorption of gas phase ammonia. More details of the weighing procedure can be found in Quinn and Coffman [1998].

# Concentrations are reported as ug/m3 at STP (25C and 1 atm).

# Berner et al., Sci. Total Environ., 13, 245 - 261, 1979.
# Quinn et al., J. Geophys. Res., 105, 6785 - 6805, 2000.
#     """,
#     "total_mass_icealot": """Gravimetrically-determined Aerosol Mass
# Two-stage multi-jet cascade impactors (Berner et al., 1979) sampling air at <25%  RH were used to determine sub- and supermicrometer aerosol mass concentrations. The RH of the sampled air stream was measured a few inches upstream from the impactor. The 50% aerodynamic cutoff diameters, D50,aero, were 1.1 and 10 um. Submicrometer refers to particles with Daero < 1.1 um at <25% RH and supermicrometer refers to particles with 1.1 um < Daero < 10 um at <25% RH.

# The impaction stage at the inlet of the impactor was coated with silicone grease to prevent the bounce of larger particles onto the downstream stages. Millipore Fluoropore films were used as the collection substrate in the impaction stage and a Millipore Fluoropore filter (1.0-um pore size) was used for the backup filter. Films were cleaned in an ultrasonic bath in 10% H2O2 for 30 min, rinsed in distilled, deionized water, and dried in an NH3- and SO2-free glove box.

# Films and filters were weighed at PMEL with a Cahn Model 29 and Mettler UMT2 microbalance, respectively. The balances are housed in a glove box kept at a humidity of <25%. The resulting mass concentrations from the gravimetric analysis include the water mass that is associated with the aerosol at <25% RH.

# The glove box was continually purged with room air that had passed through a scrubber of activated charcoal, potassium carbonate, and citric acid to remove gas phase organics, acids, and ammonia. Static charging, which can result in balance instabilities, was minimized by coating the walls of the glove box with a static dissipative polymer (Tech Spray, Inc.), placing an anti-static mat on the glove box floor, using anti-static gloves while handling the substrates, and exposing the substrates to a 210Po source to dissipate any charge that had built up on the substrates. Before and after sample collection, substrates were stored double-bagged with the outer bag containing citric acid to prevent absorption of gas phase ammonia. More details of the weighing procedure can be found in Quinn and Coffman [1998].

# Concentrations are reported as ug/m3 at STP (25C and 1 atm).

# Berner et al., Sci. Total Environ., 13, 245 - 261, 1979.
# Quinn et al., J. Geophys. Res., 105, 6785 - 6805, 2000.
#     """,
    "trace_element_chemistry": """Aerosol Trace Elements Data
Concentrations of Al, Si, Ca, Ti, and Fe were determined by thin-film x-ray primary and secondary emission spectrometry [Feely et al., 1991; Feely et al., 1998].  The analysis was conducted by Chester LabNet in Tigard, OR.  Submicron samples were collected on Teflon filters (1.0 um pore size) mounted in a Berner impactor downstream of a D50,aero 1.1 um jet plate (Berner et al., 1979).  Sub 10 micron samples were collected on Teflon filters (1.0 um pore size) mounted in a Berner impactor downstream of a D50,aero 10 um jet plate. This method of sample collection allows for the sharp size cut of the impactor while collecting a thin film of aerosol necessary for the x-ray analysis.  Sampling periods ranged from 12 to 24 hours.  The reported Ca does not include sea salt Ca (as determined from soluble Na concentrations and the ratio of Ca to Na in seawater).  Blank levels were determined by loading an impactor or filter pack with a filter but not drawing any air through it.

Concentrations are reported as ug/m3 at STP (25C and 1 atm).

The mass concentrations of Al, Si, Ca, Fe, and Ti, the major elements in soil, were combined to calculate the concentration of dust. It was assumed that each element was present in the aerosol in its most common oxide form (Al2O3, SiO2, CaO, K2O, FeO, Fe2O3, TiO2). The measured elemental mass concentration was multiplied by the appropriate molar correction factor as follows:

[Dust] = 2.2[Al] + 2.49[Si] + 1.63[Ca] + 2.42[Fe]+1.94[Ti]

[Malm et al., 1994; Perry et al., 1997]. This equation includes a 16% correction factor to account for the presence of oxides of other elements such as K, Na, Mn, Mg, and V that are not included in the linear combination. In addition, the equation omits K from biomass burning by using Fe as a surrogate for soil K and an average K/Fe ratio of 0.6 in soil [Cahill et al., 1986].

Berner et al., Sci. Total Environ., 13,  245 - 261, 1979.
Cahill, T.A., R.A. Eldred, and P.J. Feeney, Particulate monitoring and data analysis for the National Park Service, 1982 – 1985, University of California, Davis, 1986.
Feely et al., Geophys. Monogr. Ser., vol. 63, AGU, Washington, DC, 251 - 257, 1991.
Feely et al., Deep Sea Res., 45, 2637 - 2664, 1998.
Malm, W.C., J.F. Sisler, D. Huffman, R.A. Eldred, and T.A. Cahill, Spatial and seasonal trends in particle concentration and optical extinction in the United States, J. Geophys. Res., 99, 1347-1370, 1994.
Perry, K.D., T.A. Cahill, R.A. Eldred, D.D. Dutcher, and T.E. Gill, Long-range transport of North African dust to the eastern United States, J. Geophys. Res., 102, 11225- 11238, 1997.

X-Ray Fluorescence  (analyzed by CHESTER LabNet, Tigard, OR)
Sub-1.1 um and sub-10 um samples were collected on Pall PTFE Membrane Disc Filters (2 um, 47 mm) using 2 and 1 stage impactors. Filters were analyzed for total mass  by gravimetric analysis at 55 +/- 5% RH. After gravimetric analysis, a subset of filters were sent to CHESTER LabNet for XRF analysis. The following elements were reported:, Al, Si, Ca, Fe, and Ti. The XRF uncertainty measurement (as derived from calibration, counting statistics, peak overlap correction, and absorption) represents the statistical range in which a measurement may fall. More detail on XRF Data interpretation can be found here. Blank levels were determined by loading an impactor with substrates but not drawing any air through it. Concentrations are reported as ug/m3 at STP (25C and 1 atm). Values below the detection limit are denoted with a zero and missing data are denoted with a NaN.
    """,
    "trace_element_chemistry_icealot": """Aerosol Trace Elements:
Contact persons: Tim Bates, tim.bates@noaa.gov; Trish Quinn, patricia.k.quinn@noaa.gov

Concentrations of Al, Si, Ca, Ti, and Fe were determined by thin-film x-ray primary and secondary emission spectrometry [Feely et al., 1991; Feely et al., 1998].  Submicrometer and sub-10 um samples were collected on Teflo filters (1.0 um pore size) mounted in Berner impactors having a D50,aero of 1.1 um and 10 um jet plates, respectively (Berner et al., 1979).  Supermicrometer elemental concentrations were determined by difference between the submicrometer and sub-10 um concentrations.  This method of sample collection allows for the sharp size cut of the impactor while collecting a thin film of aerosol necessary for the x-ray analysis.  Sampling periods ranged from 2 to 23 hours. Blank levels were determined by loading an impactor or filter pack with a filter but not drawing any air through it.  Concentrations are reported as ug/m3 at STP (25C and 1 atm). Values below the detection limit are denoted with a 0, missing data are denoted with a NaN.

Berner et al., Sci. Total Environ., 13,  245 - 261, 1979.
Feely et al., Geophys. Monogr. Ser., vol. 63, AGU, Washington, DC, 251 - 257, 1991.
Feely et al., Deep Sea Res., 45, 2637 - 2664, 1998.
    """,
    "non-refractory_chemistry": """Chemistry Data, Aerosol Mass Spectrometer (Q-AMS):
Concentrations of submicrometer NH4+, SO4=, NO3-, POM, and Sea Salt were measured with a Quadrupole Aerosol Mass Spectrometer (Q-AMS) (Aerodyne Research Inc., Billerica, MA, USA) [Jayne et al., 2000; Allan et al., 2003]. The species measured by the AMS are referred to as non-refractory (NR) and are defined as all chemical components that vaporize at the vaporizer temperature (600°C). This includes most organic carbon species and inorganic species such as ammonium nitrate and ammonium sulfate salts but not mineral dust, elemental carbon, or sea salt. However, with the high concentrations of sea salt in the Sea Sweep samples, Na35Cl, Na37Cl, and various halide clusters were detected in the Q-AMS. The ionization efficiency of the AMS was calibrated every few days with dry monodisperse NH4NO3 particles using the procedure described by Jimenez et al. [2003]. The instrument operated on a 5 min cycle with the standard AMS aerodynamic lens. The aerodynamic particle beam forming lens on the front end of the AMS efficiently samples particles with aerodynamic diameters between 60 and 600 nm [Jayne et al., 2000]. For ambient atmospheric samples, this size range generally captures the accumulation mode aerosol and thus is readily comparable to impactor samples of submicrometer aerosol. This is not the case for sea spray particles where the dominant mass mode tails into the submicrometer size range.

Version 0 data have a "Collection Efficiency" (CE) of 1.0 applied to the four “standard” AMS measurements of sulfate, nitrate, ammonium, and organic mass, during ambient aerosol sampling periods. The CE was based on simultaneous collection of filters for ion chromatography as reference standards during ambient aerosol sampling.  A CE of 1.0 was used for Sea Sweep sampling periods assuming the POM was fully recovered and the SO4= and Sea Salt concentrations were dependent on the vaporizer temperature. The NH4+ and NO3- data were below the detection limit during Sea Sweep sampling.

The detection limits from individual species were determined by analyzing periods in which ambient filtered air was sampled and are calculated as two times the standard deviation of the reported mass concentration during those periods. The detection limits during WACS2 were 0.04, 0.24, 0.02, and 0.25 ug/m3 for sulfate, ammonium, nitrate, and POM, respectively. Samples below these detection limits are listed as 0 in the ACF file and -8888 in the ICARTT and .itx format file.  Missing data are listed as -9999 in the .acf and .ict files and NaN in the .itx file.

Jayne, J.T., D.C. Leard, X. Zhang, P. Davidovits, K.A. Smith, C.E. Kolb, and D.R. Worsnop, Development of an aerosol mass spectrometer for size and composition analysis of submicron particles, Aersol Sci. Technol., 33, 49-70, 2000.
Allan, J.D., J.L. Jimenez, P.I. Williams, M.R. Alfarra, K.N. Bower, J.T. Jayne, H. Coe, and D.R. Worsnop, Quantitative sampling using an Aerodyne aerosol mass spectrometer. Part 1: Techniques of data interpretation and error analysis, J. Geophys. Res., 108(D3), 4090, doi:10.1029/2002JD002358, 2003.
  """,
    "optics": """Aerosol in-situ Light Scattering and Absorption, Scattering and Absorption angstrom exponents, Single Scatter Albedo, and RH dependence of scattering.
A suite of instruments was used to measure aerosol light scattering and absorption. Two TSI integrating nephelometers (Model 3563) measured integrated total scattering at wavelengths of 450, 550, and 700nm (Anderson et al, 1996; Anderson and Ogren, 1998). Sample flow was taken from the AeroPhysics sampling van inlet. One nephelometer (neph_sub10) always measured aerosols of aerodynamic diameter Dae < 10 micrometers; the second nephelometer (neph_sub1) measured only aerosol of aerodynamic diameter Dae < 1.1 micrometer. When possible, both nephelometers were operated at a sensing volume RH approximately that of the indicated target sample RH. This RH was controlled by controlling the temperature of the insulated cabinet that housed the nephelometers. 

The 10 and 1.1 micrometer cut-offs were made with Berner multi-jet cascade impactors. Two Radiance Research Particle Soot Absorption Photometers were used to measure light absorption by aerosols at 467, 530, and 660nm (Bond et al., 1999; Virkkula et al.,2005) under 'dry' (<25% RH) conditions for sub 10 (psap_sub10) and sub 1 (psap_sub1) micrometer aerosols at the outlet of the respective nephelometers.

A separate humidity controlled system measured submicrometric light scattering at two different relative humidities, approximately 25% RH and 85% RH (neph_sub1_lo and neph_sub1_hi) with two TSI integrating 3-wavelength nephelometers operated in series downstream of a Berner impactor. There are no backscattering values available from the _hi or _lo nephelometers as the backscatter shutter mode was set to "total" due to problematic backscatter shutters. The first nephelometer measured scattering of the ~60% conditioned aerosol from the AeroPhysics sampling van inlet at approximately 25% RH after drying of the sample flow using a PermaPure, multiple-tube nafion dryer model PR-94. Downstream of this nephelometer a humidifier was used to add water vapor to the sample flow (6 microporous teflon tubes surrounded by a heatable water-jacket). The sample was conditioned to approximately 80% RH, scattering was measured by the second TSI neph. Humidity was measured by using a chilled mirror dew point hygrometer downstream of the second neph. 

On the PMEL Data Sever the neph_sub1_lo data are in the SUBSCATloRH file, the neph_sub1_hi data are in the SUBSCAThiRH file. 

DATA COLLECTION AND PROCESSING
Data from both systems were collected and processed at 1 sec resolution but are reported as 60-second averages. Data from each instrument are corrected and adjusted as described below, allowing for derivation of extensive parameters (light scattering and absorption) and intensive parameters (single scatter albedo, Angstrom exponent). Light absorption is box-car averaged by the instrument over a window 10-seconds wide. 

For all parameters, the bad value code is NaN. Intensive parameters are set to NaN when the extensive properties used in their calculation fell below the measurement noise threshold. Both extensive and intensive properties are set to NaN during certain events, such as during filter changes, instrument calibration, obvious instrument failure etc. Negative values of absorption might occur during periods of absorption signals near or in the range of the instrument noise, and are partly shifted into the negative range due to scattering correction.

STP are p_STP=1013.2 hPa, T_STP=273.2 K.

DERIVATION OF MEAN VALUES
EXTENSIVE PARAMETERS
Data from the TSI integrating nephelometers, Neph sub10 and Neph sub1, and f(RH=low) and f(RH=high) are processed as follows:

Span gas (air and CO2) calibrations were made before the field campaign using the standard TSI program. During the campaign zero (particle free air at ambient water vapor conc.) and CO2 span checks were made at three to four day intervals. The resulting zero offset and span factors were applied to the data.
The TSI nephelometers measure integrated light scattering into 7-170 degrees. To derive total scatter (0-180 degrees) and hemispheric backscatter (90-180 degrees) angular truncation correction factors were applied as recommended by Anderson and Ogren (1998).
Total and hemispheric backscatter were adjusted to STP. (NOTE: There are no backscattering values available from the f(RH=low) and f(RH=high) nephelometers as discussed above.)
Data from the Radiance Research Particle Soot Absorption Photometers, PSAPs sub1, sub10, and _lo,

are processed as follows:

Reported values of light absorption are corrected for spot size, flow rate, artifact response to scattering, and error in the manufacturer's calibration, all given by Bond et al. (1999). Except the spot size, all corrections were made after data collection, i.e. they are not integrated into the PSAP firmware. However, the PSAP's were flow-calibrated prior to the campaign, and a flow correction was applied based on routine flow checks during the cruise.
Light absorption is adjusted to STP
The f(RH) of scattering data is processed as follows:

Reported values of light scattering at low RH and high RH were corrected to STP.
the exponent describing the f(RH) dependence of scattering was determined using the scattering values of neph_lo_1min (fRH-optics) and neph_hi_1min (fRH-optics) and applying a linear regression of the relationship
log(scat_hi/scat_lo) = -gamma*log((1-fracRH_hi)/(1-fracRH_lo))
based on the Kasten & Hanel formula
scat_hi=scat_lo(1-fracRH)^(-gamma) [Wang et. al.,2006]
The fRH values given on the data server (SUBFRH) are at the measured high and low RH values. The gamma factor calculated from the equation above is available upon request.

INTENSIVE PARAMETERS
The Angstrom exponent for scattering at (450,550,700nm),

A_Blue = -log(Bs/Gs)/log(450/550)

A_Green = -log(Bs/Rs)/log(450/700)

A_Red = -log(Gs/Rs)/log(550/700)

where Bs, Gs and Rs are light scattering values that apply to 450, 550 and 700 nm, respectively and where these values have been smoothed by averaging over a 30-sec wide window.

The Angstrom exponent for absorption at (467,530,660nm),

A_Blue = -log(Ba/Ga)/log(467/530)

A_Green = -log(Bs/Rs)/log(467/660)

A_Red = -log(Gs/Rs)/log(530/660)

where Ba, Ga and Ra are light absorption values that apply to 467, 530 and 660 nm, respectively and where these values have been smoothed by averaging over a 30-sec wide window.

The single scatter albedo of the sub-micron aerosol was calculated as follows:

SSA = Neph1_scat / (Neph1_scat + PSAP1_abs)

where light absorption values and scattering have been averaged over 60 seconds. SSA is given for 532nm, i.e. the nephelometer data was wavelength-shifted to match the PSAP wavelength using the nephelometer based Angstrom exponent.

The sub 1 micron and sub 10 micron Scattering Angstrom exponents can be found on the PMEL Data Server in the SUBSCATANG and TOTSCATANG files. The sub 1 micron and sub 10 micron Absorption Angstrom exponents can be found in the SUBABSANG and TOTABSANG files. The sub 1 micron and sub 10 micron single scatter albedo values can be found in the SUBSSA and TOTSSA files.

REFERENCES
Anderson, T.L., D.S. Covert, S.F. Marshall, M. L. Laucks, R.J. Charlson, A.P. Waggoner, J.A. Ogren, R. Caldow, R. Holm, F. Quant, G. Sem, A. Wiedensohler, N.A. Ahlquist, and T.S. Bates, "Performance characteristics of a high-sensitivity, three-wavelength, total scatter/backscatter nephelometer", J. Atmos. Oceanic Technol., 13, 967-986, 1996.
Anderson, T.L., and J.A. Ogren, "Determining aerosol radiative properties using the TSI 3563 integrating nephelometer", Aerosol Sci. Technol., 29, 57-69, 1998.
Bond, T.C., T.L. Anderson, and D. Campbell, "Calibration and intercomparison of filter-based measurements of visible light absorption by aerosols", Aerosol Sci. and Tech., 30, 582-600, 1999.

A. Virkkula, N. C. Ahquist, D. S. Covert, P. J. Sheridan, W. P. Arnott, J. A Ogren,"A three-wavelength optical extinction cell for measuring aerosol light extinction and its application to determining absorption coefficient", Aero. Sci. and Tech., 39,52-67, 2005
A. Virkkula, N. C. Ahquist, D. S. Covert, W. P. Arnott, P. J. Sheridan, P. K. Quinn,D. J. Coffman, "Modification, calibration and a field test of an instrument for measuring light absorption by particles", Aero. Sci. and Tech., 39, 68-83, 2005
Wang et. al, Aerosol optical properties over the Northwestern Atlantic Ocean during NEAQS-ITCT 2004, and the influence of particulate matter on aerosol hygroscopicity, submitted to J. Geo. Phys. Res., 2006
  """,
#     "optics_dry": """Aerosol in-situ Light Scattering and Absorption, Scattering and Absorption angstrom exponents, Single Scatter Albedo, and RH dependence of scattering.
# A suite of instruments was used to measure aerosol light scattering and absorption.  Two TSI integrating nephelometers (Model 3563) measured integrated total scattering and hemispheric backscattering at wavelengths of 450, 550, and 700nm (Anderson et al, 1996; Anderson and Ogren, 1998). Sample flow was taken from the AeroPhysics sampling van inlet.  One nephelometer (neph_sub10) always measured aerosols of aerodynamic diameter Dae < 10 micrometers; the second nephelometer (neph_sub1 SUBSCAT) measured only aerosol of aerodynamic diameter Dae < 1 micrometer.  Both nephelometers were operated at a sensing volume RH of less than 30%.  The 10 and 1 micrometer cut-offs were made with Berner multi-jet cascade impactors.  Two Radiance Research Particle Soot Absorption Photometers were used to measure light absorption by aerosols at 467, 530, and 660nm (Bond et al., 1999; Virkkula et al.,2005) under 'dry' (<25% RH) conditions for sub 10 (psap_sub10) and sub 1 (psap_sub1) micrometer aerosols at the outlet of the respective nephelometers.

# The 10 and 1.1 micrometer cut-offs were made with Berner multi-jet cascade impactors. Two Radiance Research Particle Soot Absorption Photometers were used to measure light absorption by aerosols at 467, 530, and 660nm (Bond et al., 1999; Virkkula et al.,2005) under 'dry' (<25% RH) conditions for sub 10 (psap_sub10) and sub 1 (psap_sub1) micrometer aerosols at the outlet of the respective nephelometers.

# A separate humidity controlled system measured submicrometric light scattering at two different relative humidities, approximately 25% RH and 85% RH (neph_sub1_lo and neph_sub1_hi) with two TSI integrating 3-wavelength nephelometers operated in series downstream of a Berner impactor. There are no backscattering values available from the _hi or _lo nephelometers as the backscatter shutter mode was set to "total" due to problematic backscatter shutters. The first nephelometer measured scattering of the ~60% conditioned aerosol from the AeroPhysics sampling van inlet at approximately 25% RH after drying of the sample flow using a PermaPure, multiple-tube nafion dryer model PR-94. Downstream of this nephelometer a humidifier was used to add water vapor to the sample flow (6 microporous teflon tubes surrounded by a heatable water-jacket). The sample was conditioned to approximately 80% RH, scattering was measured by the second TSI neph. Humidity was measured by using a chilled mirror dew point hygrometer downstream of the second neph. 

# On the PMEL Data Sever the neph_sub1_lo data are in the SUBSCATloRH file, the neph_sub1_hi data are in the SUBSCAThiRH file. 

# DATA COLLECTION AND PROCESSING
# Data from both systems were collected and processed at 1 sec resolution but are reported as 60-second averages. Data from each instrument are corrected and adjusted as described below, allowing for derivation of extensive parameters (light scattering and absorption) and intensive parameters (single scatter albedo, Angstrom exponent). Light absorption is box-car averaged by the instrument over a window 10-seconds wide. 

# For all parameters, the bad value code is NaN. Intensive parameters are set to NaN when the extensive properties used in their calculation fell below the measurement noise threshold. Both extensive and intensive properties are set to NaN during certain events, such as during filter changes, instrument calibration, obvious instrument failure etc. Negative values of absorption might occur during periods of absorption signals near or in the range of the instrument noise, and are partly shifted into the negative range due to scattering correction.

# STP are p_STP=1013.2 hPa, T_STP=273.2 K.

# DERIVATION OF MEAN VALUES
# EXTENSIVE PARAMETERS
# Data from the TSI integrating nephelometers, Neph sub10 and Neph sub1, and f(RH=low) and f(RH=high) are processed as follows:

# Span gas (air and CO2) calibrations were made before the field campaign using the standard TSI program. During the campaign zero (particle free air at ambient water vapor conc.) and CO2 span checks were made at three to four day intervals. The resulting zero offset and span factors were applied to the data.
# The TSI nephelometers measure integrated light scattering into 7-170 degrees. To derive total scatter (0-180 degrees) and hemispheric backscatter (90-180 degrees) angular truncation correction factors were applied as recommended by Anderson and Ogren (1998).
# Total and hemispheric backscatter were adjusted to STP. (NOTE: There are no backscattering values available from the f(RH=low) and f(RH=high) nephelometers as discussed above.)
# Data from the Radiance Research Particle Soot Absorption Photometers, PSAPs sub1, sub10, and _lo,

# are processed as follows:

# Reported values of light absorption are corrected for spot size, flow rate, artifact response to scattering, and error in the manufacturer's calibration, all given by Bond et al. (1999). Except the spot size, all corrections were made after data collection, i.e. they are not integrated into the PSAP firmware. However, the PSAP's were flow-calibrated prior to the campaign, and a flow correction was applied based on routine flow checks during the cruise.
# Light absorption is adjusted to STP
# The f(RH) of scattering data is processed as follows:

# Reported values of light scattering at low RH and high RH were corrected to STP.
# the exponent describing the f(RH) dependence of scattering was determined using the scattering values of neph_lo_1min (fRH-optics) and neph_hi_1min (fRH-optics) and applying a linear regression of the relationship
# log(scat_hi/scat_lo) = -gamma*log((1-fracRH_hi)/(1-fracRH_lo))
# based on the Kasten & Hanel formula
# scat_hi=scat_lo(1-fracRH)^(-gamma) [Wang et. al.,2006]
# The fRH values given on the data server (SUBFRH) are at the measured high and low RH values. The gamma factor calculated from the equation above is available upon request.

# INTENSIVE PARAMETERS
# The Angstrom exponent for scattering at (450,550,700nm),

# A_Blue = -log(Bs/Gs)/log(450/550)

# A_Green = -log(Bs/Rs)/log(450/700)

# A_Red = -log(Gs/Rs)/log(550/700)

# where Bs, Gs and Rs are light scattering values that apply to 450, 550 and 700 nm, respectively and where these values have been smoothed by averaging over a 30-sec wide window.

# The Angstrom exponent for absorption at (467,530,660nm),

# A_Blue = -log(Ba/Ga)/log(467/530)

# A_Green = -log(Bs/Rs)/log(467/660)

# A_Red = -log(Gs/Rs)/log(530/660)

# where Ba, Ga and Ra are light absorption values that apply to 467, 530 and 660 nm, respectively and where these values have been smoothed by averaging over a 30-sec wide window.

# The single scatter albedo of the sub-micron aerosol was calculated as follows:

# SSA = Neph1_scat / (Neph1_scat + PSAP1_abs)

# where light absorption values and scattering have been averaged over 60 seconds. SSA is given for 532nm, i.e. the nephelometer data was wavelength-shifted to match the PSAP wavelength using the nephelometer based Angstrom exponent.

# The sub 1 micron and sub 10 micron Scattering Angstrom exponents can be found on the PMEL Data Server in the SUBSCATANG and TOTSCATANG files. The sub 1 micron and sub 10 micron Absorption Angstrom exponents can be found in the SUBABSANG and TOTABSANG files. The sub 1 micron and sub 10 micron single scatter albedo values can be found in the SUBSSA and TOTSSA files.

# REFERENCES
# Anderson, T.L., D.S. Covert, S.F. Marshall, M. L. Laucks, R.J. Charlson, A.P. Waggoner, J.A. Ogren, R. Caldow, R. Holm, F. Quant, G. Sem, A. Wiedensohler, N.A. Ahlquist, and T.S. Bates, "Performance characteristics of a high-sensitivity, three-wavelength, total scatter/backscatter nephelometer", J. Atmos. Oceanic Technol., 13, 967-986, 1996.
# Anderson, T.L., and J.A. Ogren, "Determining aerosol radiative properties using the TSI 3563 integrating nephelometer", Aerosol Sci. Technol., 29, 57-69, 1998.
# Bond, T.C., T.L. Anderson, and D. Campbell, "Calibration and intercomparison of filter-based measurements of visible light absorption by aerosols", Aerosol Sci. and Tech., 30, 582-600, 1999.

# A. Virkkula, N. C. Ahquist, D. S. Covert, P. J. Sheridan, W. P. Arnott, J. A Ogren,"A three-wavelength optical extinction cell for measuring aerosol light extinction and its application to determining absorption coefficient", Aero. Sci. and Tech., 39,52-67, 2005
# A. Virkkula, N. C. Ahquist, D. S. Covert, W. P. Arnott, P. J. Sheridan, P. K. Quinn,D. J. Coffman, "Modification, calibration and a field test of an instrument for measuring light absorption by particles", Aero. Sci. and Tech., 39, 68-83, 2005
# Wang et. al, Aerosol optical properties over the Northwestern Atlantic Ocean during NEAQS-ITCT 2004, and the influence of particulate matter on aerosol hygroscopicity, submitted to J. Geo. Phys. Res., 2006
#   """,
    "ccn": """CCN Measurements:
A Droplet Measurement Technologies CCN Counter (DMT CCNC) was used to determine CCN concentrations of sub-1 um particles at supersaturations ranging from 0.1 to 0.62%.  A multijet cascade impactor with a 50% aerodynamic cut-off diameter of 1.1 um was upstream of the CCNC. The sampled air was dried prior to reaching the CCNC.  Details concerning the characteristics of the DMT CCN counter can be found in Roberts and Nenes [2005] and Lance et al. [2006]. The CCN counter was calibrated before and during the experiment as outlined by Lance et al. [2006]. The uncertainty associated with the CCN number concentration is estimated to be less than +/- 10% [Roberts and Nenes, 2005]. Uncertainty in the instrumental supersaturation is less than +/- 10% for the operating conditions of this experiment [Roberts and Nenes, 2005].

The data are in 10 second time intervals and include CCN concentration (in n/cm^3), CCN/CN ratio, and Supersaturation (in %).

Lance, S., J. Medina, J.N. Smith, and A. Nenes, Mapping the operation of the DMT continuous flow CCN counter, Aer. Sci. Tech., 40, 242 - 254, 2006.
Roberts, G.C. and A. Nenes, A continuous-flow streamwise thermal gradient CCN chamber for atmospheric measurements, Aer. Sci. Tech., 39, 206 - 221, 2005.
    """,
    "carbon_chemistry": """Organic Carbon (Sunset Laboratory thermal/optical analyzer)
Sub-1.1 um and sub-10 um samples were collected on pre-combusted quartz fiber filters using 2 and 1 stage impactors, respectively, for organic carbon (OC) and elemental carbon (EC) analysis [Bates et al., 2004]. A charcoal diffusion denuder was deployed upstream of the submicrometer impactor to remove gas phase organic species. OC and EC concentrations were determined with a Sunset Laboratory thermal/optical analyzer. Three temperature steps were used to evolve OC under O2-free conditions for quantification. The first step heated the filter to 230 Deg C; the second step heated the filter to 600 Deg C (AMS vaporizer temperature); and the final step heated the filter to 870 Deg C. After cooling the sample down to 550 Deg C, a He/O2 mixture was introduced and the sample was heated in four temperature steps to 910 Deg C to drive off EC. The transmission of light through the filter was measured to correct the observed EC for any OC that charred during the initial stages of heating. No correction was made for carbonate carbon so OC includes both organic and carbonate carbon. The percentage of carbonate carbon is unknown. Super-micrometer OC concentrations were determined by difference between submicrometer and sub-10 um impactor samples without denuders.
    """,
    "carbon_chemistry_180nm": """Organic Carbon (Sunset Laboratory thermal/optical analyzer)
Sub-0.18 um, sub-1.1 um and sub-10 um samples were collected on pre-combusted quartz fiber filters using 2, 2 and 1 stage impactors, respectively, for organic carbon (OC) and elemental carbon (EC) analysis [Bates et al., 2004]. A charcoal diffusion denuder was deployed upstream of the submicrometer and sub-0.18 um impactors to remove gas phase organic species. OC and EC concentrations were determined with a Sunset Laboratory thermal/optical analyzer. Three temperature steps were used to evolve OC under O2-free conditions for quantification. The first step heated the filter to 230 Deg C; the second step heated the filter to 600 Deg C (AMS vaporizer temperature); and the final step heated the filter to 870 Deg C. After cooling the sample down to 550 Deg C, a He/O2 mixture was introduced and the sample was heated in four temperature steps to 910 Deg C to drive off EC. The transmission of light through the filter was measured to correct the observed EC for any OC that charred during the initial stages of heating. No correction was made for carbonate carbon so OC includes both organic and carbonate carbon. The percentage of carbonate carbon is unknown. EC was below the detection limit for all samples. Super-micrometer OC concentrations were determined by difference between submicrometer and sub-10 um impactor samples without denuders.
    """,
    "carbon_chemistry_icealot": """Aerosol OC/EC
1. Inlet
Aerosol particles were sampled 18m above the sea surface through a heated mast that extended 5 m above the aerosol measurement container. The mast was capped with a cone-shaped inlet nozzle that was rotated into the relative wind to maintain nominally isokinetic flow and minimize the loss of supermicrometer particles. Air was drawn through the 5 cm diameter inlet nozzle at 1 m3 min-1 and down the 20 cm diameter mast. The lower 1.5 m of the mast were heated to dry the aerosol to a relative humidity (RH) of <25%. This allowed for constant instrumental size cuts through variations in ambient RH. Twenty three 1.9 cm diameter electrically conductive polyethylene or stainless-steel tubes extend into this heated zone to direct the air stream at flows of 30 l min-1 to the various aerosol sizing/counting instruments and impactors. The efficiency of the mast inlet is discussed in Bates et al. (JGR 2002).

2. Sample collection
Stainless-steel tubes extending from the base of the sampling mast supplied air at 30 l min-1 to each of the impactors used for organic aerosol sampling. Two-stage and one-stage multi-jet cascade impactors (Berner et al., 1979) sampling air at <25% RH were used to determine the submicrometer and sub 10 micrometer concentrations of organic carbon (OC) and elemental carbon (EC). The 50% aerodynamic cutoff diameters, D50,aero, were 1.1 and 10 mm. For the data reported here, submicrometer refers to particles with Daero < 1.1 mm at <25% RH and supermicrometer, the difference between the concentrations measured with the two impactors, refers to particles with 1.1 mm < Daero < 10 mm at <25% RH. A 47mm quartz filter (Pall Gelman Sciences, #7202, 9.62 cm2 effective sample area) was used as the stage 1 filter in these impactors. An additional quartz filter was used as the backup filter to assess sampling artifacts.

A third submicrometer impactor with two quartz filters was deployed downstream of a 32 cm long diffusion denuder that contained 16 parallel strips (30 faces) of 20.3 cm x 3 cm carbon-impregnated glass fiber (CIG) filters (Whatman-10320163) separated by ~1.6 mm. The denuder cross-sectional area was 7.45 cm2.

The quartz filters were cleaned on board ship by baking at 550˚C for 12 hours. The cleaned filters were stored in Al foil lined (press-fitted) petri dishes, sealed with Teflon tape, in a freezer dedicated solely to these filters. After sample collection the filters and substrates were returned to their petri dishes and stored in the freezer until analysis. All samples were analyzed on board ship.

3. Filter sample analysis
The analysis of the filter samples was done using a Sunset Laboratory thermal/optical analyzer. The instrument heated the sample converting evolved carbon to CO2 and then CH4 for analysis by a FID. The thermal program was the same as that used during ACE-Asia (Schauer et al.2003, Mader et al., 2003). Four temperature steps were used to achieve a final temperature of 870°C in He to drive off OC. After cooling the sample down to 550°C, a He/O2 mixture was introduced and the sample was heated in four temperature steps to 890˚C to drive off elemental carbon (EC). The instrument measured the transmission of laser light through the filter to enable the separation of EC from OC that charred during the first stages of heating.

No correction has been made for carbonate carbon in these samples so OC includes both organic carbon and carbonate carbon if it was present.

4. Uncertainties
The uncertainties associated with positive and negative artifacts in the sampling of semi-volatile organic species can be substantial [Turpin et al., 1994; Turpin et al., 2000]. An effort was made to minimize and assess positive (adsorption of gas phase species) and negative (volatilization of aerosol organic species which may have resulted from the pressure drop across the impactor and filter) artifacts by using a denuder upstream of the impactor and by comparing undenuded and denuder-filter samplers. Results from these comparisons have shown that after correcting for sampling artifacts, measured OC concentrations can vary by 10% between samplers [Mader et al., 2003]. Other sources of uncertainty in the OC mass include the air volume sampled (5%), the area of the filter (5%), 2 times the standard deviation of the blanks measured over the course of the experiment (0.44 µg/cm2) which was on average 40% of the sample, and the precision of the method (5%) based on the results of Schauer et al. [2003]. The total uncertainty, calculated as the sum of the squares was 13%. Sub-micrometer OC values were always above the detection limit of 0.1 to 0.8 ug/m3 which varied with volume. Missing values are denoted with a -9999. The supermicrometer OC values are the difference between generally similar numbers. Samples where the difference was insignificant (<0.1 ug/m3) are denoted with a -8888.

Sources of uncertainty in the EC mass include the air volume sampled (5%), the area of the filter (5%), and the precision of the method (5%) based on the results of Schauer et al. [2003]. The total uncertainty, calculated as the sum of the squares was 9%. The limit of detection varied from 0.015 to 0.12 ug/m3 based on the volume sampled. Values below the detection limit are denoted with a -8888. Missing values are denoted with a -9999. The supermicrometer EC values were not above detection limit.

 5. Data reported in archive
The following OC/EC data sets are reported in the data archive:
Sub-micrometer OC – data are from the denuder/impactor sampler. The back up quartz filter behind the stage 1 quartz filter was used as the blank.
Sub-micrometer EC – data are the average of the two sub-micrometer impactor samplers (with and without denuders). Missing data were below the limit of detection.
Super-micrometer OC – data are the difference between the sub-10 um impactor and the sub-1 um impactor. Both impactors were run without denuders. Both impactors were corrected for blanks/artifacts using the backup quartz filter behind the stage 1 quartz filter.

Bates, T.S., D.J. Coffman, D.S. Covert, and P.K. Quinn (2002). Regional marine boundary layer aerosol size distributions in the Indian, Atlantic and Pacific Oceans: A comparison of INDOEX measurements with ACE-1, ACE-2, and Aerosols99. J. Geophys. Res., 107(D19), 10.1029/2001JD001174.
Eatough, D.J., B.D. Grover, N.L. Eatough, R.A. Cary, D.F. Smith, P.K. Hopke, and W.E. Wilson, Continuous measurement of PM2.5 semi-volatile and nonvolatile organic material. Presented at the 8th International Conference on Carbonaceous Particles in the Atmosphere, September 14-16, 2004, Vienna, Austria.
Mader, B.T., J.J. Schauer, J.H. Seinfeld, R.C. Flagan, J.Z.Yu, H. Yang, Ho-Jin Lim, B.J. Turpin, J. T. Deminter, G. Heidemann, M. S. Bae, P. Quinn, T. Bates, D.J. Eatough, B.J. Huebert, T. Bertram, and S. Howell (2003). Sampling methods used for the collection of particle-phase organic and elemental carbon during ACE-Asia, Atmos. Environ., in press.
Schauer, J.J., B.T. Mader, J. T. DeMinter, G. Heidemann, M. S. Bae, J.H. Seinfeld, R.C. Flagan, R.A. Cary, D. Smith, B.J. Huebert, T. Bertram, S. Howell, J. T. Kline, P. Quinn, T. Bates, B. Turpin, H. J. Lim, J. Z. Yu, H. Yang, and M. D. Keywood (2003). ACE-Asia intercomparison of a thermal-optical method for the determination of particle-phase organic and elemental carbon, Environ. Sci. Technol., 37, 993-1001, 10.1021/es020622f.
Turpin, B.J., J.J. Huntzicker, and S.V. Hering, Investigation of organic aerosol sampling artifacts in the Los Angeles Base, Atmos. Environ., 28, 23061-3071, 1994.
Turpin, B.J., P. Saxena, and E. Andrews, Measuring and simulating particulate organics in the atmosphere: problems and prospects, Atmos. Environ., 34, 2983-3013, 2000.
    """,
    "radon": """Radon:
The PMEL radon instrument is a "dual flow loop, two filtered radon detector". The general features of the instrument are described in Whittlestone and Zahorowski, Baseline radon detectors for shipboard use: Development and deployment in the First Aerosol Characterization Experiment (ACE1), J. Geophys. Res., 103, 16,743-16,751, 1998. The instrument response is due to radon gas, not radon daughters (all of the existing radon daughters are filtered out before entering the decay/counting tank). The instrument registers the total number of decay counts per 30 minute interval on a filter (wire screen) arising from the decay of radon in the tank. The volume of the decay/counting tank was 905 l and the sample flow rate into and out of the tank was typically 70 l/min. The response time of the radon instrument is limited to about 30 minutes by the radiological decay time constants of the radon daughters on the wire screen filter. Thus, the start time given in the data file is 15 minutes prior to the midpoint of the counting interval. The instrument was calibrated with a known radon source in Seattle before the cruise and a second calibration was performed after the instrument was shipped back to PMEL. Radon concentrations are given in mBq m-3.
    """,
    "dms": """Seawater DMS:
Seawater entered the ship at the bow, 5.3 m below the ship waterline, and was pumped to the main lab.  Every 30 minutes a 5 ml water sample was valved from the water line directly into a Teflon gas stripper.  The sample was purged with hydrogen at 80 ml/min for 5 min. DMS and other sulfur gases in the hydrogen purge gas were collected on a Tenax filled trap, held at -5 deg C.  During the sample trapping period, 6.2 pmoles of methylethyl sulfide (MES) were valved into the hydrogen stream as an internal standard.  At the end of the sampling/purge period the trap was rapidly heated to +120 deg C and the sulfur gases were desorbed from the trap, separated on a DB-1 megabore fused silica column held at 70 deg C, and quantified with a sulfur chemiluminesence detector.  Between each water sample the system analyzed either a DMS standard or a system blank.  The system was calibrated using gravimetrically calibrated DMS and MES permeation tubes.  The precision of the analysis has been shown to be ± 2% based on replicate analysis of a single water sample at 3.6 nM DMS. The automated DMS system is described in greater detail in Bates et al. (J. Geophys. Res., 103, 16369-16383, 1998; Tellus, 52B, 258-272, 2000).  The major improvements since these papers are a new automation-data system and a more reliable cold trap consisting of an electrically heated stainless steel tube embedded in an aluminum block that is cooled to -5 deg C with a thermoelectric cooling chip.
    """,
    "aod": """Aerosol Optical Depth (AOD)
A handheld Microtops sunphotometer (Solar Light Co.) was used for the measurement of AOD at wavelengths of 380, 440, 500, 675, and 870 nm.  Details about the data processing can be found at:

https://aeronet.gsfc.nasa.gov/new_web/man_data.html
    """,
    "aod_3units": """PMEL Aerosol Optical Depth Data
Three handheld Microtops sunphotometer (Solar Light Co.) were used. Two units (SN 4080 and 3803) have wavelengths of 380, 440, 500, 675, and 870 nm). The third unit (SN 3774) has wavelengths of 440, 500, 675, and 870 nm).  The full angular field of view for the Microtops is 2.5 deg.  The instruments have built in pressure and temperature sensors and were operated with a GPS connection to obtain position and time of the measurements. Raw signal voltages were converted to aerosol optical depths by correcting for Rayleigh scattering [Penndorf, 1957], ozone optical depth, and an air mass that accounts for the Earth's curvature [Kasten and Young, 1989].  For the Ozone correction the table from Burrows et al (1999) was used.
Calibrations were done using a Langley plot approach [Shaw, 1983]. These data were reduced as part of NASA's Maritime Aerosol Network. The data for MAN can be found at http://aeronet.gsfc.nasa.gov/new_web/man_data.html. The MAN contact is Alexander Smirnov (Alexander.Smirnov-1@nasa.gov).

Measurements on the ship followed the protocol of Knobelspiesse et al. [2003]. The scan length was set to 20 so that 20 measurements are obtained during each "shot". The largest voltage of the 20 measurements is recorded which corresponds to the lowest AOD. This approach helps to eliminate erroneous measurements that result from pointing errors on a moving ship. After the experiment, a post processing algorithm was applied. This algoritm calculates a coefficient of variation for each measurement equal to the sample standard deviation divided by the sample mean. If the CoV > than 0.05, the highest AOD is removed and CoV is recalculated. This procedure is repeated until all points "pass".

These data are Level 1.5 cloud screened data as defined by the MAN data quality format.

Burrows, J. P., Richter, A., Dehn, A., Deters, B., Himmelmann, S., Voigt, S. and Orphal J., Atmospheric remote -sensing-reference data from GOME: 2. Temperature-dependent absorption cross sections of O3 in the 231-794 nm range, JQSRT, 61, 509-517, 1999.
Kasten, F. and A. T. Young, Revised optical air mass tables and approximation formula, Applied Optics, 28, 4735 - 4738, 1989.
Knobelspiesse, K.D. et al., Sun-pointing-error correction for sea deployment of the Microptops II handheld sun photometer, J. Atmos. Ocean. Tech., 20, 767, 2003.
Penndorf, R. , Tables of refractive index for standard air and the Rayleigh scattering coefficient for the spectral region between 0.2 and 20 um and their application to atmospheric optics, J. Opt. Soc. America, 47, 176 - 182, 1957.
Shaw, G. E., Sun Photometry, Bull. Am. Met. Soc., 64, 4-9, 1983.
    """,
    "aod_2units": """PMEL Aerosol Optical Depth Data
Two handheld Microtops sunphotometer (Solar Light Co.) were used with wavelengths of 380, 440, 500, 675, and 870 nm). The full angular field of view for the Microtops is 2.5 deg. The instruments have built in pressure and temperature sensors and were operated with a GPS connection to obtain position and time of the measurements. Raw signal voltages were converted to aerosol optical depths by correcting for Rayleigh scattering [Penndorf, 1957], ozone optical depth, and an air mass that accounts for the Earth's curvature [Kasten and Young, 1989]. For the Ozone correction the table from Burrows et al (1999) was used.

Measurements on the ship followed the protocol of Knobelspiesse et al. [2003]. The scan length was set to 20 so that 20 measurements are obtained during each "shot". The largest voltage of the 20 measurements is recorded which corresponds to the lowest AOD. This approach helps to eliminate erroneous measurements that result from pointing errors on a moving ship. After the experiment, a post processing algorithm was applied. This algorithm calculates a coefficient of variation for each measurement equal to the sample standard deviation divided by the sample mean. If the CoV > than 0.05, the highest AOD is removed and CoV is recalculated. This procedure is repeated until all points "pass".

3803 data are Level 2.0 cloud screened data as defined by the MAN data quality format. 4080 are level 1.0.

Burrows, J. P., Richter, A., Dehn, A., Deters, B., Himmelmann, S., Voigt, S. and Orphal J., Atmospheric remote -sensing-reference data from GOME: 2. Temperature-dependent absorption cross sections of O3 in the 231-794 nm range, JQSRT, 61, 509-517, 1999.
Kasten, F. and A. T. Young, Revised optical air mass tables and approximation formula, Applied Optics, 28, 4735 - 4738, 1989.
Knobelspiesse, K.D. et al., Sun-pointing-error correction for sea deployment of the Microptops II handheld sun photometer, J. Atmos. Ocean. Tech., 20, 767, 2003.
Penndorf, R. , Tables of refractive index for standard air and the Rayleigh scattering coefficient for the spectral region between 0.2 and 20 um and their application to atmospheric optics, J. Opt. Soc. America, 47, 176 - 182, 1957.
Shaw, G. E., Sun Photometry, Bull. Am. Met. Soc., 64, 4-9, 1983.
    """,
    "csp_link": """https://saga.pmel.noaa.gov/data/view_info.php?cruise=CSP""",
    "ace1_link": """https://saga.pmel.noaa.gov/data/view_info.php?cruise=ACE1""",
    "rits94_link": """https://saga.pmel.noaa.gov/data/view_info.php?cruise=RITS94""",
    "rits93_link": """https://saga.pmel.noaa.gov/data/view_info.php?cruise=RITS93""",
    "mage92_link": """https://saga.pmel.noaa.gov/data/view_info.php?cruise=MAGE92""",
    "psi3_link": """https://saga.pmel.noaa.gov/data/view_info.php?cruise=PSI3""",
}
readme = {
    "ATOMIC": {
        "atm": dataset_readme["atm_atomic"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "carbon_chemistry": dataset_readme["carbon_chemistry"],
        "gas_chemistry": dataset_readme["gas_chemistry_ozone"],
        "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        "optics": dataset_readme["optics"],
        "optics_intensive": dataset_readme["optics"],
        "optics_frh": dataset_readme["optics"],
        "ccn": dataset_readme["ccn"],
        "aod": dataset_readme["aod"],
    },
    "NAAMES4": {
        "atm": dataset_readme["atm"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "carbon_chemistry": dataset_readme["carbon_chemistry_180nm"],
        "gas_chemistry": dataset_readme["gas_chemistry_ozone"],
        "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        "optics": dataset_readme["optics"],
        # "optics_intensive": dataset_readme["optics"],
        "ccn": dataset_readme["ccn"],
    },
    "NAAMES3": {
        "atm": dataset_readme["atm"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "carbon_chemistry": dataset_readme["carbon_chemistry_180nm"],
        "gas_chemistry": dataset_readme["gas_chemistry_ozone"],
        "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        "optics": dataset_readme["optics"],
        # "optics_intensive": dataset_readme["optics"],
        "ccn": dataset_readme["ccn"],
    },
    "NAAMES2": {
        "atm": dataset_readme["atm"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "carbon_chemistry": dataset_readme["carbon_chemistry_180nm"],
        "gas_chemistry": dataset_readme["gas_chemistry_ozone"],
        "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater_naames1_2"],
        "optics": dataset_readme["optics"],
        # "optics_intensive": dataset_readme["optics"],
        "optics_frh": dataset_readme["optics"],
        "ccn": dataset_readme["ccn"],
    },
    "NAAMES1": {
        "atm": dataset_readme["atm"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "carbon_chemistry": dataset_readme["carbon_chemistry_180nm"],
        "gas_chemistry": dataset_readme["gas_chemistry_ozone"],
        "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater_naames1_2"],
        "optics": dataset_readme["optics"],
        # "optics_intensive": dataset_readme["optics"],
        "optics_frh": dataset_readme["optics"],
        "ccn": dataset_readme["ccn"],
    },
    "WACS2014": {
        "atm": dataset_readme["atm"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "total_mass": dataset_readme["total_mass"],
        "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        "carbon_chemistry": dataset_readme["carbon_chemistry_180nm"],
        "gas_chemistry": dataset_readme["gas_chemistry_ozone"],
        "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater_wacs2014"],
        "optics": dataset_readme["optics"],
        # "optics_intensive": dataset_readme["optics"],
        "optics_frh": dataset_readme["optics"],
        "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["dms"],
        "aod": dataset_readme["aod"],
    },
    "WACS2012": {
        "atm": dataset_readme["atm"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "total_mass": dataset_readme["total_mass"],
        "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        "carbon_chemistry": dataset_readme["carbon_chemistry_180nm"],
        # "gas_chemistry": dataset_readme["gas_chemistry_ozone"],
        "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        "optics": dataset_readme["optics"],
        "optics_intensive": dataset_readme["optics"],
        "optics_frh": dataset_readme["optics"],
        # "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["dms"],
        "aod": dataset_readme["aod"],
    },
    "DYNAMO": {
        "atm": dataset_readme["atm"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "total_mass": dataset_readme["total_mass"],
        "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        # "carbon_chemistry": dataset_readme["carbon_chemistry_180nm"],
        # "gas_chemistry": dataset_readme["gas_chemistry_ozone"],
        # "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        "optics": dataset_readme["optics"],
        "optics_intensive": dataset_readme["optics"],
        "optics_frh": dataset_readme["optics"],
        # "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["dms"],
        "aod": dataset_readme["aod"],
    },
    "CALNEX": {
        "atm": dataset_readme["atm"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "total_mass": dataset_readme["total_mass"],
        "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        "carbon_chemistry": dataset_readme["carbon_chemistry"],
        "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2"],
        "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        "optics": dataset_readme["optics"],
        "optics_intensive": dataset_readme["optics"],
        # "optics_frh": dataset_readme["optics"],
        "ccn": dataset_readme["ccn"],
        # "dms": dataset_readme["dms"],
        "aod": dataset_readme["aod"],
    },
    "VOCALS": {
        "atm": dataset_readme["atm_pre_calnex"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "total_mass": dataset_readme["total_mass"],
        "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        # "carbon_chemistry": dataset_readme["carbon_chemistry"],
        "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2"],
        "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        "optics": dataset_readme["optics"],
        "optics_intensive": dataset_readme["optics"],
        "optics_frh": dataset_readme["optics"],
        # "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["dms"],
        "aod": dataset_readme["aod"],
    },
    "ICEALOT": {
        "atm": dataset_readme["atm_pre_calnex"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry_icealot"],
        "trace_element_chemistry": dataset_readme["trace_element_chemistry_icealot"],
        "total_mass": dataset_readme["total_mass"],
        "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        "carbon_chemistry": dataset_readme["carbon_chemistry_icealot"],
        "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2"],
        "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        "optics": dataset_readme["optics"],
        "optics_intensive": dataset_readme["optics"],
        "optics_frh": dataset_readme["optics"],
        "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["dms"],
        "aod": dataset_readme["aod"],
    },
    "TEXAQS2006": {
        "atm": dataset_readme["atm_pre_calnex"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "total_mass": dataset_readme["total_mass"],
        "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        "carbon_chemistry": dataset_readme["carbon_chemistry"],
        "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2"],
        "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        "optics": dataset_readme["optics"],
        "optics_intensive": dataset_readme["optics"],
        "optics_frh": dataset_readme["optics"],
        "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["dms"],
        "aod": dataset_readme["aod"],
    },
    "NEAQS2004": {
        "atm": dataset_readme["atm_pre_calnex"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "total_mass": dataset_readme["total_mass"],
        # "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        "carbon_chemistry": dataset_readme["carbon_chemistry"],
        "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2"],
        "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        "optics": dataset_readme["optics"],
        # "optics_intensive": dataset_readme["optics"],
        # "optics_frh": dataset_readme["optics"],
        # "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["dms"],
        "aod": dataset_readme["aod"],
    },
    "NEAQS2002": {
        "atm": dataset_readme["atm_pre_calnex"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "total_mass": dataset_readme["total_mass"],
        # "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        "carbon_chemistry": dataset_readme["carbon_chemistry"],
        "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2"],
        "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        "optics": dataset_readme["optics"],
        # "optics_intensive": dataset_readme["optics"],
        # "optics_frh": dataset_readme["optics"],
        # "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["dms"],
        "aod": dataset_readme["aod"],
    },
    "ACEASIA": {
        "atm": dataset_readme["atm_pre_calnex"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "total_mass": dataset_readme["total_mass"],
        # "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        "carbon_chemistry": dataset_readme["carbon_chemistry"],
        "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2_co"],
        "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        "optics": dataset_readme["optics"],
        # "optics_intensive": dataset_readme["optics"],
        # "optics_frh": dataset_readme["optics"],
        # "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["dms"],
        "aod": dataset_readme["aod"],
    },
    "NAURU99": {
        "atm": dataset_readme["atm_pre_calnex"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        # "total_mass": dataset_readme["total_mass_55"],
        # "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        # "carbon_chemistry": dataset_readme["carbon_chemistry"],
        # "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2_co"],
        # "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        # "optics": dataset_readme["optics"],
        # "optics_intensive": dataset_readme["optics"],
        # "optics_frh": dataset_readme["optics"],
        # "ccn": dataset_readme["ccn"],
        # "dms": dataset_readme["dms"],
        "aod": dataset_readme["aod"],
    },
    "AEROINDO99": {
        "atm": dataset_readme["atm_pre_calnex"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "total_mass": dataset_readme["total_mass"],
        # "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        # "carbon_chemistry": dataset_readme["carbon_chemistry"],
        # "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2_co"],
        # "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        # "optics": dataset_readme["optics"],
        # "optics_intensive": dataset_readme["optics"],
        # "optics_frh": dataset_readme["optics"],
        # "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["dms"],
        "aod": dataset_readme["aod"],
    },
    "ACE2": {
        "atm": dataset_readme["atm_pre_calnex"],
        "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "total_mass": dataset_readme["total_mass"],
        # "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        # "carbon_chemistry": dataset_readme["carbon_chemistry"],
        # "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2_co"],
        # "radon": dataset_readme["radon"],
        "seawater": dataset_readme["seawater"],
        # "optics": dataset_readme["optics"],
        # "optics_intensive": dataset_readme["optics"],
        # "optics_frh": dataset_readme["optics"],
        # "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["dms"],
        "aod": dataset_readme["aod"],
    },
    "CSP": {
        "atm": dataset_readme["csp_link"],
        "inorganic_ion_chemistry": dataset_readme["csp_link"],
        # # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        # "total_mass": dataset_readme["total_mass_55"],
        # # "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        # # "carbon_chemistry": dataset_readme["carbon_chemistry"],
        # # "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2_co"],
        # # "radon": dataset_readme["radon"],
        "seawater": dataset_readme["csp_link"],
        "optics": dataset_readme["csp_link"],
        # # "optics_intensive": dataset_readme["optics"],
        # # "optics_frh": dataset_readme["optics"],
        # # "ccn": dataset_readme["ccn"],
        # "dms": dataset_readme["dms"],
    },
    "ACE1": {
        "atm": dataset_readme["ace1_link"],
        "inorganic_ion_chemistry": dataset_readme["ace1_link"],
        # # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "total_mass": dataset_readme["ace1_link"],
        # # "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        # # "carbon_chemistry": dataset_readme["carbon_chemistry"],
        # # "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2_co"],
        # # "radon": dataset_readme["radon"],
        "seawater": dataset_readme["ace1_link"],
        "optics": dataset_readme["ace1_link"],
        # # "optics_intensive": dataset_readme["optics"],
        # # "optics_frh": dataset_readme["optics"],
        # # "ccn": dataset_readme["ccn"],
        # "dms": dataset_readme["dms"],
        "aod": dataset_readme["ace1_link"],
    },
    "RITS94": {
        "atm": dataset_readme["rits94_link"],
        "inorganic_ion_chemistry": dataset_readme["rits94_link"],
        # # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "total_mass": dataset_readme["rits94_link"],
        # # "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        # # "carbon_chemistry": dataset_readme["carbon_chemistry"],
        # # "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2_co"],
        # # "radon": dataset_readme["radon"],
        "seawater": dataset_readme["rits94_link"],
        # # "optics": dataset_readme["optics"],
        # # "optics_intensive": dataset_readme["optics"],
        # # "optics_frh": dataset_readme["optics"],
        # # "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["rits94_link"],
        "aod": dataset_readme["rits94_link"],
    },
    "RITS93": {
        "atm": dataset_readme["rits93_link"],
        "inorganic_ion_chemistry": dataset_readme["rits93_link"],
        # # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        "total_mass": dataset_readme["rits93_link"],
        # # "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        # # "carbon_chemistry": dataset_readme["carbon_chemistry"],
        # # "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2_co"],
        # # "radon": dataset_readme["radon"],
        "seawater": dataset_readme["rits93_link"],
        # # "optics": dataset_readme["optics"],
        # # "optics_intensive": dataset_readme["optics"],
        # # "optics_frh": dataset_readme["optics"],
        # # "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["rits93_link"],
        "aod": dataset_readme["rits93_link"],
    },
    "MAGE92": {
        "atm": dataset_readme["mage92_link"],
        "inorganic_ion_chemistry": dataset_readme["mage92_link"],
        # # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        # "total_mass": dataset_readme["total_mass_55"],
        # # "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        # # "carbon_chemistry": dataset_readme["carbon_chemistry"],
        # "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2_co"],
        # # "radon": dataset_readme["radon"],
        # "seawater": dataset_readme["seawater"],
        # # "optics": dataset_readme["optics"],
        # # "optics_intensive": dataset_readme["optics"],
        # # "optics_frh": dataset_readme["optics"],
        # # "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["mage92_link"],
    },
    "PSI3": {
        "atm": dataset_readme["psi3_link"],
        # "inorganic_ion_chemistry": dataset_readme["inorganic_ion_chemistry"],
        # # "trace_element_chemistry": dataset_readme["trace_element_chemistry"],
        # "total_mass": dataset_readme["total_mass_55"],
        # # "non-refractory_chemistry": dataset_readme["non-refractory_chemistry"],
        # # "carbon_chemistry": dataset_readme["carbon_chemistry"],
        # # "gas_chemistry": dataset_readme["gas_chemistry_ozone_so2_co"],
        # # "radon": dataset_readme["radon"],
        "seawater": dataset_readme["psi3_link"],
        # # "optics": dataset_readme["optics"],
        # # "optics_intensive": dataset_readme["optics"],
        # # "optics_frh": dataset_readme["optics"],
        # # "ccn": dataset_readme["ccn"],
        "dms": dataset_readme["psi3_link"],
    },
}

if __name__ == "__main__":
    # main = readme["main"]
    # main = main.replace("\n\n", "\n").replace('"', "")
    # print(main)
    # readme["main"] = main

    with open("readme.json", "w") as f:
        json.dump(readme, f)
