sql = """
    CREATE TABLE stocks_holding(
        symbol VARCHAR(20) NOT NULL,
        number_of_shares INT,
        PRIMARY KEY (symbol)
    );
"""
