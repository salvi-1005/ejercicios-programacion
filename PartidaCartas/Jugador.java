public class Jugador{

    private Carta[] mano;
    private String nombre;

    public Jugador(String nombre) {
        this.nombre = nombre;
        this.mano = new Carta[5];
    }

    public String getNombre() {
        return nombre;
    }

    public Carta[] getMano() {
        return mano;
    }

    
    public void agregarCarta(Carta carta) {
        for (int i = 0; i < mano.length; i++) {
            if (mano[i] == null) {
                mano[i] = carta;
                break;
            }
        }
    }


    public void vaciarMano() {
        for (int i = 0; i < mano.length; i++) {
            mano[i] = null;
        }
    }

    public int getPuntos() {
        Carta[] manoNueva = new Carta[5];
        for (int i = 0; i < mano.length; i++) {
            if (mano[i] != null && (mano[i].getValor() == "1" || mano[i].getValor() == "2" || mano[i].getValor() == "3" || mano[i].getValor() == "4" || mano[i].getValor() == "5" || mano[i].getValor() == "6" || mano[i].getValor() == "7" || mano[i].getValor() == "8" || mano[i].getValor() == "9" || mano[i].getValor() == "10")) {
                manoNueva[i] = mano[i];
            }
            if (mano[i] != null && mano[i].getValor() == "J") {
                manoNueva[i] = new Carta(mano[i].getPalo(), "11");
            }
            if (mano[i] != null && mano[i].getValor() == "Q") {
                manoNueva[i] = new Carta(mano[i].getPalo(), "12");
            }
            if (mano[i] != null && mano[i].getValor() == "K") {
                manoNueva[i] = new Carta(mano[i].getPalo(), "13");
            }
        }
        int puntos = 0;
        for (Carta carta : manoNueva) {
            if (carta != null) {
                puntos += Integer.parseInt(carta.getValor());
            }
        }
        return puntos;
    }

    public boolean tieneCartasDelMismoPalo() {
        String palo = null;
        for (Carta carta : mano) {
            if (carta != null) {
                if (palo == null) {
                    palo = carta.getPalo();
                } else if (!palo.equals(carta.getPalo())) {
                    return false;
                }
            }
        }
        return true;
    }

    public boolean tieneCartasDelMismoColor() {
        String color = null;
        for (Carta carta : mano) {
            if (carta != null) {
                String palo = carta.getPalo();
                String colorActual;
                if (palo.equals("Corazones") || palo.equals("Diamantes")) {
                    colorActual = "Rojo";
                } else {
                    colorActual = "Negro";
                }

                if (color == null) {
                    color = colorActual;
                } else if (!color.equals(colorActual)) {
                    return false;
                }
            }
        }
        return true;
    }

    public boolean tieneEscalera() {
        int[] valores = new int[5];
        int index = 0;
        for (Carta carta : mano) {
            if (carta != null) {
                valores[index++] = Integer.parseInt(carta.getValor());
            }
        }
        java.util.Arrays.sort(valores);
        for (int i = 1; i < index; i++) {
            if (valores[i] != valores[i - 1] + 1) {
                return false;
            }
        }
        return true;
    }

    public int cantidadDeCartasConElMismoValor() {
        int[] conteo = new int[14]; // Índices del 1 al 13 para las cartas
        for (Carta carta : mano) {
            if (carta != null) {
                int valor = Integer.parseInt(carta.getValor());
                conteo[valor]++;
            }
        }
        int maxConteo = 0;
        for (int c : conteo) {
            if (c > maxConteo) {
                maxConteo = c;
            }
        }
        return maxConteo;
    }

    public int cualEsElNumeroDeDosDigitosMasAltoQueSePuedeFormarConCartasDel1al9sinContarJQyK() {
        int[] valores = new int[5];
        int index = 0;
        Carta[] manoNueva = new Carta[5];
        for (int i = 0; i < mano.length; i++) {
            if (mano[i] != null && (mano[i].getValor() == "1" || mano[i].getValor() == "2" || mano[i].getValor() == "3" || mano[i].getValor() == "4" || mano[i].getValor() == "5" || mano[i].getValor() == "6" || mano[i].getValor() == "7" || mano[i].getValor() == "8" || mano[i].getValor() == "9")) {
                manoNueva[i] = mano[i];
            }
        }
        for (Carta carta : manoNueva) {
            if (carta != null && Integer.parseInt(carta.getValor()) >= 1 && Integer.parseInt(carta.getValor()) <= 9) {
                valores[index++] = Integer.parseInt(carta.getValor());
            }
        }
        java.util.Arrays.sort(valores);
        if (index < 2) {
            return -1; // No se pueden formar números de dos dígitos
        }
        return valores[index - 1] * 10 + valores[index - 2]; // El número más alto se forma con las dos cartas más altas
        
    }

}