public class Main {
    
    public static void main(String[] args){

        Par<String, Integer> p1 = new Par<>("Edad", 25);

        System.out.println(p1.getPrimero());
        System.out.println(p1.getSegundo());

        Par<Double, Double> p2 = new Par<>(2.5, 7.3);

        System.out.println(p2.getPrimero());
        System.out.println(p2.getSegundo());

    }

}
