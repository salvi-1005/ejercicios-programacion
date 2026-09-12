public class Polar{
    private double radio;
    private double angulo;

    public Polar(double rad, double ang) {
        this.radio = rad; 
        this.angulo = ang;
    }

    public double getRadio() {
        return radio;
    }

    public double getAngulo() {
        return angulo;
    }

    public Punto pasarARectangulares(){
        double x = radio*Math.cos(angulo);
        double y = radio*Math.sin(angulo);
        return new Punto(x,y);
    }

    public Polar suma(Polar p){
        Punto p1 = this.pasarARectangulares();
        Punto p2 = p.pasarARectangulares();

        double x = p1.getX() + p2.getX();
        double y = p1.getY() + p2.getY();

        double nuevoRadio = Math.sqrt(x*x + y*y);
        double nuevoAngulo = Math.atan2(y, x);

        return new Polar(nuevoRadio,nuevoAngulo);
    }
}