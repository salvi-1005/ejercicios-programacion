public class Fraccion{

    //Dos constructores

    private int numerador;
    private int denominador;

    public Fraccion(int num, int den){
       this.numerador = num;
       this.denominador = den;
    }

    public Fraccion(int num){
       this.numerador = num;
       this.denominador = 1;
    }
    
    public void setDenominador(int n){
        this.denominador = n;
    }

    public int getDenominador(){
        return this.denominador;
    }

    //Operaciones aritméticas comunes

    public Fraccion suma(Fraccion f){
        int num = this.numerador * f.denominador + this.denominador * f.numerador;
        int den = this.denominador * f.denominador;

        return new Fraccion(num, den);
    }

    public Fraccion resta(Fraccion f){
        int num = this.numerador * f.denominador - this.denominador * f.numerador;
        int den = this.denominador * f.denominador;

        return new Fraccion(num, den);
    }
    

    public Fraccion multiplicacion(Fraccion f){
        int num = this.numerador * f.numerador;
        int den = this.denominador * f.denominador;

        return new Fraccion(num, den);
    }

    public Fraccion division(Fraccion f){
        int num = this.numerador * f.denominador;
        int den = this.denominador * f.numerador;

        return new Fraccion(num, den);
    }

    public String toString(){
        return numerador + "/" + denominador;
    }
}