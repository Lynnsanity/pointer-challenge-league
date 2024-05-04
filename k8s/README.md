# K8S
1. install microk8s on server
2. microk8s enable ingress
3. in ~/.bashrc put `alias k='microk8s.kubectl'`
4. 
```sh
k -n pcl apply -f secrets.yml
k -n pcl apply -f pcl-deployment.yml
k -n pcl apply -f ingress.yml
```
