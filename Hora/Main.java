public class Main
{
    public static void main(String[] args) 
    {
        Hora ho1 = new Hora(23,44,55);
        Hora ho2 = new Hora(2,23,14);
        ho1.mostrar();
        ho2.mostrar();
        Hora sumaDeHoras = ho1.suma(ho2);
        sumaDeHoras.mostrar();
        ho1.suma2(ho2);
        ho1.mostrar();
    }
}