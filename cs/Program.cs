using System;
using System.Linq;

namespace frog_problem
{
    class Program
    {
        static void Main(string[] args)
        {
            int sims = 1000000;
            int totalPads = 10;
            Random jumpSize = new Random();
            int[] answers = new int[sims];

            for(int i = 0; i < sims; i++)
            {
                int jumps = 0;
                int currentPad = 0;
                while(currentPad < totalPads)
                {
                    currentPad = currentPad + jumpSize.Next(1,11 - currentPad);
                    jumps++;
                }
                answers[i] = jumps;
            }

            double meanJumps = answers.Average();
            Console.WriteLine(meanJumps);
        }
    }
}