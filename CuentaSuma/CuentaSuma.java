public class CuentaSuma {
    
    private int[] numeros;

    public CuentaSuma(int[] numeros){
        this.numeros = numeros;
    }

    public ParAB<Integer, Integer> devolverPar(){
        int positivos = 0;
        for (int i = 0; i < this.numeros.length; i++) {
            if (this.numeros[i] > 0) {
                positivos += 1;
            }
        }
        int sumaNegativos = 0;
        for (int i = 0; i < this.numeros.length; i++) {
            if (this.numeros[i] < 0) {
                sumaNegativos += this.numeros[i];
            }
        }
        return new ParAB<>(positivos, sumaNegativos);
    }

}
