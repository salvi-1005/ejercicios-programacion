package aed;

class Funciones {
    int cuadrado(int x) {
        return x*x;
    }


    double distancia(double x, double y) {
        return Math.sqrt(x*x + y*y);
    }

    boolean esPar(int n) {
        if (n % 2 == 0){
            return true;
        }
        else{
            return false;
        }
        }

    boolean esBisiesto(int n) {
        if ((n % 4 == 0 && n % 100 != 0) || (n % 400 == 0)){
            return true;
        }
        return false;
    }

    int factorialIterativo(int n) {
        int respuesta = 1;
        for(int i = 1; i <= n; i++){
            respuesta *= i;
        }
        return respuesta;
    }

    int factorialRecursivo(int n) {
        if (n == 0){
            return 1;
        }
        else{
            return (n*factorialRecursivo(n-1));
        }
    }

    boolean esPrimo(int n) {
        if (n <= 1){
            return false;
        }
        for(int i = 2; i <= Math.sqrt(n); i++){
            if (n % i == 0){
                return false;
            }
        }
        return true;
    }

    int sumatoria(int[] numeros) {
        int respuesta = 0;
        for(int i : numeros){
            respuesta += i;
        }
        return respuesta;
    }

    int busqueda(int[] numeros, int buscado) {
        for(int i = 0; i < numeros.length; i++){
            if(numeros[i] == buscado){
                return i;
            }
        }
        return 0;
    }

    boolean tienePrimo(int[] numeros) {
        for(int i = 0; i < numeros.length; i++){
            if(esPrimo(numeros[i])){
                return true;
            }
        }
        return false;
    }

    boolean todosPares(int[] numeros) {
        for(int i = 0; i < numeros.length; i++){
            if(!esPar(numeros[i])){
                return false;
            }
        }
        return true;
    }

    boolean esPrefijo(String s1, String s2) {
        if(s1.length() > s2.length()){
            return false;
        }
        for(int i = 0; i < s1.length(); i++){
            if(s1.charAt(i) != s2.charAt(i)){
                return false;
            }

        }
        return true;
    }

    boolean esSufijo(String s1, String s2) {
        if(s1.length() > s2.length()){
            return false;
        }
        int string1 = s1.length() - 1;
        int string2 = s2.length() - 1;
        while(string1 >= 0){
            if(s1.charAt(string1) != s2.charAt(string2)){
                return false;
            }
            string1--;
            string2--;

        }
        return true;
        
    }
}
