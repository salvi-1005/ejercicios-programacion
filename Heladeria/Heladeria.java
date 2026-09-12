import java.util.ArrayList;

public class Heladeria {

    private double[] dulceDeLeche; 
    private double[] bananaSplit; 
    private double[] frutilla; 
    String[] dias; 
    ArrayList<Venta> ventas; 

    
    public Heladeria(){
        this.dulceDeLeche = new double[] {18.5, 12, 6, 8.0, 20.0, 25.25, 22.0};
        this.bananaSplit = new double[] {12.0, 15.0, 4.0, 13.75, 10.0, 21.0, 23.5};
        this.frutilla = new double[] {11.0, 3.75, 5.0, 12.0, 17.0, 18.0, 21.25};
        this.dias = new String[] {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"};
        this.ventas = new ArrayList<>();
    }

    public double sumar(double[] array){
        double suma = 0;

        for(double numero : array){
            suma += numero;
        }

        return suma;
    }

    public double promedio(double[] array){
        double suma = 0;

        for(double numero : array){
            suma += numero;
        }

        double promedio = Math.round((suma / array.length) * 100.0) / 100.0;
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
        double[] arraySuma = new double[7];
        arraySuma[0] = dulceDeLeche[0] + bananaSplit[0] + frutilla[0];
        arraySuma[1] = dulceDeLeche[1] + bananaSplit[1] + frutilla[1];
        arraySuma[2] = dulceDeLeche[2] + bananaSplit[2] + frutilla[2];
        arraySuma[3] = dulceDeLeche[3] + bananaSplit[3] + frutilla[3];
        arraySuma[4] = dulceDeLeche[4] + bananaSplit[4] + frutilla[4];
        arraySuma[5] = dulceDeLeche[5] + bananaSplit[5] + frutilla[5];
        arraySuma[6] = dulceDeLeche[6] + bananaSplit[6] + frutilla[6];
        
        for(int i = 0; i < arraySuma.length; i++){
            ventas.add(new Venta(dias[i], arraySuma[i]));
        }

        ventas.sort((v1, v2) -> Double.compare(v2.getKilos(), v1.getKilos()));

        for(Venta v : ventas){
            System.out.println(v.getDia() + "       " + v.getKilos());
        }

    }

}
