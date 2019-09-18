using System;
using System.Linq;

namespace frog_problem
{
    class Program
    {
        static void Main(string[] args)
        {
            int sims = 1000000;
            int total_pads = 10;
            Random jumpSize = new Random();
            int[] answers = new int[sims];

            for(int i = 0; i < sims; i++)
            {
                int jumps = 0;
                int current_pad = 0;
                while(current_pad < total_pads)
                {
                    current_pad = current_pad + jumpSize.Next(1,11 - current_pad);
                    jumps++;
                }
                answers[i] = jumps;
            }

            double meanJumps = answers.Average();
            Console.WriteLine(meanJumps);
        }
    }
}