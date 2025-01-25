package net.runelite.client.plugins.skeletonplugin;

import net.runelite.client.config.Config;
import net.runelite.client.config.ConfigGroup;
import net.runelite.client.config.ConfigItem;

@ConfigGroup("skeletonplugin")
public interface SkeletonPluginConfig extends Config
{
    @ConfigItem(
            keyName = "exampleSetting",
            name = "Example Setting",
            description = "An example configuration setting"
    )
    default boolean exampleSetting()
    {
        return false;
    }
}
