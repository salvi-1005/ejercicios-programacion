import java.util.ArrayList;
import java.util.Arrays;

public class HeladeriaArrayList {

    private ArrayList<Double> dulceDeLeche;
    private ArrayList<Double> bananaSplit; 
    private ArrayList<Double> frutilla; 
    private ArrayList<String> dias; 
    ArrayList<Venta> ventas; 

    
    public HeladeriaArrayList(){
        this.dulceDeLeche = new ArrayList<>(Arrays.asList(18.5, 12.0, 6.0, 8.0, 20.0, 25.25, 22.0));
        this.bananaSplit = new ArrayList<>(Arrays.asList(12.0, 15.0, 4.0, 13.75, 10.0, 21.0, 23.5));
        this.frutilla = new ArrayList<>(Arrays.asList(11.0, 3.75, 5.0, 12.0, 17.0, 18.0, 21.25));
        this.dias = new ArrayList<>(Arrays.asList("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"));
        this.ventas = new ArrayList<>();
    }


    public double sumar(ArrayList<Double> array){
        double suma = 0;

        for(double numero : array){
            suma += numero;
        }

        return suma;
    }

    public double promedio(ArrayList<Double> array){
        double suma = 0;

        for(double numero : array){
            suma += numero;
        }

        double promedio = Math.round((suma / array.size()) * 100.0) / 100.0;
        return promedio;
    }

    
    public void mostrarGustoMasPedido(){
        double totalDDL = sumar(dulceDeLeche);
        double totalBanana = sumar(bananaSplit);
        double totalFrutilla = sumar(frutilla);

        System.out.println("Gusto mas pedido durante la semana: ");

        if (totalDDL > totalBanana && totalDDL > totalFrutilla){
            System.out.println("dulce de leche con " + totalDDL + " kg");
        }

        if (totalBanana > totalDDL && totalBanana > totalFrutilla){
            System.out.println("banana split con " + totalBanana + " kg");
        }

        if (totalFrutilla > totalBanana && totalFrutilla > totalDDL){
            System.out.println("frutilla con " + totalDDL + " kg");
        }
        
    }

    public void mostrarPromedioSemanal(){
        double promedioDDL = promedio(dulceDeLeche);
        double promedioBanana = promedio(bananaSplit);
        double promedioFrutilla = promedio(frutilla);

        System.out.println("PROMEDIO SEMANAL DE CADA GUSTO: ");

        System.out.println("- Dulce de leche: " + promedioDDL + " kg por dia");
        System.out.println("- Banana split: " + promedioBanana + " kg por dia");
        System.out.println("- Frutilla: " + promedioFrutilla + " kg por dia");

    }

    

    public void mostrarVentasTotales(){
        System.out.println("DIA          TOTAL(kg)");
        ArrayList<Double> arraySuma = new ArrayList<>();
        arraySuma.add(dulceDeLeche.get(0) + bananaSplit.get(0) + frutilla.get(0));
        arraySuma.add(dulceDeLeche.get(1) + bananaSplit.get(1) + frutilla.get(1));
        arraySuma.add(dulceDeLeche.get(2) + bananaSplit.get(2) + frutilla.get(2));
        arraySuma.add(dulceDeLeche.get(3) + bananaSplit.get(3) + frutilla.get(3));
        arraySuma.add(dulceDeLeche.get(4) + bananaSplit.get(4) + frutilla.get(4));
        arraySuma.add(dulceDeLeche.get(5) + bananaSplit.get(5) + frutilla.get(5));
        arraySuma.add(dulceDeLeche.get(6) + bananaSplit.get(6) + frutilla.get(6));
        
        
        for(int i = 0; i < arraySuma.size(); i++){
            ventas.add(new Venta(dias.get(i), arraySuma.get(i)));
        }

        ventas.sort((v1, v2) -> Double.compare(v2.getKilos(), v1.getKilos()));

        for(Venta v : ventas){
            System.out.println(v.getDia() + "       " + v.getKilos());
        }

    }
    
}
