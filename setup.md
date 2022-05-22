Setting up git

* create ssh key:
    ```
    mkdir ~/.ssh
    cd ~/.ssh
    ssh-keygen -t ed25519 -C "manjunathmmass7548@gmail.com"
    pbcopy < id_rsa.pub
    ```
* In https://github.com, go to settings->SSH and GPG keys -> New SSH key.
* paste the key and save
* clone the repo
```
    git clone git@github.com:Manjunath200105/crypto_predictor_app.git
```

docker logs -f crypto_predictor_app


install docker desktop
docker build --tag crypto-python-docker .

