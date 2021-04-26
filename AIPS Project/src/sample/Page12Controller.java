package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.ProgressBar;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.*;
import java.net.URL;
import java.util.ResourceBundle;

public class Page12Controller implements Initializable {

    @FXML
    private ProgressBar progressBar;
    TextField portNumber;
    private String port = "";
    private Stage stage;
    private Scene scene;
    private Parent root;
    private String path ="/home/host/Documents/Project/full_scan.log";
    //private String pathDirSearch="cd C:\\Users\\saura\\Documents\\Project\\Dirito";
    private String fileForDirSearch ="";
    private String fileForSubDomain ="";
    private String domain="";
    private String ip="";
    private double progress=0;

    public void start() {

        try {
            // Just one line and you are done !
            // We have given a command to start cmd
            // /K : Carries out command specified by string

            PrintStream o = new PrintStream(new File(path));
            File file = new File(path);
            System.setOut(o);
            String ip_address = "http://"+ip+":8000";
            increaseProgress();
            Process p1 = Runtime.getRuntime().exec("python3 /home/host/Documents/Project/Scholz/scholz.py "+ip+" 65535");
            p1.waitFor();
            BufferedReader reader = new BufferedReader(new InputStreamReader((p1.getInputStream())));
            String line = "";
            while((line=reader.readLine()) != null){
                System.out.println(line);
            }
            System.out.println("------------------------------------------------------------------------ TCP ------------------------------------------------------------------------------");
            Process p2 = Runtime.getRuntime().exec("python3 /home/host/Documents/Project/Scholz/tcp_scan.py "+ip+" 65535");
            p2.waitFor();
           BufferedReader reader2 = new BufferedReader(new InputStreamReader(p2.getInputStream()));
           while((line=reader2.readLine()) != null){
               System.out.println(line);
           }
            System.out.println("------------------------------------------------------------------------ UDP ------------------------------------------------------------------------------");
            Process p3 = Runtime.getRuntime().exec("python3 /home/host/Documents/Project/Scholz/udp_scan.py "+ip+" "+port+"");
            p3.waitFor();
            BufferedReader reader3 = new BufferedReader(new InputStreamReader(p3.getInputStream()));
            while((line=reader3.readLine()) != null){
                System.out.println(line);
            }
            System.out.println("------------------------------------------------------------------------ Dirsearch ------------------------------------------------------------------------------");
            Process p4 = Runtime.getRuntime().exec("python3 /home/host/Documents/Project/Dirito/dirsearch.py http://"+ip+":"+port+" "+fileForDirSearch+"");
            p4.waitFor();
            BufferedReader reader4 = new BufferedReader(new InputStreamReader(p4.getInputStream()));
            while((line=reader4.readLine()) != null){
                System.out.println(line);
            }
            System.out.println("------------------------------------------------------------------------ SUBDOMAIN ------------------------------------------------------------------------------");
            Process p5 = Runtime.getRuntime().exec("python3 /home/host/Documents/Project/Dirito/domain_enum.py "+domain+" "+fileForSubDomain+"");
            p5.waitFor();
            BufferedReader reader5 = new BufferedReader(new InputStreamReader(p5.getInputStream()));
            while((line=reader5.readLine()) != null){
                System.out.println(line);
            }
            System.out.println("------------------------------------------------------------------------ NIKTO ------------------------------------------------------------------------------");
            Process p6 = Runtime.getRuntime().exec("nikto -h "+ip+":"+port+"");
            p6.waitFor();
            BufferedReader reader6 = new BufferedReader(new InputStreamReader(p6.getInputStream()));
            while((line=reader6.readLine()) != null){
                System.out.println(line);
            }
            Main.stage.close();
            Runtime.getRuntime().exec("gedit /home/host/Documents/Project/full_scan.log");
        } catch (Exception a) {
            System.out.println("HEY Buddy ! U r Doing Something Wrong ");
            a.printStackTrace();
        }
    }

    public void terminate(ActionEvent e) throws IOException {
        progressBar.setProgress(0);
        root = FXMLLoader.load(getClass().getResource("Page2.fxml"));
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

    public void setFileForDirSearch(String fileForDirSearch) {
        this.fileForDirSearch = fileForDirSearch;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }

    public void setFileForSubDomain(String fileForSubDomain) {
        this.fileForSubDomain = fileForSubDomain;
    }

    public void setPort(String port) {
        this.port = port;
    }
}

