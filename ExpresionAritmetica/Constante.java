public class Constante extends ExpresionAritmetica {

    private int valor;

    public Constante(int valor){
        this.valor = valor;
    }

    @Override
    public int evaluar(){
        return valor;
    }   
}
