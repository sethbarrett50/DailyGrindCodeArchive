// Now, let's see an example of how we can implement the Factory Pattern in Java:
public interface Animal {
    public void makeSound();
 }
 
 public class Dog implements Animal {
    @Override
    public void makeSound() {
       System.out.println("Woof");
    }
 }
 
 public class Cat implements Animal {
    @Override
    public void makeSound() {
       System.out.println("Meow");
    }
 }
 
 public abstract class AnimalFactory {
    public abstract Animal createAnimal();
 }
 
 public class DogFactory extends AnimalFactory {
    @Override
    public Animal createAnimal() {
       return new Dog();
    }
 }
 
 public class CatFactory extends AnimalFactory {
    @Override
    public Animal createAnimal() {
       return new Cat();
    }
 }


// Now, let's see how we can use these classes to create objects:
 public class Main {
    public static void main(String[] args) {
       AnimalFactory dogFactory = new DogFactory();
       Animal dog = dogFactory.createAnimal();
       dog.makeSound(); // Output: Woof
 
       AnimalFactory catFactory = new CatFactory();
       Animal cat = catFactory.createAnimal();
       cat.makeSound(); // Output: Meow
    }
 }