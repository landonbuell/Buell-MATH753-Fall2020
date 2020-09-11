/*
 * Landon Buell
 * Pandemic Modeling
 * Location Based Objects
 * 1 September 2020
 */

using System;
using System.Collections.Generic;
using System.Text;

namespace PandemicModel
{

    public class SystemModel
    {
        // World Board Instance Holds all People, Locations, etc.

        public string name;

        private BaseLocation[,] locationBoard;

        public int totalVectors;
        public int totalLocations;

        public SystemModel(string name)
        {
            // Constructor Method for World Board
            this.name = name;

            // Locations in the World are stored in this Matrix
            this.locationBoard = new BaseLocation[10,10];

            this.totalVectors = 0;
            this.totalLocations = 0;
        }

        public void AddLocation (BaseLocation newLocation)
        {
            // Add New Location to World
            
        }

        public List<BaseLocation> GetLocations ()
        {
            // Get All Locations Instances as List
            List<BaseLocation> locations = new List<BaseLocation>();
            for (int i = 0; i < locationBoard.GetLength(0); i++)
            {
                for (int j = 0; j < locationBoard.GetLength(1); j++)
                {
                    locations.Add(locationBoard[i, j]);
                }
            }
            return locations;
        }

    }

   
}
