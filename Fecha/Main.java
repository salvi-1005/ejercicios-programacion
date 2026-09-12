public class Main {
    public static void main(String[] args) {
        Fecha f1 = new Fecha(10,5,2003);
        Fecha f2 = new Fecha(5,5,2005);
        System.out.println(f1.toString());
        System.out.println(f2.toString());
        System.out.println(f1.esMayor(f1,f2));
    }
}