public class Main {
    
    public static void main(String[] args){

        Trayecto t = new Trayecto(50, 5);

        Viaje v1 = new Viaje(t, 75, new Diesel());
        Viaje v2 = new Viaje(t, 75, new Electrico());
        Viaje v3 = new Viaje(t, 75, new AltaVelocidad());

        System.out.println(v1.tiempoDeDemora());
        System.out.println(v2.tiempoDeDemora());
        System.out.println(v3.tiempoDeDemora());

    }
}
