package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.TextField;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.io.File;
import java.io.IOException;

public class Page11Controller {

    @FXML
    TextField domainName;
    @FXML
    TextField portNumber;
    private String port = "";

    private FileChooser wordlist = new FileChooser();
    private String pathForDirSearch="";
    private String pathForSubDomain="";
    private String domain="";
    private Stage stage;
    private Scene scene;
    private Parent root;

    private String ip="";

    private boolean fileChosenForDirSearch = false;
    private boolean fileChosenForSubDomain = false;

    public void fileChooserForDirSearch(){

        FileChooser.ExtensionFilter extFilter = new FileChooser.ExtensionFilter("TXT files (*.txt)", "*.txt");
        wordlist.getExtensionFilters().add(extFilter);
        File selectedFile = wordlist.showOpenDialog(null);
        if(selectedFile!= null){
            pathForDirSearch = selectedFile.getAbsolutePath();
            System.out.println(pathForDirSearch);
            fileChosenForDirSearch = true;
        }


    }

    public void fileChooserForSubDomain(){

        FileChooser.ExtensionFilter extFilter = new FileChooser.ExtensionFilter("TXT files (*.txt)", "*.txt");
        wordlist.getExtensionFilters().add(extFilter);
        File selectedFile = wordlist.showOpenDialog(null);
        if(selectedFile!= null){
            pathForSubDomain = selectedFile.getAbsolutePath();
            System.out.println(pathForSubDomain);
            fileChosenForSubDomain = true;
        }


    }

    public void fullScan(ActionEvent e) throws IOException {
        port = portNumber.getText();
        if(PortChecker.isValidPortNumber(port)) {
            System.out.println(port);
            domain = domainName.getText();
            if(fileChosenForDirSearch == true) {
                if(DomainChecker.isValidDomainName(domain)){
                    if(fileChosenForSubDomain == true){

                        FXMLLoader loader = new FXMLLoader(getClass().getResource("Page12.fxml"));
                        root = loader.load();

                        Page12Controller page12controller = loader.getController();
                        page12controller.setIp(ip);
                        page12controller.setPort(port);
                        page12controller.setDomain(domain);
                        page12controller.setFileForDirSearch(pathForDirSearch);
                        page12controller.setFileForSubDomain(pathForSubDomain);

                        stage = (Stage)((Node)e.getSource()).getScene().getWindow();
                        scene = new Scene(root);
                        stage.setScene(scene);
                        stage.show();
                    }
                    else{
                        Alert alert = new Alert(Alert.AlertType.ERROR);
                        alert.setTitle("Select a File for Sub-Domain");
                        alert.setContentText("You haven't  Chosen a File yet!!! ");
                        alert.showAndWait();
                    }
                }
                else{
                    Alert alert = new Alert(Alert.AlertType.ERROR);
                    alert.setTitle("Invalid Domain Name");
                    alert.setContentText("The Domain Name you entered "+ domain + " is Invalid!!");
                    alert.showAndWait();
                }
            }
            else{
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setTitle("Select a File for Dir-Search");
                alert.setContentText("You haven't  Chosen a File yet!!! ");
                alert.showAndWait();
            }
        }
        else{
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Port Number");
            alert.setContentText("Enter a Valid Port Number!!! ");
            alert.showAndWait();
        }
    }

    public void setIp(String ip) {
        this.ip = ip;
    }


}
