# RPI configure documentation

```
This README explain to you how to configure your RPI as an WIFI router. So that the players can access the private network. The laptop can be connect throught USB if wanted.
```

## Set USB drive as Network
### Create file configuration of the RPI
* Edit `config`
* * `sudo nano /boot.config.txt`
* * Add `dtoverlay=dwc2` at the last line
* * Save
### Activated USB gadget
*Use to connect the RPI to the computer and use the PRI as a WIFI router*
* * `sudo nano /boot/cmdline.txt`
* * Add `modules-load=dwc2,g_ether` after `rootwait`
### Final result
`root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait modules-load=dwc2,g_ether`

## Change RPI as WIFI router
### Install dnsmasp
* `sudo apt update`
* `sudo apt install hostapd dnsmasq`
### Configure hostpad for WIFI
* `sudo nano /etc/hostpad/hostpad.conf`
And add
```
interface=wlan0
driver=nl80211
ssid=JDR_Game
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=monpassword
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
```
### Activated hostapd et reboot
* `sudo systemctl enable hostpad`
* `sudo systemctl restart hostapd`