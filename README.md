# my_jupyter
## conda activate;jupyter notebook
## cd $HOME/jupyter/my_jupyter/; jupyter lab

- sudo iptables -t mangle -A POSTROUTING -j TTL --ttl-set 65
- > https://pikabu.ru/story/khelp_pomogite_okonchatelno_izmenit_ttl_v_linux_mint_19_6252555
- sudo -s
- echo "net.ipv4.ip_default_ttl=65" >> /etc/sysctl.conf
- sysctl --system
- > https://sollus-soft.blogspot.com/2018/06/ttl-linux.html
- ping 127.0.0.1

- su <username> -c "jupyter notebook --config=/location/of/your/config/file/.jupyter/jupyter_notebook_config.py --no-browser --notebook-dir=/location/of/yournotebooks" &
- e.g.
- su kde -c "jupyter lab --config=/location/of/your/config/file/.jupyter/jupyter_notebook_config.py --no-browser --notebook-dir=/location/of/yournotebooks" &

# something add for autostart

- mkdir $HOME/.config/autostart
- cd $HOME/.config/autostart/
- nano file.desktop
    
- - [Desktop Entry]
- - Type=Application
- - Exec=cd $HOME/jupyter/my_jupyter; jupyter lab
- - Hidden=false
- - NoDisplay=false
- - X-GNOME-Autostart-enabled=true
- - Name=jupyter lab
- - Comment=
- - RunHook=0

> cd $HOME/jupyter/my_jupyter/;jupyter notebook
> cd $HOME/jupyter/my_jupyter/;git add .;git commit -m "replace generate img function from BAD to COOL";git push origin
