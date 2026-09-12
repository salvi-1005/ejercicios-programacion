public class Termometro implements Medible {
    
    private float temperatura;
    
    public Termometro(int temp){
        this.temperatura = temp;
    }

    @Override
    public float obtenerMedida(){
        return this.temperatura;
    }

    @Override
    public float incrementar(float inc){
        return this.temperatura + inc;
    };

    @Override
    public float decrementar(float dec){
        try {
            if (this.temperatura - dec < -273) {
                throw new ArithmeticException();
            }
        }
        catch (ArithmeticException e) {
            System.out.println("Error: La temperatura no puede ser menor que -273°C");
        } finally {
            System.out.println("Finalizando proceso.");
        }
        return this.temperatura - dec;
    
    }
}
