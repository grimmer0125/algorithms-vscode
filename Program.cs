using System;

namespace CSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            String tmp = args[0];
            var type = Type.GetType("CSharp."+tmp);
            dynamic myObject = Activator.CreateInstance(type);
            // var myObject = (Program3) Activator.CreateInstance(type);

            myObject.test_solution();
        }
    }
}
