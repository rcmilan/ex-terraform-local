Instalar **Terraform**, **tflocal**, **Docker**, **AWS CLI** e **Localstack**

- [Como usar Terraform + Localstack (com Docker)](https://dev.to/rotirotirafa/como-usar-terraform-localstack-com-docker-h44)
- [LocalStack](https://www.localstack.cloud/)
- [DynamoDB no localstack](https://docs.localstack.cloud/user-guide/aws/dynamodb/)

```bash
# subir o Localstack
# simula os serviços da cloud
docker-compose up -d
```

```bash
# inicia a configuração do Terraform
tflocal init

# valida o que será aplicado
tflocal plan

# aplica as configurações
tflocal apply

# remove as coisas que estão rodando
tflocal destroy
```

```bash
# Exibe as tabelas do DynamoDB
aws dynamodb list-tables --endpoint-url http://localhost:4566
```
