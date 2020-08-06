# ToDo API

An api used to create, edit and view simple todo notes, this app uses Laravel Sanctum with API token authentication. 

## Install software (using Mac and brew)
### Composer
- Install with brew
```
brew install composer
```
### PHP
- Install PHP 7.4 with brew
```
brew install php@7.4
```

### MySQL
- Install in MacOS via brew
```
brew install mysql
```
## Setup 
- Install packages
```
composer install
```
- Copy the .env.example file to a new file named .env
```
cp .env.example .env
```
- Fill in .env variables in new file
```
vim .env
```
- Generate Laravel app key
```
php artisan key:generate
```
- Run migration files to add DB tables
```
php artisan migrate
```
- Run DB seeding to add test data
```
php artisan db:seed
```
## Commands
- Run app in development
```
php artisan serve
```
