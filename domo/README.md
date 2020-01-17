# PvMonit Domotique - Ou comment utilisé le surplus d'une installation solaire autonome

Article / vidéo lier à cet module domotique : 

* https://david.mercereau.info/?p=5703
* https://vimeo.com/385514728

**Prés-requis: programmation PHP sommaire**. En effet pour le moment il n'y a pas d'interface graphique pour programmer des évènement sur les relais, il faut donc coder un peu en PHP pour s'en sortir...

## Câblage / Matériel 

Matériel : 

- Le raspbery pi (zéro ça suffit) sur lequel est installé PvMonit (expliqué [ici](https://david.mercereau.info/pvmonit-v1-0-monitoring-de-mon-installation-photovoltaique-autonome/))
- Une plaque de 8 relais (mais vous pouvez envisagez en avoir autant que vous voulez… ça correspond à mon besoin…) qui allume tel ou tel appareil pour (9€)
- (option) [Un afficheur 8 chiffres + 8 leds + 8 boutons (tm1638)](https://os.mbed.com/components/TM1638-LED-controller-80-LEDs-max-Keyboa/) nous permet d’interagir avec le système sans allumer un ordinateur (ou sans smartphone)  : forcé l’allumage, interdire l'allumage… (~6€). 

<img src="https://david.mercereau.info/wp-content/uploads/2020/01/PvMonit-Domo-v2_bb.png" alt="https://david.mercereau.info/wp-content/uploads/2020/01/PvMonit-Domo-v2_bb.png" style="zoom:30%;" />

## Daemon "domo"

C'est le daemon qui regard l'état du système (batterie, régulateur) et qui déclenche des actions selon des scripts

Pour la configuration, regarder le fichier config.yaml, dans la partie "domo:"

Dépendance du script : 

```bash
aptitude install php-pdo-sqlite
```

Lancement du script à la main

```bash
/opt/PvMonit/domo/domo-launch.sh
```

Pour le lancement au démarrage, ajouter avant "exit 0" dans le fichier /etc/rc.local la ligne suivant

```bash
screen -A -m -d -S domo /opt/PvMonit/domo/domo-launch.sh
```

Il vous faut ensuite configurer les scripts pour l'automatisme, il se trouve dans /opt/PvMonit/domo/relay.script.d/ et il faut les nommer X.php (X étant le numéro du relai)

Voir /opt/PvMonit/domo/relay.script.d/ID.php.exemple pour connaître le champs des possibles / des fonctions.

## Activation dans l'interface web PvMonit

Dans le ficheir config.yaml activer "domo" :

```yaml
www:
    domo: true
```

Ceci vous permet d’interagir avec les relais via l'interface web :

[<img src="https://david.mercereau.info/wp-content/uploads/2020/01/Screenshot_2020-01-07-Pv-Monit1.png" alt="https://david.mercereau.info/wp-content/uploads/2020/01/PvMonit-Domo-v2_bb.png" style="zoom:60%;" />](https://david.mercereau.info/wp-content/uploads/2020/01/Screenshot_2020-01-07-Pv-Monit1.png)

## (Option) Afficheur 8 chiffres + 8 leds + 8 boutons (tm1638)

Nous permet d’interagir avec le système sans allumer un ordinateur (ou sans smartphone).

Dépendance du script : 

```bash
aptitude install python3 python3-yaml python3-json pip3
pip3 install rpi-TM1638
```

Lancement du script à la main

```bash
/opt/PvMonit/domo/tm1638-launch.sh
```

Pour le lancement au démarrage, ajouter avant "exit 0" dans le fichier /etc/rc.local la ligne suivant

```bash
screen -A -m -d -S tm1638 /opt/PvMonit/domo/tm1638-launch.sh
```

## Configuration

La configuration ce fait dans le même fichier que pvmonit /opt/PvMonit/config.yaml, vous avez une section "domo". 

Ensuite il vous faut faire les scripts qui correspondent à vos usages, c'est en PHP que ça ce joue. Les scripts sont contenu dans /opt/PvMonit/domo/relay.script.d/NUMEROduRELAIS.php

Un script exemple est présent avec toutes les fonctionnalités possibles : https://framagit.org/kepon/PvMonit/blob/master/domo/relay.script.d/ID.php.exemple

## Pour interagir avec d'autres scripts maisons

Seul les mod son modifiés, les état en son déduit par le script domo/relay-actions si vous voulez interagir avec d'autres applications il vous suffit de modifier le fichier json "/tmp/PvMonit_domo_mod"  (par défaut, modifiable dans le config.yaml : domo / jsonFile / modPath: /tmp/PvMonit_domo_mod)


