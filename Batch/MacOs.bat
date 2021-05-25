cd "C:\Program Files\Oracle\VirtualBox\"
VBoxManage modifyvm "High Sierra" --cpuidset 00000001 000306a9 04100800 7fbae3ff bfebfbff  
VBoxManage setextradata "High Sierra" "VBoxInternal/Devices/efi/0/Config/DmiSystemProduct" "MacBookPro11,3"  
VBoxManage setextradata "High Sierra" "VBoxInternal/Devices/efi/0/Config/DmiSystemVersion" "1.0"  
VBoxManage setextradata "High Sierra" "VBoxInternal/Devices/efi/0/Config/DmiBoardProduct" "Mac-2BD1B31983FE1663"
VBoxManage setextradata "High Sierra" "VBoxInternal/Devices/smc/0/Config/DeviceKey" "ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc"  
VBoxManage setextradata "High Sierra" "VBoxInternal/Devices/smc/0/Config/GetKeyFromRealSMC" 1   