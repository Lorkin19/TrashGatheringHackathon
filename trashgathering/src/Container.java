import java.io.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

public class Container {
    private String id;
    private Map<Date, List<String>> containerHistorico;

    public Container(String id){
        this.id = id;
        this.containerHistorico = new HashMap<>();
    }

    private void addLineaToMap(List<String> linea){
        SimpleDateFormat formatter = new SimpleDateFormat("dd/mm/yyyy");
        try {
            Date fecha = formatter.parse(linea.get(0));
            containerHistorico.putIfAbsent(fecha, linea.subList(1, linea.size()));
        } catch (ParseException e) {
            e.printStackTrace();
        }
    }

    public void readHistorico(String fileName){
        File historico = new File(fileName);
        FileReader fr;
        BufferedReader bf;
        try {
            fr = new FileReader(historico);
            bf = new BufferedReader(fr);

            String linea = bf.readLine();
            String[] datos;
            while (linea != null){
                datos = linea.split("#");
                addLineaToMap(Arrays.asList(datos));
                linea = bf.readLine();
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public List<String> dameDatosDeFecha(Date fecha){
        List<String> listaDatos = containerHistorico.get(fecha);
        return (listaDatos != null) ? listaDatos : new ArrayList<String>();
    }
}