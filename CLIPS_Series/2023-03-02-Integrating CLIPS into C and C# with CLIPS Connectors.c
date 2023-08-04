#include "clips.h"

int main() {
void *theEnv;
theEnv = CreateEnvironment();

/* Load the rules */
Load(theEnv, "my-rules.clp");

/* Define a fact */
AssertString(theEnv, "(my-fact)");

/* Run the rules */
Run(theEnv, -1);

/* Destroy the environment */
DestroyEnvironment(theEnv);

return 0;
}