public class Conversor {

    public static Decimal aDecimal(String binario) {
        int resultado = 0;
        int potencia = 0;

        for (int i = binario.length() - 1; i >= 0; i--) {
            if (binario.charAt(i) == '1') {
                resultado += Math.pow(2, potencia);
            }
            potencia++;
        }

        return new Decimal(resultado);
    }

    public static Binario aBinario(int decimal) {
        if (decimal == 0) {
            return new Binario("0");
        }

        String binario = "";
        int num = decimal;

        while (num > 0) {
            binario = (num % 2) + binario;
            num /= 2;
        }

        return new Binario(binario);
    }
}
