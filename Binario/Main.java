public class Main {
    public static void main(String[] args) {

        Binario nb = new Binario("1011");
        Decimal nd = nb.aDecimal();
        System.out.println(nd.getValor()); // 11

        Decimal nd2 = new Decimal(10);
        Binario nb2 = nd2.aBinario();
        System.out.println(nb2.getValor()); // 1010

        Decimal d = Conversor.aDecimal("1011");
        Binario b = Conversor.aBinario(10);
        System.out.println(d.getValor());
        System.out.println(b.getValor());
    }
}