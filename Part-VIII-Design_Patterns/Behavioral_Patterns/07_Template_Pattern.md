# 7 Template Pattern
## 7.1 Basics
- useful to removing duplicate code
- by defining a sceleton of an algorithm in a superclass but the specific implementations are shared

## 7.2 Usecase
- when only a specific part of the code changes but the rest will be the same in a bunch of objects

## 7.3 General Design
- the common functionality is implemented in a base class
- the destinct functionality is then overwritten in subclasses
- similar sections are shared between the subclasses

## 7.4 Python Implementation
````python
    import sqlite3, pathlib, datetime

    def create_db():
        if pathlib.Path(pathlib.Path.cwd()) / "sales.db":
            return

        conn = sqlite3.connect("sales.db")

        conn.execute(
            "CREATE TABLE Sales (salesperson text,"
            "amt currency, year integer, model text, new boolean)")

        conn.execute(
            "INSERT INTO sales values"
            "('Tim',9000,2006,'Ford Focus', 'false')")

        conn.execute(
            "INSERT INTO sales values"
            "('Gayle',8000,2004,'Dodge Neon', 'false')")

        conn.execute(
            "INSERT INTO sales values"
            "('Gayle',28000,2009,'Ford Mustang', 'true')")

        conn.execute(
            "INSERT INTO sales values"
            "('Gayle',50000,2010,'Lincoln Navigator', 'true')")

        conn.execute(
            "INSERT INTO sales values"
            "('Don',20000,2008,'Toyota Prius', 'false')")

        conn.commit()
        conn.close

    class QueryTemplate:
        def connect(self):
            self.conn = sqlite3.connect("sales.db")

        def construct_query(self):
            raise NotImplementedError()

        def do_query(self):
            result = self.conn.execute(self.query)
            self.results = results.fetchall()

        def format_results(self):
            output = []
            for row in self.results:
                row = [str(i) for i in row]
                output.append(",".join(row))
            self.formatted_results = "\n".join(output)

        def output_results(self):
            raise NotImplementedError()

        def process(self):
            self.connect()
            self.construct_query()
            self.do_query()
            self.format_results()
            self.output_results()

    class NewVehiclesQuery(QueryTemplate):
        def construct_query(self):
            self.query = "select from sales where new='true'"

        def output_results(self):
            print(self.formatted_results)

    class UserGrossQuery(QueryTemplate):
        def construct_query(self):
            self.query = (
                "select salesperson, sum(amt)"
                + "from sales group by salesperson")

        def output_results(self):
            filename = f"gross_sales_{datetime.date.today().strftime('%Y%m%d')}"
            with open(filename, "w") as outfile:
                outfile.write(self.formatted_results)
````