public class Binario {

    private String valor; // solo '0' y '1'

    public Binario(String valor) {
        this.valor = valor;
    }

    public String getValor() {
        return valor;
    }

    // Convertir a decimal
    public Decimal aDecimal() {
        int resultado = 0;
        int potencia = 0;

        for (int i = valor.length() - 1; i >= 0; i--) {
            char c = valor.charAt(i);
            if (c == '1') {
                resultado += Math.pow(2, potencia);
            }
            potencia++;
        }

        return new Decimal(resultado);
    }
}
