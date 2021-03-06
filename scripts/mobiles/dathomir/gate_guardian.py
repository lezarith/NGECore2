import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector


def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('')
	mobileTemplate.setCustomName('Gate Guardian')
	mobileTemplate.setLevel(81)
	mobileTemplate.setDifficulty(Difficulty.ELITE)

	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(6)
	mobileTemplate.setSocialGroup('nightsister')
	mobileTemplate.setRespawnTime(300)
	mobileTemplate.setOptionsBitmask(Options.CONVERSABLE | Options.INVULNERABLE)
	
	templates = Vector()
	templates.add('object/mobile/shared_dressed_dathomir_nightsister_protector.iff')
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/sword/shared_sword_01.iff', WeaponType.ONEHANDEDMELEE, 1.0, 5, 'kinetic')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('meleehit')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('gate_guardian', mobileTemplate)
	