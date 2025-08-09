// Simple utilitario que lista nombres de almacenes desde la consola.
// No es necesario para correr la app en Flask, es un añadido Java.
import java.util.*;
public class WarehouseClient {
    public static void main(String[] args) {
        System.out.println("DisetekSolution - Cliente Java");
        List<String> warehouses = Arrays.asList("MiniBox Centro", "Storage Plus", "Large Depot");
        for (int i=0;i<warehouses.size();i++){
            System.out.printf("%d. %s\n", i+1, warehouses.get(i));
        }
    }
}
