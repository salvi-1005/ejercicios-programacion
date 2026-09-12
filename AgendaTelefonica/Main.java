public class Main {
    
    public static void main(String[] args){
        Individuo individuo1 = new Individuo("Salvador D'Angelo", "Nazarre 4711", "41877247");
        Individuo individuo2 = new Individuo("Juan Pérez", "Calle Falsa 123", "55512345");
        Individuo individuo3 = new Individuo("María Gómez", "Avenida Siempre Viva 456", "55567890");
        AgendaTelefonica agenda = new AgendaTelefonica(3);
        agenda.agregarIndividuo(individuo1, 0);
        agenda.agregarIndividuo(individuo2, 1);
        agenda.agregarIndividuo(individuo3, 2);
        agenda.buscarIndividuo("Juan Pérez");
        agenda.eliminarIndividuo("Juan Pérez");
        agenda.buscarIndividuo("Juan Pérez");
        
    }

}
