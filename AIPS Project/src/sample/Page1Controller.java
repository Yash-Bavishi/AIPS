package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import java.net.Inet4Address;
import java.net.UnknownHostException;

import java.io.IOException;

public class Page1Controller {
    @FXML
    TextField ipAddressid;

    private Stage stage;
    private Scene scene;
    private Parent root;
    private static String  ip;

    public void selectMethod(ActionEvent e) throws IOException {

        ip = ipAddressid.getText();
        if(ipChecker(ip)){

            //root = FXMLLoader.load(getClass().getResource("Page2.fxml"));
            FXMLLoader loader = new FXMLLoader(getClass().getResource("Page2.fxml"));
            root = loader.load();

            Page2Controller page2controller = loader.getController();
            page2controller.setIp(ip);

            stage = (Stage)((Node)e.getSource()).getScene().getWindow();
            scene = new Scene(root);
            stage.setScene(scene);
            stage.show();
        }
        else{
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Invalid Ip Address");
            alert.setContentText("The Ip Address you entered "+ ip + " is Invalid!!");
            alert.showAndWait();
        }



    }

    public boolean ipChecker(String ip){
        try {
            return Inet4Address.getByName(ip).getHostAddress().equals(ip);
        }
        catch (UnknownHostException ex) {
            return false;
        }
    }

}
