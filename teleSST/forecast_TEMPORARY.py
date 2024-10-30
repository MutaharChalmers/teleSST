#!/usr/bin/env python3
# -*- coding: utf-8 -*-

    #def _forecast(self, fmonth, fyear, N_batches, seed=42):
    #    """Generate forecast-stochastic set forced by SEAS5 SST forecast.

    #    Parameters
    #    ----------
    #        fmonth : int
    #            Effective month of forecast.
    #        fyear : int
    #            Effective year of forecast.
    #        N_batches : int
    #            Number of batches to simulate.
    #        seed : int, optional
    #            Seed or random number generator state variable.

    #    Returns
    #    -------
    #        stoc_forecast : DataFrame
    #            Stochastic forecast multiPCs.
    #    """

    #    # Assumes ECMWF SEAS5 forecasts to set up stochastic forecast
    #    N_ens = 51 if fyear > 2016 else 25

    #    # Define initial values
    #    multiPCs_init = np.repeat(self.multiPCs.loc[fyear, fmonth].values[None,:],
    #                              N_ens*N_batches, axis=0)[:,None]
    #    telePCs_init = pd.concat({i+1: self.tele.PCs.loc[[(fyear, fmonth)]]
    #                              for i in range(N_ens)}, names=['number'])

    #    # Load forecast SST data, project onto SST EOFs and convert to numpy
    #    self.tele.calc_anoms_forecast(self.telefore_inpath, fyear, fmonth)
    #    self.tele.anoms_fore = self.tele.anoms_fore.assign_coords(number=self.tele.anoms_fore.number+1)
    #    telePCs_fore = self.tele.project(self.tele.anoms_fore)
    #    telePCs = pd.concat([telePCs_init, telePCs_fore]).sort_index()
    #    telePCs = pd.concat({batch+1: telePCs
    #                         for batch in range(N_batches)}, names=['batch'])
    #    telePCs_np = telePCs.to_numpy().reshape(N_ens*N_batches, 7, -1)

    #    # Define period (i.e. month) labels
    #    periods_sim = (np.arange(fmonth, fmonth+7) - 1) % 12 + 1

    #    # Run simulation and post-process
    #    stoc_forecast = self.model.simulate(7, X0=multiPCs_init, Xx=telePCs_np,
    #                                        batches=N_ens*N_batches,
    #                                        periods=periods_sim, seed=seed)
    #    return pd.DataFrame(stoc_forecast.reshape(-1, self.N_multiPCs),
    #                        index=telePCs.index).rename_axis('pc_multi', axis=1)