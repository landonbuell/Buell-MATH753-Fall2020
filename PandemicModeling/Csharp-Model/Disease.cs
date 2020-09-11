using System;
using System.Collections.Generic;
using System.Text;

namespace PandemicModel
{
    public class Disease
    {
        // Class to Represent Pandemic Disease
        public string name;
        public decimal R0;
        public float infectionRadius;
        public decimal infectionChance;
        public int infectionDuration;
        
        public Disease(string name, decimal rNaught)
        {
            // Constructor Method for Disease
            this.name = name;
            this.R0 = rNaught;
            this.infectionRadius = 1;
            this.infectionChance = 0.5m;
            this.infectionDuration = 10;
        }

        public void IntroduceDisease()
        {
            // Apply the Disease to the Location Model
            throw new NotImplementedException();
        }
    }
}
