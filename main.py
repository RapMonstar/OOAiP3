# команда
# Переключатель настольной лампы и музыкальной станции
from typing import List
from abc import ABC, abstractmethod

class ICommand:
    @abstractmethod
    def execute(self) -> None:
        ...


class Light:
    def onLight(self):
        print('Лампа включается')

    def offLight(self):
        print('Лампа выключается')


class MusicCenter:
    def onMusicCenter(self):
        print('Музыкальный центр включается')

    def offMusicCenter(self):
        print('Музыкальный центр выключается')

    def changeSong(self):
        print('Изменение песни')


class PrepareOnLight(ICommand):
    def __init__(self, executor: Light):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.onLight()


class PrepareOffLight(ICommand):
    def __init__(self, executor: Light):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.offLight()


class PrepareOnMusicCenter(ICommand):
    def __init__(self, executor: MusicCenter):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.onMusicCenter()


class PrepareOffMusicCenter(ICommand):
    def __init__(self, executor: MusicCenter):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.offMusicCenter()


class PrepareChangeSong(ICommand):
    def __init__(self, executor: MusicCenter):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.changeSong()


class Smartpult:
    def __init__(self):
        self.history: List[ICommand] = []

    def addCommand(self, command: ICommand) -> None:
        self.history.append(command)

    def work(self) -> None:
        if not self.history:
            print('Не задана очерёдность работы предметов')
        else:
            for executor in self.history:
                executor.execute()
        self.history.clear()


if __name__ == '__main__':
    light = Light()
    musicCenter = MusicCenter()
    smartpult = Smartpult()

    smartpult.addCommand(PrepareOnLight(light))
    smartpult.addCommand(PrepareOnMusicCenter(musicCenter))
    smartpult.addCommand(PrepareChangeSong(musicCenter))
    smartpult.addCommand(PrepareOffMusicCenter(musicCenter))
    smartpult.addCommand(PrepareOffLight(light))

    smartpult.work()
