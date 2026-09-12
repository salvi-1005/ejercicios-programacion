public class Main {

    public static void main(String[] args){
        
        Trayecto t = new Trayecto(50, 5);

        Diesel d = new Diesel(t,5,75,75);
        Electrico e = new Electrico(t,5,75,75);
        AltaVelocidad a = new AltaVelocidad(t,5,75,75);

        System.out.println(d.tiempoDeDemora());
        System.out.println(e.tiempoDeDemora());
        System.out.println(a.tiempoDeDemora());
    }
}
