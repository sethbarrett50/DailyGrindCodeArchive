// First, let's create an interface that will define the method that will accept the Visitor.
public interface Animal {
    void accept(AnimalVisitor visitor);
}

// Next, let's create some concrete classes that will implement the Animal interface.
public class Lion implements Animal {

    @Override
    public void accept(AnimalVisitor visitor) {
        visitor.visit(this);
    }
}

public class Bear implements Animal {

    @Override
    public void accept(AnimalVisitor visitor) {
        visitor.visit(this);
    }
}

// Now, let's create the Visitor interface that defines the operations we want to perform.
public interface AnimalVisitor {
    void visit(Lion lion);
    void visit(Bear bear);
}

// Next, let's create the concrete classes that will implement the AnimalVisitor interface.
public class FeedingVisitor implements AnimalVisitor {

    @Override
    public void visit(Lion lion) {
        System.out.println("Feeding Lion");
    }

    @Override
    public void visit(Bear bear) {
        System.out.println("Feeding Bear");
    }
}

public class PlayingVisitor implements AnimalVisitor {

    @Override
    public void visit(Lion lion) {
        System.out.println("Playing with Lion");
    }

    @Override
    public void visit(Bear bear) {
        System.out.println("Playing with Bear");
    }
}

// Now, let's create a class that will use the Visitor pattern to perform operations on the Animal objects.
public class AnimalOperations {

    public void performOperation(List animals, AnimalVisitor visitor) {
        for (Animal animal : animals) {
            animal.accept(visitor);
        }
    }
}

// Let's see how we can use this pattern to perform the operation.
public class Main {

    public static void main(String[] args) {
        List animals = new ArrayList<>();
        animals.add(new Lion());
        animals.add(new Bear());

        AnimalOperations animalOperations = new AnimalOperations();

        AnimalVisitor feedingVisitor = new FeedingVisitor();
        AnimalVisitor playingVisitor = new PlayingVisitor();

        animalOperations.performOperation(animals, feedingVisitor);
        animalOperations.performOperation(animals, playingVisitor);
    }
}
