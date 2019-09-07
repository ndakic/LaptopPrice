from enum import Enum


class ProcessorBrand(Enum):
	INTEL = "intel"


class ProcessorCores(Enum):
	FOUR = 4
	TWO = 2


class ProcessorNumber(Enum):
	I7 = "i7"
	I5 = "i5"
	I3 = "i3"


class RamGeneration(Enum):
	DDR4 = "ddr4"
	DDR3 = "ddr3"
	DDR2 = "ddr2"


class StorageType(Enum):
	SSD = "ssd"
	HDD = "hdd"


class Condition(Enum):
	NEW = "new"
	USED = "used"
	DEFECTIVE = "defective"


class LaptopBrand(Enum):
	APPLE = "apple"
	HP = "hp"
	DELL = "dell"
	ACER = "acer"
	TERRA = "terra"
	LENOVO = "lenovo"
	SAMSUNG = "samsung"
	SONY = "sony"
	ASUS = "asus"
	FUJITSU = "fujitsu"
	TOSHIBA = "toshiba"
