// Now, let's see an example of how we can implement the Abstract Factory Pattern in Java:
public interface Button {
    public void render();
 }
 
 public class WindowsButton implements Button {
    @Override
    public void render() {
       System.out.println("Rendering Windows button...");
    }
 }
 
 public class MacButton implements Button {
    @Override
    public void render() {
       System.out.println("Rendering Mac button...");
    }
 }
 
 public interface GUIFactory {
    public Button createButton();
 }
 
 public class WindowsGUIFactory implements GUIFactory {
    @Override
    public Button createButton() {
       return new WindowsButton();
    }
 }
 
 public class MacGUIFactory implements GUIFactory {
    @Override
    public Button createButton() {
       return new MacButton();
    }
 }

//  Now, let's see how we can use these classes to create related objects:
public class Main {
    public static void main(String[] args) {
       GUIFactory factory;
 
       // Determine the user's operating system
       String os = System.getProperty("os.name").toLowerCase();
       if (os.contains("windows")) {
          factory = new WindowsGUIFactory();
       } else {
          factory = new MacGUIFactory();
       }
 
       Button button = factory.createButton();
       button.render(); // Output: Rendering Windows button... or Rendering Mac button...
    }
 }