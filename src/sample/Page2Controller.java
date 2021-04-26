package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.File;
import java.io.IOException;

public class Page2Controller {
    private static String ip = "";
    private Stage stage;
    private Scene scene;
    private Parent root;

    public void sochlz(ActionEvent e) throws IOException {

        FXMLLoader loader = new FXMLLoader(getClass().getResource("Page3.fxml"));
        root = loader.load();

        Page3Controller page3controller = loader.getController();
        page3controller.setIp(ip);

        stage = (Stage)((Node)e.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();


    }

    public void nikto(ActionEvent e) throws IOException {

        FXMLLoader loader = new FXMLLoader(getClass().getResource("Page7.fxml"));
        root = loader.load();

        Page7Controller page7controller = loader.getController();
        page7controller.setIp(ip);

        stage = (Stage)((Node)e.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();

        System.out.println("Nikto");
    }

    public void dirSearch(ActionEvent e) throws IOException {

        FXMLLoader loader = new FXMLLoader(getClass().getResource("Page8.fxml"));
        root = loader.load();

        Page8Controller page8controller = loader.getController();
        page8controller.setIp(ip);


        stage = (Stage)((Node)e.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();

        System.out.println("Dir-Search");
    }

    public void fullScan(ActionEvent e) throws IOException {

        FXMLLoader loader = new FXMLLoader(getClass().getResource("Page11.fxml"));
        root = loader.load();

        Page11Controller page11controller = loader.getController();
        page11controller.setIp(ip);

        stage = (Stage)((Node)e.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
        System.out.println("FullScan");
    }


    public void setIp(String ip) {
        this.ip = ip;
    }
}
