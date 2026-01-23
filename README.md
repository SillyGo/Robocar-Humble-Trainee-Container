# Robocar-Humble-Trainee-Container

## GUIA BASICO:

1. dê git clone nesse repo
2. vá para a pasta
3. dê build com `./docker_build.sh`
4. rode o container com `./docker_run.sh`
5. divirta-se :D

## EXEMPLOS:

Por enquanto (23 jan 26) só temos um exemplo, para roda-lo, dentro do container, faça:

```bash
cd exemplos_trainee
```

para navegar para dentro da pasta. Na pasta, basta fazer:

```bash
python3 ImagePubExample.py
```

que o código começará a rodar. Nesse momento, imagens da sua webcam (se tudo der certo) serão publicadas no tópico:

```
/camera/image_raw
```

para visualiza-lo, abra outro terminal e digite:

```bash
ros2 run rqt_image_view rqt_image_view /camera/image_raw
```

daí, maximize a janelinha que abriu e voilá, deve ter aberto o feed da sua webcam. Para parar a execução, basta dar control C onde você rodou o exemplo, o mesmo para o visualizador da imagem
