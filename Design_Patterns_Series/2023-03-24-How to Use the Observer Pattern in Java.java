// Here's an example code snippet that demonstrates the Bridge Pattern:


// Abstraction interface
    interface Shape {
        public void draw();
    }
    
    // Concrete classes for abstraction
    class Circle implements Shape {
        private DrawingAPI drawingAPI;
        private double x, y, radius;
        
        public Circle(double x, double y, double radius, DrawingAPI drawingAPI) {
            this.x = x;
            this.y = y;
            this.radius = radius;
            this.drawingAPI = drawingAPI;
        }
        
        public void draw() {
            drawingAPI.drawCircle(x, y, radius);
        }
    }
    
    class Square implements Shape {
        private DrawingAPI drawingAPI;
        private double x, y, side;
        
        public Square(double x, double y, double side, DrawingAPI drawingAPI) {
            this.x = x;
            this.y = y;
            this.side = side;
            this.drawingAPI = drawingAPI;
        }
        
        public void draw() {
            drawingAPI.drawSquare(x, y, side);
        }
    }
    
    // Implementation interface
    interface DrawingAPI {
        public void drawCircle(double x, double y, double radius);
        public void drawSquare(double x, double y, double side);
    }
    
    // Concrete classes for implementation
    class RasterDrawingAPI implements DrawingAPI {
        public void drawCircle(double x, double y, double radius) {
            // draw circle using raster graphics
        }
        
        public void drawSquare(double x, double y, double side) {
            // draw square using raster graphics
        }
    }
    
    class VectorDrawingAPI implements DrawingAPI {
        public void drawCircle(double x, double y, double radius) {
            // draw circle using vector graphics
        }
        
        public void drawSquare(double x, double y, double side) {
            // draw square using vector graphics
        }
    }
    
    // Client code
    public class Client {
        public static void main(String[] args) {
            Shape circle = new Circle(1, 2, 3, new VectorDrawingAPI());
            circle.draw();
            
            Shape square = new Square(4, 5, 6, new RasterDrawingAPI());
            square.draw();
        }
    }
