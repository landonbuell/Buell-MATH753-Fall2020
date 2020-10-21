using System;
using System.Collections.Generic;
using System.Text;

namespace RealityCheck04
{
    class MultivariateNewtonsMethodSolver
    {
    }

    public class SystemGPS
    {
        // Representas a GPS System of Equations
        private readonly double c = 299792458;

        public SystemGPS(double[] r1, double[] r2, double[] r3, double[] r4)
        {
            // Constructor Method for SystemGPS Instance
            Satellite1Position = r1;
            Satellite2Position = r2;
            Satellite3Position = r3;
            Satellite4Position = r4;
        }

        public SystemGPS(double[] _r0, double[] _t0)
        {
            // Constructor for different arguments
            InitialPosition = _r0;
            TimeIntervals = _t0;
        }
            
        public double[] TimeIntervals { get; set; }

        public double[] InitialPosition { get; set; }

        public double[] Satellite1Position { get; set; }
        public double[] Satellite2Position { get; set; }
        public double[] Satellite3Position { get; set; }
        public double[] Satellite4Position { get; set; }

        public void SystemOfEquations(double _r0)
        {
            // Return value of system of equations
        }

    }
}
