/*
 * Landon Buell
 * Mark Lyon
 * MATH 753.01 - EC
 * 20 october 2020
 */

using System;

namespace RealityCheck04
{
    class Q1Main
    {
        static void Main()
        {
            // Establish Initial Positions & time Intervals
            double[] _r0 = new double[4] { 0, 0, 6370, 0 };
            double[] _t0 = new double[4] { 0.07074, 0.07220, 0.07690, 0.07242 };

            // Create GPS System & Position the satellites
            SystemGPS GPS = new SystemGPS(_r0,_t0);
            GPS.Satellite1Position = new double[3] { 15600, 7540, 20140};
            GPS.Satellite2Position = new double[3] { 18760, 2750, 18610 };
            GPS.Satellite3Position = new double[3] { 17610, 14630, 13480 };
            GPS.Satellite4Position = new double[3] { 19170, 610, 18390 };

        }
    }

}
