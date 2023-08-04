// Let's take a look at an example of how to use the Template pattern in C#.

using System;

    // Abstract class that defines the template method
    abstract class AbstractClass
    {
        public void TemplateMethod()
        {
            Step1();
            Step2();
            Step3();
        }
    
        public abstract void Step1();
    
        public abstract void Step2();
    
        public void Step3()
        {
            Console.WriteLine("AbstractClass: Step 3");
        }
    }
    
    // Concrete class that implements specific steps of the algorithm
    class ConcreteClassA : AbstractClass
    {
        public override void Step1()
        {
            Console.WriteLine("ConcreteClassA: Step 1");
        }
    
        public override void Step2()
        {
            Console.WriteLine("ConcreteClassA: Step 2");
        }
    }
    
    // Concrete class that implements specific steps of the algorithm
    class ConcreteClassB : AbstractClass
    {
        public override void Step1()
        {
            Console.WriteLine("ConcreteClassB: Step 1");
        }
    
        public override void Step2()
        {
            Console.WriteLine("ConcreteClassB: Step 2");
        }
    }
    
    // Client code
    class Client
    {
        static void Main(string[] args)
        {
            AbstractClass obj1 = new ConcreteClassA();
            obj1.TemplateMethod();
    
            AbstractClass obj2 = new ConcreteClassB();
            obj2.TemplateMethod();
        }
    }