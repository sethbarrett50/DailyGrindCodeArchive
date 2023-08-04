// Now, let's see an example of how we can implement the Singleton Pattern in Java:
public class Singleton {
    private static Singleton instance;
 
    private Singleton() {
       // Private constructor to prevent instantiation from outside the class
    }
 
    public static Singleton getInstance() {
       if (instance == null) {
          instance = new Singleton();
       }
       return instance;
    }
 }

// Now, let's see how we can use this Singleton class:
public class Main {
    public static void main(String[] args) {
       Singleton singleton1 = Singleton.getInstance();
       Singleton singleton2 = Singleton.getInstance();
 
       // singleton1 and singleton2 are the same instance
       if (singleton1 == singleton2) {
          System.out.println("singleton1 and singleton2 are the same instance");
       } else {
          System.out.println("singleton1 and singleton2 are not the same instance");
       }
    }
 }