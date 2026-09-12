public class Binaria extends ExpresionAritmetica2 {
    
    private ExpresionAritmetica2 izq;
    private ExpresionAritmetica2 der;

    public Binaria(ExpresionAritmetica2 izq, ExpresionAritmetica2 der){
        this.izq = izq;
        this.izq = izq;
    }

    public int sumar(){
        return izq.evaluar() + der.evaluar();
    }

    public int multiplicar(){
        return izq.evaluar() * der.evaluar();
    }

    

}
