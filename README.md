### Deploy to k8s

**Step 1.** Install Keda

```bash
$ k apply -f https://github.com/kedacore/keda/releases/download/v2.8.0/keda-2.8.0.yaml
```

**Step 2.** Upload credentials

```env
REDIS_OM_URL=redis://<username>:<password>@<host>:<port>
REDIS_HOST=<host>
REDIS_PASSWORD=<password>
REDIS_USERNAME=<username>
REDIS_PORT=<port>
```

```bash
$ k create secret generic credentials --from-env-file .env
```

**Step 3.** Apply the YAMLs

```bash
$ k apply -f products/k8s.yaml \
    -f orders/k8s.yaml \
    -f api-server/k8s.yaml
```

Once KEDA in installed and all above deployments and services are up and running, apply the next YAML.

```bash
$ k apply -f invoice/k8s.yaml
```

**Step 4.** Clean Up

```bash
$ k delete -f invoice/k8s.yaml
```

```bash
$ k delete -f products/k8s.yaml \
    -f orders/k8s.yaml \
    -f api-server/k8s.yaml \
```

```bash
$ k delete secret credentials
```

```bash
$ k delete -f https://github.com/kedacore/keda/releases/download/v2.8.0/keda-2.8.0.yaml
```
