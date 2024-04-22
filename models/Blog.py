class Blog:
    base_table = "blogs"

    @classmethod
    def categories(cls):
        return (cls.base_table, "categories", "category_id", "id")