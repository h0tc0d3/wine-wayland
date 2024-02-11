# Build Wine with NtSync patches

Build kernel with `kernel-ntsync.patch` patch.

Apply patches to Wine and Wine-Staging.

```bash
git clone https://gitlab.winehq.org/wine/wine.git
cd wine
git clean -fd
git reset --hard
git checkout tags/wine-9.2 -b ntsync_dev
git am ../wine-wayland/ntsync/0001-winewayland.drv-Advertise-common-display-modes.patch
git am ../wine-wayland/ntsync/0002-winewayland.drv-Advertise-display-modes-for-8-bpp-an.patch
git am ../wine-wayland/ntsync/0003-winewayland.drv-Dissociate-current-display-mode-from.patch
git am ../wine-wayland/ntsync/0004-winewayland.drv-Respect-current-device-mode-on-displ.patch
git am ../wine-wayland/ntsync/0005-winewayland.drv-Associate-each-GDI-adapter-with-its-.patch
git am ../wine-wayland/ntsync/0006-winewayland.drv-Adjust-window-scaling-based-on-the-m.patch
git am ../wine-wayland/ntsync/0007-winewayland.drv-Refresh-surfaces-after-display-confi.patch
git am ../wine-wayland/ntsync/0008-user32-tests-Test-that-display-settings-are-restored.patch
git am ../wine-wayland/ntsync/0009-winex11.drv-Call-X11DRV_DisplayDevices_RegisterEvent.patch
git am ../wine-wayland/ntsync/0010-winex11.drv-Process-events-in-X11DRV_GetCurrentDispl.patch
git am ../wine-wayland/ntsync/0011-win32u-explorer-Restore-display-settings-on-process-.patch
git am ../wine-wayland/ntsync/0012-ntdll-Better-track-thread-pool-wait-s-wait_pending-s.patch
git am ../wine-wayland/ntsync/0013-ntdll-Make-sure-wakeups-from-already-unset-events-ar.patch
git am ../wine-wayland/ntsync/0014-wined3d-Merge-shader_load_constants-into-shader_sele.patch
git am ../wine-wayland/ntsync/0015-wined3d-Introduce-a-separate-vp_disable-method.patch
git am ../wine-wayland/ntsync/0016-wined3d-Introduce-a-separate-fp_disable-method.patch
git am ../wine-wayland/ntsync/0017-wined3d-Pass-a-wined3d_state-pointer-to-the-vp_enabl.patch
git am ../wine-wayland/ntsync/0018-wined3d-Pass-a-non-const-wined3d_context-pointer-to-.patch
git am ../wine-wayland/ntsync/0019-wined3d-arb-Move-fragment-program-compilation-from-f.patch
git am ../wine-wayland/ntsync/0020-ntdll-Avoid-sending-context-in-wait_suspend-when-not.patch
git am ../wine-wayland/ntsync/0021-winewayland.drv-Add-unaccelerated-pointer-support.patch
git am ../wine-wayland/ntsync/0022-Replace-CLOCK_MONOTONIC_RAW-with-CLOCK_MONOTONIC.patch
git am ../wine-wayland/ntsync/0023-Add-ntsync-support.patch
git am ../wine-wayland/ntsync/0024-Add-Steam-support.patch
git am ../wine-wayland/ntsync/0025-Add-EasyAnticheat.patch
git am ../wine-wayland/ntsync/0026-Fix-Battle.net-client.patch
git am ../wine-wayland/ntsync/0027-Update-configure-files.patch
cd ..

git clone https://gitlab.winehq.org/wine/wine-staging.git
cd wine-staging
git checkout tags/v9.2 -b ntsync_dev
git am ../wine-wayland/ntsync/wine-staging.patch
cd ..
```

Build Wine:

