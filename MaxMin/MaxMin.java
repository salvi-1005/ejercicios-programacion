public class MaxMin {
    
    private int[] numeros;

    public MaxMin(String entrada) {
        if (entrada == null || entrada.isEmpty()) {
            throw new IllegalArgumentException("La cadena está vacía");
        }

        String[] partes = entrada.trim().split(" ");
        numeros = new int[partes.length];

        for (int i = 0; i < partes.length; i++) {
            numeros[i] = Integer.parseInt(partes[i]);
        }
    }

    public int[] devolverMaxMin() {
        if (numeros.length == 0) {
            throw new IllegalStateException("No hay números");
        }

        int max = numeros[0];
        int min = numeros[0];

        for (int i = 1; i < numeros.length; i++) {
            if (numeros[i] > max) {
                max = numeros[i];
            }
            if (numeros[i] < min) {
                min = numeros[i];
            }
        }

        return new int[]{max, min};
    }

}
