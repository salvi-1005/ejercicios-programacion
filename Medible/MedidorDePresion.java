public class MedidorDePresion implements Medible{
    
    private float unidades;
    private int incrementosConsecutivos;
    private boolean ultimoFueIncremento;

    public MedidorDePresion(){
        this.unidades = 0;
    }

    public float obtenerMedida(){
        return this.unidades;
    }

    public float incrementar(float inc){
        incrementosConsecutivos++;
        ultimoFueIncremento = true;
        return this.unidades + inc;
    }
    
    public float decrementar(float dec) {
    try {
        if (!ultimoFueIncremento) {
            throw new IllegalStateException("No se permiten dos decrementos consecutivos");
        }

        float decrementoReal = dec / incrementosConsecutivos;
        unidades -= decrementoReal;

    } catch (Exception e) {
        System.out.println(e.getMessage());
    } finally {
        System.out.println("Finalizando proceso.");
    }

    incrementosConsecutivos = 0;
    ultimoFueIncremento = false;

    return unidades;
}

}


