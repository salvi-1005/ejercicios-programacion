public class Main {
    
    public static void main(String[] args){

        Wrapper<String> w1 = new Wrapper<>("Edad");
        System.out.println(w1.getClase());

        w1.mostrar();

        Wrapper<Double> w2 = new Wrapper<>(2.5);
        System.out.println(w2.getClase());

        w2.mostrar();

    }

}