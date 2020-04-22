:delay 15s
/interface wireless security-profiles
add authentication-types=wpa2-psk eap-methods="" management-protection=\
    allowed mode=dynamic-keys name=Security supplicant-identity="" \
    wpa2-pre-shared-key="\$TELECABLEcartaya=\"<2510-1985>\";#"
/interface wireless
set [ find default-name=wlan1 ] band=5ghz-a/n channel-width=20mhz \
    country=spain disabled=no name=wlan1-gateway ssid=TCC_MAIN_WIFI \
    wireless-protocol=any radio-name=CPE5117-1 security-profile=Security
/interface ethernet
set [ find default-name=ether1 ] name=ether1-local
/interface pppoe-client
add add-default-route=yes disabled=no interface=wlan1-gateway name=pppoe-out1 \
    password=OvF6ooYWWh22p09776cNNXvvG66O4k user=ppp5117-1
/ip neighbor discovery-settings
set discover-interface-list=none
/ip pool
add name=default-dhcp ranges=192.168.100.100-192.168.100.254
/ip dhcp-server
add address-pool=default-dhcp disabled=no interface=ether1-local lease-time=\
    3d name=default
/snmp community
add addresses=0.0.0.0/0 name=snmprueba write-access=yes
/ip address
add address=192.168.88.1/24 comment=Administracion interface=ether1-local \
    network=192.168.88.0
add address=192.168.100.1/24 comment="Red del CLiente" interface=ether1-local network=192.168.100.0
/ip dhcp-client
add comment="DHCP nodo WIFI" dhcp-options=hostname,clientid disabled=\
    no interface=wlan1-gateway
/ip dhcp-server network
add address=192.168.100.0/24 comment="default configuration" dns-server=\
    8.8.8.8,8.8.4.4 gateway=192.168.100.1 netmask=24
/ip dns
set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
/ip dns static
add address=192.168.100.1 name=router
/ip firewall filter
add chain=input comment="default configuration" disabled=no protocol=icmp
add chain=input comment="default configuration" connection-state=established \
    disabled=no
add chain=input comment="default configuration" connection-state=related \
    disabled=no
add action=drop chain=input comment="default configuration" disabled=no \
    in-interface=pppoe-out1
add chain=forward comment="default configuration" connection-state=\
    established disabled=no
add chain=forward comment="default configuration" connection-state=related \
    disabled=no
add action=drop chain=forward comment="default configuration" \
    connection-state=invalid disabled=no
/ip firewall mangle
add action=set-priority chain=forward comment="Prioridad SIP Llamada" dscp=46 \
    new-priority=8 passthrough=no
add action=set-priority chain=forward comment="Prioridad SIP Gestion" dscp=26 \
    new-priority=8 passthrough=no
/ip firewall nat
add action=masquerade chain=srcnat comment="Nateo hacia internet" \
    out-interface=pppoe-out1 to-addresses=0.0.0.0
add action=dst-nat chain=dstnat in-interface=pppoe-out1 \
    to-addresses=192.168.100.254 disabled=yes  comment="DMZ"
/ip service
set telnet address=10.0.0.0/26 port=6923
set ftp address=10.0.0.0/26 port=6921
set www address=10.0.0.0/26 port=6980
set ssh port=6922
set www-ssl address=10.0.0.0/26
set api address=10.0.0.0/26
set api-ssl address=10.0.0.0/26
/snmp
set contact=juan.redondo@telecablecartaya.es enabled=yes location=\
    "Cartaya" trap-community=snmprueba
/system clock
set time-zone-name=Europe/Madrid
/system identity
set name=CPE5117-1
/system leds
set 0 interface=wlan1-gateway
/system ntp client
set enabled=yes primary-ntp=172.16.0.10
/tool mac-server
set allowed-interface-list=none
/tool mac-server mac-winbox
set allowed-interface-list=none
/user set password=ChC3R0Ju_CPE admin
/user add name=tccuser password=TCC_pass group=read