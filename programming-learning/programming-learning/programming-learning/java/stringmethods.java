

public class stringmethods {
    public static void main(String[] args){
        String sc;
        sc="Vivek kumar ";
        System.out.println(sc);
        System.out.println(sc.length());
        System.out.println(sc.toLowerCase());
        System.out.println(sc.toUpperCase());
        System.out.println(sc.trim()); // remove all spaces of leading and trailing of the iriginal string and forms a new string
        System.out.println(sc.substring(3)); 
        System.out.println(sc.substring(3,7));
        System.out.println(sc.replace("V","c"));
        System.out.println(sc.startsWith("v"));// satisfies then true otherwise false
        System.out.println(sc.endsWith(" ")); // satisfies then true otherwise false
        System.out.println(sc.charAt(0));
        System.out.println(sc.indexOf("K"));// if not satisfies then result will be -1
        System.out.println(sc.lastIndexOf("k"));
        System.out.println(sc.indexOf("v",1));
        System.out.println(sc.lastIndexOf("v",5));
        System.out.println(sc.equals("Vivek kumar "));
        System.out.println(sc.equalsIgnoreCase("VIVEK KUMAR "));

    }
}

// escape sequence character............:
//   1. \n-----> new line     2.\t ------> tab         3. \ ------->single quote      4. \\ -----> backslash
