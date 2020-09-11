/*
 * Landon Buell
 * Pandemic Modeling
 * Individals Objects
 * 1 September 2020
 */

using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Text;

namespace PandemicModel
{
    public class BaseIndiviual
    {
        // Individual Carrier or Vector
        public string name;
        

        public BaseIndiviual (string name)
        {
            // Constructor Method for BaseIndividual Class
            this.name = name;
            Condition = 0;
        }

        public int Condition { get; set; }
        // get or Set the health condition of this individual

    }
}
