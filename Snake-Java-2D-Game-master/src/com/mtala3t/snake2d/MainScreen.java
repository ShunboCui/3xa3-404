/*
 * Main.java
 *
 * Created on 23 闱礞, 2007, 06:25 �
 *
 * To change this template, choose Tools | Template Manager
 * and open the template in the editor.
 */
package com.mtala3t.snake2d;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
/**
 *
 * @author Mohammed.Talaat (mtala3t)
 * @version 1.0
 */
public class MainScreen extends JFrame implements ActionListener {

	private static final long serialVersionUID = -1299314404835604855L;
	JRadioButton levels[] = new JRadioButton[3];
	String levelStrings[] = { "Easy", "Normal", "Hard" };
	MainScreenPanel buttonPanel;	//继承自JPanel

	public MainScreen() {
		//设置主页面框架
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(0, 0, 600, 400);
		setResizable(false);


		//设置主页面panel添加按钮
		buttonPanel = new MainScreenPanel();
		for (int i = 0; i < levels.length; i++) {	//添加三个按钮
			levels[i] = new JRadioButton(levelStrings[i]);
			levels[i].addActionListener(this);
			levels[i].setBackground(Color.yellow);	//按钮颜色
			levels[i].setBounds(260, 200 + i * 50, 80, 30);
			buttonPanel.add(levels[i]);
		}

		add(buttonPanel);

		setVisible(true);
	}

	public void actionPerformed(ActionEvent e) {
		Object obj = e.getSource();
		System.out.println(e.getSource());
		if (obj == levels[0]) {
			new GameBoardWindow(1);	//进入游戏界面with level 1
		}else if (obj == levels[1]) {
			new GameBoardWindow(2);
		}else{
			new GameBoardWindow(3);
		}
		dispose();
	}
}
