import pandas as pd
from django.core.management.base import BaseCommand
from kindle.models import KindleBook

class Command(BaseCommand):
    help = 'Import Kindle dataset into the database'

    def handle(self, *args, **kwargs):
        df = pd.read_csv('kindle_data-v2.csv')
        df = df.dropna()
        df.rename(columns={'soldBy': 'sold_by', 'isKindleUnlimited': 'is_kindle_unlimited'}, inplace=True)
        df['publishedDate'] = pd.to_datetime(df['publishedDate'], errors='coerce')
        
        for _, row in df.iterrows():
            KindleBook.objects.update_or_create(
                asin=row['asin'],
                defaults={
                    'title': row['title'],
                    'author': row['author'],
                    'sold_by': row['sold_by'],
                    'img_url': row['imgUrl'],
                    'product_url': row['productURL'],
                    'stars': row['stars'],
                    'reviews': row['reviews'],
                    'price': row['price'],
                    'is_kindle_unlimited': row['is_kindle_unlimited'],
                    'category_id': row['category_id'],
                    'is_best_seller': row['isBestSeller'],
                    'is_editors_pick': row['isEditorsPick'],
                    'is_good_reads_choice': row['isGoodReadsChoice'],
                    'published_date': row['publishedDate'] if pd.notna(row['publishedDate']) else None,
                    'category_name': row['category_name'],
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully imported Kindle data'))
