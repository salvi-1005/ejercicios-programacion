public class Main {
    
    public static void main(String[] args){

        VehiculoMotorizado m = new Motocicleta("Tomas", "Peugeot", 2012, 1000, "Repartir pedidos");
        VehiculoMotorizado c = new Camion("Fabian", "Renault", 2004, 10000, 6, 4);
        VehiculoMotorizado a = new AutomovilNormal("Alberto", "Chevrolet", 2016, 1500, 5);
        VehiculoMotorizado v = new Van("Rodrigo", "Volkswagen", 2020, 800, 3);

        System.out.println(m.getModelo());
        System.out.println(c.getModelo());
        System.out.println(a.getModelo());
        System.out.println(v.getModelo());

        System.out.println(m.toString());
        System.out.println(c.toString());
        System.out.println(a.toString());
        System.out.println(v.toString());

    }

}
