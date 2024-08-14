import random
from faker import Faker
from django.core.management.base import BaseCommand
from books.models import Book
from authentication.models import CustomUser
from django.conf import settings

class Command(BaseCommand):
    help = 'Generate fake data for users and books'

    def handle(self, *args, **kwargs):
        fake = Faker()
        NUM_USERS = 100
        NUM_BOOKS = 500
        USER_TYPES = ['author', 'reader', 'seller']
        VISIBILITY_OPTIONS = ['public', 'private']
        GENRES = [
            "Action/Adventure fiction", "Children’s fiction", "Classic fiction",
            "Contemporary fiction", "Fantasy", "Graphic novel", "Historical fiction",
            "Horror", "LGBTQ+", "Literary fiction", "Mystery", "New adult", "Romance",
            "Satire", "Science fiction", "Short story", "Thriller", "Western",
            "Women’s fiction", "Young adult", "Art & photography", "Autobiography/Memoir",
            "Biography", "Essays", "Food & drink", "History", "How-To/Guides",
            "Humanities & social sciences", "Humor", "Parenting", "Philosophy",
            "Religion & spirituality", "Science & technology", "Self-help", "Travel",
            "True crime"
        ]

        used_usernames = set()

        # Create 100 users
        for _ in range(NUM_USERS):
            username = fake.user_name()
            while username in used_usernames:
                username = fake.user_name()
            used_usernames.add(username)

            user = CustomUser(
                username=username,
                email=fake.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                birth_date=fake.date_of_birth(minimum_age=18, maximum_age=80),
                user_type=random.choice(USER_TYPES),
                bio=fake.text(max_nb_chars=500)
            )
            user.set_password('password123')
            user.save()

        # Generate mock file paths and URLs
        image_base_url = "https://via.placeholder.com/200x300.png?text=Book+Image+"
        pdf_base_url = "https://www.pdf995.com/samples/pdf.pdf"  # Sample PDF link

        # Create 500 books
        for _ in range(NUM_BOOKS):
            title = fake.sentence(nb_words=3)
            num_genres = min(3, len(GENRES))  # Ensure we don't sample more than available
            genre = ", ".join(random.sample(GENRES, k=num_genres))

            image_url = f"{image_base_url}{random.randint(1, 100)}"
            pdf_url = pdf_base_url

            # Create the book instance
            book = Book(
                title=title,
                author=fake.name(),
                publish_date=fake.date_this_century(),
                publisher=fake.company(),
                language=fake.language_name(),
                pages=random.randint(100, 1000),
                published_in=fake.city(),
                series=fake.sentence(nb_words=2) if random.choice([True, False]) else None,
                genre=genre,
                description=fake.text(max_nb_chars=1000),
                message_from_author=fake.text(max_nb_chars=500) if random.choice([True, False]) else None,
                cost=round(random.uniform(10, 500), 2),
                visibility=random.choice(VISIBILITY_OPTIONS),
                user=CustomUser.objects.order_by('?').first(),
                image=image_url,
                book_pdf=pdf_url
            )

            book.save()

        self.stdout.write(self.style.SUCCESS(f"{NUM_USERS} users and {NUM_BOOKS} books have been successfully created."))
