# Settings here will take effect for all games run in this Proton version.

user_settings = {
    # By default, logs are saved to $HOME/steam-<STEAM_GAME_ID>.log, overwriting any previous log with that name.
    # Log directory can be overridden with $PROTON_LOG_DIR.

    # Enable logging
    #"PROTON_LOG": "1",

    # Custom Wine debug logging
    #"WINEDEBUG": "+timestamp,+pid,+tid,+seh,+unwind,+threadname,+debugstr,+loaddll,+mscoree",

    # DXVK debug logging
    #"DXVK_LOG_LEVEL": "info",

    # vkd3d debug logging
    #"VKD3D_DEBUG": "warn",

    #vkd3d-shader debug logging
    #"VKD3D_SHADER_DEBUG": "fixme",

    # Wine-Mono debug logging (Wine's .NET replacement)
    #"WINE_MONO_TRACE": "E:System.NotImplementedException",
    #"MONO_LOG_LEVEL": "info",

    # Enable futex-based in-process synchronization primitives, default enabled
    #"FSYNC": "1",
    
    # Enable Wayland
    #"WAYLAND": "1",
    # Enable Realtime scheduling
    "REALTIME": "1",

    # Custom ENV settings
    #"DXVK_CONFIG_FILE": "/home/user/Games/overwatch/dxvk.conf",
    #"RADV_PERFTEST": "sam,nggc",
    #"VK_DRIVER_FILES": "/usr/share/vulkan/icd.d/radeon_icd.i686.json:/usr/share/vulkan/icd.d/radeon_icd.x86_64.json",
}
