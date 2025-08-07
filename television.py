class Television:
    """Creates an object with methods for controlling a television"""
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initialize class with default values"""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Used to turn the TV off and on"""
        if not self.__status:
            self.__status = True
        elif self.__status:
            self.__status = False

    def mute(self) -> None:
        """Mutes or unmutes the TV"""
        if self.__status:
            if not self.__muted:
                self.__muted = True
            elif self.__muted:
                self.__muted = False

    def channel_up(self) -> None:
        """Increases the selected channel. Wraps around to minimum channel if exceeding the max"""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Decreases the selected channel. Wraps around to maximum channel if below the mix"""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increases the volume and unmutes if TV muted"""
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decreases the volume and unmutes if TV muted"""
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """set string when printing class:Television to show TV status"""
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {0 if self.__muted else self.__volume}'