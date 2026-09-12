public class Main {

    public static void main(String[] args){

        GestorAnimales gestor = new GestorAnimales();

        Animal perro = new Perro("Rex", 15.5);
        Animal gato = new Gato("Mishi", 4.2);
        Animal vaca = new Vaca("Lola", 450.0);

        gestor.agregarAnimal(perro);
        gestor.agregarAnimal(gato);
        gestor.agregarAnimal(vaca);

        //4.1 Mostrar animales:

        gestor.mostrarAnimales();

        //4.2 Listar los animales ordenados por peso de menor a mayor

        gestor.ordenarAnimalesPorPeso();

        //4.3 Mostrar el animal más pesado

        gestor.mostrarAnimalMasPesado();

    }
    
}
