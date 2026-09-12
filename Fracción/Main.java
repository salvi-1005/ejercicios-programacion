public class Main{
    public static void main(String[] args){
        Fraccion f = new Fraccion(2,5);
        System.out.println(f.toString());
        System.out.println(f.suma(f));
        System.out.println(f.resta(f));
        System.out.println(f.multiplicacion(f));
        System.out.println(f.division(f));
    }
}