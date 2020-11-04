# Loja de roupas


### Dependências

- Docker >=18
- docker-compose >=1.21

### Setup ambiente

Para prepara o ambiente inicial execute uma única vez:


`$ cp api/.env.sample api/.env`
`$ make up`
`$ make dj migrate`
`$ make createsu`

Estará disponível:
- [http://localhost:3000](http://localhost:3000)
- [http://localhost:8000/api/stock/products/](http://localhost:8000/api/stock/products/)
- [http://localhost:8000/api/stock/products/id/](http://localhost:8000/api/stock/products/id/)
- [http://localhost:8000/api/stock/products/import/](http://localhost:8000/api/stock/products/import/)

para executar os testes rode:

`$ make test`

para efetuar autenticação use:

admin@stock.com:stock123
