public class SumaX {
    
    private int[] numeros;
    private int x;

    public SumaX(int[] numeros, int x){
        this.numeros = numeros;
        this.x = x;
    }

    public boolean sumaX(){
        for (int i = 0; i < numeros.length; i++) {
            for (int j = 0; j < numeros.length; j++) {
                for (int k =0 ; k < numeros.length; k++) {
                    if (((i != j) && (j != k) && (i != k)) && (numeros[i] + numeros[j] + numeros[k] == x)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

}