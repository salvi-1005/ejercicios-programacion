public class EsSecuencia {
    
    private int[] numeros;

    public EsSecuencia(int[] numeros){
        this.numeros = numeros;
    }

    public boolean esSecuencia(){
        for (int i = 1; i < numeros.length; i++) {
            if (numeros[i] != numeros[i - 1] + 1) {
                return false;
            }
        }
        return true;
    }

}
