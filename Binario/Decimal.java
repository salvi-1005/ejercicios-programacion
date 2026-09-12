public class Decimal {

    private int valor;

    public Decimal(int valor) {
        this.valor = valor;
    }

    public int getValor() {
        return valor;
    }

    // Convertir a binario
    public Binario aBinario() {
        if (valor == 0) {
            return new Binario("0");
        }

        int num = valor;
        String binario = "";

        while (num > 0) {
            binario = (num % 2) + binario;
            num = num / 2;
        }

        return new Binario(binario);
    }
}
