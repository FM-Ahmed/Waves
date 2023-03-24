# Waves
Function for waves.

## Content of repository

### jonswap.py
Takes Hs, Tp, df and fcutoff_high to return the JONSWAP spectrum. It is based on the JONSWAP implementation in the HydroDyn module in OpenFAST. Returns the JONSWAP spectrum as a function of both frequency and angular frequency.  

### Example_JONSWAP.py
This file shows an example of the usage of the function jonswap.py. First, an arbitrary spectrum was made with randomly chosen inputs. Then, the spectrum was converted to a wave elevation time series. 
