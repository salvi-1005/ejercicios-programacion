public class Reversa{

    private String cadena;

    public Reversa(String cadena){
        this.cadena = cadena;
    }

    public String invertir(){
        String resultado = "";
        for (int i = this.cadena.length() - 1; i >= 0; i--) {
            resultado += this.cadena.charAt(i);
        }
        return resultado;
    }

}