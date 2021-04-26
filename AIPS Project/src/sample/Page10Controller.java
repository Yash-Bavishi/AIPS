package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.ProgressBar;
import javafx.scene.control.TextField;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.io.*;
import java.net.URL;
import java.util.ResourceBundle;

public class Page10Controller implements Initializable  {

    @FXML
    TextField domainName;
    @FXML
    private ProgressBar progressBar;

    private FileChooser wordlist = new FileChooser();
    private String fileName ="";
    private String domain="";
    private Stage stage;
    private Scene scene;
    private Parent root;
    private boolean fileChosen = false;
    private double progress=0;
    private String path="/home/host/Documents/Project/Dirito/domain_log.txt";
    private String ip =  "";


    public void start(ActionEvent e) throws IOException {

        domain = domainName.getText();
            System.out.println(domain);
        if(DomainChecker.isValidDomainName(domain)){
                if (fileChosen == true) {
                    try {
                        // Just one line and you are done !
                        // We have given a command to start cmd
                        // /K : Carries out command specified by string

                        PrintStream o = new PrintStream(new File(path));
                        File file = new File(path);
                        System.setOut(o);
                        String ip_address = "http://"+ip+":8000";
                        increaseProgress();
                        Process pr = Runtime.getRuntime().exec("python3 /home/host/Documents/Project/Dirito/domain_enum.py "+domain+" "+fileName+"");
                        pr.waitFor();
                        BufferedReader reader = new BufferedReader(new InputStreamReader((pr.getInputStream())));
                        String line = "";
                        while((line=reader.readLine()) != null){
                            System.out.println(line);
                        }
                        Main.stage.close();
                        Runtime.getRuntime().exec("gedit /home/host/Documents/Project/Dirito/domain_log.txt");
                    } catch (Exception a) {
                        System.out.println("HEY Buddy ! U r Doing Something Wrong ");
                        a.printStackTrace();
                    }
                } else {
                    Alert alert = new Alert(Alert.AlertType.ERROR);
                    alert.setTitle("Select a File");
                    alert.setContentText("You haven't  Chosen a File yet!!! ");
                    alert.showAndWait();
                }
            }
            else {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Invalid Domain Name");
            alert.setContentText("The Domain Name you entered "+ domain + " is Invalid!!");
            alert.showAndWait();
            }
    }

    public void fileChooser(){

        FileChooser.ExtensionFilter extFilter = new FileChooser.ExtensionFilter("TXT files (*.txt)", "*.txt");
        wordlist.getExtensionFilters().add(extFilter);
        File selectedFile = wordlist.showOpenDialog(null);
        if(selectedFile!= null){
            fileName = selectedFile.getAbsolutePath();
            System.out.println(fileName);
            fileChosen =true;
        }


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
