package net.runelite.client.plugins.skeletonplugin;

import javax.inject.Inject;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics2D;
import net.runelite.api.Client;
import net.runelite.client.ui.overlay.Overlay;
import net.runelite.client.ui.overlay.OverlayLayer;
import net.runelite.client.ui.overlay.OverlayPosition;

public class SkeletonOverlay extends Overlay
{
    private final Client client;
    private final SkeletonPluginConfig config;

    @Inject
    public SkeletonOverlay(Client client, SkeletonPluginConfig config)
    {
        this.client = client;
        this.config = config;
        setPosition(OverlayPosition.DYNAMIC);
        setLayer(OverlayLayer.ABOVE_SCENE);
    }

    @Override
    public Dimension render(Graphics2D graphics)
    {
        // Draw a simple rectangle on the screen
        graphics.setColor(Color.CYAN);
        graphics.drawString("Skeleton Overlay Active", 50, 50);
        return null;
    }
}