```bash
#!/usr/bin/bash

SOURCE_DIR="${HOME:?}/code"
BUILD_DIR="/tmp/build-wine"
INSTALL_DIR="${HOME:?}/wine"
BUILD_CFLAGS="-march=native -mtune=native"
BUILD_CFLAGS_32="-mtune=native -I/usr/include/freetype2 -I/usr/include/gstreamer-1.0 -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include"

BUILD_OPTIONS=(
    --x-includes=/usr/include
    --with-x
    --with-wayland
    --with-vulkan
    --with-dbus
    --with-gstreamer
    --without-cups
    --without-sane
    --without-capi
    --without-gphoto
    --without-unwind
    --without-pcap
    --without-v4l2
    --without-xinputwinebuild   
    --without-xinerama
    --disable-tests
    --disable-win16
)

set -euo pipefail

rm -fr "${BUILD_DIR:?}"
mkdir -p "${BUILD_DIR:?}"

unset CPPFLAGS
unset CFLAGS
unset CXXFLAGS
unset LDFLAGS

cd "${SOURCE_DIR:?}/wine"
git reset --hard
git clean -fd

export CPPFLAGS="${BUILD_CFLAGS:?}"
export CFLAGS="${BUILD_CFLAGS:?}"
export CXXFLAGS="${BUILD_CFLAGS:?}"
export LDFLAGS="-Wl,-O1 -Wl,--as-needed -Wl,--no-copy-dt-needed-entries -Wl,--sort-common -Wl,--hash-style=gnu"

python "${SOURCE_DIR:?}/wine-staging/staging/patchinstall.py" DESTDIR="${SOURCE_DIR:?}/wine" \
    dsound-Fast_Mixer \
    gdiplus-Performance-Improvements \
    loader-KeyboardLayouts \
    ntdll-APC_Performance \
    ntdll-HashLinks \
    ntdll-Hide_Wine_Exports \
    ntdll-Serial_Port_Detection \
    ntdll-Junction_Points \
    ntdll-NtDevicePath \
    ntdll-ProcessQuotaLimits \
    ntdll-RtlQueryPackageIdentity \
    ntdll_reg_flush \
    programs-where \
    server-File_Permissions \
    server-Stored_ACLs \
    server-default_integrity \
    setupapi-DiskSpaceList \
    setupapi-DriverStoreFindDriverPackageW \
    kernel32-CopyFileEx \
    shell32-SHFileOperation_Move \
    shell32-Progress_Dialog \
    shell32-ACE_Viewer \
    shell32-Context_Menu \
    shell32-IconCache \
    shell32-NewMenu_Interface \
    shell32-SFGAO_HASSUBFOLDER \
    shell32-SHGetStockIconInfo \
    shell32-registry-lookup-app \
    shlwapi-AssocGetPerceivedType \
    shlwapi-UrlCanonicalize \
    shlwapi-UrlCombine \
    user32-DM_SETDEFID \
    user32-Dialog_Paint_Event \
    user32-DrawTextExW \
    user32-FlashWindowEx \
    user32-Implement-CascadeWindows \
    user32-ListBox_Size \
    user32-LoadKeyboardLayoutEx \
    user32-Refresh_MDI_Menus \
    user32-ScrollWindowEx \
    user32-message-order \
    user32-msgbox-Support-WM_COPY-mesg \
    vcomp_for_dynamic_init_i8 \
    windows.networking.connectivity-new-dll \
    windowscodecs-GIF_Encoder \
    windowscodecs-TIFF_Support \
    wined3d-Accounting \
    wined3d-atomic_minmax_merge \
    wined3d-bindless-texture \
    wined3d-mesa_texture_download \
    wined3d-rotate-WINED3D_SWAP_EFFECT_DISCARD \
    wined3d-unset-flip-gdi \
    wined3d-WINED3DFMT_B8G8R8X8_UNORM \
    wined3d-wined3d_guess_gl_vendor \
    wined3d-zero-inf-shaders \
    winedevice-Default_Drivers \
    winepulse-PulseAudio_Support \
    winepulse-aux_channels \
    wintrust-WTHelperGetProvCertFromChain

rm -fr "${BUILD_DIR:?}/wine-64"
mkdir "${BUILD_DIR:?}/wine-64"
cd "${BUILD_DIR:?}/wine-64"

"${SOURCE_DIR:?}/wine/configure" \
    --prefix="${INSTALL_DIR:?}" \
    --libdir="${INSTALL_DIR:?}/lib64" \
    --x-libraries=/usr/lib64 \
    --with-system-dllpath=/usr/i686-w64-mingw32 \
    --enable-win64 \
    ${BUILD_OPTIONS[@]}

make -j$(nproc)

export CPPFLAGS="${BUILD_CFLAGS_32:?}"
export CFLAGS="${BUILD_CFLAGS_32:?}"
export CXXFLAGS="${BUILD_CFLAGS_32:?}"

rm -fr "${BUILD_DIR:?}/wine-32"
mkdir "${BUILD_DIR:?}/wine-32"
cd "${BUILD_DIR:?}/wine-32"

"${SOURCE_DIR:?}/wine/configure" \
    --prefix="${INSTALL_DIR:?}" \
    --libdir="${INSTALL_DIR:?}/lib" \
    --x-libraries=/usr/lib \
    --with-system-dllpath=/usr/x86_64-w64-mingw32 \
    --with-wine64="${BUILD_DIR:?}/wine-64" \
    ${BUILD_OPTIONS[@]}

make -j$(nproc)

rm -fr "${INSTALL_DIR:?}"
mkdir -p "${INSTALL_DIR:?}"

cd "${BUILD_DIR:?}/wine-32"
make -j$(nproc) prefix="${INSTALL_DIR:?}" \
    libdir="${INSTALL_DIR:?}/lib" \
    dlldir="${INSTALL_DIR:?}/lib/wine" install

cd "${BUILD_DIR:?}/wine-64"
make -j$(nproc) prefix="${INSTALL_DIR:?}" \
    libdir="${INSTALL_DIR:?}/lib64" \
    dlldir="${INSTALL_DIR:?}/lib64/wine" install

rm -fr "${BUILD_DIR:?}/wine-32"
rm -fr "${BUILD_DIR:?}/wine-64"
rm -fr "${BUILD_DIR:?}"
```
