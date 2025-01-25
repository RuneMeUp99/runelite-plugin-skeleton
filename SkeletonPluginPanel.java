package net.runelite.client.plugins.skeletonplugin;

import javax.swing.*;
import net.runelite.client.ui.PluginPanel;

public class SkeletonPluginPanel extends PluginPanel
{
    public SkeletonPluginPanel()
    {
        // Add simple UI components to the panel
        setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));

        JLabel label = new JLabel("Skeleton Plugin Panel");
        JButton button = new JButton("Click Me");

        button.addActionListener(e -> JOptionPane.showMessageDialog(this, "Button Clicked!"));

        add(label);
        add(button);
    }
}
