package net.runelite.client.plugins.skeletonplugin;

import com.google.inject.Provides;
import javax.inject.Inject;
import net.runelite.client.ui.ClientToolbar;
import net.runelite.client.ui.NavigationButton;
import net.runelite.client.ui.PluginPanel;
import lombok.extern.slf4j.Slf4j;
import net.runelite.api.Client;
import net.runelite.client.config.ConfigManager;
import net.runelite.client.eventbus.Subscribe;
import net.runelite.api.events.GameTick;
import net.runelite.client.plugins.Plugin;
import net.runelite.client.plugins.PluginDescriptor;
import net.runelite.client.ui.overlay.OverlayManager;
import java.awt.image.BufferedImage;
import net.runelite.client.util.ImageUtil;

@Slf4j
@PluginDescriptor(
        name = "Skeleton Plugin",
        description = "A starting template for creating new plugins",
        tags = {"skeleton", "template", "plugin"}
)
public class SkeletonPlugin extends Plugin
{
    @Inject
    private Client client;

    @Inject
    private OverlayManager overlayManager;

    @Inject
    private SkeletonOverlay skeletonOverlay;

    @Inject
    private ClientToolbar clientToolbar;

    @Inject
    private SkeletonPluginPanel panel;

    private NavigationButton navButton;

    @Provides
    SkeletonPluginConfig provideConfig(ConfigManager configManager)
    {
        return configManager.getConfig(SkeletonPluginConfig.class);
    }

    @Override
    protected void startUp() throws Exception
    {
        log.info("Skeleton Plugin started!");
        overlayManager.add(skeletonOverlay);

        // Load an icon for the navigation button
        final BufferedImage icon = ImageUtil.loadImageResource(getClass(), "/net/runelite/client/plugins/skeletonplugin/skeleton_icon.png");
        if (icon == null)
        {
            throw new IllegalStateException("Icon could not be loaded. Check if skeleton_icon.png exists and is valid.");
        }

        navButton = NavigationButton.builder()
                .tooltip("Skeleton")
                .icon(icon) // Ensure this is the valid icon
                .panel(panel)
                .build();


        // Add the navigation button to the client toolbar
        clientToolbar.addNavigation(navButton);
    }

    @Override
    protected void shutDown() throws Exception
    {
        log.info("Skeleton Plugin stopped!");
        overlayManager.remove(skeletonOverlay);

        // Remove the navigation button
        clientToolbar.removeNavigation(navButton);
    }

    @Subscribe
    public void onGameTick(GameTick gameTick)
    {
        log.debug("Game tick detected!");
        // Example: Add logic to update the overlay or plugin panel here
    }
}
