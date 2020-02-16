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
	MainScreenPanel buttonPanel = null;

	public MainScreen() {

		buttonPanel = new MainScreenPanel();

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(0, 0, 600, 400);
		setResizable(false);
		buttonPanel.setBackground(Color.black);//背景颜色
		
		for (int i = 0; i < levels.length; i++) {//添加按钮
			levels[i] = new JRadioButton(levelStrings[i]);
			levels[i].addActionListener(this);
			levels[i].setBackground(Color.yellow);//按钮颜色
			levels[i].setBounds(260, 200 + i * 50, 80, 30);
			buttonPanel.add(levels[i]);
		}

		buttonPanel.setLayout(null);
		getContentPane().add(buttonPanel);
		setVisible(true);
	}

	public void actionPerformed(ActionEvent e) {
		Object obj = e.getSource();

		if (obj == levels[0]) {
			new GameBoardWindow(1);
		}else if (obj == levels[1]) {
			new GameBoardWindow(2);
		}else{
			new GameBoardWindow(3);
		}
		dispose();
	}

	@SuppressWarnings("serial")
	class MainScreenPanel extends JPanel {

		MainScreenPanel() {
		}

		public void paintComponent(Graphics g) {
			super.paintComponent(g);
			Graphics2D g2 = (Graphics2D) g;

			g2.setColor(Color.RED);
			g2.setFont(new Font("Comic Sans MS", Font.BOLD, 45));
			g2.drawString("Snake2D Game", 135, 85);
			g2.setColor(Color.ORANGE);
			g2.drawString("mtala3t", 210, 150);
		}
	}
}