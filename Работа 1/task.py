class SocialNetwork:
    """
    Базовый класс для представления социальной сети.

    Атрибуты:
        name (str): Название социальной сети.
        user_count (int): Количество пользователей в социальной сети.
    """

    def __init__(self, name: str, user_count: int):
        """
        Инициализирует экземпляр класса SocialNetwork.

        Args:
            name (str): Название социальной сети.
            user_count (int): Количество пользователей в социальной сети.
        """
        self.name = name
        self._user_count = user_count  # Инкапсуляция для предотвращения прямого изменения количества пользователей

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети.

        Returns:
            str: Название и количество пользователей.
        """
        return f"SocialNetwork(name={self.name}, user_count={self._user_count})"

    def __repr__(self) -> str:
        """
        Возвращает строку для технического представления объекта.

        Returns:
            str: Техническое представление.
        """
        return f"SocialNetwork(name={self.name!r}, user_count={self._user_count!r})"

    def get_user_count(self) -> int:
        """
        Возвращает количество пользователей в социальной сети.

        Returns:
            int: Количество пользователей.
        """
        return self._user_count

class TikTok(SocialNetwork):
    """
    Дочерний класс для представления социальной сети TikTok.

    Атрибуты:
        name (str): Название социальной сети (унаследовано).
        user_count (int): Количество пользователей (унаследовано).
        average_video_length (float): Средняя длина видео на платформе.
    """

    def __init__(self, name: str, user_count: int, average_video_length: float):
        """
        Инициализирует экземпляр класса TikTok.

        Args:
            name (str): Название социальной сети.
            user_count (int): Количество пользователей.
            average_video_length (float): Средняя длина видео на платформе.
        """
        super().__init__(name, user_count)  # Унаследованная инициализация базового класса
        self.average_video_length = average_video_length

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети TikTok.

        Перегрузка добавляет отображение средней длины видео, что является уникальной характеристикой TikTok.

        Returns:
            str: Название, количество пользователей и средняя длина видео.
        """
        return (f"TikTok(name={self.name}, user_count={self._user_count}, "
                f"average_video_length={self.average_video_length})")

    def get_user_count(self) -> int:
        """
        Возвращает количество пользователей TikTok.

        Перегруженный метод добавляет вывод сообщения, чтобы подчеркнуть, что это специфическая реализация
        для платформы TikTok, хотя основная функциональность остается неизменной (возврат количества пользователей).

        Returns:
            int: Количество пользователей.
        """
        print("Этот метод предоставляет количество пользователей TikTok.")
        return super().get_user_count()