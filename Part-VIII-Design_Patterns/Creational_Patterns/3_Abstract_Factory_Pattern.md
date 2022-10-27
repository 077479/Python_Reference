# 3 Abstract Factory
## 3.1 Basics
- provides multiple implementations of a system depending on some configuration or plattform

## 3.2 Usecase
- when different implementations depending on different configurations are needed
- e.g. django uses this to create interfaces depending on the db that is used(MySQL, PostgradeSQL, SQLite . . .)
- e.g. orders from different countries might need different ways of calculating the taxes

## 3.3 General Design
1. Formatter Factory(FormatterFactory[create_date_formatter, create_currency_formatter])
2. Concrete Factory(USAFormatterFactory, FranceFormatterFactory)
3. Concrete Products(DateFormatter)
- abstract factories often return singletons

## 3.4 Python Implementation
- there is no need for interfaces in python
- the factories should be in own modules
e.g. directory structure for a localized based factory design
>
    localize/
        __init__.py
        backends/
            __init__.py
            USA.py
            France.py
        main.py
            from .backends import USA,France
            if country_code == "France":
                current_backend = France