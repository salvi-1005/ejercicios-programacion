public class Main {
    
    public static void main(String[] args) {
        Integer[] numeros = {5, 2, 9, 1, 5, 6};
        FiltrarElementos<Integer> filtro = new FiltrarElementos<>(numeros, 5);
        
        System.out.println("Elementos menores a 5:");
        filtro.filtrarElementosMenoresACiertoValor();
        
        System.out.println("\nElementos distintos a 5:");
        filtro.filtrarElementosDistintosACiertoValor();
    }
}
