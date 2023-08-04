// Now, let's see an example of how we can implement the Builder Pattern in Java:
public class Product {
    private String part1;
    private String part2;
    private String part3;
 
    public void setPart1(String part1) {
       this.part1 = part1;
    }
 
    public void setPart2(String part2) {
       this.part2 = part2;
    }
 
    public void setPart3(String part3) {
       this.part3 = part3;
    }
 
    public String getPart1() {
       return part1;
    }
 
    public String getPart2() {
       return part2;
    }
 
    public String getPart3() {
       return part3;
    }
 }
 
 public interface Builder {
    public void buildPart1(String part1);
    public void buildPart2(String part2);
    public void buildPart3(String part3);
    public Product getProduct();
 }
 
 public class ConcreteBuilder implements Builder {
    private Product product = new Product();
 
    public void buildPart1(String part1) {
       product.setPart1(part1);
    }
 
    public void buildPart2(String part2) {
       product.setPart2(part2);
    }
 
    public void buildPart3(String part3) {
       product.setPart3(part3);
    }
 
    public Product getProduct() {
       return product;
    }
 }
 
 public class Director {
    private Builder builder;
 
    public Director(Builder builder) {
       this.builder = builder;
    }
 
    public void construct() {
       builder.buildPart1("Part 1");
       builder.buildPart2("Part 2");
       builder.buildPart3("Part 3");
    }
 }
 
 public class Main {
    public static void main(String[] args) {
       Builder builder = new ConcreteBuilder();
       Director director = new Director(builder);
       director.construct();
       Product product = builder.getProduct();
 
       System.out.println(product.getPart1());
       System.out.println(product.getPart2());
       System.out.println(product.getPart3());
    }
 }
