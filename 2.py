"""
В PySpark приложении датафреймами(pyspark.sql.DataFrame) заданы продукты, категории и 
их связи. Каждому продукту может соответствовать несколько категорий или ни одной. 
А каждой категории может соответствовать несколько продуктов или ни одного. Напишите метод 
на PySpark, который в одном датафрейме вернет все пары «Имя продукта – Имя категории» и 
имена всех продуктов, у которых нет категорий.
"""


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit


spark = SparkSession.builder.appName("ProductsCategories").getOrCreate()


products_data = [
    (1, "ProductA"),
    (2, "ProductB"),
    (3, "ProductC"),
    (4, "ProductD")
]

categories_data = [
    (1, "Category1"),
    (2, "Category2"),
    (3, "Category3")
]

product_category_data = [
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 1)
]


products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])
categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])
product_category_df = spark.createDataFrame(product_category_data, ["product_id", "category_id"])


product_category_pairs_df = product_category_df.join(products_df, "product_id") \
                                                .join(categories_df, "category_id") \
                                                .select("product_name", "category_name")


product_category_pairs_df.show()


products_with_categories_df = product_category_df.join(products_df, "product_id", "right") \
                                                  .join(categories_df, "category_id", "left") \
                                                  .filter(col("category_id").isNull()) \
                                                  .select("product_name")


products_without_categories_df = products_with_categories_df.withColumn("category_name", lit(None))


result_df = product_category_pairs_df.union(products_without_categories_df)


result_df.show()
