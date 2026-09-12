public class Main {
    public static void main(String[] args) {
        Polar p1 = new Polar(4,60);
        Polar p2 = new Polar(11, 85);
        Polar p3 = p1.suma(p2);
        System.out.println(p3.getRadio());
        System.out.println(p3.getAngulo());
        Polar p4 = new Polar(15, 90);
        Punto p5 = p4.pasarARectangulares();
        System.out.println(p5.getX());
        System.out.println(p5.getY());
    }
}