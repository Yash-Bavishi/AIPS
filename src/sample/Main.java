package sample;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;

import javafx.scene.Parent;
import javafx.scene.Scene;

import javafx.scene.control.Button;
import javafx.scene.image.Image;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

public class Main extends Application {

    static Scene general;
    static Stage stage;


    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {
        this.stage = stage;
        try {
            Parent page1Root = FXMLLoader.load(getClass().getResource("Page1.fxml"));

            Image logo = new Image("shield.png");
            stage.getIcons().add(logo);


            //Page1
            Scene page1 = new Scene(page1Root, Color.WHITESMOKE);
            general = page1;

            stage.setResizable(false);
            stage.setTitle("AIPS");
            stage.setScene(general);
            stage.show();
        }
        catch (Exception e){
            e.printStackTrace();
        }


    }



}
