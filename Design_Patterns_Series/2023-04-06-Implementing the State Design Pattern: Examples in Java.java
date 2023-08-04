// Let's see how this can be implemented using the State Design Pattern:



// Context Class
public class VendingMachine {
    private State currentState;
    
    // Constructor
    public VendingMachine() {
        this.currentState = new NoMoneyState();
    }
    
    // Setter method for changing the state
    public void setCurrentState(State currentState) {
        this.currentState = currentState;
    }
    
    // Delegate method to the current state
    public void insertMoney(int amount) {
        this.currentState.insertMoney(amount, this);
    }
    
    // Delegate method to the current state
    public void selectProduct(int productId) {
        this.currentState.selectProduct(productId, this);
    }
    
    // Delegate method to the current state
    public void dispenseProduct() {
        this.currentState.dispenseProduct(this);
    }
}

// State Interface
public interface State {
    public void insertMoney(int amount, VendingMachine vendingMachine);
    public void selectProduct(int productId, VendingMachine vendingMachine);
    public void dispenseProduct(VendingMachine vendingMachine);
}

// No Money State
public class NoMoneyState implements State {
    public void insertMoney(int amount, VendingMachine vendingMachine) {
        vendingMachine.setCurrentState(new HasMoneyState());
    }
    
    public void selectProduct(int productId, VendingMachine vendingMachine) {
        System.out.println("Please insert money first");
    }
    
    public void dispenseProduct(VendingMachine vendingMachine) {
        System.out.println("Please insert money and select a product first");
    }
}

// Has Money State
public class HasMoneyState implements State {
    public void insertMoney(int amount, VendingMachine vendingMachine) {
        System.out.println("You have already inserted money");
    }
    
    public void selectProduct(int productId, VendingMachine vendingMachine) {
        vendingMachine.setCurrentState(new SoldState());
    }
    
    public void dispenseProduct(VendingMachine vendingMachine) {
        System.out.println("Please select a product first");
    }
}

// Sold State
public class SoldState implements State {
    public void insertMoney(int amount, VendingMachine vendingMachine) {
        System.out.println(amount + vendingMachine);
    }
}
public class Fan {
    private State currentState;

    public Fan() {
        currentState = new OffState();
    }

    public void setState(State state) {
        currentState = state;
    }

    public void pullChain() {
        currentState.handleRequest(this);
    }
}

interface State {
    void handleRequest(Fan fan);
}

class OffState implements State {
    @Override
    public void handleRequest(Fan fan) {
        System.out.println("Turning fan on to low.");
        fan.setState(new LowState());
    }
}

class LowState implements State {
    @Override
    public void handleRequest(Fan fan) {
        System.out.println("Turning fan on to medium.");
        fan.setState(new MediumState());
    }
}

class MediumState implements State {
    @Override
    public void handleRequest(Fan fan) {
        System.out.println("Turning fan on to high.");
        fan.setState(new HighState());
    }
}

class HighState implements State {
    @Override
    public void handleRequest(Fan fan) {
        System.out.println("Turning fan off.");
        fan.setState(new OffState());
    }
}