import java.io.*;
import java.util.Date;
import java.util.List;

public class TrashGathering {

    public List<Container> containers;
    public Date fecha;

    public TrashGathering (List containers){
        this.containers = containers;
    }

    public void setFecha(Date fecha){
        this.fecha = fecha;
    }
}
