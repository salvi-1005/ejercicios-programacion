public class Main {
    public static void main(String[] args) {
        MatriculaAuto matricula = new MatriculaAuto('B', 12345678);
        try{
        if ((matricula.getLetra() == 'A' || matricula.getLetra() == 'B') && (String.valueOf(matricula.getNumero()).length() == 8 )) {
            System.out.println("Letra: " + matricula.getLetra() + " Número: " + matricula.getNumero());
        }
        if ((matricula.getLetra() != 'A' && matricula.getLetra() != 'B') && (String.valueOf(matricula.getNumero()).length() != 8 )) {
            throw new Exception("La matricula debe comenzar con 'A' o 'B' y el numero debe tener 8 digitos.");
        }
        if ((matricula.getLetra() != 'A' && matricula.getLetra() != 'B')){
            throw new Exception("La matricula debe comenzar con 'A' o 'B'.");
        }
        if (String.valueOf(matricula.getNumero()).length() != 8 ) {
            throw new Exception("El numero debe tener 8 digitos.");
        }
        } catch (Exception e) {
            System.out.println("Error: Matricula invalida. " + e.getMessage());
        } finally {
            System.out.println("Proceso de validacion de matricula finalizado.");
        }
    }
}
