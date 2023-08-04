using CLIPSNET;

namespace MyProgram {
    class Program {
        static void Main(string[] args) {
            /* Create a new CLIPS environment */
            Environment theEnv = new Environment();
            /* Load the rules */
            theEnv.Load("my-rules.clp");

            /* Define a fact */
            theEnv.AssertString("(my-fact)");

            /* Run the rules */
            theEnv.Run();

            /* Destroy the environment */
            theEnv.Destroy();
        }
    }
}