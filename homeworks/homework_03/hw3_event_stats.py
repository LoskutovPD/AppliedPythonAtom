#!/usr/bin/env python
# coding: utf-8
from collections import deque as dq
from invert_dict import invert_dict as inv


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.users = []
        self.times = []

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        self.users.append(user_id)
        self.times.append(time)

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count
        действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        # TODO: реализовать метод
        tmp1, tmp2 = None, None
        for x in range(len(self.times) - 1, -1, -1):
            if self.times[x] <= time and tmp2 is None:
                tmp2 = x + 1
            if self.times[x] < time - self.FIVE_MIN:  # 1552564881
                tmp1 = x + 1
                break
        deque = dq(self.users[tmp1:tmp2])
        x = inv(dict(deque))
        if x.get(count) is None:
            return 0
        else:
            return len(x.get(count))
