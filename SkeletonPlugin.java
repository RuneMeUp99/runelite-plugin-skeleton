package net.runelite.client.plugins.skeletonplugin;

import com.google.inject.Provides;
import javax.inject.Inject;
import lombok.extern.slf4j.Slf4j;
import net.runelite.api.Client;
import net.runelite.client.config.ConfigManager;
import net.runelite.client.eventbus.Subscribe;
import net.runelite.client.events.GameTick;
import net.runelite.client.plugins.Plugin;
import net.runelite.client.plugins.PluginDescriptor;
import net.runelite.client.ui.overlay.OverlayManager;

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
    private SkeletonPluginPanel skeletonPluginPanel;

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
    }

    @Override
    protected void shutDown() throws Exception
    {
        log.info("Skeleton Plugin stopped!");
        overlayManager.remove(skeletonOverlay);
    }

    @Subscribe
    public void onGameTick(GameTick gameTick)
    {
        log.debug("Game tick detected!");
        // Example: Add logic to update the overlay or plugin panel here
    }
}
