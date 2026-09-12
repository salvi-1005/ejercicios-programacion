public class Main {
    public static void main(String[] args) {

        GeneradorDeNumeros gen = new GeneradorDeNumeros(2, 10, 2);

        System.out.println("Usando Iterator:");
        while (gen.hasNext()) {
            System.out.println(gen.next());
        }

        System.out.println("\nUsando List:");

        GeneradorDeNumeros gen2 = new GeneradorDeNumeros(2, 10, 2);

        for (int i = 0; i < gen2.size(); i++) {
            System.out.println(gen2.get(i));
        }

        System.out.println("\nContains 6: " + gen2.contains(6));
        System.out.println("Contains 7: " + gen2.contains(7));
    }
}
