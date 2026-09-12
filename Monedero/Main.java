public class Main {
    public static void main(String[] args) {

        Monedero m = new Monedero(500);
        m.MeterDinero(1000);
        System.out.println(m.ConsultarDineroDisponible());
        m.SacarDinero(200);
        System.out.println(m.ConsultarDineroDisponible());
        m.SacarDinero(2000);
        System.out.println(m.ConsultarDineroDisponible());
    }
}