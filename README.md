Instalar **Terraform**, **tflocal**, **Docker** e **Localstack**

```bash
# subir o loclastack
# simula os serviços da cloud
docker-compose up -d
```

```bash
# inicia a configuração do terraform
tflocal init

# valida o que será aplicado
tflocal plan

# aplica as configurações
tflocal apply
```

```bash
# Exibe as tabelas do DynamoDB
aws dynamodb list-tables --endpoint-url http://localhost:4566
```