public class Main {
    public static void main(String[] args) {

        EnumeradorString e = new EnumeradorString("hola");

        System.out.println("Iterator:");
        while (e.hasNext()) {
            System.out.println(e.next());
        }

        System.out.println("\nList:");

        EnumeradorString e2 = new EnumeradorString("hola");

        for (int i = 0; i < e2.size(); i++) {
            System.out.println(e2.get(i));
        }

        System.out.println("\nContains 'o': " + e2.contains('o'));
        System.out.println("Index of 'l': " + e2.indexOf('l'));
    }
}
