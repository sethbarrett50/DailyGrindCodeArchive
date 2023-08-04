// Now, let's see an example of how we can implement the Prototype Pattern in Java:
public interface Prototype {
    public Prototype clone();
 }
 
 public class ConcretePrototype implements Prototype {
    private String name;
 
    public ConcretePrototype(String name) {
       this.name = name;
    }
 
    public Prototype clone() {
       return new ConcretePrototype(name);
    }
 }

//  Now, let's see how we can use this Prototype pattern:
public class Main {
    public static void main(String[] args) {
       ConcretePrototype prototype1 = new ConcretePrototype("Prototype 1");
       ConcretePrototype prototype2 = (ConcretePrototype) prototype1.clone();
 
       System.out.println("Prototype 1 name: " + prototype1.getName());
       System.out.println("Prototype 2 name: " + prototype2.getName());
 
       prototype2.setName("Prototype 2");
 
       System.out.println("Prototype 1 name: " + prototype1.getName());
       System.out.println("Prototype 2 name: " + prototype2.getName());
    }
 }