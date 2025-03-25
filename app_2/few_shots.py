# few_shots = [
#     {'Question' : "How many t-shirts do we have left for Nike in XS size and white color?",
#      'SQLQuery' : "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
#      'SQLResult': "Result of the SQL query",
#      'Answer' : "91"},
#     {'Question': "How much is the total price of the inventory for all S-size t-shirts?",
#      'SQLQuery':"SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
#      'SQLResult': "Result of the SQL query",
#      'Answer': "22292"},
#     {'Question': "If we have to sell all the Levi’s T-shirts today with discounts applied. How much revenue  our store will generate (post discounts)?" ,
#      'SQLQuery' : """SELECT SUM(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
# (select SUM(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi'
# group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
#  """,
#      'SQLResult': "Result of the SQL query",
#      'Answer': "16725.4"} ,
#      {'Question' : "If we have to sell all the Levi’s T-shirts today. How much revenue our store will generate without discount?" ,
#       'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
#       'SQLResult': "Result of the SQL query",
#       'Answer' : "17462"},
#     {'Question': "How many white color Levi's shirt I have?",
#      'SQLQuery' : "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White'",
#      'SQLResult': "Result of the SQL query",
#      'Answer' : "290"
#      },
#     {'Question': "how much sales amount will be generated if we sell all large size t shirts today in nike brand after discounts?",
#      'SQLQuery' : """SELECT SUM(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
# (select SUM(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Nike' and size="L"
# group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
#  """,
#      'SQLResult': "Result of the SQL query",
#      'Answer' : "290"
#     }
# ]

few_shots = [
    {'Question': "How many t-shirts do we have left for Nike in XS size and white color?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
     },
    {'Question': "How much is the total price of the inventory for all S-size t-shirts?",
     'SQLQuery': "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'"
     },
    {'Question': "If we have to sell all the Levi’s T-shirts today with discounts applied. How much revenue  our store will generate (post discounts)?",
     'SQLQuery': """SELECT SUM(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select SUM(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi'
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
 """,
     },
    {'Question': "If we have to sell all the Levi’s T-shirts today. How much revenue our store will generate without discount?",
     'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'"
     },
    {'Question': "How many white color Levi's shirt I have?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White'"
     },
    {'Question': "how much sales amount will be generated if we sell all large size t shirts today in nike brand after discounts?",
     'SQLQuery': """SELECT SUM(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select SUM(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Nike' and size="L"
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
 """
     }
]
