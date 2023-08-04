// First, let's create an interface that will define the method that will accept the Visitor.
public interface IAnimal {
    void Accept(IAnimalVisitor visitor);
}

// Next, let's create some concrete classes that will implement the IAnimal interface.
public class Lion : IAnimal {

    public void Accept(IAnimalVisitor visitor) {
        visitor.Visit(this);
    }
}

public class Bear : IAnimal {

    public void Accept(IAnimalVisitor visitor) {
        visitor.Visit(this);
    }
}

// Now, let's create the Visitor interface that defines the operations we want to perform.
public interface Visitor {
    void visit(Book book);
    void visit(CD cd);
    void visit(DVD dvd);
}

// We have defined three visit methods, one for each type of item in our library. Now, let's create concrete visitor classes that implement these operations:
public class DisplayVisitor implements Visitor {

    @Override
    public void visit(Book book) {
        System.out.println("Displaying Book: " + book.getTitle() + ", by " + book.getAuthor());
    }

    @Override
    public void visit(CD cd) {
        System.out.println("Displaying CD: " + cd.getTitle() + ", by " + cd.getArtist());
    }

    @Override
    public void visit(DVD dvd) {
        System.out.println("Displaying DVD: " + dvd.getTitle() + ", directed by " + dvd.getDirector());
    }
}

public class RentVisitor implements Visitor {

    @Override
    public void visit(Book book) {
        System.out.println("Renting Book: " + book.getTitle() + ", by " + book.getAuthor());
    }

    @Override
    public void visit(CD cd) {
        System.out.println("Renting CD: " + cd.getTitle() + ", by " + cd.getArtist());
    }

    @Override
    public void visit(DVD dvd) {
        System.out.println("Renting DVD: " + dvd.getTitle() + ", directed by " + dvd.getDirector());
    }
}

// Finally, let's see how we can use the visitor pattern to perform these operations on our library:
public class Library {
    private List items;

    public Library() {
        items = new ArrayList<>();
    }

    public void addItem(Item item) {
        items.add(item);
    }

    public void accept(Visitor visitor) {
        for (Item item : items) {
            item.accept(visitor);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Library library = new Library();
        library.addItem(new Book("The Great Gatsby", "F. Scott Fitzgerald"));
        library.addItem(new CD("Thriller", "Michael Jackson"));
        library.addItem(new DVD("The Godfather", "Francis Ford Coppola"));
        library.addItem(new Book("To Kill a Mockingbird", "Harper Lee"));

        Visitor displayVisitor = new DisplayVisitor();
        Visitor rentVisitor = new RentVisitor();

        System.out.println("Displaying items:");
        library.accept(displayVisitor);

        System.out.println("\nRenting items:");
        library.accept(rentVisitor);
    }
}
