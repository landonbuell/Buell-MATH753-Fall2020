using System;
using System.Collections.Generic;
using System.Text;

namespace PandemicModel
{
    public class BaseLocation
    {
        public string name;
        public int xloc, yloc;
        public int width, height;

        public List<BaseIndiviual> individuals;

        public BaseLocation(string name, int[] xyLoc, int[] shape )
        {
            // Constructor Method for Base Individual Class
            this.name = name;
            this.individuals = new List<BaseIndiviual>();

            this.xloc = xyLoc[0];
            this.xloc = xyLoc[1];
            this.width = shape[0];
            this.height = shape[1];
        }

        public void AddnIndividuals(int number)
        {

        }


    }
}
