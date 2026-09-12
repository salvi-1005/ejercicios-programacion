public class Par<A,B> {
    
    private A primero;
    private B segundo;

    public Par(A prim, B segu){
        this.primero = prim;
        this.segundo = segu;
    }

    public void setPrimero(A primero){
        this.primero = primero;
    }

    public void setSegundo(B segundo){
        this.segundo = segundo;
    }

    public A getPrimero(){
        return primero;
    }

    public B getSegundo(){
        return segundo;
    }

}
