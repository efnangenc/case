from django.core.management.base import BaseCommand
from users.models import User, Album, Post, Comment, Todo, Photo, Address, Company, Geo


class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **kwargs):
        if User.objects.exists():
            self.stdout.write(self.style.WARNING('Data already exists. Skipping seed.'))
            return

        # Geo konumu
        geo = Geo.objects.create(
            lat="39.950289",
            lng="32.7732722"
        )

        # Şirket ve adres oluştur
        address = Address.objects.create(
            street='Çamlıca Mahallesi',
            suite='Apt. 556',
            city='Ankara',
            zipcode='06200',
            geo=geo
        )

        company = Company.objects.create(
            name='N2Mobil Araç Takip Sistemleri A.Ş',
        )

        # Kullanıcı oluştur
        user = User.objects.create(
            name='Müslüm Türk',
            username='muslum.turk',
            email='muslum.turk@n2mobil.com.tr',
            phone='+90 555 55 55',
            website='www.n2mobil.com.tr',
            address=address,
            company=company
        )

        # Albüm ve fotoğraf
        album = Album.objects.create(user=user, title='quidem molestiae enim')
        
        Photo.objects.create(album=album, title='accusamus beatae ad facilis cum similique qui sunt', url='https://via.placeholder.com/600/92c952', thumbnailUrl='https://via.placeholder.com/150/92c952')
        Photo.objects.create(album=album, title='reprehenderit est deserunt velit ipsam', url='https://via.placeholder.com/600/771796', thumbnailUrl='https://via.placeholder.com/150/92c952')
        Photo.objects.create(album=album, title='officia porro iure quia iusto qui ipsa ut modi', url='https://via.placeholder.com/600/24f355', thumbnailUrl='https://via.placeholder.com/150/92c952')
        Photo.objects.create(album=album, title='culpa odio esse rerum omnis laboriosam voluptate', url='https://via.placeholder.com/600/d32776', thumbnailUrl='https://via.placeholder.com/150/92c952')
        Photo.objects.create(album=album, title='natus nisi omnis corporis facere molestiae rerum in', url='https://via.placeholder.com/600/f66b97', thumbnailUrl='https://via.placeholder.com/150/92c952')

        # Gönderi ve yorum
        post1 = Post.objects.create(user=user, title='sunt aut facere repellat provident occaecati excepturi optio reprehenderit', body='sunt aut facere repellat provident occaecati excepturi optio reprehenderit.')
        Comment.objects.create(post=post1, name='id labore ex et quam laborum', email='Eliseo@gardner.biz', body='laudantium enim quasi est quidem magnam voluptate ipsam eos tempora quo necessitatibus\ndolor quam autem quasi reiciendis et nam sapiente accusantium')
        Comment.objects.create(post=post1, name='quo vero reiciendis velit similique earum', email='Jayne_Kuhic@sydney.com', body='est natus enim nihil est dolore omnis voluptatem numquam t omnis occaecati quod ullam atvoluptatem error expedita pariatur nihil sint nostrum voluptatem reiciendis et')
    
        post2 = Post.objects.create(user=user, title='qui est esse', body='est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque fugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis  aperiam non debitis possimus qui neque nisi nulla.')
        Comment.objects.create(post=post2, name='odio adipisci rerum aut animi', email='Nikita@garfield.biz', body='quia molestiae reprehenderit quasi aspernatur aut expedita occaecati aliquam eveniet laudantium mnis quibusdam delectus saepe quia accusamus maiores nam est cum et ducimus et vero voluptates excepturi deleniti ratione')
        Comment.objects.create(post=post2, name='alias odio sit', email='Lew@alysha.tv', body='non et atque\noccaecati deserunt quas accusantium unde odit nobis qui voluptatem quia voluptas consequuntur itaque doloret qui rerum deleniti ut occaecati')
        Comment.objects.create(post=post2, name='vero eaque aliquid doloribus et culpa', email='Hayden@althea.biz', body='harum non quasi et ratione tempore iure ex voluptates in ratione\nharum architecto fugit inventore cupiditate voluptates magni quo et')

        # Todo
        Todo.objects.create(user=user, title='delectus aut autem', completed=False)
        Todo.objects.create(user=user, title='quis ut nam facilis et officia qui', completed=False)
        Todo.objects.create(user=user, title='fugiat veniam minus', completed=True)
        Todo.objects.create(user=user, title='et porro tempora', completed=True)
        Todo.objects.create(user=user, title='laboriosam mollitia et enim quasi adipisci quia provident illum', completed=False)
        Todo.objects.create(user=user, title='qui ullam ratione quibusdam voluptatem quia omnis', completed=True)
        Todo.objects.create(user=user, title='illo expedita consequatur quia in', completed=True)
        Todo.objects.create(user=user, title='quo adipisci enim quam ut ab', completed=False)

        self.stdout.write(self.style.SUCCESS('Seed data successfully inserted.'))
