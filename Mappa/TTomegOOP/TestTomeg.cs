using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TTomegOOP
{
    struct Testtomeg
    {
        public string tomeg; // A testtömeg nav
    }
    struct TestMagasság
    {
        public string magass;
    }
    internal class TestTomeg
    {
        private int[,] testtomeg = null;

        public TestTomeg(int[,] p)
     {
         this.testtomeg = p;
     }

        // Tömeg bekérés

        // Súly bekérés

        //Testtömeg index kiszámítása

        private void testtomeg()

        {
            int testtomeg = 0;
            if (testtomeg < 10)
            {
                Console.WriteLine("Súlyosan soványság");

            }
            else if (testtomeg < 17)
            {
                Console.WriteLine("Mérsékelt soványság");

            }
            else if (testtomeg < 18.5)
            {
                Console.WriteLine("Enyhe soványság");

            }
            else if (testtomeg < 25)
            {
                Console.WriteLine("Normális soványság");

            }
            else if (testtomeg < 30)
            {
                Console.WriteLine("Túlsúlyos");
            }
        }
        }
}
