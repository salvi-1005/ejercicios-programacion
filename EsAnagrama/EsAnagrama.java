public class EsAnagrama {
    
    private String cadena1;
    private String cadena2;

    public EsAnagrama(String cadena1, String cadena2){
        this.cadena1 = cadena1;
        this.cadena2 = cadena2;
    }

    public boolean esAnagrama(){
        String c1 = this.cadena1.replaceAll("\\s+", "").toLowerCase();
        String c2 = this.cadena2.replaceAll("\\s+", "").toLowerCase();

        if (c1.length() != c2.length()) {
            return false;
        }

        char[] arr1 = c1.toCharArray();
        char[] arr2 = c2.toCharArray();

        java.util.Arrays.sort(arr1);
        java.util.Arrays.sort(arr2);

        return java.util.Arrays.equals(arr1, arr2);
    }

}
