import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('stunted huf dun')
	mobileTemplate.setLevel(36)
	mobileTemplate.setMinLevel(36)
	mobileTemplate.setMaxLevel(36)
	mobileTemplate.setDifficulty(0)
	mobileTemplate.setAttackRange(5)
	mobileTemplate.setAttackSpeed(1.0)
	mobileTemplate.setWeaponType(6)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(.6)
	mobileTemplate.setMeatType("Herbivore Meat")
	mobileTemplate.setMeatAmount(775)
	mobileTemplate.setHideType("Leathery Hide")
	mobileTemplate.setHideAmount(800)
	mobileTemplate.setBoneType("Mammal Bones")
	mobileTemplate.setBoneAmount(775)
	mobileTemplate.setSocialGroup("huf dun")
	mobileTemplate.setAssistRange(0)
	mobileTemplate.setStalker(False)
	
	templates = Vector()
	templates.add('object/mobile/shared_huf_dun.iff')
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', 6, 1.0)
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('stunted_huf_dun', mobileTemplate)
	return