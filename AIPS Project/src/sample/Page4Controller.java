package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.ProgressBar;
import javafx.stage.Stage;

import java.io.*;
import java.net.URL;
import java.util.ResourceBundle;

public class Page4Controller implements Initializable {

    @FXML
    private ProgressBar progressBar;
    private Stage stage;
    private Scene scene;
    private Parent root;
    private String ip="sad";
    private String path="/home/host/Documents/Project/Scholz/scholz_log.txt";
    private double progress=0;

    public void start() {
        System.out.println(ip);
        try
        {
            // Just one line and you are done !
            // We have given a command to start cmd
            // /K : Carries out command specified by string
            PrintStream o = new PrintStream(new File(path));
            File file = new File(path);
            System.setOut(o);
            increaseProgress();
            //Runtime.getRuntime().exec("bash /home/host/Documents/Project/main.sh tcp "+ip+" ");
            Process pr = Runtime.getRuntime().exec("python3 /home/host/Documents/Project/Scholz/scholz.py "+ip+" 65535");
            pr.waitFor();
            BufferedReader reader = new BufferedReader(new InputStreamReader((pr.getInputStream())));
            String line = "";
            while((line=reader.readLine()) != null){
                System.out.println(line);
            }
            Main.stage.close();
            System.out.println("File cannot be opened");
            Runtime.getRuntime().exec("gedit /home/host/Documents/Project/Scholz/scholz_log.txt");
        }
        catch (Exception e)
        {
            System.out.println("HEY Buddy ! U r Doing Something Wrong ");
            e.printStackTrace();
        }

    }

    public void terminate(ActionEvent e) throws IOException {
        progressBar.setProgress(0);
        root = FXMLLoader.load(getClass().getResource("Page3.fxml"));
        stage = (Stage)((Node)e.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        progressBar.setStyle("-fx-accent:  #331800;");
    }

    public void increaseProgress(){
        while(progress < 1){
            progress += 0.1;
            progressBar.setProgress(progress);
        }
    }

    public void setIp(String ip) {
        this.ip = ip;
    }



}
