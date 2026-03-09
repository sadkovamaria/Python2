if __name__ == "__main__":
    class SocialNetwork:
        """Базовый класс социальной сети."""

        def __init__(self, name: str, users: int) -> None:
            """
            Конструктор.

            :param name: название сети
            :param users: количество пользователей
            """
            self.name: str = name
            self._users: int = users  # защищённый атрибут

        def post(self, user: str, text: str) -> str:
            """
            Публикация сообщения.

            :param user: имя пользователя
            :param text: текст сообщения
            :return: строка сообщения
            """
            return f"{user}: {text}"

        def __str__(self) -> str:
            return f"{self.name} ({self._users} пользователей)"

        def __repr__(self) -> str:
            return f"SocialNetwork(name={self.name!r}, users={self._users!r})"


    class VK(SocialNetwork):
        """Дочерний класс социальной сети VK."""

        def __init__(self, users: int, groups: int) -> None:
            """
            Расширенный конструктор.

            :param users: количество пользователей
            :param groups: количество групп
            """
            super().__init__("VK", users)
            self.groups: int = groups

        def post(self, user: str, text: str) -> str:
            """
            Перегруженный метод публикации.

            Причина: в VK посты обычно размещаются на стене.
            """
            return f"[VK пост] {user} написал: {text}"

        def create_group(self, name: str) -> str:
            """
            Создание группы.

            :param name: название группы
            :return: сообщение о создании
            """
            self.groups += 1
            return f"Группа '{name}' создана"

        def __repr__(self) -> str:
            return f"VK(users={self._users!r}, groups={self.groups!r})"
    pass
