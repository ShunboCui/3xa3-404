package com.mtala3t.snake2d;

import javax.swing.*;
import java.awt.*;

class MainScreenPanel extends JPanel {

    MainScreenPanel(){
        setLayout(null);
        setBackground(Color.black); //背景颜色
    }

    @Override   //JPanel<-JComponent<-paintComponent()
    public void paintComponent(Graphics g) {//自动调用 最小化恢复，遮挡。。。

        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;

        g2.setColor(Color.RED);
        g2.setFont(new Font("Comic Sans MS", Font.BOLD, 45));
        g2.drawString("Snake2D Game", 135, 85);
        g2.setColor(Color.ORANGE);
        g2.drawString("mtala3t", 210, 150);

    }
}