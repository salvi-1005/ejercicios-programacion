import java.util.ArrayList;

public class GestorAnimales {

    private ArrayList<Animal> animales;

    public GestorAnimales(){
        this.animales = new ArrayList<>();
    }

    public void agregarAnimal(Animal animal){
        animales.add(animal);
    }

    public void mostrarAnimales(){
        System.out.println("=== 4.1 LISTA DE ANIMALES ===");
        for (Animal animal : animales){
            System.out.println(animal.toString());
        }
    }

    public void ordenarAnimalesPorPeso(){
        System.out.println("=== 4.2. ANIMALES ORDENADOS POR PESO (menor a mayor) ===");
        animales.sort((p1, p2) -> Double.compare(p1.getPeso(), p2.getPeso()));
        for (Animal animal : animales){
            System.out.println(animal.getNombre() + " - " + animal.getPeso() + " kg");
        }
    }

    public void mostrarAnimalMasPesado(){
        Animal animalMasPesado = null;
        for (Animal animal : animales){
            if (animalMasPesado == null || animal.getPeso() > animalMasPesado.getPeso()){
                animalMasPesado = animal;
            }
        }
        if (animalMasPesado != null){
            System.out.println("=== ANIMAL MAS PESADO =: " + animalMasPesado.getNombre() + " - " + animalMasPesado.getPeso() + " kg");
        } else{
            System.out.println("No hay animales en la lista");
        }
    }
    
}
