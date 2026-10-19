from typing import List, Optional


class User:
    def __init__(self, user_id: int, username: str, email: str):
        self.user_id = user_id
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return f"User(id={self.user_id}, username='{self.username}')"


class Post:
    def __init__(self, post_id: int, title: str, content: str, author_id: int):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.author_id = author_id

    def __repr__(self) -> str:
        return f"Post(id={self.post_id}, title='{self.title}', author_id={self.author_id})"


class Forum:
    def __init__(self, title: str):
        self.title = title
        self.users: List[User] = []
        self.posts: List[Post] = []

    def register_user(self, user: User) -> None:
        self.users.append(user)

    def create_post(self, post: Post) -> None:
        self.posts.append(post)

    # Lookup helper: find user by username
    def find_user_by_username(self, username: str) -> Optional[User]:
        for user in self.users:
            if user.username.lower() == username.lower():
                return user
        return None

    # Lookup helper: find user by email
    def find_user_by_email(self, email: str) -> Optional[User]:
        for user in self.users:
            if user.email.lower() == email.lower():
                return user
        return None

    # Retrieve all posts authored by a specific user id
    def find_posts_by_user_id(self, user_id: int) -> List[Post]:
        return [post for post in self.posts if post.author_id == user_id]

    # Retrieve all posts authored by a given email address
    def find_posts_by_user_email(self, email: str) -> List[Post]:
        user = self.find_user_by_email(email)
        if not user:
            return []
        return self.find_posts_by_user_id(user.user_id)


# --- Demonstration & Testing ---
forum = Forum("Python Developers Hub")

user1 = User(1, "Paayas", "paayas@example.com")
user2 = User(2, "Alex", "alex@example.com")
forum.register_user(user1)
forum.register_user(user2)

forum.create_post(Post(101, "Docker Compose Tips", "Keep services isolated...", 1))
forum.create_post(Post(102, "FastAPI Routing", "Use APIRouter for modularity...", 1))
forum.create_post(Post(103, "NextJS App Router", "Server vs client components...", 2))

# Find by username & email
found_user = forum.find_user_by_username("Paayas")
print("Found user:", found_user)

# Retrieve posts authored by user email
paayas_posts = forum.find_posts_by_user_email("paayas@example.com")
print(f"Posts authored by paayas@example.com ({len(paayas_posts)} total):")
for p in paayas_posts:
    print(" -", p)