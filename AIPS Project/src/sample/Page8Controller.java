package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.ProgressBar;
import javafx.stage.Stage;

import java.io.IOException;

public class Page8Controller {
    @FXML
    private ProgressBar progressBar;
    private String ip;
    private Stage stage;
    private Scene scene;
    private Parent root;
    private double progress=0;


    public void dirSearch(ActionEvent e) throws IOException {

        FXMLLoader loader = new FXMLLoader(getClass().getResource("Page9.fxml"));
        root = loader.load();

        Page9Controller page9controller = loader.getController();
        page9controller.setIp(ip);


        stage = (Stage)((Node)e.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();

    }

    public void subDomain(ActionEvent e) throws IOException {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("Page10.fxml"));
        root = loader.load();

        Page10Controller page10Controller =loader.getController();
        page10Controller.setIp(ip);


        stage = (Stage)((Node)e.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();


    }

    public void setIp(String ip) {
        this.ip = ip;
    }


}
